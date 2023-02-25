<template>
  <div>
    <!-- <input type="checkbox" v-bind="complete"/> -->
    <!-- <h2>{{ text }}</h2> -->
    <span>{{ task.complete }} | {{ task.text }}</span>
  </div>
</template>

<script>
export default {
  name: "TaskItem",
  props: {
    task: Object,
  }
}
</script>

<style>

</style>