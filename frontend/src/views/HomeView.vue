<template>
  <div class="homeBackground">
    <div class="welcome">
      {{ welcomeTxt }}
    </div>
    <div>
      <div class="loginButton" @click="onLoginClicked">
        {{ loginTxt }}
      </div>
      <div class="signupButton" @click="onSignUpClicked">
        {{ signupTxt }}
      </div>
    </div>
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
    onSignUpClicked() {
      console.log("Signup was clicked!")
    }
  }
}
</script>

<style>
.homeBackground {
  background-image: "../assets/honey-background.jpg";
}
.welcome {
  background-color: lightyellow;
  font-size: 16px;
  font-family: sans-serif;
}

.login {
  border-style: 1px;
}
</style>