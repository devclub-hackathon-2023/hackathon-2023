<template>

  <h1 class="welcomeTxt"> {{ welcomeTxt }} </h1>
  
  <br>

  <div class="welcomeContainer">

      <button class="homeButton" v-text="loginTxt" @click="onLoginClicked"/>

      <br><br>

      <button class="homeButton" v-text="signupTxt" @click="onSignupClicked"/>

      <br><br>

  </div>
  
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      welcomeTxt: "Welcome to the Bee's Kneez",
      loginTxt: "Login",
      signupTxt: "Sign Up",
    }
  },
  methods: {
    onLoginClicked() {
      console.log("Login was clicked!")
    },
    onSignupClicked() {
      console.log("Signup was clicked!")
      this.$router.go("/login")
    }
  }
}
</script>

<style>

.welcomeContainer {
  width: 60%;
  overflow: hidden;
  margin: auto;
  padding: 40px;
  background: grey;
  border-radius: 15px;
}

.homeButton {
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  font-size: 18px;
  width: 80%;
  margin: auto;
  padding: 10px;
  border-radius: 5px;
}

.welcomeTxt {
    text-align: center;
    color: black;
    padding: 24px;
}

</style>