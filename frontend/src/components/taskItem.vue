<template>
  <div>
    <input type = "checkbox" v-model = "task.complete" @click= "onCheckBoxClicked">
    {{ addtxt }} 
    <!-- <input type="checkbox" v-bind="complete"/> -->
    <!-- <h2>{{ text }}</h2> -->

    <span>{{ task.complete}} | {{ task.text }} </span>
    <div v-if="task.complete"></div>
    <span>{{ task.complete }} | {{ task.text }}</span>

  </div>
</template>

<script>
export default 
{
  name: "TaskItem",
  props: 
  {
    task: Object,
  },
  methods: 
  {
      onCheckBoxClicked() 
      {
        console.log(this.task.complete)
        console.log("CheckBox clicked!")
      },
  },
}
</script>

<style>
  
</style>
