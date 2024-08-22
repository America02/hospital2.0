<template>
  <div class="container mx-auto p-6">
    <h1 class="text-4xl font-bold text-center text-gray-800 mb-6">Puestos</h1>
    <div class="shadow-lg rounded-lg overflow-hidden bg-white">
      <table class="w-full table-fixed">
        <thead class="bg-gray-200">
          <tr>
            <th class="w-1/4 py-3 px-4 text-left text-gray-700 font-bold uppercase">Nombre</th>
            <th class="w-1/3 py-3 px-4 text-left text-gray-700 font-bold uppercase">Descripción</th>
            <th class="w-1/4 py-3 px-4 text-left text-gray-700 font-bold uppercase">Salario</th>
            <th class="w-1/4 py-3 px-4 text-left text-gray-700 font-bold uppercase">Turno</th>
          </tr>
        </thead>
        <tbody class="bg-white">
          <tr v-for="puesto in puestos" :key="puesto.PuestoID" class="hover:bg-gray-50">
            <td class="py-4 px-6 border-b border-gray-200">{{ puesto.Nombre }}</td>
            <td class="py-4 px-6 border-b border-gray-200">{{ puesto.Descripcion }}</td>
            <td class="py-4 px-6 border-b border-gray-200">{{ puesto.Salario }}</td>
            <td class="py-4 px-6 border-b border-gray-200">{{ puesto.Turno }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      puestos: [],
      token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6Implc3MiLCJDb3JyZW9fRWxlY3Ryb25pY28iOiJzdHJpbmciLCJDb250cmFzZW5hIjoiMTIzIiwiTnVtZXJvX1RlbGVmb25pY29fTW92aWwiOiJzdHJpbmcifQ.eulYRMRY3dI3pLCOX2Q35hlCTmUxSMYOvd2btfgFAeg'  // Reemplaza con tu token real
    };
  },
  mounted() {
    this.obtenerPuestos();
  },
  methods: {
    async obtenerPuestos() {
      try {
        const response = await axios.get('http://localhost:8000/puestos', {
          headers: {
            'Authorization': `Bearer ${this.token}`
          }
        });
        this.puestos = response.data;
      } catch (error) {
        console.error('Error al obtener los puestos:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Diseño mejorado para la tabla */
.container {
  max-width: 1200px;
}

table {
  border-collapse: collapse;
}

thead th {
  background-color: #f3f4f6;
}

tbody tr:hover {
  background-color: #f9fafb;
}

td {
  font-size: 16px;
  color: #4b5563;
}

th {
  font-size: 16px;
}
</style>
