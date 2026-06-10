# CLAUDE.md — rov-skin-sorter

> ถูกเรียกผ่าน Telegram bot → ตอบ **ภาษาไทย สั้น กระชับ**

## Stack
Nuxt 2.15 (target: **static** — `nuxt generate`) + Vue 2.6 + TypeScript + BootstrapVue + vuedraggable + html2canvas
Deploy: Vercel (`rov-skin-sorter.vercel.app`)

## Commands
```bash
yarn dev      # dev server :8000 (0.0.0.0)
yarn build    # = nuxt generate (static)
yarn start    # serve build
yarn lint     # eslint .js/.vue

make sort-ids    # เรียง id ใน lib/skin.ts ใหม่ 1..N
make verify-ids  # ดู id แรก/ท้าย + นับรวม
```

## Layout
```
pages/index.vue       — หน้าเดียวของแอป (grid + UI)
lib/skin.ts           — DB สกินทั้งหมด (ไฟล์ใหญ่ ~MB อย่า read ทั้งไฟล์)
model/rov.ts          — IRovSkin, IRovSkinOnTable
plugins/              — vue-multiselect, bootstrap-vue-icon, vuedraggable
assets/images/skin/   — รูปสกิน
python/               — get_skin.py, convert_skin.py (scrape/แปลงรูป)
nuxt.config.ts        — config + SEO meta (เป็น .ts ไม่ใช่ .js)
```

## Data Model
```ts
IRovSkin { id, base?, name?, image, position? }
IRovSkinOnTable extends IRovSkin { key }   // key = ตำแหน่งใน grid
```

## Responsive Breakpoints (Bootstrap)
- `cols` = mobile default, `md` = ≥768px (tablet portrait), `lg` = ≥992px (tablet landscape+)
- Select-skin row: `cols="12" md="6"` (selector) + `cols="6" md="3"` × 2 (buttons)
- Grid controls (`ipad-grid-controls`): auto-fit ปกติ, 4 cols ที่ 768px+, 4 cols ที่ 1024px+

## Gotchas
- **`lib/skin.ts` ใหญ่มาก** — ใช้ `grep`/`Read` แบบ offset+limit อย่า read เต็มไฟล์
- **เพิ่มสกินใหม่** → ใส่ใน `lib/skin.ts` แล้วรัน `make sort-ids` เพื่อจัด id ใหม่
- **Nuxt 2 + Vue 2.6** — อย่าใช้ Composition API syntax ของ Vue 3 / Nuxt 3
- **Static build** — ห้ามใช้ SSR-only API (`asyncData` server-side, server middleware)
- UI/text/error เป็น **ภาษาไทย**
- **`vue-multiselect` dropdown** — `.multiselect__content-wrapper` เป็น `position: absolute, z-index: 50` → ห้ามใส่ `overflow: hidden` บน parent ใดๆ (รวมถึง `b-form-group` / `fieldset`) เด็ดขาด มิฉะนั้น dropdown จะถูก clip หาย
- **Screenshot/ทดสอบ UI** — ใช้ `playwright` (global: `npm root -g`) + `require('$(npm root -g)/playwright')`; dev server port **8000**

## Write Permission
เฉพาะ `~/Desktop/work/**` (rule จาก global CLAUDE.md)
