<template>

    <div class= "ViewToDos">
      <h1>Your To Do List:</h1>
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
export default 
{
  name: "ViewToDos",
  data() 
  {
    return {
      tasks: [],
      newTask: {
        completed: false,
        text: "",
      },
      welcomeTxt: "Select/Create a To-Do-List:",
      addtxt : "Update List",
    }
  },
  methods: 
  {
    onAddNew() 
    {
      document.getElementById("textAdded").innerText = document.getElementById("comment").value
      var hello = document.getElementById("comment").value
      console.log(hello)
      console.log("Update list checked");
    },
    onAddTaskClicked() {
      console.log("new task:" + this.newTask)
      this.tasks.push(this.newTask)
      this.newTask = ""
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