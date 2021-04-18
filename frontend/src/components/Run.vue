<template>
  <div>
    <h1>New Run</h1>
      <b-form id="user-form" action="" @submit="submitForm">
      <b-form-group
          id="input-group-1"
          label="Run file:"
          label-for="input-1"
        >
        <b-form-file
          id="input-1"
          v-model="run.file"
          required
          placeholder="Upload run file"
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
      problemId: this.$route.params.problem_id
    }
  },
  components: {
    BaseButton
  },
  props: {
    run: {
      type: Object,
      default: function() {
        return {
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
      formData.append('file', this.run.file)
      this.loading = true

      BocaService.postRun(this.token, this.problemId, formData)
        .then(response => {
          console.log(response)
          this.$router.push({name: 'Runs'});
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