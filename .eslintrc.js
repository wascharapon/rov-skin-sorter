module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  extends: ['@nuxtjs/eslint-config-typescript', 'plugin:nuxt/recommended'],
  plugins: [],
  // add your custom rules here
  rules: {
    quotes: [2, 'single', { avoidEscape: true }],
    'space-before-function-paren': [2, 'never'],
    'import/named': 0,
    'import/no-mutable-exports': 0,
    'no-use-before-define': 0
  }
}
