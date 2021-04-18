import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Workings from '../components/Workings.vue'
import Working from '../components/Working.vue'
import Users from '../components/Users.vue'
import User from '../components/User.vue'
import Problems from '../components/Problems.vue'
import Problem from '../components/Problem.vue'
import Runs from '../components/Runs.vue'
import Run from '../components/Run.vue'
import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/home',
    component: Home,
    name: 'Home',
    children: [
      {
        path: '/workings',
        component: Workings,
        name: 'Workings'
      },
      {
        path: '/workings/create',
        component: Working,
        name: 'CreateWorking'
      },
      {
        path: '/workings/:working_id/edit',
        component: Working,
        name: 'EditWorking',
        props: true
      },
      {
        path: '/users',
        component: Users,
        name: 'Users'
      },
      {
        path: '/users/create',
        component: User,
        name: 'CreateUser'
      },
      {
        path: '/workings/:working_id/problems',
        component: Problems,
        name: 'Problems',
        props: true
      },
      {
        path: '/workings/:working_id/problems/create',
        component: Problem,
        name: 'CreateProblem'
      },
      {
        path: '/workings/:working_id/problems/:problem_id/edit',
        component: Problem,
        name: 'EditProblem',
        props: true
      },
      {
        path: '/workings/:working_id/problems/:problem_id/runs',
        component: Runs,
        name: 'Runs',
        props: true
      },
      {
        path: '/workings/:working_id/:problem_id/runs/create',
        component: Run,
        name: 'CreateRun'
      }
    ]
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

router.beforeEach((to, from, next) => {
  store.commit('initialiseStore')
  if (to.name !== 'Login' && !store.getters.loggedIn) next({ name: 'Login' })
  else next()

  if (to.name === 'Login' && store.getters.loggedIn) next({ name: 'Workings' })
  else next()

  if (to.name === 'Home') next({ name: 'Workings' })
  else next()
})

export default router
