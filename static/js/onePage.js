const titulos = [
    "Gato Curioso",
    "Gato Dormilón",
    "Gato Juguetón",
    "Gato Elegante",
    "Gato Travieso",
    "Gato Cariñoso",
    "Gato Aventurero",
    "Gato Observador",
    "Gato Misterioso",
    "Gato Consentido"
];

const descripciones = [
    "Siempre atento a todo lo que sucede a su alrededor, no se le escapa ningún detalle.",
    "Puede dormir en cualquier lugar y a cualquier hora, su talento es el descanso absoluto.",
    "Le encanta correr, saltar y jugar con cualquier cosa que encuentre a su paso.",
    "Camina con porte y gracia, como si supiera que es el rey de la casa.",
    "Le gusta meterse en pequeños problemas y desaparecer justo antes de ser descubierto.",
    "Busca mimos y compañía, y ronronea con solo recibir una caricia.",
    "Explora cada rincón como si fuera una gran expedición.",
    "Prefiere observar en silencio antes de decidir si vale la pena actuar.",
    "Aparece y desaparece sin aviso, siempre guardando un aire enigmático.",
    "Exige atención, comida y cariño… en ese orden."
];

const imagenes = [
    "img/1.png","img/2.png","img/3.png","img/4.png","img/5.png",
    "img/6.png","img/7.png","img/8.png","img/9.png","img/10.png"
];

const container = document.getElementById("cards-container");
const LIMITE_TOTAL = 100;
let totalCargadas = 0;
let cargando = false;

function randomItem(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function loadCards(cantidad = 3) {
    if (cargando || totalCargadas >= LIMITE_TOTAL) {
        return;
    }

    cargando = true;

    if (totalCargadas + cantidad > LIMITE_TOTAL) {
        cantidad = LIMITE_TOTAL - totalCargadas;
    }

    for (let i = 0; i < cantidad; i++) {
        const card = document.createElement("div");
        card.className = "col-4 mb-4";

        card.innerHTML = `
            <div class="card h-100">
                <img src="${STATIC_URL + randomItem(imagenes)}"
                     class="card-img-top"
                     style="max-height:200px; object-fit:cover;">
                <div class="card-body">
                    <h5 class="card-title">${randomItem(titulos)}</h5>
                    <p class="card-text">${randomItem(descripciones)}</p>
                </div>
            </div>
        `;

        container.appendChild(card);
        totalCargadas++;
    }

    console.log(`Cards cargadas: ${totalCargadas}/${LIMITE_TOTAL}`);
    
    cargando = false;
}


window.addEventListener('scroll', () => {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        loadCards();
    }
});

loadCards(6);
