let boton = document.querySelector(".enviar");
window.gaglobal = "ga";
boton.addEventListener("click",()=>{
    let confirmacion = confirm("quieres añadir este articulo al carrito?");
    if(confirmacion){
        agregarHTML();

    }
})

function agregarHTML(){
    window.gaglobal = "god";
}