<template>
  <div class="card center">
    <div class="card-header">
      Login
    </div>
    <div class="card-body">
      <form action="" @submit="submitForm">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" class="form-control" name="username" id="username" aria-describedby="helpId" placeholder="" v-model="username" required>
        </div>
        <div class="form-group" id="password-input">
          <label for="password">Password</label>
          <input type="password" class="form-control" name="password" id="password" aria-describedby="helpId" placeholder="" v-model="password" required>
        </div>
        <base-button :btnType="'primary'" :loading="loading"></base-button>
      </form>
    </div>
  </div>
</template>

<script>
  import BaseButton from "@/components/BaseButton.vue";
  // import BaseLoading from "@/components/BaseLoading.vue";
  import BocaService from '@/services/BocaService.js';

  export default {
    components: {
      BaseButton,
      // BaseLoading
    },
    name: "LoginCard",
    data() {
      return {
        username: '',
        password: '',
        loading: false
      }
    },
    methods: {
      submitForm: function (e) {
        e.preventDefault();
        this.$toastr.removeByType("error");
        const formData = {
          username: this.username,
          password: this.password
        }
        this.loading = true;

        BocaService.login(formData)
          .then(response => {
            this.$store.commit('SET_USER_DATA', response.data);
            this.$router.push('/home');
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
              this.$toastr.e('An error has ocurred ')
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
.card {
  margin: 0 auto;
  width: 30rem;
  height: 20rem;
}

.form-group {
  margin: 0 auto;
  width: 60%;
}

#password-input {
  margin-top: 10px;
  margin-bottom: 30px;
}
</style>