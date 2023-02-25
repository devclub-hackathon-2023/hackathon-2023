<template>
    <div class= "ViewToDos">
      <h1>Your To Do List:</h1>
    </div>
    <div class="checklist">
             <h1>Complete or Add to your list!</h1>
             <br>
             <form class="checklist" method="post">
              <br> <br>
                 <button type="button" id="addListButton" @click="onAddNew()">
                  {{ addtxt }}
            </button>
            <br>
            <p> </p><textarea id="comment" name="comments" rows="1" cols="20"></textarea>
            </form>
            <br><br>
            <ul id="list"></ul>
            <input type= "list" value = "addToList" id = "add">
             
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