import Vue from 'vue'
import App from './App.vue'

import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import TweetMain from './TweetMain.vue'
import jQuery from 'jquery';
import Vuelidate from 'vuelidate'

window.jQuery = jQuery;
window.$ = jQuery;

Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuelidate);

const routes = [
  {
    path: '/',
    redirect: '/tweets'
  },
  {
    path: '/tweets',
    component: TweetMain
  }
];

const router = new VueRouter({
  routes
});

new Vue({
  el: '#app',
  router,
  render: h => h(App),
})
