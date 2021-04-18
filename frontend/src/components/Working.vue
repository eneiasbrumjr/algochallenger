<template>
  <div>
    <h1>Working</h1>
      <b-form id="working-form" action="" @submit="submitForm">
        <b-form-group
          id="input-group-1"
          label="Name:"
          label-for="input-1"
        >
        <b-form-input
          id="input-1"
          type="text"
          v-model="working.name"
          required
          placeholder="Enter working name"
        ></b-form-input>
      </b-form-group>

      <b-form-group
          class="inline-block col-5"
          id="input-group-1"
          label="Start date:"
          label-for="start-date-input"
        >
        <b-form-datepicker id="start-date-input" v-model="working.start_date" class="mb-2" :date-format-options="{ year: 'numeric', month: '2-digit', day: '2-digit' }"
          locale="en"></b-form-datepicker>
      </b-form-group>

      <b-form-group
          class="inline-block col-5 offset-2"
          label="Start time:"
          label-for="start-time-input"
        >
        <b-form-timepicker id="start-time-input" v-model="working.start_time" locale="en"></b-form-timepicker>
      </b-form-group>

      <b-form-group
          class="inline-block col-5"
          label="Finish date:"
          label-for="finish-date-input"
        >
        <b-form-datepicker id="finish-date-input" v-model="working.finish_date" class="mb-2" :date-format-options="{ year: 'numeric', month: '2-digit', day: '2-digit' }"
          locale="en"></b-form-datepicker>
      </b-form-group>

      <b-form-group
          class="inline-block col-5 offset-2"
          label="Finish time:"
          label-for="finish-time-input"
        >
        <b-form-timepicker id="finish-time-input" v-model="working.finish_time" locale="en"></b-form-timepicker>
      </b-form-group>

      <b-form-group
        id="input-group-1"
        label="Import students from working:"
        label-for="input-1"
      >
      <b-form-select id="select" v-model="importFromWorkingValue" :options="importFromWorkingOptions" required></b-form-select>
      
      </b-form-group>
      <b-form-group
        id="input-group-1"
        label="Select students:"
        label-for="input-1"
      >
        <div class="col-5 inline-block">
          Unselected students
          <b-form-select v-model="unselected" :options="unselectedStudentsOptions" :select-size="10"></b-form-select>
        </div>

        <div class="col-2 inline-block" id="selectButtons">
          <b-button class="selectButton" type="button" v-on:click="selectStudent" variant="outline-info"><b-icon icon="arrow-bar-right"></b-icon></b-button>
          <b-button class="selectButton" type="button" v-on:click="unselectStudent" variant="outline-info"><b-icon icon="arrow-bar-left"></b-icon></b-button>
        </div>

        <div class="col-5 inline-block">
          Selected students
          <b-form-select v-model="selected" :options="selectedStudentsOptions" :select-size="10"></b-form-select>
        </div>

      </b-form-group>

      <!-- <multiselect v-model="studentsValue" :options="studentsOptions" :multiple="true"></multiselect> -->

      <base-button :loading="loading"></base-button>

    </b-form>
    
  </div>
</template>

<script>
import BocaService from '@/services/BocaService.js'
import BaseButton from '@/components/BaseButton.vue'

export default {
  data() {
    return {
      loading: false,
      token: this.$store.state.token,
      importFromWorkingValue: 'None',
      importFromWorkingOptions: ['None','teste', 'teste2'],
      studentsOptions: ['teste1', 'teste2'],
      studentsValue: null,
      unselected: null,
      selected: null,
      unselectedStudents: [],
      selectedStudents: [],
      unselectedStudentsOptions: null,
      selectedStudentsOptions: null,
      working: {}
    }
  },
  components: {
    BaseButton
  },
  methods: {
    submitForm: function (e) {
      e.preventDefault();
      this.$toastr.removeByType("error");
      const formData = {
        name: this.working.name,
        start_date: this.working.start_date + ' ' + this.working.start_time,
        finish_date: this.working.finish_date + ' ' + this.working.finish_time,
        students: this.selectedStudents.map(({id}) => (id))
      }
      this.loading = true

      if (this.working.id) {
        BocaService.putWorking(this.token, this.working.id, formData)
          .then(response => {
            console.log(response)
            this.$router.push('/workings');
          })
          .catch(error => {
            switch (error.response.status) {
            case 422:
              Object.entries(error.response.data.errors).forEach((element) => {
                this.$toastr.e(element[1])
              });
              break
            default: 
              this.$toastr.e('An error has ocurred')
            }
          })
          .then(() => {
            this.loading = false;
          });
      } else {
        BocaService.postWorking(this.token, formData)
          .then(response => {
            console.log(response)
            this.$router.push('/workings');
          })
          .catch(error => {
            switch (error.response.status) {
            case 422:
              Object.entries(error.response.data.errors).forEach((element) => {
                this.$toastr.e(element[1])
              });
              break
            default: 
              this.$toastr.e('An error has ocurred')
            }
          })
          .then(() => {
            this.loading = false;
          });
      }
    },
    getStudentsFromWorking(working_id) {
      BocaService.getUsers(this.token, 'student', working_id)
          .then(response => {
            this.selectedStudents = response.data
            this.unselectedStudents = this.unselectedStudents.filter( student => {
              return !this.selectedStudents.find(function(studentInWorking) {
                return student.id === studentInWorking.id
              })
            })
            this.parseOptions()

          })
          .catch(error => {
            console.log(error)
            this.$toastr.e('An error has ocurred')
          })
    },
    select(student) {
      var removeIndex = this.unselectedStudents.map(function(item) { return item.id; }).indexOf(student.id);
      this.unselectedStudents.splice(removeIndex, 1);
      this.selectedStudents.push(student)
      this.parseOptions()
    },
    unselect(student) {
      var removeIndex = this.selectedStudents.map(function(item) { return item.id; }).indexOf(student.id);
      this.selectedStudents.splice(removeIndex, 1);
      this.unselectedStudents.push(student)
      this.parseOptions()
    },
    parseOptions() {
      this.unselectedStudentsOptions = this.unselectedStudents.map(({id, username}) => ({value: {id, username}, text: username}))
      this.selectedStudentsOptions = this.selectedStudents.map(({id, username}) => ({value: {id, username}, text: username}))

    },
    selectStudent() {
      if (!this.unselected) {
        return
      }
      this.select(this.unselected)
      this.unselected = null
      this.selected = null
    },
    unselectStudent() {
      if (!this.selected) {
        return
      }
      this.unselect(this.selected)
      this.selected = null
      this.unselected = null
    },
  },
  created() {
    if (this.$route.params.working_id) {
      BocaService.getWorking(this.token, this.$route.params.working_id)
        .then(response => {
          let working = response.data
          let start_date = working.start_date
          let finish_date = working.finish_date

          working.start_date = this.$moment.utc(start_date).format('Y-MM-DD')
          working.start_time = this.$moment.utc(start_date).format('HH:mm:ss')

          working.finish_date = this.$moment.utc(finish_date).format('Y-MM-DD')
          working.finish_time = this.$moment.utc(finish_date).format('HH:mm:ss')

          this.working = working
        })
        .catch(error => {
          console.log(error)
          this.$toastr.e('An error has ocurred')
        })
    }

    BocaService.getUsers(this.token, 'student')
      .then(response => {
        this.unselectedStudents = response.data
        if (this.working.id) {
          this.getStudentsFromWorking(this.working.id)
        }
        this.parseOptions()

      })
      .catch(error => {
        console.log(error)
        this.$toastr.e('An error has ocurred')
      })
  },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped>
#working-form {
  width: 40%;
  margin:0 auto;
}
.inline-block {
  display: inline-block
}
.selectButton {
  display: block;
  margin: 0 auto;
}
</style>