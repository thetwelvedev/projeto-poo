
const estadosECidades = {
    "AC": ["Rio Branco", "Cruzeiro do Sul", "Sena Madureira"],
    "AL": ["Maceió", "Arapiraca", "Palmeira dos Índios"],
    "AP": ["Macapá", "Santana", "Laranjal do Jari"],
    "AM": ["Manaus", "Parintins", "Itacoatiara"],
    "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
    "CE": ["Fortaleza", "Caucaia", "Juazeiro do Norte"],
    "DF": ["Brasília"],
    "ES": ["Vitória", "Vila Velha", "Serra"],
    "GO": ["Goiânia", "Aparecida de Goiânia", "Anápolis"],
    "MA": ["São Luís", "Imperatriz", "Caxias"],
    "MT": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
    "MS": ["Campo Grande", "Dourados", "Três Lagoas"],
    "MG": ["Belo Horizonte", "Uberlândia", "Contagem"],
    "PA": ["Belém", "Ananindeua", "Santarém"],
    "PB": ["João Pessoa", "Campina Grande", "Santa Rita"],
    "PR": ["Curitiba", "Londrina", "Maringá"],
    "PE": ["Recife", "Jaboatão dos Guararapes", "Olinda"],
    "PI": ["Teresina", "Parnaíba", "Picos"],
    "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis"],
    "RN": ["Natal", "Mossoró", "Parnamirim"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas"],
    "RO": ["Porto Velho", "Ji-Paraná", "Ariquemes"],
    "RR": ["Boa Vista", "Rorainópolis", "Caracaraí"],
    "SC": ["Florianópolis", "Joinville", "Blumenau"],
    "SP": ["São Paulo", "Campinas", "Santos"],
    "SE": ["Aracaju", "Nossa Senhora do Socorro", "Lagarto"],
    "TO": ["Palmas", "Araguaína", "Gurupi"]
};

function carregarEstados() {
    const estadoSelect = document.getElementById("estado");

    for (let estado in estadosECidades) {
        let option = document.createElement("option");
        option.value = estado;
        option.textContent = estado;
        estadoSelect.appendChild(option);
    }
}

function formatarCEP(input) {
        let valor = input.value.replace(/\D/g, ''); // Remove tudo que não for número

        if (valor.length > 5) {
            input.value = valor.substring(0, 5) + '-' + valor.substring(5, 8);
        } else {
            input.value = valor;
        }
    }

function atualizarCidades() {
    const estadoSelecionado = document.getElementById("estado").value;
    const cidadeSelect = document.getElementById("cidade");

    cidadeSelect.innerHTML = "<option value=''>Selecione uma cidade</option>";

    if (estadoSelecionado && estadosECidades[estadoSelecionado]) {
        estadosECidades[estadoSelecionado].forEach(cidade => {
            let option = document.createElement("option");
            option.value = cidade;
            option.textContent = cidade;
            cidadeSelect.appendChild(option);
        });
    }
}

function formatarCPF(input) {
    let valor = input.value.replace(/\D/g, ''); // Remove tudo que não for número

    if (valor.length > 3 && valor.length <= 6) {
        input.value = valor.substring(0, 3) + '.' + valor.substring(3);
    } else if (valor.length > 6 && valor.length <= 9) {
        input.value = valor.substring(0, 3) + '.' + valor.substring(3, 6) + '.' + valor.substring(6);
    } else if (valor.length > 9) {
        input.value = valor.substring(0, 3) + '.' + valor.substring(3, 6) + '.' + valor.substring(6, 9) + '-' + valor.substring(9, 11);
    } else {
        input.value = valor;
    }
}

function formatarTelefone(input) {
    let valor = input.value.replace(/\D/g, ''); // Remove tudo que não for número

    if (valor.length > 2 && valor.length <= 7) {
        input.value = '(' + valor.substring(0, 2) + ') ' + valor.substring(2);
    } else if (valor.length > 7) {
        input.value = '(' + valor.substring(0, 2) + ') ' + valor.substring(2, 7) + '-' + valor.substring(7, 11);
    } else {
        input.value = valor;
    }
}

function formatarCartao(input) {
    let valor = input.value.replace(/\D/g, ''); // Remove tudo que não for número
    valor = valor.substring(0, 16); // Limita a 16 dígitos

    // Adiciona espaços a cada 4 dígitos
    let formatado = valor.replace(/(\d{4})/g, '$1 ').trim();

    input.value = formatado;
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("enviarDados").addEventListener("click", function () {
        validarFormulario();
    });
});

// Função para validar o formulário
function validarFormulario() {
    let formValido = true;
    let campos = document.querySelectorAll(".form-control, .form-select");

    campos.forEach(campo => {
        if (campo.id === "newsletter1") return;
        if (!campo.value.trim()) {
            campo.classList.add("is-invalid"); // Adiciona borda vermelha ao campo inválido
            campo.nextElementSibling.style.display = "block"; // Exibe a mensagem de erro
            formValido = false;
        } else {
            campo.classList.remove("is-invalid"); // Remove erro caso seja preenchido
            campo.nextElementSibling.style.display = "none";
        }
    });

    if (formValido) {
        coletarDados(); // Se estiver tudo certo, coleta os dados
    }
}

// Função para coletar os dados do formulário
function coletarDados() {
    let dados = {
        primeiroNome: document.getElementById("primeiroNome").value.trim(),
        sobreNome: document.getElementById("sobreNome").value.trim(),
        cpf: document.getElementById("cpf").value.trim(),
        telefone: document.getElementById("telefone").value.trim(),
        cartao: document.getElementById("cartao").value.trim(),
        email: document.getElementById("email").value.trim(),
        endereco: document.getElementById("endereco").value.trim(),
        estado: document.getElementById("estado").value.trim(),
        cidade: document.getElementById("cidade").value.trim(),
        cep: document.getElementById("cep").value.trim()
    };

    console.log("Dados coletados:", dados);
    alert("Formulário enviado com sucesso!");
}


// Carregar os estados quando a página carregar
window.onload = carregarEstados;