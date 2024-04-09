(function () {

    const btnEliminacionProveedor = document.querySelectorAll(".btnEliminacionProveedor");

    btnEliminacionProveedor.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el proveedor?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();    