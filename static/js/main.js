const btnBorrar = document.querySelectorAll('.btn-delete') /*devuelve una lista de nodos de html*/

if (btnBorrar) {
    const btnArray = Array.from(btnBorrar);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('¿Esta seguro de querer eliminar la información?')) {
                e.preventDefault(); /*para que no se envie la petición al servidor*/
            }
        })
    })

}


