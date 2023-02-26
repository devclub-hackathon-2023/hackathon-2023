<template>

    <div class= "ViewToDos">
      <h1>Your To Do List:</h1>
    </div>

    <taskItem v-for="task in tasks" :task="task" :key="task.id" @deleteTask="onDeleteTask"/>

    <div class="checklist">
      <br>

      <h1>Add new task to list:</h1>
      <input type= "text" id="add" v-model="newTask.text">
      <br><br>

      <button value="add task" @click="onAddTaskClicked"> {{ addtxt }} </button><br><br>
      <input type ="checkbox">
      {{ tasks }}
      <br><br>
    </div>
  <div id = "textAdded">

  </div>    
</template>

<script>
import taskItem from '@/components/taskItem.vue'

export default 
{
  name: "ViewToDos",
  components: {
    taskItem
  },
  data()
  {
    return {
      tasks: [],
      newTask: {
        complete: false,
        text: "",
      },
      welcomeTxt: "Select/Create a To-Do-List:",
      addtxt : "Update List",
    }
  },
  methods: 
  {
    async onAddTaskClicked() {
      console.log("new task: " + this.newTask)
      
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userID: this.$store.state.userID, taskname: this.newTask.text, taskvalue: false })
      };

      
      await fetch("http://127.0.0.1:5000/api/todo", requestOptions)
      .then((response) => {
        return response
        })
        .then((result) => {
          console.log("tasks: " + result)
          this.tasks = result
        })
        .catch((error) => {
          console.log("error: " + error)
        })

      // let newText = this.newTask.text
      // this.tasks.push({complete: false, text: newText})
      // this.newTask.text = ""

    },
    async onDeleteTask(task) {
      console.log("delete task: " + task)
      
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userID: this.$store.state.userID, taskname: task, taskvalue: true })
      };

      await fetch("http://127.0.0.1:5000/api/todo", requestOptions)
      .then((response) => {
        return response
        })
        .then((result) => {
          console.log("tasks: " + result)
          this.tasks = result
        })
        .catch((error) => {
          console.log("error: " + error)
        })
    }
  }
}
</script>

<style>
.ViewToDos
{
  background: goldenrod;
  font-size: 16px;
  font-family: sans-serif;
}

</style>