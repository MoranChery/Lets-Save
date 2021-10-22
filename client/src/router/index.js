import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ProvidentFundCalculator from '../views/ProvidentFundCalculator.vue'
import PageNotFound from '../views/PageNotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/provident_fund_calculator',
    name: 'ProvidentFundCalculator',
    component: ProvidentFundCalculator
  },
  {
    path: '*',
    name: 'PageNotFound',
    component: PageNotFound
  }
]

const router = new VueRouter({
  behavior: 'smooth',
  routes,
  scrollBehavior () {
    document.getElementById('app').scrollIntoView()
  }
})

export default router
