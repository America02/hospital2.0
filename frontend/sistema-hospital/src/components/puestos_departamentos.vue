<template>
    <div id="accordion-puestos-departamentos" data-accordion="collapse" data-active-classes="bg-blue-100 dark:bg-gray-800 text-blue-600 dark:text-white">
        <h2 id="accordion-puestos-departamentos-heading-1">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-800 dark:border-gray-700 dark:text-gray-400 hover:bg-blue-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-puestos-departamentos-body-1" aria-expanded="true" aria-controls="accordion-puestos-departamentos-body-1">
                <span>Registrar un nuevo puesto-departamento</span>
                <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5" />
                </svg>
            </button>
        </h2>
        
        <div id="accordion-puestos-departamentos-body-1" class="hidden" aria-labelledby="accordion-puestos-departamentos-heading-1">
            <div class="flex items-center justify-center p-12">
                <div class="mx-auto w-full max-w-[550px] bg-white p-8 rounded-lg shadow-lg">
                    <h2 class="text-2xl font-bold text-center mb-1 text-[#07074D]">HOSPITAL PRIVILAGE CARE</h2>
                    <p class="text-sm text-center mb-8 text-[#6B7280]">REGISTRO DE PUESTOS-DEPARTAMENTOS</p>
                    <form>
                        <div class="-mx-3 flex flex-wrap">
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="id_puesto" class="mb-3 block text-base font-medium text-[#07074D]">ID Puesto</label>
                                    <input type="text" name="id_puesto" id="id_puesto" placeholder="ID Puesto" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="id_departamento" class="mb-3 block text-base font-medium text-[#07074D]">ID Departamento</label>
                                    <input type="text" name="id_departamento" id="id_departamento" placeholder="ID Departamento" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="fecha-inicio" class="mb-3 block text-base font-medium text-[#07074D]">Fecha de Inicio</label>
                                    <input type="date" name="fecha_inicio" id="fecha_inicio" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                                </div>
                            </div>
                            <div class="w-full px-3 sm:w-1/2">
                                <div class="mb-5">
                                    <label for="dia-semana" class="mb-3 block text-base font-medium text-[#07074D]">Día de la Semana</label>
                                    <input type="date" name="dia_semana" id="dia_semana" class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
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
    id_puesto: '',
    id_departamento: '',
    fecha_inicio: '',
    dia_semana: '',
    turno: ''
});

const submit = () => {
    post('/puestos_departamentos', data);
};
</script>

<style scoped>
/* Add any additional styles here */
</style>
