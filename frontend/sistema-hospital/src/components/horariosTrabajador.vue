<template>
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
</template>
