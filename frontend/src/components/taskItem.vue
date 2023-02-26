<template>

  <div v-if="task.complete" class="taskContainer">
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
<<<<<<< HEAD
        console.log("CheckBox clicked!")
=======
        console.log("deleting task...")
        this.$emit("deleteTask", this.task.text)
>>>>>>> e8a71addb0a34b5cfdad020104c2c336ca98f0b3
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
