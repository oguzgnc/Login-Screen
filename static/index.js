const container = document.getElementById("container");
const registerBtn = document.getElementById("register");
const loginBtn = document.getElementById("login");
const kayitOlButonu = document.getElementById("kayitOlButonu"); 
const kaydiTamamlaButonu = document.getElementById("kaydiTamamlaButonu"); 
const kayitFormu = document.getElementById("kayitFormu"); 
const mesajAlani = document.getElementById("mesajAlani"); 
const kayitFormux = document.getElementById("kayitFormu");


if (registerBtn) {
    registerBtn.addEventListener("click", function(event) {
        event.preventDefault(); 
        container.classList.add("active"); 
    });
}

if (loginBtn) {
    loginBtn.addEventListener("click", function(event) {
        event.preventDefault(); 
        container.classList.remove("active"); 
    });
}

if(kayitOlButonu){
    kayitOlButonu.addEventListener("click", function(event) {
        event.preventDefault();
        container.classList.add("active"); 
    });
}
if (kayitFormux) {
    kayitFormux.addEventListener("submit", function(event) {
        
        event.preventDefault();
    });
}

if (kaydiTamamlaButonu) {
    kaydiTamamlaButonu.addEventListener("click", function(event) {
     
        event.preventDefault();

      
        const formData = new FormData(kayitFormu);

        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text(); 
        })
        .then(data => {
            mesajAlani.innerHTML = data; 
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            mesajAlani.innerHTML = "Bir hata oluştu. Lütfen tekrar deneyin.";
        });
        
    });
}