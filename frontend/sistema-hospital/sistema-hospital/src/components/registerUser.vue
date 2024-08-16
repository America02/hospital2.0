<template>
  <div class="xl bg-purple-700 text-white text-center p-5 ">
    <div class="columns-3">
      <div class="xl bg-indigo-300 text-white text-center p-5"></div>
      <span class="box-decoration-slice  bg-gradient-to-r from-gray-600 to-blue-500 text-white px-2 ...">
        BIENVENIDO
        <br/>
        HOSPITAL
        </span>
        <div class="xl bg-purple-300 text-white text-center p-5"></div>
        <div class="xl bg-fuchsia-500 text-white text-center p-5"></div>
    </div>
  </div>
 
    <div class="flex items-center justify-center p-12">
      
    <div class="w-full p-8 lg:w1/2">
      <Personas/>
    </div>
    <div class="w-full p-8 lg:w1/2">
        <usuario/>
    </div>
  </div>
  </template>

 <script>
  import Personas from './personas.vue'
  import Usuario from './usuario.vue'
  export default{
    components:{
      Personas,
      Usuario
    }
  }
</script>