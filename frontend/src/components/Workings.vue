<template>
  <div>
    <h1>Workings</h1>
    <template v-if="user.type == 'admin'">
      <b-button class="m-1" :to="{name: 'CreateWorking'}" variant="primary">New Working</b-button>
    </template>
    <base-table id="workings_table" :data="workings" :fields="tableFields" :loading="loading">
    <template v-slot:default="slotProps">
      <div class="custom-actions actions-wrapper">
        <div v-if="user.type == 'admin' ">
          <b-button class="mr-1" variant="info"
            :to="{name: 'EditWorking', params: { working_id: slotProps.parentProps.rowData.id, working: slotProps.parentProps.rowData } }">
          <i class="zoom icon"></i> Edit
          </b-button>
          <b-button variant="danger" class="mr-1" @click="deleteAction(props.rowData, props.rowIndex)">
            <i class="trash icon"></i> Delete
            </b-button>
        </div>
        <b-button variant="primary" class="mr-1"
          :to="{name: 'Problems', params: { working_id: slotProps.parentProps.rowData.id, working: slotProps.parentProps.rowData } }">
          <b-icon-book></b-icon-book> Problems
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
  components: {BaseTable},
  data () {
    return {
      token: this.$store.state.token,
      user: this.$store.state.user,
      loading: false,
      workings:[],
      tableFields: [
        {
          title: 'Identifier',
          name: 'id',
          sortField: 'id'
        },
        {
          title: 'Name',
          name: 'name',
          sortField: 'name'
        },
        {
          title: 'Start date',
          name: 'start_date',
          sortField: 'start_date',
          callback: (value) =>  {
            return this.$moment.utc(value).format('MM/DD/YYYY HH:mm:ss')
          }
        }, 
        {
          title: 'Finish Date',
          name: 'finish_date',
          sortField: 'finish_date',
          callback: (value) =>  {
            return this.$moment.utc(value).format('MM/DD/YYYY HH:mm:ss')
          }
        },
        {
          title: 'Multilogin',
          name: 'is_multilogin',
          sortField: 'is_multilogin',
        },
        {
          name: '__slot:custom-actions',
          title: 'Actions'
        }
      ]
    }
  },
  created() {
    this.loading = true;
    BocaService.getWorkings(this.token)
      .then(response => {
        this.loading = false;
        this.workings = response.data.map(({id, name, start_date, finish_date, is_multilogin}) => ({id, name, start_date, finish_date, is_multilogin}))
      })
      .catch(response => {
        this.loading = false;
        console.log(response)
      })
  },
  methods: {
    editAction(a,b) {
      this.$router.push()
      console.log(b)
    }
  }
}
</script>

<style scoped>
#workings_table {
  width: 90%;
  margin: 0 auto;
  padding-bottom: 100px;
}

</style>