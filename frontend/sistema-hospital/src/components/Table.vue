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
            <div class="py-16">
                <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-5xl">
                    <div class="hidden lg:block lg:w-1/3 bg-cover" style="
          background-image: url('https://images.pexels.com/photos/4021779/pexels-photo-4021779.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
        "></div>
                    <div class="w-full p-8 lg:w-2/3">
                        <p class="text-xl text-teal-600 text-center uppercase">¡Bienvenido!</p>

                        <div class="mt-4 flex items-center justify-between">
                            <span class="border-b w-1/5 lg:w-1/4"></span>
                            <a href="#" class="text-xs text-center text-gray-500 uppercase">Realiza tu registro</a>
                            <span class="border-b w-1/5 lg:w-1/4"></span>
                        </div>
                        <div class="flex">
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label class="block text-gray-700 text-sm font-bold mb-2">Nombre(s)</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="email" />
                            </div>
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label class="block text-gray-700 text-sm font-bold mb-2">Primer Apellido</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="password" />
                            </div>
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label class="block text-gray-700 text-sm font-bold mb-2">Segundo Apellido</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="email" />
                            </div>
                        </div>
                        <div class="flex">

                            <div class="lg:w-2/4 mt-4 mx-2">
                                <label class="block text-gray-700 text-sm font-bold mb-2">CURP</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="password" />
                            </div>
                            <div class="lg:w-1/4 mt-4 mx-2">
                                <label for="countries" class="lock text-gray-700 text-sm font-bold mb-2">Género</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option selected>-- Seleccionar --</option>
                                    <option value="US">Masculino</option>
                                    <option value="CA">Femenino</option>
                                    <option value="FR">Indistinto</option>

                                </select>
                            </div>
                            <div class="lg:w-1/4 mt-4 mx-2">
                                <label for="countries" class="lock text-gray-700 text-sm font-bold mb-2">Tipo de
                                    Sangre</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option selected>-- Seleccionar --</option>
                                    <option value="A+">A+</option>
                                    <option value="A-">A-</option>
                                    <option value="B+">B+</option>
                                    <option value="B-">B-</option>
                                    <option value="AB+">AB+</option>
                                    <option value="AB-">AB-</option>
                                    <option value="O+">O+</option>
                                    <option value="O-">O-</option>
                                </select>
                            </div>
                        </div>

                        <div class="flex">
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label for="countries" class="lock text-gray-700 text-sm font-bold mb-2">Fecha
                                    Nacimiento</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="date" />
                            </div>
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label for="countries"
                                    class="lock text-gray-700 text-sm font-bold mb-2">Telefono</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="number" />
                            </div>
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label for="countries" class="lock text-gray-700 text-sm font-bold mb-2">email</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="email" />
                            </div>
                        </div>
                        <div class="flex">
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label for="countries" class="lock text-gray-700 text-sm font-bold mb-2">Usuario</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="text" />
                            </div>
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label for="countries"
                                    class="lock text-gray-700 text-sm font-bold mb-2">Contraseña</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="password" />
                            </div>
                            <div class="lg:w-1/3 mt-4 mx-2">
                                <label for="countries" class="lock text-gray-700 text-sm font-bold mb-2">Repite
                                    Contraseña</label>
                                <input
                                    class="bg-gray-50 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                                    type="password" />
                            </div>
                        </div>
                        <div class="mt-8">
                            <button class="bg-teal-500 text-white font-bold py-2 px-4 w-1/3 rounded hover:bg-gray-600">
                                Iniciar Sesion
                            </button>
                        </div>
                        <div class="mt-4 flex items-center justify-between">
                            <span class="border-b w-1/5 md:w-1/4"></span>
                            <router-link to="/login">
                                <a href="#" class="text-xs text-gray-500 uppercase">Ya tengo una cuenta</a>
                                <span class="border-b w-1/5 md:w-1/4"></span>
                            </router-link>
                        </div>
                    </div>
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
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                    Agregar Puesto
                </button>

                <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="px-6 py-3">Product name</th>
                                <th scope="col" class="px-6 py-3">Color</th>
                                <th scope="col" class="px-6 py-3">Category</th>
                                <th scope="col" class="px-6 py-3">Price</th>
                                <th scope="col" class="px-6 py-3"><span class="sr-only">Edit</span></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(product, index) in products" :key="index"
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                                <th scope="row"
                                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                    {{ product.name }}
                                </th>
                                <td class="px-6 py-4">{{ product.color }}</td>
                                <td class="px-6 py-4">{{ product.category }}</td>
                                <td class="px-6 py-4">{{ product.price }}</td>
                                <td class="px-6 py-4 text-right">
                                    <a href="#"
                                        class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
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
            products: [
                {
                    name: "Apple MacBook Pro 17\"",
                    color: "Silver",
                    category: "Laptop",
                    price: "$2999"
                },
                {
                    name: "Microsoft Surface Pro",
                    color: "White",
                    category: "Laptop PC",
                    price: "$1999"
                },
                {
                    name: "Magic Mouse 2",
                    color: "Black",
                    category: "Accessories",
                    price: "$99"
                },
                {
                    name: "Tablet 2",
                    color: "White",
                    category: "Personal",
                    price: "$50"
                }
            ]
        };
    }
};
</script>

<style scoped>
/* Aquí puedes agregar tus estilos personalizados */
</style>