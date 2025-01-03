const productSearchBtn = document.getElementById('productSearchBtn');

productSearchBtn.addEventListener("button",(e) =>{
    console.log("salam")
    let productName = document.getElementById('productName').value;
    fetch("http://127.0.0.1:8000/search/"+productName)
});
