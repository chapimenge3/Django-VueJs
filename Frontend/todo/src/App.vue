<template>
<div>
  <HelloWorld msg="Welcome to Your Todo App"/>
  <span> Add Todo:</span>
  <p style="white-space: pre-line;">{{ newTodo }}</p>
  <br>
  <textarea v-model="newTodo" placeholder="Add Todo "></textarea>
  <ul id="example-1">
  <li v-for="todos in todo" :key="todos.id">
    <label :for="todos.id"></label>
    {{ todos.description }}
  </li>
</ul>


</div>
    
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios' 

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      todo: null, 
      newTodo: null
    }
  },
  created(){
    this.todo = this.fetchTodo();
    console.log("this printed");
  },
  methods: {
    fetchTodo(){
      axios
      .get('http://127.0.0.1:8000/todo/')
      .then(response=>{
        this.todo = response.data;
        return response;
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
