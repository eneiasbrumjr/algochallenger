<template>
  <div class="home">
    <base-header></base-header>
    <hr>
    <router-view></router-view>
    <base-footer></base-footer>
  </div>
</template>

<script>
  import BaseHeader from '@/components/BaseHeader'
  import BaseFooter from '@/components/BaseFooter'

  export default {
    name: 'Home',
    components: {
      BaseHeader,
      BaseFooter
    },
    data: function () {
      return {
        username: this.$store.state.user.username
      }
    }
    // beforeCreate() {
    //   if (this.$store.state.token == '') {
    //     this.$router.push('/');
    //   }
    // }
  }
</script>

<style scoped>
.home {
  margin: 5% auto;
  width: 90%;
  /* height: 90%; */
  min-height: 90%;
  background-color: white;
  align-self: center;
  justify-self: center;
  position: relative;
}
</style>
