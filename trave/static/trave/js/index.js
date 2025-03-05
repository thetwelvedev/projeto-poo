const opcoes = [
    { value: "ida_volta", text: "Ida e volta" },
    { value: "ida_ou_volta", text: "Só ida ou volta" },
    { value: "varios_trechos", text: "Vários trechos" }
];

// Obtendo referência ao select
const selectTrechos = document.getElementById("trechos");

// Função para adicionar opções ao select
function adicionarOpcoes() {
    selectTrechos.innerHTML = '<option value="" disabled selected>Selecione...</option>'; // Reseta antes de adicionar
    
    opcoes.forEach(opcao => {
        let optionElement = document.createElement("option");
        optionElement.value = opcao.value;
        optionElement.textContent = opcao.text;
        selectTrechos.appendChild(optionElement);
    });
}

// Evento para adicionar opções ao clicar no botão
document.getElementById("addOption").addEventListener("click", adicionarOpcoes);
