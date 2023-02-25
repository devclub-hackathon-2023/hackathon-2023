<template>
  <div>
    <!-- <input type="checkbox" v-bind="complete"/> -->
    <!-- <h2>{{ text }}</h2> -->
    <div v-if="task.complete">completed</div>
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