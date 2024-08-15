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
            <tr>
                <td class="py-4 px-6 border-b border-gray-200">1</td>
                <td class="py-4 px-6 border-b border-gray-200 truncate">Servicios Médicos</td>
                <td class="py-4 px-6 border-b border-gray-200">Atención y cuidado de la salud.</td>
                <td class="py-4 px-6 border-b border-gray-200">
                    <span class="bg-green-500 text-white py-1 px-2 rounded-full text-xs">Activo</span>
                </td>
                <td class="py-4 px-6 border-b border-gray-200">2024-01-15</td>
                <td class="py-4 px-6 border-b border-gray-200">2024-08-10</td>
            </tr>
            <tr>
                <td class="py-4 px-6 border-b border-gray-200">2</td>
                <td class="py-4 px-6 border-b border-gray-200 truncate">Servicios de apoyo</td>
                <td class="py-4 px-6 border-b border-gray-200">Servicios auxiliares para atención médica.</td>
                <td class="py-4 px-6 border-b border-gray-200">
                    <span class="bg-green-500 text-white py-1 px-2 rounded-full text-xs">Activo</span>
                </td>
                <td class="py-4 px-6 border-b border-gray-200">2023-11-20</td>
                <td class="py-4 px-6 border-b border-gray-200">2024-07-30</td>
            </tr>
            <tr>
                <td class="py-4 px-6 border-b border-gray-200">3</td>
                <td class="py-4 px-6 border-b border-gray-200 truncate">Servicios Médicos-Administrativos</td>
                <td class="py-4 px-6 border-b border-gray-200">Por definir</td>
                <td class="py-4 px-6 border-b border-gray-200">
                    <span class="bg-green-500 text-white py-1 px-2 rounded-full text-xs">Activo</span>
                </td>
                <td class="py-4 px-6 border-b border-gray-200">2022-05-10</td>
                <td class="py-4 px-6 border-b border-gray-200">2024-03-22</td>
            </tr>
            <tr>
                <td class="py-4 px-6 border-b border-gray-200">4</td>
                <td class="py-4 px-6 border-b border-gray-200 truncate">Servicios de Enfermería</td>
                <td class="py-4 px-6 border-b border-gray-200">Cuidado y asistencia al paciente.</td>
                <td class="py-4 px-6 border-b border-gray-200">
                    <span class="bg-green-500 text-white py-1 px-2 rounded-full text-xs">Activo</span>
                </td>
                <td class="py-4 px-6 border-b border-gray-200">2021-08-08</td>
                <td class="py-4 px-6 border-b border-gray-200">2024-06-12</td>
            </tr>
            <!-- Add more rows here -->
            <tr>
                <td class="py-4 px-6 border-b border-gray-200">5</td>
                <td class="py-4 px-6 border-b border-gray-200 truncate">Departamento Administrativos</td>
                <td class="py-4 px-6 border-b border-gray-200">Gestión y organización interna institucional.</td>
                <td class="py-4 px-6 border-b border-gray-200">
                    <span class="bg-green-500 text-white py-1 px-2 rounded-full text-xs">Activo</span>
                </td>
                <td class="py-4 px-6 border-b border-gray-200">2021-08-08</td>
                <td class="py-4 px-6 border-b border-gray-200">2024-06-12</td>
            </tr>
            <tr>
                <td class="py-4 px-6 border-b border-gray-200">6</td>
                <td class="py-4 px-6 border-b border-gray-200 truncate">Nueva Área Médica</td>
                <td class="py-4 px-6 border-b border-gray-200">Por definir</td>
                <td class="py-4 px-6 border-b border-gray-200">
                    <span class="bg-red-500 text-white py-1 px-2 rounded-full text-xs">Inactivo</span>
                </td>
                <td class="py-4 px-6 border-b border-gray-200">2021-08-08</td>
                <td class="py-4 px-6 border-b border-gray-200">2024-06-12</td>
            </tr>

            
        </tbody>
    </table>
</div>

</template>
