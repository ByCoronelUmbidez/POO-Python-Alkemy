// Función para actualizar el valor del campo oculto cuando cambia la selección del proveedor
function updateProveedorSeleccionado() {
    var proveedorId = document.getElementById("proveedor_id").value;
    if (proveedorId === "nuevo") {
        document.getElementById("proveedor_seleccionado").value = "nuevo";
    } else {
        document.getElementById("proveedor_seleccionado").value = proveedorId;
    }
}

// Agregar un listener para el evento onchange del select
document.getElementById("proveedor_id").addEventListener("change", updateProveedorSeleccionado);