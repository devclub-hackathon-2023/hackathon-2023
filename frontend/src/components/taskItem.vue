<template>
<<<<<<< HEAD
  <div v-if="!task.complete" class="taskContainer">
=======

  <div v-if="task.complete" class="taskContainer">
>>>>>>> 17f4340eb4ed9f2643dbfb6c6f073f56066c0c9d
    <span class="deleteIcon" @click= "onDeleteClicked"> [x] </span>
    <span class="taskText">{{ task.text }}</span>

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
  data()
  {
    return{
      thing: this.Object,
    }
  },
  methods: 
  {
      onDeleteClicked() 
      {
        console.log("deleting task...")
        this.$emit("deleteTask", this.task.text)
      },
  },
}
</script>

<style>
.deleteIcon {
  font-size: 20px;
  font-weight: bold;
}

.taskText {
  font-size: 20px;
  padding-left: 5px;
}

.taskContainer {
  margin-left: 45%;
  display: flex;
  padding: 10px;
}
</style>
