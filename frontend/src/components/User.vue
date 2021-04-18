<template>
  <div>
    <h1>User - </h1>
      <b-form id="user-form" action="" @submit="submitForm">
        <b-form-group
          id="input-group-1"
          label="Username:"
          label-for="input-1"
        >
        <b-form-input
          id="input-1"
          type="text"
          v-model="user.username"
          required
          placeholder="Enter username"
        ></b-form-input>
      </b-form-group>

      <b-form-group
          id="input-group-1"
          label="Password:"
          label-for="input-1"
        >
        <b-form-input
          id="input-1"
          type="password"
          v-model="user.password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-form-group
          id="input-group-1"
          label="Full name:"
          label-for="input-1"
        >
        <b-form-input
          id="input-1"
          type="text"
          v-model="user.full_name"
          required
          placeholder="Enter full name"
        ></b-form-input>
      </b-form-group>

      <b-form-group
          id="input-group-1"
          label="Type:"
          label-for="input-1"
        >
        <b-form-select id="select" v-model="user.type" :options="options" required></b-form-select>

      </b-form-group>
      
      <base-button :loading="loading"></base-button>
    </b-form>
    
  </div>
</template>

<script>
import BocaService from '@/services/BocaService.js';
import BaseButton from '@/components/BaseButton.vue'

export default {
  data() {
    return {
      loading: false,
      token: this.$store.state.token,
        options: [
          { value: null, text: 'Please select some item' },
          { value: 'admin', text: 'Admin' },
          { value: 'staff', text: 'Staff' },
          { value: 'student', text: 'Student' }
        ]
    }
  },
  components: {
    BaseButton
  },
  props: {
    user: {
      type: Object,
      default: function() {
        return {
          name: '',
          type: null
        }
      }
    }
  },
  methods: {
    submitForm: function (e) {
      e.preventDefault();
      this.$toastr.removeByType("error");
      const formData = {
        full_name: this.user.full_name,
        username: this.user.username,
        password: this.user.password,
        type: this.user.type
      }
      console.log(formData)
      this.loading = true

      BocaService.postUser(this.token, formData)
        .then(response => {
          console.log(response)
          this.$router.push('/users');
        })
        .catch(error => {
          switch (error.response.status) {
          case 422:
            Object.entries(error.response.data.errors).forEach((element) => {
              this.$toastr.e(element[1])
            });
            break;
          case 401:
            this.$toastr.e('Wrong username or password')
            break;
          default: 
            this.$toastr.e('An error has ocurred')
          }
        })
        .then(() => {
          this.loading = false;
        });
    }
  }
}
</script>

<style scoped>
#user-form {
  width: 30%;
  margin:0 auto;
}
</style>