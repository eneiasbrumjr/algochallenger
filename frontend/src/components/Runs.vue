<template>
  <div>
    <h1> Runs</h1>
    <template v-if="user.type == 'student'">
      <b-button :to="{name: 'CreateRun'}" variant="primary">New Run</b-button>
    </template>
    <base-table id="runs_table" :data="runs" :fields="tableFields" :loading="loading">
    <template v-slot:default="slotProps">
      <div class="custom-actions actions-wrapper">
        <b-button type="button" variant="primary" class="mr-1" @click="download(slotProps.parentProps.rowData.id)">
          <i class="download icon"></i> Download
        </b-button>
      </div>
    </template>
    </base-table>
  </div>
</template>

<script>
import BocaService from '@/services/BocaService.js'
import BaseTable from '@/components/BaseTable.vue'

export default {
  components: {
    BaseTable
  },
  data() {
    return {
      token: this.$store.state.token,
      user: this.$store.state.user,
      runs:[],
      loading: false,
      tableFields: [
        {
          title: 'ID',
          name: 'id'
        },
        {
          title: 'File name',
          name: 'file_name'
        },
        {
          title: 'Answer',
          name: 'jail_answer'
        },
        {
          title: 'Created at',
          name: 'created_at',
          callback: (value) =>  {
            return this.$moment(value).format('MM/DD/YYYY HH:mm:ss')
          }
        },
        {
          name: '__slot:custom-actions',
          title: 'Actions'
        }
      ]
    }
  },
  methods: {
      download(runId) {
        BocaService.getRunFile(this.token, runId)
        .then(response => {
          const blob = new Blob([response.data])
          const link = document.createElement('a')
          link.href = URL.createObjectURL(blob, 'teste.c')
          link.download = 'teste.c'
          link.click()
          URL.revokeObjectURL(link.href)
        })
      }
  },
  created() {
    this.loading = true
    BocaService.getRuns(this.token, this.$route.params.problem_id)
      .then(response => {
        this.loading = false
        this.runs = response.data.map(({id, file_name, created_at, jail_answer}) => ({id, file_name, created_at, jail_answer}))
      })
      .catch(response => {
        this.loading = false
        console.log(response)
      })
  }
}
</script>

<style scoped>
#runs_table {
  width: 90%;
  margin: 0 auto;
  padding-bottom: 100px;
}
</style>