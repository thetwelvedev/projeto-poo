const texteBotao = document.getElementById("butao");
const check1 = document.getElementById("IdaEVolta");
const check2 = document.getElementById("IdaOuVolta");

// Função para atualizar o texto
function atualizarTexto() {
    if (check1.checked) {
    texteBotao.textContent = "TRECHO  Ida e Volta";
    } else if (check2.checked) {
    texteBotao.textContent = "TRECHO  Só ida ou volta";
    }
}

check1.addEventListener("change", atualizarTexto);
check2.addEventListener("change", atualizarTexto);



const Botao = document.getElementById("trecho");
// Ao clicar no botão, altera sua cor (toggle)
Botao.addEventListener('click', function(event) {
    // Impede que o clique no botão seja propagado para o documento
    event.stopPropagation();
    Botao.classList.toggle('actives');
});

// Ao clicar fora do botão, remove a classe "active"
document.addEventListener('click', function(event) {
    if (!Botao.contains(event.target)) {
    Botao.classList.remove('actives');
    }
});



document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.getElementById("dropdownButton");
    const dropdownMenu = document.getElementById("dropdownMenu");
    btn = document.getElementById("Passageiros");

    // Impede o Bootstrap de fechar o dropdown automaticamente
    dropdownButton.addEventListener("click", function (event) {
        
        event.stopPropagation();
        const isOpen = dropdownMenu.classList.toggle("show");
        btn.classList.toggle('actives', isOpen);
        
    });

    // Fecha o dropdown ao clicar fora
    document.addEventListener("click", function (event) {
        if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove("show");
            btn.classList.remove('actives');
            atualizarResumo();
        }
    });
    
});


function alterarValor(id, delta) {
    let input = document.getElementById(id);
    let valorAtual = parseInt(input.value);
    let novoValor = valorAtual + delta;
    if (novoValor >= 0) {
        input.value = novoValor;
    }
}



function atualizarResumo() {
    let adultos = parseInt(document.getElementById('adultos').value);
    let adolescentes = parseInt(document.getElementById('adolescentes').value);
    let criancas = parseInt(document.getElementById('criancas').value);
    let bebes = parseInt(document.getElementById('bebes').value);

    let resumo = ["PASSAGEIROS  "];
    if (adultos >= 1) resumo.push(`${adultos} Adultos`);
    if (adolescentes >= 1) resumo.push(`${adolescentes} Adolescentes`);
    if (criancas >= 1) resumo.push(`${criancas} Crianças`);
    if (bebes >= 1) resumo.push(`${bebes} Bebês`);

    let textoResumo = resumo.length > 0 ? resumo.join(' ') : '';
    document.getElementById('dropdownButton').innerText = textoResumo.substring(0, 28);
}