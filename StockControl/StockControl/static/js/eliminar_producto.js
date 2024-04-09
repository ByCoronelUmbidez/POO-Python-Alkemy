(function () {

    const btnEliminacionProducto = document.querySelectorAll(".btnEliminacionProducto");

    btnEliminacionProducto.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el producto?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})(); 