<template>
  <h1 class="PointsTxt"> {{ PointsTxt }} </h1>
 
</template>


<script>

export default {
  name: 'PtsView',
  
  data(){
    return{
      PointsTxt: "Congratulations you have successfully completed some tasks from your list",
    }
  },
}
</script>

<style>
.PointsTxt {
  text-align: center;
  color: #5d2901;
  padding: 25px;
}
</style>