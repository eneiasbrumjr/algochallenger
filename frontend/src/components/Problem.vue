<template>
  <div>
    <h1>Problem - </h1>
      <b-form id="user-form" action="" @submit="submitForm">
        <b-form-group
          id="input-group-1"
          label="Problem name:"
          label-for="input-1"
        >
        <b-form-input
          id="input-1"
          type="text"
          v-model="problem.name"
          required
          placeholder="Enter problem name"
        ></b-form-input>
      </b-form-group>

      <b-form-group
          id="input-group-1"
          label="Problem file (zip):"
          label-for="input-1"
        >
        <b-form-file
          id="input-1"
          v-model="problem.file"
          required
          placeholder="Upload problem file"
        ></b-form-file>
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
      workingId: this.$route.params.working_id
    }
  },
  components: {
    BaseButton
  },
  props: {
    problem: {
      type: Object,
      default: function() {
        return {
          name: '',
          file: null
        }
      }
    }
  },
  methods: {
    submitForm: function (e) {
      e.preventDefault();
      this.$toastr.removeByType("error")
      const formData = new FormData()
      formData.append('name', this.problem.name)
      formData.append('file', this.problem.file)
      this.loading = true

      BocaService.postProblem(this.token, this.workingId, formData)
        .then(response => {
          console.log(response)
          this.$router.push({name: 'Problems'});
        })
        .catch(error => {
          switch (error.response.status) {
          case 422:
            Object.entries(error.response.data.errors).forEach((element) => {
              this.$toastr.e(element[1])
            });
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