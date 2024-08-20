<template>
    <div class="shadow-lg rounded-lg overflow-hidden mx-4 md:mx-10">
      <table class="w-full table-fixed">
        <thead>
          <tr class="bg-gray-100">
            <th class="w-1/6 py-4 px-6 text-left text-gray-600 font-bold uppercase">ID</th>
            <th class="w-1/6 py-4 px-6 text-left text-gray-600 font-bold uppercase">Nombre</th>
            <th class="w-1/3 py-4 px-6 text-left text-gray-600 font-bold uppercase">Descripción</th>
            <th class="w-1/6 py-4 px-6 text-left text-gray-600 font-bold uppercase">Estatus</th>
            <th class="w-1/6 py-4 px-6 text-left text-gray-600 font-bold uppercase">Fecha Registro</th>
            <th class="w-1/6 py-4 px-6 text-left text-gray-600 font-bold uppercase">Fecha Actualización</th>
          </tr>
        </thead>
        <tbody class="bg-white">
          <tr v-for="item in data" :key="item.ID">
            <td class="py-4 px-6 border-b border-gray-200">{{ item.ID }}</td>
            <td class="py-4 px-6 border-b border-gray-200 truncate">{{ item.Nombre }}</td>
            <td class="py-4 px-6 border-b border-gray-200">{{ item.Descripcion }}</td>
            <td class="py-4 px-6 border-b border-gray-200">
              <span :class="{'bg-green-500': item.Estatus === 'Activo', 'bg-red-500': item.Estatus === 'Inactivo'}" class="text-white py-1 px-2 rounded-full text-xs">
                {{ item.Estatus }}
              </span>
            </td>
            <td class="py-4 px-6 border-b border-gray-200">{{ new Date(item.Fecha_Registro).toLocaleDateString() }}</td>
            <td class="py-4 px-6 border-b border-gray-200">{{ new Date(item.Fecha_Actualizacion).toLocaleDateString() }}</td>
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
      data: [],
      token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6IkFtZXJpY3giLCJDb3JyZW9fRWxlY3Ryb25pY28iOiJhQGdtYWlsLmNvbSIsIkNvbnRyYXNlbmEiOiIxMjM0IiwiTnVtZXJvX1RlbGVmb25pY29fTW92aWwiOiI3NjQxMDIyNDM2In0.kdfyhbc5v118pMnGZgW6YelWCDLK_6Xk_iDnbuN5p7E'  // Reemplaza con tu token real
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:8000/areas_medicas', {
        headers: {
          'Authorization': `Bearer ${this.token}`  // Agrega el token en el encabezado
        }
      })
        .then(response => {
          this.data = response.data;
          console.log(response.data);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  }
}

  </script>
  
  <style scoped>
  /* Añade estilos personalizados si es necesario */
  </style>
  