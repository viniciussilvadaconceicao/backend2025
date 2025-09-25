document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const emailInput = document.querySelector('input[type="email"]');
    const passwordInput = document.querySelector('input[type="password"]');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            if (!emailInput.value.trim() || !passwordInput.value.trim()) {
                e.preventDefault();
                alert('Por favor, preencha todos os campos!');
            }
        });
    }
});