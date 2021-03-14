import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/lib/mdbvue.css';
import Vue from 'vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import AOS from 'aos';
import 'aos/dist/aos.css';
import loader from 'vue-ui-preloader';
import VueCookies from 'vue-cookies';

import App from './App.vue';
import router from './router';
import store from './store';
import './icons';

Vue.use(VueCookies);
Vue.config.productionTip = false;
Vue.use(loader);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

new Vue({
  created() {
    AOS.init();
  },
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
