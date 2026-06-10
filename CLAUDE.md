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

## Gotchas
- **`lib/skin.ts` ใหญ่มาก** — ใช้ `grep`/`Read` แบบ offset+limit อย่า read เต็มไฟล์
- **เพิ่มสกินใหม่** → ใส่ใน `lib/skin.ts` แล้วรัน `make sort-ids` เพื่อจัด id ใหม่
- **Nuxt 2 + Vue 2.6** — อย่าใช้ Composition API syntax ของ Vue 3 / Nuxt 3
- **Static build** — ห้ามใช้ SSR-only API (`asyncData` server-side, server middleware)
- UI/text/error เป็น **ภาษาไทย**

## Write Permission
เฉพาะ `~/Desktop/work/**` (rule จาก global CLAUDE.md)
