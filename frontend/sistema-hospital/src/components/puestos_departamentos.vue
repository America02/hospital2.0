<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Gestión de Puestos por Departamento</h1>
      <form @submit.prevent="agregarPuestoDepto" class="mb-4">
        <div class="grid grid-cols-2 gap-4">
          <input v-model="nuevoPuesto.Nombre" type="text" placeholder="Nombre" class="p-2 border rounded" required />
          <input v-model="nuevoPuesto.Descripcion" type="text" placeholder="Descripción" class="p-2 border rounded" />
          <input v-model="nuevoPuesto.Salario" type="number" placeholder="Salario" class="p-2 border rounded" />
          <select v-model="nuevoPuesto.Turno" class="p-2 border rounded">
            <option disabled value="">Seleccionar turno</option>
            <option value="Mañana">Mañana</option>
            <option value="Tarde">Tarde</option>
            <option value="Noche">Noche</option>
          </select>
          <input v-model="nuevoPuesto.DepartamentoID" type="number" placeholder="Departamento ID" class="p-2 border rounded" required />
        </div>
        <button type="submit" class="bg-blue-500 text-white p-2 rounded mt-4">Agregar Puesto</button>
      </form>
  
      <table class="w-full border-collapse bg-white">
        <thead class="bg-gray-100">
          <tr>
            <th class="border p-2">Nombre</th>
            <th class="border p-2">Descripción</th>
            <th class="border p-2">Salario</th>
            <th class="border p-2">Turno</th>
            <th class="border p-2">Departamento ID</th>
            <th class="border p-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="puesto in puestos" :key="puesto.PuestoID" class="text-center">
            <td class="border p-2">{{ puesto.Nombre }}</td>
            <td class="border p-2">{{ puesto.Descripcion }}</td>
            <td class="border p-2">{{ puesto.Salario }}</td>
            <td class="border p-2">{{ puesto.Turno }}</td>
            <td class="border p-2">{{ puesto.DepartamentoID }}</td>
            <td class="border p-2">
              <button @click="editarPuesto(puesto)" class="bg-yellow-500 text-white p-1 rounded mx-1">Editar</button>
              <button @click="eliminarPuesto(puesto.PuestoID)" class="bg-red-500 text-white p-1 rounded mx-1">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        nuevoPuesto: {
          Nombre: '',
          Descripcion: '',
          Salario: '',
          Turno: '',
          DepartamentoID: ''
        },
        puestos: [],
        editando: false,
        idEditando: null
      };
    },
    methods: {
      async obtenerPuestos() {
        try {
          const response = await fetch('/api/puestos_departamentos');
          if (response.ok) {
            this.puestos = await response.json();
          } else {
            console.error('Error al obtener los puestos por departamento:', response.statusText);
          }
        } catch (error) {
          console.error('Error al obtener los puestos por departamento:', error);
        }
      },
      async agregarPuestoDepto() {
        try {
          let response;
          if (this.editando) {
            response = await fetch(`/api/puestos_departamentos/${this.idEditando}`, {
              method: 'PUT',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(this.nuevoPuesto)
            });
            this.editando = false;
            this.idEditando = null;
          } else {
            response = await fetch('/api/puestos_departamentos', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(this.nuevoPuesto)
            });
          }
  
          if (response.ok) {
            this.nuevoPuesto = { Nombre: '', Descripcion: '', Salario: '', Turno: '', DepartamentoID: '' };
            await this.obtenerPuestos();
          } else {
            console.error('Error al guardar el puesto por departamento:', response.statusText);
          }
        } catch (error) {
          console.error('Error al agregar o actualizar el puesto por departamento:', error);
        }
      },
      editarPuesto(puesto) {
        this.nuevoPuesto = { ...puesto };
        this.editando = true;
        this.idEditando = puesto.PuestoID;
      },
      async eliminarPuesto(id) {
        try {
          const response = await fetch(`/api/puestos_departamentos/${id}`, {
            method: 'DELETE'
          });
  
          if (response.ok) {
            await this.obtenerPuestos();
          } else {
            console.error('Error al eliminar el puesto por departamento:', response.statusText);
          }
        } catch (error) {
          console.error('Error al eliminar el puesto por departamento:', error);
        }
      }
    },
    mounted() {
      this.obtenerPuestos();
    }
  };
  </script>
  
  <style scoped>
  .container {
    background-color: #f9f9f9;
    padding: 2rem;
    border-radius: 0.5rem;
  }
  button {
    transition: background-color 0.3s ease;
  }
  button:hover {
    background-color: #333;
  }
  </style>
  