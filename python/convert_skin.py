#!/usr/bin/env python3
import json
import os
import re
import sys
import argparse
from typing import Dict, List, Optional, Any

def extract_field_value(obj_str: str, field_name: str, field_type: str = 'string') -> Optional[Any]:
    """Extract field value from TypeScript object string"""
    if field_type == 'number':
        match = re.search(rf'{field_name}:\s*(\d+)', obj_str)
        return int(match.group(1)) if match else None
    
    elif field_type == 'position':
        match = re.search(rf'{field_name}:\s*([\d.]+)', obj_str)
        if match:
            value = match.group(1)
            return float(value) if '.' in value else int(value)
        return None
    
    elif field_type == 'image':
        match = re.search(rf"{field_name}:\s*require\('([^']*)'\)", obj_str)
        if match:
            image_path = match.group(1)
            return image_path.replace('~/', '')
        return None
    
    else:  # string type
        # Try single quotes first, then double quotes
        patterns = [
            rf"{field_name}:\s*'([^']*)',?",
            rf'{field_name}:\s*"([^"]*)",?',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, obj_str)
            if match:
                return match.group(1)
        return None


def generate_missing_image_path(skin: Dict[str, Any]) -> str:
    """Generate image path for skins missing image field"""
    base = skin.get('base', '').lower().replace(' ', '-')
    name = skin.get('name', '').lower().replace(' ', '-').replace("'", "")
    
    if base and name:
        return f"assets/images/skin/{base}-{name}.png"
    elif base:
        # If only base is available, use base name as fallback
        return f"assets/images/skin/{base}-default.png"
    else:
        # Last resort fallback
        return "assets/images/skin/default.png"


def fill_missing_fields(skin: Dict[str, Any], index: int, add_default_position: bool = False) -> Dict[str, Any]:
    """Fill in missing optional fields with default values"""
    
    # Fill missing image field
    if 'image' not in skin or not skin['image']:
        if 'base' in skin or 'name' in skin:
            skin['image'] = generate_missing_image_path(skin)
            print(f"🔧 Generated image path for ID {skin.get('id', index)}: {skin['image']}")
        else:
            skin['image'] = "assets/images/skin/default.png"
            print(f"🔧 Used default image for ID {skin.get('id', index)}")
    
    # Fill missing position field if requested
    if add_default_position and 'position' not in skin:
        skin['position'] = None  # or could use a default number like 0
        print(f"🔧 Added default position for ID {skin.get('id', index)}")
    
    return skin


def validate_skin_object(skin: Dict[str, Any], index: int) -> bool:
    """Validate skin object has required fields"""
    required_fields = ['id']
    missing_fields = [field for field in required_fields if field not in skin]
    
    if missing_fields:
        print(f"⚠️  Object at index {index} missing required fields: {missing_fields}")
        print(f"   Object: {skin}")
        return False
    
    return True


def convert_ts_to_json(add_default_position: bool = False):
    """Convert lib/skin.ts to ai_python/lib/skin.json with improved parsing and validation"""
    
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ts_file = os.path.join(base_dir, 'lib', 'skin.ts')
    json_file = os.path.join(os.path.dirname(__file__), 'lib', 'skin.json')
    
    print(f"🔍 Reading TypeScript file: {ts_file}")
    
    if not os.path.exists(ts_file):
        print(f"❌ File not found: {ts_file}")
        return
    
    # Read TypeScript file
    with open(ts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the array content between 'export const rov: IRovSkin[] = [' and the last ']'
    pattern = r'export const rov: IRovSkin\[\] = \[(.*)\]'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("❌ Could not find skin data in TypeScript file")
        return
    
    array_content = match.group(1)
    
    # Parse each skin object
    skins = []
    skipped_objects = []
    
    # Split by object boundaries (look for },\n  { patterns)
    objects = re.split(r'\},\s*\n\s*\{', array_content)
    
    print(f"🔄 Processing {len(objects)} objects...")
    
    for i, obj_str in enumerate(objects):
        # Clean up the object string
        if i == 0:
            obj_str = obj_str.strip().lstrip('{')
        if i == len(objects) - 1:
            obj_str = obj_str.strip().rstrip('}')
        
        # Parse individual fields using helper function
        skin = {}
        
        # Extract required and optional fields
        skin_id = extract_field_value(obj_str, 'id', 'number')
        if skin_id:
            skin['id'] = skin_id
        
        name = extract_field_value(obj_str, 'name', 'string')
        if name:
            skin['name'] = name
        
        base = extract_field_value(obj_str, 'base', 'string')
        if base:
            skin['base'] = base
        
        image = extract_field_value(obj_str, 'image', 'image')
        if image:
            skin['image'] = image
        
        position = extract_field_value(obj_str, 'position', 'position')
        if position is not None:
            skin['position'] = position
        
        # Validate and add skin object
        if skin and validate_skin_object(skin, i):
            # Fill missing fields before adding to results
            skin = fill_missing_fields(skin, i, add_default_position)
            skins.append(skin)
        else:
            skipped_objects.append(i)
            if not skin:
                print(f"⚠️  Skipped empty object at index {i}")
    
    if skipped_objects:
        print(f"⚠️  Skipped {len(skipped_objects)} invalid objects at indices: {skipped_objects[:10]}{'...' if len(skipped_objects) > 10 else ''}")
    
    print(f"✅ Parsed {len(skins)} skins")
    
    # Validate final results
    validate_conversion_results(skins)
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    
    # Write JSON file
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(skins, f, ensure_ascii=False, indent=2)
        print(f"✅ Successfully converted to: {json_file}")
    except Exception as e:
        print(f"❌ Failed to write JSON file: {e}")
        return False
    
    print(f"📊 Total skins: {len(skins)}")
    return True

def validate_conversion_results(skins: List[Dict[str, Any]]) -> None:
    """Validate the conversion results"""
    print("\n🔍 Validating conversion results...")
    
    # Check for duplicates
    ids = [skin.get('id') for skin in skins if 'id' in skin]
    duplicates = [id for id in set(ids) if ids.count(id) > 1]
    if duplicates:
        print(f"⚠️  Found duplicate IDs: {duplicates[:5]}{'...' if len(duplicates) > 5 else ''}")
    
    # Check field coverage
    total_skins = len(skins)
    field_stats = {
        'id': sum(1 for skin in skins if 'id' in skin),
        'name': sum(1 for skin in skins if 'name' in skin),
        'base': sum(1 for skin in skins if 'base' in skin),
        'image': sum(1 for skin in skins if 'image' in skin),
        'position': sum(1 for skin in skins if 'position' in skin),
    }
    
    print("📈 Field coverage:")
    for field, count in field_stats.items():
        percentage = (count / total_skins * 100) if total_skins > 0 else 0
        print(f"   {field}: {count}/{total_skins} ({percentage:.1f}%)")
    
    # Check for items missing critical fields
    missing_name = [skin.get('id', '?') for skin in skins if 'name' not in skin]
    if missing_name:
        print(f"⚠️  Items missing 'name' field (IDs): {missing_name[:10]}{'...' if len(missing_name) > 10 else ''}")


def main():
    """Main function with command-line argument support"""
    parser = argparse.ArgumentParser(
        description="Convert lib/skin.ts to ai_python/lib/skin.json",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_skin.py                    # Basic conversion (fill missing images only)
  python convert_skin.py --fill-position    # Fill missing images and positions
        """
    )
    
    parser.add_argument(
        '--fill-position', 
        action='store_true', 
        help='Fill missing position fields with default value (None)'
    )
    
    args = parser.parse_args()
    
    print("🚀 Starting skin conversion...")
    if args.fill_position:
        print("📝 Will fill missing position fields with default values")
    
    success = convert_ts_to_json(add_default_position=args.fill_position)
    
    if success:
        print("🎉 Conversion completed successfully!")
    else:
        print("💥 Conversion failed!")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()