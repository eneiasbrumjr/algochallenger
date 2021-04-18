<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view/>
  </div>
</template>

<style>
@import 'https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.14/semantic.min.css';
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #E0E0CF;
  min-height: 100%;
  display: flex;
  overflow: auto;
}

html {
  min-height: 100%;
  margin: 0;
  padding: 0;
  overflow: auto;
}

.center {
	align-self: center;
  justify-self: center;
}

body {
  min-height: 100%;
  margin: 0;
  padding: 0;
  overflow: auto;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.actions-wrapper {
  display: flex;
}
</style>
