
/* Abre e fecha menu lateral em modulo mobile */

const  menuMobile = document.querySelector(".menu-mobile"); 
const body = document.querySelector("body");


menuMobile.addEventListener("click", () => {
    menuMobile.classList.contains("bi-list")
     ? menuMobile.classList.replace("bi-list","bi-x")
     : menuMobile.classList.replace("bi-x","bi-list");
    body.classList.toggle("menu-nav-active");
});

/* Fechar o menu quando clicar em algum item e muda o icone para lista*/
const navItem =document.querySelectorAll('.nav-item');
// console.log(navItem)
navItem.forEach(item => {
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")){
            body.classList.remove("menu-nav-active") 
            menuMobile.classList.replace("bi-x","bi-list");
        }
    })

})


/* Animar todos os itens na tela que tiveram meu atributo data-anime*/
const item = document.querySelectorAll("[data-anime]"); /*Gerando um array*/
const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;
    // console.log(windowTop)

    item.forEach(element => {
        if (windowTop > element.offsetTop){
            element.classList.add("animate");
        }
        else
        {
            element.classList.remove("animate");
        }

    });
};

animeScroll();

window.addEventListener("scroll",  () => {
    animeScroll();
});



/* Ativar carregamento no botão de enviar formulario para */
const btnEnviar = document.querySelector("#btn-enviar")
const btnEnviarLoader = document.querySelector("#btn-enviar-loader")

btnEnviar.addEventListener("click", () => {
    btnEnviarLoader.style.display = "block";
    btnEnviar.style.display = "none"
})


/*Tira a Alerta de sucesso depois de 5 segundos*/ 
setTimeout(() => {
    document.querySelector('#alerta').style.display = 'none';
}, 5000) /* milisegundos */