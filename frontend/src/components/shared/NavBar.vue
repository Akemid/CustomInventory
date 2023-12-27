<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
<template>
<nav class="navbar navbar-expand-lg bg-primary-subtle">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/">InventoryApp 
        <i class="bi bi-shop-window"></i>
      </RouterLink>
      <button 
        class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarSupportedContent" 
        aria-controls="navbarSupportedContent" 
        aria-expanded="false" 
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink class="nav-link active" to="/">Productos</RouterLink>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" 
            href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Operaciones
            </a>
            <ul class="dropdown-menu">
              <li><RouterLink class="dropdown-item"  to="/about">Ingreso de inventario</RouterLink></li>
              <li><RouterLink class="dropdown-item" to="/about">Salida de productos</RouterLink></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" 
            href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Usuario
            </a>
            <ul class="dropdown-menu">
              <li><RouterLink class="dropdown-item"  to="/about">Editar perfil</RouterLink></li>
              <li><RouterLink class="dropdown-item"  to="/about">Cambiar contraseña</RouterLink></li>
              <li><RouterLink class="dropdown-item"  to="/about">Administración</RouterLink></li>
              <li><hr class="dropdown-divider"></li>
              <li><RouterLink class="dropdown-item"  to="/about">Cerrar sesión</RouterLink></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>