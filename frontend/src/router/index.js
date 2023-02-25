import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView'
import PtsView from '../views/PtsView'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  
  {
    path: '/Ptsview',
    name: 'points',
    component: PtsView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
