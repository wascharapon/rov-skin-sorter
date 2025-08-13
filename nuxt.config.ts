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
      { name: 'theme-color', content: '#343a40' },
      { property: 'og:title', content: 'ROV Skin Sorter - เครื่องมือจัดเรียงสกินเกมส์ RoV' },
      {
        property: 'og:description',
        content: 'เครื่องมือจัดเรียงและจัดระเบียบสกินตัวละครในเกม Arena of Valor (RoV) สร้างกริดที่ปรับแต่งได้ ลากวางสลับตำแหน่ง นำเข้าส่งออก JSON และสร้างภาพ PNG'
      },
      { property: 'og:type', content: 'website' },
      { property: 'og:url', content: 'https://rov-skin-sorter.vercel.app' },
      { property: 'og:image', content: 'https://rov-skin-sorter.vercel.app/favicon.ico' },
      { property: 'og:image:alt', content: 'ROV Skin Sorter - Grid organizer for Arena of Valor character skins' },
      { property: 'og:image:type', content: 'image/png' },
      { property: 'og:image:width', content: '1200' },
      { property: 'og:image:height', content: '630' },
      { property: 'og:site_name', content: 'ROV Skin Sorter' },
      { property: 'og:locale', content: 'th_TH' },
      { property: 'og:locale:alternate', content: 'en_US' },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:site', content: '@rovskinsorter' },
      { name: 'twitter:title', content: 'ROV Skin Sorter - เครื่องมือจัดเรียงสกินเกมส์ RoV' },
      {
        name: 'twitter:description',
        content: 'เครื่องมือจัดเรียงและจัดระเบียบสกินตัวละครในเกม Arena of Valor (RoV) สร้างกริดที่ปรับแต่งได้ ลากวางสลับตำแหน่ง นำเข้าส่งออก JSON และสร้างภาพ PNG'
      },
      { name: 'twitter:image', content: '/og-image.png' },
      { name: 'twitter:image:alt', content: 'ROV Skin Sorter - Grid organizer for Arena of Valor character skins' }
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
