import axios from 'axios'
import store from '@/store/index'
import router from '@/router/index'

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

apiClient.interceptors.response.use(null, function (error) {
  if (error.response.status === 401) {
    store.commit('CLEAR_USER_DATA')
    router.push('/')
    // console.log(store.state.token)
    // return apiClient.post('/refresh', {}, {
    //   headers: {
    //     Authorization: 'Bearer ' + store.state.token
    //   }
    // })
    //   .then(response => {
    //     store.commit('update_token', response.data.access_token)
    //     return axios.request(error.config)
    //   })
  }
  return Promise.reject(error)
})

export default {
  login (data) {
    return apiClient.post('/login', data)
  },
  logout (token) {
    return apiClient.post('/logout',
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  getWorkings (token) {
    return apiClient.get('/working',
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  getUsers (token, tipo = null, working = null) {
    return apiClient.get('/user',
      {
        headers: {
          Authorization: 'Bearer ' + token
        },
        params: {
          type: tipo,
          working: working
        }
      })
  },
  postWorking (token, data) {
    return apiClient.post('/working', data,
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  putWorking (token, working, data) {
    return apiClient.put('/working/' + working, data,
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  postUser (token, data) {
    return apiClient.post('/user', data,
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  getProblems (token, workingId) {
    return apiClient.get('/working/' + workingId + '/problem',
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  getRuns (token, problemId) {
    return apiClient.get('/problem/' + problemId + '/run',
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  },
  getProblemZip (token, problemId) {
    return apiClient.get('/download/problem/' + problemId + '/zip',
      {
        responseType: 'arraybuffer',
        headers: {
          Accept: 'application/octet-stream, application/json',
          Authorization: 'Bearer ' + token
        }
      })
  },
  getProblemDescription (token, problemId) {
    return apiClient.get('/download/problem/' + problemId + '/description',
      {
        responseType: 'arraybuffer',
        headers: {
          Accept: 'application/octet-stream, application/json',
          Authorization: 'Bearer ' + token
        }
      })
  },
  getRunFile (token, runId) {
    return apiClient.get('/download/run/' + runId + '/file',
      {
        responseType: 'arraybuffer',
        headers: {
          Accept: 'application/octet-stream',
          Authorization: 'Bearer ' + token
        }
      })
  },
  postProblem (token, workingId, data) {
    return apiClient.post('/working/' + workingId + '/problem', data,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: 'Bearer ' + token
        }
      })
  },
  postRun (token, problemId, data) {
    return apiClient.post('/problem/' + problemId + '/run', data,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: 'Bearer ' + token
        }
      })
  },
  getWorking (token, workingId) {
    return apiClient.get('/working/' + workingId,
      {
        headers: {
          Authorization: 'Bearer ' + token
        }
      })
  }
}
