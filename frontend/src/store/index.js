import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const localStorage = window.localStorage

export default new Vuex.Store({
  state: {
    token: '',
    user: null
  },
  mutations: {
    update_token (state, token) {
      state.token = token
      localStorage.setItem('token', JSON.stringify(token))
      axios.defaults.headers.common.Authorization = 'Bearer ' + token
    },
    store_user (state, user) {
      state.user = user
    },
    SET_USER_DATA (state, response) {
      state.user = response.user
      state.token = response.access_token
      localStorage.setItem('user', JSON.stringify(response.user))
      localStorage.setItem('token', JSON.stringify(response.access_token))
      axios.defaults.headers.common.Authorization = 'Bearer ' + response.access_token
    },
    CLEAR_USER_DATA (state) {
      localStorage.removeItem('user')
      state.token = ''
      state.user = null
      localStorage.removeItem('token')
    },
    initialiseStore (state) {
      if (localStorage.getItem('user')) {
        state.user = JSON.parse(localStorage.getItem('user'))
        state.token = JSON.parse(localStorage.getItem('token'))
      }
    }
  },
  actions: {
  },
  modules: {
  },
  getters: {
    loggedIn (state) {
      return !!state.user
    },
    isAdmin (state) {
      return state.user.type === 'admin'
    }
  }
})
