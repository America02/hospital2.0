<template>
  <div class="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-md">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Gestión de Puestos por Departamento</h1>
    
    <!-- Formulario para agregar o editar puesto -->
    <form @submit.prevent="agregarOActualizarPuesto" class="space-y-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="form-group">
          <label for="nombre" class="block text-gray-700">Nombre</label>
          <input v-model="nuevoPuesto.Nombre" id="nombre" type="text" placeholder="Nombre" class="p-3 border border-gray-300 rounded-lg w-full" required />
        </div>
        <div class="form-group">
          <label for="descripcion" class="block text-gray-700">Descripción</label>
          <input v-model="nuevoPuesto.Descripcion" id="descripcion" type="text" placeholder="Descripción" class="p-3 border border-gray-300 rounded-lg w-full" />
        </div>
        <div class="form-group">
          <label for="salario" class="block text-gray-700">Salario</label>
          <input v-model="nuevoPuesto.Salario" id="salario" type="number" placeholder="Salario" class="p-3 border border-gray-300 rounded-lg w-full" />
        </div>
        <div class="form-group">
          <label for="turno" class="block text-gray-700">Turno</label>
          <select v-model="nuevoPuesto.Turno" id="turno" class="p-3 border border-gray-300 rounded-lg w-full">
            <option disabled value="">Seleccionar turno</option>
            <option value="Mañana">Mañana</option>
            <option value="Tarde">Tarde</option>
            <option value="Noche">Noche</option>
          </select>
        </div>
        <div class="form-group">
          <label for="departamentoID" class="block text-gray-700">Departamento ID</label>
          <input v-model="nuevoPuesto.DepartamentoID" id="departamentoID" type="number" placeholder="Departamento ID" class="p-3 border border-gray-300 rounded-lg w-full" required />
        </div>
      </div>
      <button type="submit" class="bg-blue-500 text-white p-3 rounded-lg w-full hover:bg-blue-600 transition duration-300">
        {{ editando ? 'Actualizar Puesto' : 'Guardar Puesto' }}
      </button>
    </form>

    <!-- Tabla para mostrar los puestos por departamento -->
    <table class="mt-6 w-full bg-white rounded-lg shadow-md">
      <thead class="bg-gray-100 text-gray-600">
        <tr>
          <th class="py-3 px-4 border-b">Nombre</th>
          <th class="py-3 px-4 border-b">Descripción</th>
          <th class="py-3 px-4 border-b">Salario</th>
          <th class="py-3 px-4 border-b">Turno</th>
          <th class="py-3 px-4 border-b">Departamento ID</th>
          <th class="py-3 px-4 border-b">Fecha Registro</th>
          <th class="py-3 px-4 border-b">Fecha Actualización</th>
          <th class="py-3 px-4 border-b">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="puesto in puestos" :key="puesto.PuestoID">
          <td class="py-3 px-4 border-b">{{ puesto.Nombre }}</td>
          <td class="py-3 px-4 border-b">{{ puesto.Descripcion }}</td>
          <td class="py-3 px-4 border-b">{{ puesto.Salario }}</td>
          <td class="py-3 px-4 border-b">{{ puesto.Turno }}</td>
          <td class="py-3 px-4 border-b">{{ puesto.DepartamentoID }}</td>
          <td class="py-3 px-4 border-b">{{ new Date(puesto.Creado).toLocaleDateString() }}</td>
          <td class="py-3 px-4 border-b">{{ puesto.Modificado ? new Date(puesto.Modificado).toLocaleDateString() : 'Nunca' }}</td>
          <td class="py-3 px-4 border-b text-center">
            <button @click="editarPuesto(puesto)" class="bg-yellow-500 text-white p-2 rounded-lg hover:bg-yellow-600 transition duration-300">Editar</button>
            <button @click="eliminarPuesto(puesto.PuestoID)" class="bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition duration-300 mt-2">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      puestos: [],
      nuevoPuesto: {
        Nombre: '',
        Descripcion: '',
        Salario: '',
        Turno: '',
        DepartamentoID: ''
      },
      editando: false,
      idEditando: null,
      token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6Ikplc3MiLCJDb3JyZW9fRWxlY3Ryb25pY28iOiJqZXNzQDEuY29tIiwiQ29udHJhc2VuYSI6IjEyMyIsIk51bWVyb19UZWxlZm9uaWNvX01vdmlsIjoiNzY0MTExMTExMSJ9.0nMdZw0ZcxmDvVwW9N9e7ztfXxhBdeY8DJB5WCMwx-8'
    };
  },
  methods: {
    async obtenerPuestos() {
      try {
        const response = await axios.get('http://localhost:8000/puestos_departamentos', {
          headers: {
            'Authorization': `Bearer ${this.token}`
          }
        });
        this.puestos = response.data;
      } catch (error) {
        console.error('Error al obtener los puestos:', error);
      }
    },
    async agregarOActualizarPuesto() {
      try {
        let response;
        const puestoData = { ...this.nuevoPuesto };

        // Agrega valores predeterminados para Creado y Modificado si están vacíos
        if (!puestoData.Creado) {
          puestoData.Creado = new Date().toISOString();
        }
        if (!puestoData.Modificado) {
          puestoData.Modificado = new Date().toISOString();
        }

        if (this.editando) {
          response = await axios.put(`http://localhost:8000/puesto_departamento/${this.idEditando}`, puestoData, {
            headers: {
              'Authorization': `Bearer ${this.token}`
            }
          });
          this.editando = false;
          this.idEditando = null;
        } else {
          response = await axios.post('http://localhost:8000/puestos_departamentos', puestoData, {
            headers: {
              'Authorization': `Bearer ${this.token}`
            }
          });
        }

        if (response.status === 200 || response.status === 201) {
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
        await axios.delete(`http://localhost:8000/puesto_departamento/${id}`, {
          headers: {
            'Authorization': `Bearer ${this.token}`
          }
        });
        await this.obtenerPuestos();
      } catch (error) {
        console.error('Error al eliminar el puesto:', error);
      }
    }
  },
  created() {
    this.obtenerPuestos();
  }
};
</script>

<style scoped>
/* Estilos personalizados para una mejor apariencia */
.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #4a5568;
}

button {
  font-size: 1rem;
  font-weight: 600;
  border: none;
  cursor: pointer;
}

button:hover {
  opacity: 0.9;
}

button:focus {
  outline: none;
}
</style>
