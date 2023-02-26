import { createStore } from 'vuex'

export default createStore({
  state: {
    userID: 0,
  },
  getters: {
  },
  mutations: {
    addUserID(state, id) {
      state.userID = id
    },
    getUserID(state) {
      return state.userID
    }
  },
  actions: {
  },
  modules: {
  }
})
