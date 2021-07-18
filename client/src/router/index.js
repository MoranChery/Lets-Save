import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Calculator from '../views/Calculator.vue'
import PageNotFound from '../views/PageNotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/calculator',
    name: 'Calculator',
    component: Calculator
  },
  {
    path: '*',
    name: 'PageNotFound',
    component: PageNotFound
  }
]

const router = new VueRouter({
  routes
})

export default router
