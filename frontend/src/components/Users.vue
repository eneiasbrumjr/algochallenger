<template>
  <div>
    <h1>Users</h1>
    <b-button :to="{name: 'CreateUser'}" variant="primary">New User</b-button>
    <base-table id="users_table" :data="users" :fields="tableFields" :loading="loading"></base-table>
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
      loading: false,
      users:[],
      tableFields: [
        {
          title: 'ID',
          name: 'id'
        },
        {
          title: 'Full name',
          name: 'full_name'
        },
        {
          title: 'Username',
          name: 'username'
        },
        {
          title: 'Type',
          name: 'type'
        },
        {
          title: 'Enabled',
          name: 'is_enabled'
        }
      ]
    }
  },
  created() {
    this.loading = true
    BocaService.getUsers(this.token)
      .then(response => {
        this.loading = false
        this.users = response.data.map(({id, username, type, is_enabled, full_name}) => ({id, username, type, is_enabled, full_name}))
      })
      .catch(response => {
        this.loading = false
        console.log(response)
      })
  }
}
</script>

<style scoped>
#users_table {
  width: 90%;
  margin: 0 auto;
  padding-bottom: 100px;
}
</style>