const host = 'http://127.0.0.1:8000'
const productSearchBtn = document.getElementById('productSearchBtn');
    console.log('salam1')

productSearchBtn.addEventListener("click",(e) =>{
    let productName = document.getElementById('productName').value;
    // return fetch(host + '/search/'+productName)
    window.location.assign(host + '/search/'+productName)
});
