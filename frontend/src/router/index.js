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
<<<<<<< HEAD
    path: '/ViewToDos',
    name: 'ViewToDos',
=======
    path: '/todos',
    name: 'todos',
>>>>>>> refs/remotes/origin/main
    component: ViewToDos
  },
  {
    path: '/points',
    name: 'points',
    component: PtsView
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
