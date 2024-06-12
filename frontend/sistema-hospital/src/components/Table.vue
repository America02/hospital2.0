<template>


    <div id="accordion-color" data-accordion="collapse"
        data-active-classes="bg-blue-100 dark:bg-gray-800 text-blue-600 dark:text-white">
        <h2 id="accordion-color-heading-1">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-800 dark:border-gray-700 dark:text-gray-400 hover:bg-blue-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-color-body-1" aria-expanded="true"
                aria-controls="accordion-color-body-1">
                <span>Registra un nuevo puesto</span>
                <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M9 5 5 1 1 5" />
                </svg>
            </button>
        </h2>
        <div id="accordion-color-body-1" class="hidden" aria-labelledby="accordion-color-heading-1">
            <div class="flex items-center justify-center p-12">
                <!-- Author: FormBold Team -->
                <div class="mx-auto w-full max-w-[550px] bg-white p-8 rounded-lg shadow-lg">
                    <h2 class="text-2xl font-bold text-center mb-1 text-[#07074D]">HOSPITAL PRIVILAGE CARE</h2>
                    <p class="text-sm text-center mb-8 text-[#6B7280]">PUESTOS</p>
                    <form>
                        <div class="-mx-3 flex flex-wrap">
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="nombre-puesto"
                                        class="mb-3 block text-base font-medium text-[#07074D]">Nombre del
                                        Puesto</label>
                                    <input type="text" name="nombre-puesto" id="nombre-puesto"
                                        placeholder="Nombre del Puesto"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="departamento"
                                        class="mb-3 block text-base font-medium text-[#07074D]">Departamento</label>
                                    <input type="text" name="departamento" id="departamento" placeholder="Departamento"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="descripcion"
                                        class="mb-3 block text-base font-medium text-[#07074D]">Descripción</label>
                                    <input type="text" name="descripcion" id="descripcion"
                                        placeholder="Descripción del Puesto"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="requisitos"
                                        class="mb-3 block text-base font-medium text-[#07074D]">Requisitos</label>
                                    <input type="text" name="requisitos" id="requisitos"
                                        placeholder="Requisitos del Puesto"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="salario" class="mb-3 block text-base font-medium text-[#07074D]">Salario
                                        Base</label>
                                    <input type="text" name="salario" id="salario" placeholder="Salario Base"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="horario"
                                        class="mb-3 block text-base font-medium text-[#07074D]">Horario</label>
                                    <input type="text" name="horario" id="horario" placeholder="Horario del Puesto"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="estado"
                                        class="mb-3 block text-base font-medium text-[#07074D]">Estado</label>
                                    <select name="estado" id="estado"
                                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md">
                                        <option value="">Seleccione</option>
                                        <option value="ocupado">Ocupado</option>
                                        <option value="vacante">Vacante</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div>
                            <button
                                class="hover:shadow-form w-full rounded-md bg-[#6A64F1] py-3 px-8 text-center text-base font-semibold text-white outline-none">
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
                data-accordion-target="#accordion-color-body-2" aria-expanded="false"
                aria-controls="accordion-color-body-2">
                <span>Consulta los puestos existentes</span>
                <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M9 5 5 1 1 5" />
                </svg>
            </button>
        </h2>
        <div id="accordion-color-body-2" class="hidden" aria-labelledby="accordion-color-heading-2">
            <div class="mt-4">
                <button type="button"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                    data-accordion-target="#accordion-color-body-1" aria-expanded="true"
                    aria-controls="accordion-color-body-1">
                    Agregar Puesto
                </button>

                <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="px-6 py-3">ID del Puesto</th>
                                <th scope="col" class="px-6 py-3">Nombre del Puesto</th>
                                <th scope="col" class="px-6 py-3">Departamento</th>
                                <th scope="col" class="px-6 py-3">Descripción</th>
                                <th scope="col" class="px-6 py-3">Requisitos</th>
                                <th scope="col" class="px-6 py-3">Salario Base</th>
                                <th scope="col" class="px-6 py-3">Horario</th>
                                <th scope="col" class="px-6 py-3">Estado</th>
                                <th scope="col" class="px-6 py-3"><span class="sr-only">Edit</span></th>
                                <th scope="col" class="px-6 py-3"><span class="sr-only">Delete</span></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(puesto, index) in puestos" :key="index"
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                                <th scope="row"
                                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                    {{ puesto.id }}
                                </th>
                                <td class="px-6 py-4">{{ puesto.nombre }}</td>
                                <td class="px-6 py-4">{{ puesto.departamento }}</td>
                                <td class="px-6 py-4">{{ puesto.descripcion }}</td>
                                <td class="px-6 py-4">{{ puesto.requisitos }}</td>
                                <td class="px-6 py-4">{{ puesto.salario }}</td>
                                <td class="px-6 py-4">{{ puesto.horario }}</td>
                                <td class="px-6 py-4">{{ puesto.estado }}</td>
                                <td class="px-6 py-4 text-right">
                                    <a href="#"
                                        class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                                </td>
                                <td class="px-6 py-4 text-right">
                                    <a href="#"
                                        class="font-medium text-red-600 dark:text-red-500 hover:underline">Delete</a>
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
                    id: "P001",
                    nombre: "Cardiólogo",
                    departamento: "Cardiología",
                    descripcion: "Especialista en enfermedades del corazón.",
                    requisitos: "Licenciatura en Medicina, especialización en Cardiología.",
                    salario: "$5000",
                    horario: "8:00 AM - 4:00 PM",
                    estado: "Ocupado"
                },
                {
                    id: "P002",
                    nombre: "Enfermera",
                    departamento: "Emergencias",
                    descripcion: "Atención primaria en la sala de emergencias.",
                    requisitos: "Licenciatura en Enfermería, certificación en primeros auxilios.",
                    salario: "$3000",
                    horario: "7:00 AM - 3:00 PM",
                    estado: "Vacante"
                },
                {
                    id: "P003",
                    nombre: "Técnico de Radiología",
                    departamento: "Radiología",
                    descripcion: "Operación de equipos de imagenología médica.",
                    requisitos: "Título de Técnico en Radiología.",
                    salario: "$3500",
                    horario: "9:00 AM - 5:00 PM",
                    estado: "Ocupado"
                },
                {
                    id: "P004",
                    nombre: "Cirujano",
                    departamento: "Quirófano",
                    descripcion: "Realización de operaciones quirúrgicas.",
                    requisitos: "Licenciatura en Medicina, especialización en Cirugía.",
                    salario: "$8000",
                    horario: "10:00 AM - 6:00 PM",
                    estado: "Ocupado"
                },
                {
                    id: "P005",
                    nombre: "Recepcionista",
                    departamento: "Admisiones",
                    descripcion: "Atención al paciente en el área de admisiones.",
                    requisitos: "Diplomado en Administración, habilidades de comunicación.",
                    salario: "$2500",
                    horario: "6:00 AM - 2:00 PM",
                    estado: "Vacante"
                }
            ]

        };
    }
};
</script>

<style scoped>
/* Aquí puedes agregar tus estilos personalizados */
</style>