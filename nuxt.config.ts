export default {
  head: {
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
