import { createRouter, createWebHistory } from 'vue-router';
import RegisterUser from '@/components/registerUser.vue';
import LoginView from '@/components/login.vue';
import Dashboard from '@/components/dashboard.vue';
import Usuario from '@/components/usuario.vue';
import Personas from '@/components/personas.vue';
import PersonalMedico from '@/components/personalMedico.vue';
import Puestos from '@/components/puestos.vue';
import PuestosDepartamentos from '@/components/puestos_departamentos.vue';
import AreasMedicas from '@/components/areasMedicas.vue';  // Importa el componente areasMedicas.vue

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUser,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      children: [
        {
          path: '/personas',
          name: 'personas',
          component: Personas,
        },
        {
          path: '/areasMedicas',
          name: 'areasMedicas',
          component: AreasMedicas,
        },
       
        {
          path: '/personalMedico',
          name: 'personalMedico',
          component: PersonalMedico,
        },
        {
          path: '/puestos',
          name: 'puestos',
          component: Puestos,
        },
        {
          path: '/puestos_departamentos',
          name: 'puestos_departamentos',
          component: PuestosDepartamentos,
        },
      ],
    },
    {
      path: '/usuario',
      name: 'usuario',
      component: Usuario,
    },
  ],
});

export default router;
