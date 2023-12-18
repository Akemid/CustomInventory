<template>
    <div class="row my-4">
        <div class="col position-relative">
            <div class="card position-absolute top-0 start-50 translate-middle-x" style="width: 18rem;">
            <img src="" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Nombre del producto</h5>
                    <p class="card-text">Descripcion del producto</p>
                    <div class="row g-2">
                        <div class="col-6">
                            <button 
                            type="button" 
                            class="btn btn-warning w-100"
                            data-bs-toggle="modal" 
                            data-bs-target="#editProductModal"
                            >Editar <i class="bi bi-pencil-fill"></i></button> 
                        </div>
                        <div class="col-6">
                             <button
                             type="button" 
                             class="btn btn-danger w-100"                             
                             data-bs-toggle="modal" 
                             data-bs-target="#deleteProductModal"
                             >
                             Eliminar <i class="bi bi-trash-fill"></i></button>
                        </div>
                        <div class="col-6">                        
                            <button
                             type="button" 
                            class="btn btn-success w-100"                          
                             data-bs-toggle="modal" 
                            data-bs-target="#addOperationModal"
                            >
                            Ingresar <i class="bi bi-plus-circle"></i></button> 
                        </div>
                        <div class="col-6">                        
                            <button 
                            type="button"
                            data-bs-toggle="modal"
                            class="btn btn-primary w-100"
                            data-bs-target="#substractOperationModal"
                            >Retirar <i class="bi bi-dash-circle"></i></button>
                        </div>
                    </div>                                                            
                </div>
            </div>
        </div>

    </div>
</template>