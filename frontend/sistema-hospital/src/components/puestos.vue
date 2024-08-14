<template>
    <div id="accordion-puestos" data-accordion="collapse" data-active-classes="bg-blue-100 dark:bg-gray-800 text-blue-600 dark:text-white">
        <h2 id="accordion-puestos-heading-1">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-800 dark:border-gray-700 dark:text-gray-400 hover:bg-blue-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-puestos-body-1" aria-expanded="true" aria-controls="accordion-puestos-body-1">
                <span>Registrar un nuevo puesto</span>
                <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5" />
                </svg>
            </button>
        </h2>
        
        <div id="accordion-puestos-body-1" class="hidden" aria-labelledby="accordion-puestos-heading-1">
            <div class="flex items-center justify-center p-12">
                <div class="mx-auto w-full max-w-[550px] bg-white p-8 rounded-lg shadow-lg">
                    <h2 class="text-2xl font-bold text-center mb-1 text-[#07074D]">HOSPITAL PRIVILAGE CARE</h2>
                    <p class="text-sm text-center mb-8 text-[#6B7280]">REGISTRO DE PUESTOS</p>
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
                        <div class="mb-4 text-center">
                            <button type="submit" class="rounded-lg bg-[#6A64F1] py-3 px-8 text-base font-semibold text-white outline-none hover:bg-[#6A64F1] focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-800">Registrar</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useForm } from '@inertiajs/inertia-vue3';

const { data, setData, post } = useForm({
    id: '',
    nombre: '',
    primer_apellido: '',
    segundo_apellido: '',
    puesto: '',
    tipo: '',
    fecha_inicio: '',
    dia_semana: '',
    turno: '',
    hora_entrada: '',
    hora_salida: ''
});

const submit = () => {
    post('/puestos', data);
};
</script>

<style scoped>
/* Add any additional styles here */
</style>
