<template>

    <div class= "ViewToDos">
      <h1>Your To Do List:</h1>
    </div>
    <div class ="taskThing">
      <taskItem v-for="task in tasks" :task="task" :key="task.id" @deleteTask="onDeleteTask"/>
    </div>
    <div class="checklist">
      <br>

      <h1>Add new task to list:</h1>
      <input type= "text" id="add" v-model="newTask.text">

      <br><br>

      <button value="add task" @click="onAddTaskClicked"> {{ addtxt }} </button><br><br>

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

      
      await fetch("http://127.0.0.1:5000/api/todo", requestOptions).then((response) => response.json())
      .then((response) => {
        return response
        })
        .then((result) => {
          console.log("tasks: " + result)

          delete result["username"]
          delete result["pass"]
          delete result["userID"]
          let keys = Object.keys(result)
          let values = Object.values(result)

          for (let i = 0; i < keys.length; i++) {
            console.log("key: " + keys[i])
            console.log("value: " + values[i])
            this.tasks.push({ complete: (values[i] == 'true'), text: keys[i]})
          }
        })
        .catch((error) => {
          console.log("error: " + error)
        })
    },
    async onDeleteTask(task) {
      console.log("delete task: " + task)
      
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userID: this.$store.state.userID, taskname: task, taskvalue: true })
      };

      await fetch("http://127.0.0.1:5000/api/todo", requestOptions).then((response) => response.json())
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
  font-size: 16px;
  font-family: sans-serif;
}
.taskThing
{
    width: 300px;
    overflow: hidden;
    margin: auto;
    margin: 5 20 0 100px;
    padding: 50px;
    background: rgb(163, 79, 26);
    border-radius: 15px ;
}

</style>