import colors from 'vuetify/es5/util/colors'

const isDev = process.env.NODE_ENV !== 'production'
const baseUrl = process.env.NUXT_ENV_HOST_URL || 'http://localhost:3000'
const backendUrl = process.env.NUXT_ENV_BACKEND_URL || 'http://localhost:8000'

export default {
  env: {
    baseUrl,
    backendUrl,
  },
  ssr: true, // default
  target: 'server', // default
  dev: isDev,
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'DAS',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: ['~/plugins/axios'],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/proxy',
  ],

  router: {
    middleware: ['auth'],
  },

  proxy: [backendUrl.replace(/\/+$/, '') + '/api'],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: isDev
    ? {}
    : {
      baseURL: baseUrl,
      credentials: true,
    },

  auth: {
    localStorage: false,
    cookie: {
      prefix: 'auth.',
      options: {
        path: '/',
        secure: true,
      },
    },
    redirect: {
      login: '/login',
      logout: '/login',
      callback: '/login',
      home: '/',
    },
    strategies: {
      cookie: {
        cookie: {
          // (optional) If set, we check this cookie existence for loggedIn check
          // name: 'XSRF-TOKEN',
        },
        user: {
          property: '',
        },
        endpoints: {
          // (optional) If set, we send a get request to this endpoint before login
          csrf: {
            url: '/api/accounts/set-csrf/',
            method: 'get',
          },
          login: {
            url: '/api/auth/login/',
            method: 'post',
          },
          logout: {
            url: '/api/auth/logout/',
            method: 'post',
          },
          user: {
            url: '/api/accounts/me/',
            method: 'get',
          },
        },
      },
    },
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
}
