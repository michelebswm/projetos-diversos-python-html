document.getElementById("copy-icon").addEventListener("click", function() {
    var senhaElement = document.querySelector(".result span");
    var senha = senhaElement.textContent;

    navigator.clipboard.writeText(senha).then(function() {
        alert("Senha copiada para a área de transferência!");
    }).catch(function() {
        alert("Não foi possível copiar a senha!");
    });
});
