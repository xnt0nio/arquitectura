function deleteProducto(id) { 
    Swal.fire({
        title: 'Eliminar',
        text: '¿Desea eliminar producto?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar'
      }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire('Eliminado!','Producto Eliminado Correctamente','success').then(function() {
                window.location.href = "/delete/"+id+"/";
            })
        }
      })
}
function deleteComentario(id) {
  Swal.fire({
      title: 'Eliminar',
      text: '¿Desea eliminar comentario?',
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Eliminar'
    }).then((result) => {
      if (result.isConfirmed) {
          Swal.fire('Eliminado!','Comentario Eliminado Correctamente','success').then(function() {
              window.location.href = "/deleteComent/"+id+"/";
          })
      }
    })
}






