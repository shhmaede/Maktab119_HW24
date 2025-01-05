const productSearchBtn = document.getElementById('productSearchBtn');

productSearchBtn.addEventListener("button",(e) =>{
    let productName = document.getElementById('productName').value;
    return fetch("http://127.0.0.1:8000/search/"+productName)
});
