document.getElementById('cadastroBtn').addEventListener('click', function(e) {
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const confirmarSenha = document.getElementById('confirmarSenha').value;
    
    if (!nome || !email || !senha || !confirmarSenha) {
        e.preventDefault();
        alert('Por favor, preencha todos os campos!');
        return;
    }
    
    if (senha !== confirmarSenha) {
        e.preventDefault();
        alert('As senhas não coincidem!');
        return;
    }
    
    if (senha.length < 6) {
        e.preventDefault();
        alert('A senha deve ter pelo menos 6 caracteres!');
        return;
    }
});