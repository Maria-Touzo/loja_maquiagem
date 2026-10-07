async function mostrar_carrinho(){

    // criando api
    const resposta = await fetch("api/get/carrinho");
    // tratando erro
    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO.")
    }

    // converte a resposta recebida pelo flask
    const dados = await resposta.json()

    // captura a div do meu html
    const carrinho = document.getElementById("carrinho")

    // limpa a tela antes de escrever
    carrinho.innerHTML = "";

    // percorre a lista de itens fornecida pelo banco de dados
    for (let dado of dados) {
        let linha = `
        <div class="item-info">
            <h3>${dado.nome}</h3>
            <p>${dado.preco}</p>
        </div>
        `
        // adiciona e concatena a div com os novos dados
        carrinho.innerHTML += linha
    }
}

mostrar_carrinho();
