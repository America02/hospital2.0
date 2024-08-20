import { createRouter, createWebHistory } from 'vue-router'
import RegisterUser from '@/components/registerUser.vue'
import LoginView from '@/components/login.vue'
import Dashboard from '@/components/dashboard.vue'
import Usuario from '@/components/usuario.vue'
import Personas from '@/components/personas.vue'

import PersonalMedico from '@/components/personalMedico.vue'
import Puestos from '@/components/puestos.vue'
import PuestosDepartamentos from '@/components/puestos_departamentos.vue'  // Importa el componente puestos_departamentos.vue
import areasMedicas from '@/components/areasMedicas.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUser
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
 
      children:[
        { 
          path:'/personas', 
          name:'personas',
          component:Personas 
        }, 
       
        {
          path: '/personalMedico',
          name: 'personalMedico',
          component: PersonalMedico
        },
        {
          path: '/puestos',
          name: 'puestos',
          component: Puestos
        },
        {
          path: '/puestos_departamentos',  // Define la ruta para el componente puestos_departamentos.vue
          name: 'puestos_departamentos',
          component: PuestosDepartamentos
        },
        {
          path: '/areasMedicas',
          name:'areasMedicas',
          component: areasMedicas
        }
      ]
    },
    {
      path: '/usuario',
      name: 'Usuario',
      component: Usuario
    },
    {
      path: '/personas',
      name: 'Personas',
      component: Personas
    },
  ]
})

export default router;