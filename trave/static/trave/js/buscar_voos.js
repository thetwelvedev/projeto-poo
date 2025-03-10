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



document.getElementById("buscarVoos").addEventListener("click", async function (event) {
    event.preventDefault();
    v
    const origem = document.getElementById("id_partida").value;
    const destino = document.getElementById("id_destino").value;
    const dataIda = document.querySelector("input[type='date']").value;
    const dataVolta = document.getElementById("VoltaViagem").value;
    const adultos = document.querySelector("select").value;

    const dados = { origem, destino, data_ida: dataIda, data_volta: dataVolta, adultos };

    try {
        const response = await fetch("{% url 'buscar_voos' %}", {
            method: "POST",
            headers: { "Content-Type": "application/json", "X-CSRFToken": "{{ csrf_token }}" },
            body: JSON.stringify(dados)
        });

        const data = await response.json();

        if (data.voos.length > 0) {
            // Redireciona para a página de resultados, passando os dados como parâmetros GET
            window.location.href = `{% url 'resultados-voos' %}?origem=${origem}&destino=${destino}&data_ida=${dataIda}&data_volta=${dataVolta}&adultos=${adultos}`;
        } else {
            alert("Nenhum voo encontrado!");
        }
    } catch (error) {
        console.error("Erro ao buscar voos:", error);
    }
});


async function carregarDados() {
    try {
        const response = await fetch("{% static 'trave/data/voos.json' %}");
        const dados = await response.json();
        return dados;
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
    }
}

// Função para preencher os voos
async function preencherVoos() {
    const dados = await carregarDados();
    const selectVoo = document.getElementById('id_partida');
    const selectDestino = document.getElementById('id_destino');

    dados.voos.sort((a, b) => a.cidade.localeCompare(b.cidade)).forEach(voo => {
        const option = document.createElement('option');
        const option2 = document.createElement('option');
        option.value = voo.sigla;
        option.textContent = "✈️   " + voo.cidade + " - " + voo.sigla;

        option2.value = voo.sigla;
        option2.textContent = "✈️   " + voo.cidade + " - " + voo.sigla;

        selectVoo.appendChild(option);
        selectDestino.appendChild(option2);
    });
}
preencherVoos();