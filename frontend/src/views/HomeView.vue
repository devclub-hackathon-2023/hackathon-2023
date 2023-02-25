<template>

  <h1 class="welcomeTxt"> {{ welcomeTxt }} </h1>
  
  <br>

  <p>ID: {{ this.$store.state.userID }}</p>

  <button class="homeButton" v-text="loginTxt" @click="onLoginClicked"/>
  
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      welcomeTxt: "Welcome to the Bee's Kneez",
      loginTxt: "Login / Register",
    }
  },
  methods: {
    onLoginClicked() {
      console.log("Login was clicked!")
      this.$router.push("/login")
    }
  }
}
</script>

<style>

.welcomeContainer {
  width: 382px;
  overflow: hidden;
  margin: auto;
  margin: 20 0 0 450px;
  padding: 80px;
  background: #0c0f0e;
  border-radius: 15px ;
}

.homeButton {
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  font-size: 18px;
  width: 60%;
  margin: auto;
  padding: 10px;
  border-radius: 5px;
}

.welcomeTxt {
  text-align: center;
  color: #5d2901;
  padding: 20px;
}

</style>