export default {
  head: {
    title: 'ROV Skin Sorter - เครื่องมือจัดเรียงสกินเกมส์ RoV',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        name: 'description',
        content: 'เครื่องมือจัดเรียงและจัดระเบียบสกินตัวละครในเกม Arena of Valor (RoV) สร้างกริดที่ปรับแต่งได้ นำเข้าและส่งออกการตั้งค่า และสร้างภาพจากกริดที่สร้างขึ้น'
      },
      {
        name: 'keywords',
        content: 'ROV, Arena of Valor, Skin Sorter, สกิน, จัดเรียง, เกมส์, ตัวละคร, กริด, Thai Gaming'
      },
      { name: 'author', content: 'ROV Skin Sorter Team' },
      { name: 'theme-color', content: '#343a40' }
    ],
    link: [
      {
        rel: 'icon',
        type: 'image/x-icon',
        href: '/favicon.ico'
      }
    ]
  },
  css: [
    'bootstrap/dist/css/bootstrap.min.css',
    'vue-multiselect/dist/vue-multiselect.min.css',
    '@fortawesome/fontawesome-free/css/all.min.css'
  ],
  build: {
    // สำหรับกรณีที่ใช้ Bootstrap 4 ต้องแน่ใจว่า popper.js รองรับ
    transpile: []
  },
  plugins: ['~/plugins/vue-multiselect.ts', '~/plugins/bootstrap-vue-icon.ts', '~/plugins/vuedraggable.ts'],
  buildModules: [
    '@nuxt/typescript-build'
  ],
  server: {
    port: 8000,
    host: '0.0.0.0'
  },
  vue: {
    config: {
      devtools: true
    }
  }
}
