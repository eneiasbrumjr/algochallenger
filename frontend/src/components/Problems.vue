<template>
  <div>
    <h1> Problems</h1>
    <template v-if="user.type == 'admin'">
      <b-button :to="{name: 'CreateProblem'}" variant="primary">New Problem</b-button>
    </template>
    <base-table id="problems_table" :data="users" :fields="tableFields" :loading="loading">
      <template v-slot:default="slotProps">
        <div class="custom-actions actions-wrapper">
          <div v-if="user.type == 'admin'">
            <b-button class="mr-1" variant="info">
            <i class="zoom icon"></i> Edit
            </b-button>
            <b-button variant="danger" class="mr-1" @click="deleteAction(props.rowData, props.rowIndex)">
              <i class="trash icon"></i> Delete
            </b-button>
          </div>
          <b-button variant="primary" class="mr-1"
            :to="{name: 'Runs', params: { problem_id: slotProps.parentProps.rowData.id } }">
            <b-icon-code></b-icon-code> Runs
          </b-button>
        </div>
      </template>
    </base-table>
  </div>
</template>

<script>
import BocaService from '@/services/BocaService.js';
import BaseTable from '@/components/BaseTable.vue'

export default {
  components: {
    BaseTable
  },
  data() {
    return {
      token: this.$store.state.token,
      user: this.$store.state.user,
      users:[],
      loading: false,
      tableFields: [
        {
          title: 'ID',
          name: 'id'
        },
        {
          title: 'Name',
          name: 'name'
        },
        {
          title: 'Description file',
          name: 'description_file_name',
          callback: (value) =>  {
            return "<a class='downloadDescription' href='#'>" + value + "</a>"
          }
        },
        {
          title: 'Zip file',
          name: 'base_file_name',
          callback: (value) =>  {
            return "<a class='downloadZip' href='#'>" + value + "</a>"
          }
        },
        {
          name: '__slot:custom-actions',
          title: 'Actions'
        }
      ]
    }
  },
  props: {
    working: Object
  },
  methods: {
    cellClicked(problemId, problemFileName) {
      BocaService.getProblemZip(this.token, problemId)
        .then(response => {
          const blob = new Blob([response.data], { type: 'application/zip' })
          const link = document.createElement('a')
          link.href = URL.createObjectURL(blob, problemFileName)
          link.download = problemFileName
          link.click()
          URL.revokeObjectURL(link.href)
        })
    }
  },
  created() {
    this.loading = true;
    BocaService.getProblems(this.token, this.$route.params.working_id)
      .then(response => {
        this.loading = false;
        this.users = response.data.map(({id, name, base_file_name, description_file_name}) => ({id, name, base_file_name, description_file_name}))
      })
      .catch(response => {
        this.loading = false;
        this.$toastr.e('Forbidden');
        console.log(response)
      })

    $('body').on('click', '.downloadZip', (event) => {
      let id = $(event.target).closest('tr').find('td').first().text()
      let fileName = $(event.target).text()
      BocaService.getProblemZip(this.token, id)
        .then(response => {
          const blob = new Blob([response.data], { type: 'application/zip' })
          const link = document.createElement('a')
          link.href = URL.createObjectURL(blob, fileName)
          link.download = fileName
          link.click()
          URL.revokeObjectURL(link.href)
        })
    })

    $('body').on('click', '.downloadDescription', (event) => {
      let id = $(event.target).closest('tr').find('td').first().text()
      let fileName = $(event.target).text()
      BocaService.getProblemDescription(this.token, id)
        .then(response => {
          const blob = new Blob([response.data], { type: 'application/zip' })
          const link = document.createElement('a')
          link.href = URL.createObjectURL(blob, fileName)
          link.download = fileName
          link.click()
          URL.revokeObjectURL(link.href)
        })
    })
  }
}
</script>

<style scoped>
#problems_table {
  width: 90%;
  margin: 0 auto;
  padding-bottom: 100px;
}
</style>