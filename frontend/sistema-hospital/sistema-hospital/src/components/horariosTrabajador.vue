<template>
    <div id="accordion-color" data-accordion="collapse" data-active-classes="bg-blue-100 dark:bg-gray-800 text-blue-600 dark:text-white">
        <h2 id="accordion-color-heading-1">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-800 dark:border-gray-700 dark:text-gray-400 hover:bg-blue-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-color-body-1" aria-expanded="true" aria-controls="accordion-color-body-1">
                <span>Registra un nuevo puesto</span>
                <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5" />
                </svg>
            </button>
        </h2>
        
        <div id="accordion-color-body-1" class="hidden" aria-labelledby="accordion-color-heading-1">
            <div class="flex items-center justify-center p-12">
                <div class="mx-auto w-full max-w-[550px] bg-white p-8 rounded-lg shadow-lg">
                    <h2 class="text-2xl font-bold text-center mb-1 text-[#07074D]">HOSPITAL PRIVILAGE CARE</h2>
                    <p class="text-sm text-center mb-8 text-[#6B7280]">HORARIO DE TRABAJO</p>
                    <form>
                        <div class="-mx-3 flex flex-wrap">
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="id" class="mb-3 block text-base font-medium text-[#07074D]">ID</label>
                                    <input type="text" name="id" id="id" placeholder="ID" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="nombre" class="mb-3 block text-base font-medium text-[#07074D]">Nombre</label>
                                    <input type="text" name="nombre" id="nombre" placeholder="Nombre" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="primer-apellido" class="mb-3 block text-base font-medium text-[#07074D]">Primer Apellido</label>
                                    <input type="text" name="primer-apellido" id="primer-apellido" placeholder="Primer Apellido" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="segundo-apellido" class="mb-3 block text-base font-medium text-[#07074D]">Segundo Apellido</label>
                                    <input type="text" name="segundo-apellido" id="segundo-apellido" placeholder="Segundo Apellido" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="puesto" class="mb-3 block text-base font-medium text-[#07074D]">Puesto</label>
                                    <input type="text" name="puesto" id="puesto" placeholder="Puesto" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="tipo" class="mb-3 block text-base font-medium text-[#07074D]">Tipo</label>
                                    <select name="tipo" id="tipo" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md">
                                        <option value="cirujano">Cirujano</option>
                                        <option value="pediatra">Pediatra</option>
                                        <option value="cardiologo">Cardiólogo</option>
                                        <option value="neurologo">Neurólogo</option>
                                        <option value="dermatologo">Dermatólogo</option>
                                    </select>
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="fecha-inicio" class="mb-3 block text-base font-medium text-[#07074D]">Fecha de Inicio</label>
                                    <input type="date" name="fecha-inicio" id="fecha-inicio" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="dia-semana" class="mb-3 block text-base font-medium text-[#07074D]">Día de la Semana</label>
                                    <input type="date" name="dia-semana" id="dia-semana" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="turno" class="mb-3 block text-base font-medium text-[#07074D]">Turno</label>
                                    <select name="turno" id="turno" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md">
                                        <option value="mañana">Mañana</option>
                                        <option value="tarde">Tarde</option>
                                        <option value="noche">Noche</option>
                                    </select>
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="hora-entrada" class="mb-3 block text-base font-medium text-[#07074D]">Horario de Entrada</label>
                                    <input type="time" name="hora-entrada" id="hora-entrada" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="hora-salida" class="mb-3 block text-base font-medium text-[#07074D]">Horario de Salida</label>
                                    <input type="time" name="hora-salida" id="hora-salida" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                        </div>
                        <div>
                            <button class="hover:shadow-form w-full rounded-md bg-[#95b8f6] py-3 px-8 text-center text-base font-semibold text-white outline-none">
                                Enviar
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <h2 id="accordion-color-heading-2">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-800 dark:border-gray-700 dark:text-gray-400 hover:bg-blue-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-color-body-2" aria-expanded="false" aria-controls="accordion-color-body-2">
                <span>Consulta los puestos existentes</span>
                <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5" />
                </svg>
            </button>
        </h2>
        <div id="accordion-color-body-2" class="hidden" aria-labelledby="accordion-color-heading-2">
            <div class="mt-4">
                <button type="button"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                    data-accordion-target="#accordion-color-body-1" aria-expanded="true" aria-controls="accordion-color-body-1">
                    Agregar Puesto
                </button>

                <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="px-6 py-3">ID</th>
                                <th scope="col" class="px-6 py-3">Nombre</th>
                                <th scope="col" class="px-6 py-3">Primer Apellido</th>
                                <th scope="col" class="px-6 py-3">Segundo Apellido</th>
                                <th scope="col" class="px-6 py-3">Puesto</th>
                                <th scope="col" class="px-6 py-3">Tipo</th>
                                <th scope="col" class="px-6 py-3">Fecha de Inicio</th>
                                <th scope="col" class="px-6 py-3">Día de la Semana</th>
                                <th scope="col" class="px-6 py-3">Turno</th>
                                <th scope="col" class="px-6 py-3">Horario de Entrada</th>
                                <th scope="col" class="px-6 py-3">Horario de Salida</th>
                                <th scope="col" class="px-6 py-3"><span class="sr-only">Edit</span></th>
                                <th scope="col" class="px-6 py-3"><span class="sr-only">Delete</span></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(puesto, index) in puestos" :key="index"
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ puesto.id }}</th>
                                <td class="px-6 py-4">{{ puesto.nombre }}</td>
                                <td class="px-6 py-4">{{ puesto.primerApellido }}</td>
                                <td class="px-6 py-4">{{ puesto.segundoApellido }}</td>
                                <td class="px-6 py-4">{{ puesto.puesto }}</td>
                                <td class="px-6 py-4">{{ puesto.tipo }}</td>
                                <td class="px-6 py-4">{{ puesto.fechaInicio }}</td>
                                <td class="px-6 py-4">{{ puesto.diaSemana }}</td>
                                <td class="px-6 py-4">{{ puesto.turno }}</td>
                                <td class="px-6 py-4">{{ puesto.horaEntrada }}</td>
                                <td class="px-6 py-4">{{ puesto.horaSalida }}</td>
                                <td class="px-6 py-4 text-right">
                                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                                </td>
                                <td class="px-6 py-4 text-right">
                                    <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Delete</a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            puestos: [
                {
                    id: "1",
                    nombre: "Juan",
                    primerApellido: "Perez",
                    segundoApellido: "Gomez",
                    puesto: "Cirujano",
                    tipo: "cirujano",
                    fechaInicio: "2023-01-01",
                    diaSemana: "Lunes",
                    turno: "Mañana",
                    horaEntrada: "08:00",
                    horaSalida: "14:00"
                },
                {
                    id: "2",
                    nombre: "Maria",
                    primerApellido: "Lopez",
                    segundoApellido: "Martinez",
                    puesto: "Pediatra",
                    tipo: "pediatra",
                    fechaInicio: "2023-02-01",
                    diaSemana: "Martes",
                    turno: "Tarde",
                    horaEntrada: "14:00",
                    horaSalida: "20:00"
                },
                {
                    id: "3",
                    nombre: "América",
                    primerApellido: "Estudillo",
                    segundoApellido: "Licona",
                    puesto: "Pediatra",
                    tipo: "pediatra",
                    fechaInicio: "2024-04-02",
                    diaSemana: "Martes",
                    turno: "Mañana",
                    horaEntrada: "09:00",
                    horaSalida: "15:00"
                }
            ]
        };
    }
};
</script>

<style scoped>
/* Aquí puedes agregar tus estilos personalizados */
</style>
