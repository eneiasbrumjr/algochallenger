import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueToastr from 'vue-toastr'
import jQuery from 'jquery'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

window.jQuery = jQuery
window.$ = jQuery

Vue.use(VueToastr, {
  /* OverWrite Plugin Options if you need */
})
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(require('vue-moment'))

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
