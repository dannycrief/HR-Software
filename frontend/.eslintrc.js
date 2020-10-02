module.exports = {
  extends: [
    'plugin:vue/recommended',
    'plugin:vue/base'
  ],
  parserOptions: {
    "parser": "babel-eslint",
    "ecmaVersion": 2017,
    "sourceType": "module"
  },
  plugins: [
    'vue'
  ],
  rules: {
    'vue/this-in-template': ["error", "never"],
    'semi': "error",
  }
}
