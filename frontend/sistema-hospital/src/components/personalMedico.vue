<template>
    <div class="container">
      <h1 class="title">Registro de Personal Médico</h1>
      <form class="form">
        <div class="form-group">
          <label for="persona-id">Persona ID</label>
          <input type="text" id="persona-id" v-model="personalMedico.personaID" required>
        </div>
        
        <div class="form-group">
          <label for="departamento-id">Departamento ID</label>
          <input type="text" id="departamento-id" v-model="personalMedico.departamentoID" required>
        </div>
        
        <div class="form-group">
          <label for="especialidad">Especialidad</label>
          <input type="text" id="especialidad" v-model="personalMedico.especialidad" required>
        </div>
        
        <div class="form-group">
          <label for="tipo">Tipo</label>
          <input type="text" id="tipo" v-model="personalMedico.tipo" required>
        </div>
        
        <div class="form-group">
          <label for="cedula-profesional">Cédula Profesional</label>
          <input type="text" id="cedula-profesional" v-model="personalMedico.cedulaProfesional" required>
        </div>
        
        <div class="form-group">
          <label for="estatus">Estatus</label>
          <input type="text" id="estatus" v-model="personalMedico.estatus" required>
        </div>
        
        <div class="form-group">
          <label for="fecha-contratacion">Fecha de Contratación</label>
          <input type="date" id="fecha-contratacion" v-model="personalMedico.fechaContratacion" required>
        </div>
        
        <div class="form-group">
          <label for="fecha-terminacion-contrato">Fecha de Terminación de Contrato</label>
          <input type="date" id="fecha-terminacion-contrato" v-model="personalMedico.fechaTerminacionContrato" required>
        </div>
        
        <button type="submit" class="submit-button">Guardar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        personalMedico: {
          personaID: '',
          departamentoID: '',
          especialidad: '',
          tipo: '',
          cedulaProfesional: '',
          estatus: '',
          fechaContratacion: '',
          fechaTerminacionContrato: ''
        }
      };
    },
    methods: {
      guardar() {
        // Lógica para guardar los datos
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .title {
    font-size: 2.5em;
    color: #ff6f00;
    text-align: center;
    margin-bottom: 20px;
  }
  
  .form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    font-weight: bold;
    color: #007bff;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="date"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 1em;
  }
  
  .submit-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.2em;
    margin-top: 20px;
    transition: background-color 0.3s;
  }
  
  .submit-button:hover {
    background-color: #0056b3;
  }
  </style>
  