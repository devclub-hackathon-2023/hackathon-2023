import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView'
import ViewToDos from '../views/ViewToDos'
import PtsView from '../views/PtsView'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/todos',
    name: 'To do lists',
    component: ViewToDos
  },
  {
    path: '/points',
    name: 'points',
    component: PtsView
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
