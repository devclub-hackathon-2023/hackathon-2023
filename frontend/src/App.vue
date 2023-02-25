<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to= "/ViewLists">ViewLists</router-link>
  </nav>
  <router-view/>
 
</template>

<script>

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: goldenrod;
}

nav a.router-link-exact-active {
  color: goldenrod;
}

</style>
