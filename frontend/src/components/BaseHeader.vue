<template>
<div>
  <b-navbar toggleable="lg" type="light">
    <b-navbar-brand href="#">Boca</b-navbar-brand>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto">
          <b-nav-item :to="{ name: 'Workings'}">Workings</b-nav-item>
          <template v-if="user.type == 'admin'">
            <b-nav-item :to="{ name: 'Users'}">Users</b-nav-item>
          </template>
          <b-nav-item-dropdown right>
          <template v-slot:button-content>
            <em>{{user.full_name}}</em>
          </template>
          <b-dropdown-item @click="loggout()">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
import BocaService from '@/services/BocaService.js'
export default {
  data: function () {
      return {
        user: this.$store.state.user,
        isAdmin: this.$store.getters.isAdmin
      }
    },
  methods: {
    loggout() {
      BocaService.logout()
        .then( response => {
          console.log(response)
          this.$store.commit('CLEAR_USER_DATA')
          this.$router.push({name: 'Login'});
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>

</style>