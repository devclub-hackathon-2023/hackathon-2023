<template>
    <h2>Login Page</h2><br>
    <div class="login">
    <form id="login" method="get" action="login.php">
        <label><b>User Name
        </b>
        </label>
        <input type="text" name="Uname" id="Uname" placeholder="Username">
        <br><br>
        <label><b>Password
        </b>
        </label>
        <input type="Password" name="Pass" id="Pass" placeholder="Password">
        <br><br>
        <input type="button" name="log" id="log" value="Log In Here">
        <br><br>
        <input type="checkbox" id="check">
        <span>Remember me</span>
        <br><br>
        <a href="#">Forgot Password</a> >
        
        <br><br>
        <img src ="../../public/BeeSmiling.png" width="150" height="150">
    </form>

</div>
</template>

<script>
export default {
  name: 'HomeView',
}
</script>
<style>
body
{
    margin: 0;
    padding: 0;
    background-color:#f3e015ba;
    font-family: 'Arial';
}
.login{
        width: 382px;
        overflow: hidden;
        margin: auto;
        margin: 20 0 0 450px;
        padding: 80px;
        background: #0c0f0e;
        border-radius: 15px ;

}
h2{
    text-align: center;
    color: #5d2901;
    padding: 20px;
}
label{
    color: #d7dcdb;
    font-size: 17px;
}
#Uname{
    width: 300px;
    height: 30px;
    border: none;
    border-radius: 3px;
    padding-left: 8px;
}
#Pass{
    width: 300px;
    height: 30px;
    border: none;
    border-radius: 3px;
    padding-left: 8px;

}
#log{
    width: 300px;
    height: 30px;
    border: none;
    border-radius: 17px;
    padding-left: 7px;
    color: rgb(44, 24, 1);


}
span{
    color: white;
    font-size: 17px;
}
a{
    float: right;
    color: white;
 
}
</style>