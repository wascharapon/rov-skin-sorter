# ROV Skin Sorter

ROV (Arena of Valor) Skin Sorter เป็นเว็บแอปพลิเคชันสำหรับจัดเรียงและจัดระเบียบสกินตัวละครในเกม Arena of Valor สร้างกริดที่ปรับแต่งได้ ลากวางสลับตำแหน่ง นำเข้าส่งออก JSON และสร้างภาพ PNG

## ✨ Features

- **Grid-based skin organizer**: สร้างกริดแบบปรับแต่งได้ (แถว/คอลัมน์) เพื่อจัดเรียงสกินตัวละคร
- **Visual skin browser**: เรียกดูและเลือกจากคอลเลกชันสกินตัวละคร ROV ที่ครบครัน
- **Drag & Drop**: ลากวางสลับตำแหน่งสกินภายในกริด
- **Import/Export functionality**: นำเข้าส่งออกการตั้งค่ากริดเป็นไฟล์ JSON
- **Image export**: สร้างภาพ PNG ของกริดสกินที่สร้างขึ้นโดยใช้ html2canvas
- **Auto advance**: ไปยังตำแหน่งถัดไปโดยอัตโนมัติหลังจากเลือกสกิน
- **Class information**: ระบบจัดหมวดหมู่ในตัวสำหรับความหายากและประเภทของสกิน

## 🚀 Getting Started

### การติดตั้ง

```bash
# Clone repository
git clone <repository-url>
cd rov-skin-sorter

# ติดตั้ง dependencies
yarn install
```

### การใช้งาน

```bash
# เริ่มต้น development server (รันที่ port 8000)
yarn dev

# Build สำหรับ production
yarn build

# เริ่มต้น production server
yarn start

# ตรวจสอบ code style
yarn lint
```

เว็บแอปพลิเคชันจะเข้าถึงได้ที่ `http://localhost:8000`

## 🛠️ Technical Stack

### Frontend
- **Nuxt.js 2** with TypeScript support
- **Vue.js 2.6** (เนื่องจากความเข้ากันได้กับ Nuxt 2)
- **Bootstrap 4** with **BootstrapVue** สำหรับ UI components
- **FontAwesome** สำหรับไอคอน
- **vue-multiselect** สำหรับ dropdown แบบขั้นสูง
- **html2canvas** สำหรับการสร้างภาพ

### Project Structure

```
├── pages/
│   └── index.vue          # หน้าแอปพลิเคชันหลักพร้อมอินเทอร์เฟซกริด
├── lib/
│   └── skin.ts            # ฐานข้อมูลสกินที่ครบครัน (ไฟล์ใหญ่พร้อม image mappings)
├── model/
│   └── rov.ts             # TypeScript interfaces สำหรับโครงสร้างข้อมูลสกิน
├── plugins/               # การตั้งค่า Vue plugin สำหรับ BootstrapVue และ vue-multiselect
└── assets/images/         # คอลเลกชันภาพสกินตัวละคร ROV ที่จัดระเบียบตามประเภท
```

## 📊 Data Models

```typescript
interface IRovSkin {
  id: number;
  base?: string;      // ชื่อตัวละครหลัก
  name?: string;      // ชื่อสกิน
  image: string;      // path ของภาพ
}

interface IRovSkinOnTable extends IRovSkin {
  key: number;        // ตำแหน่งในกริด
}
```

## 🎮 วิธีการใช้งาน

1. **ตั้งค่ากริด**: เลือกจำนวนแถวและคอลัมน์ที่ต้องการ (2-24)
2. **เลือกสกิน**: ใช้ dropdown พร้อมภาพตัวอย่างเพื่อเลือกสกิน
3. **วางสกิน**: คลิกที่ตำแหน่งในกริดเพื่อวางสกินที่เลือก
4. **จัดเรียง**: ลากและวางเพื่อสลับตำแหน่งสกิน
5. **ส่งออก**: บันทึกเป็นไฟล์ JSON หรือส่งออกเป็นภาพ PNG

## 🎨 Features หลัก

### ระบบกริด
- ขนาดกริดแบบไดนามิก (2-24 คอลัมน์/แถว)
- การควบคุมความกว้างแบบ responsive (เปอร์เซ็นต์)
- การเลือกตำแหน่งสกินด้วยการคลิก
- ลากวางสลับตำแหน่งได้
- เอฟเฟกต์ hover และ transition

### การจัดการสกิน
- Multi-select dropdown พร้อมภาพตัวอย่าง
- ไปยังตำแหน่งถัดไปโดยอัตโนมัติหลังจากเลือก
- การสลับสกินระหว่างตำแหน่งในกริด
- การรีเซ็ตและยกเลิกการดำเนินการ

### ฟีเจอร์ส่งออก
- ส่งออก/นำเข้า JSON พร้อมการตั้งชื่อ timestamp
- การสร้างภาพ PNG พร้อมพื้นหลังโปร่งใส
- การสร้างชื่อไฟล์อัตโนมัติพร้อม timestamp

## 🌐 การตั้งค่าเซิร์ฟเวอร์

- Development server รันที่ `0.0.0.0:8000` เพื่อให้เข้าถึงได้จากเครือข่าย
- รองรับ TypeScript build
- ESLint ตั้งค่าด้วย Nuxt TypeScript rules

## 🎯 การสนับสนุนภาษาไทย

- ข้อความ UI เป็นภาษาไทยเป็นหลัก
- ระบบจัดหมวดหมู่สกินรวมถึงหมวดหมู่วันหยุด/ตามฤดูกาลของไทย
- ข้อความแสดงข้อผิดพลาดและ placeholder เป็นภาษาไทย

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.