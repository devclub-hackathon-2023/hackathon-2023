import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView'
import ViewToDos from '../views/ViewToDos'
import PtsView from '../views/PtsView'
import LogIn from '../views/LogIn'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    name: 'To do lists',
    component: ViewToDos
  },
  {
    path: '/Ptsview',
    name: 'points',
    component: PtsView
  },
  {
    path: '/Login',
    name: 'login',
    component: LogIn
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
