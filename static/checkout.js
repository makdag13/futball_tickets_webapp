document.addEventListener("DOMContentLoaded", function() {
    
    const products = JSON.parse(document.querySelector('input[name="products"]').value);
    
    const cartItemsContainer = document.getElementById("cart-items");
    const totalPriceContainer = document.getElementById("total-price");
    let totalPrice = 0;

    function displayCart() {
        cartItemsContainer.innerHTML = "";
        if (products.length > 0) {
            products.forEach(product => {
                const listItem = document.createElement("li");
                listItem.textContent = `${product.name} - ${product.price} PLN`;
                cartItemsContainer.appendChild(listItem);
                totalPrice += product.price;
            });
        } else {
            cartItemsContainer.innerHTML = "<li><b>Sepetiniz boş.</b></li>";
        }
        totalPriceContainer.textContent = `${totalPrice} PLN`;
    }

    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        const productsInput = form.querySelector('input[name="products"]');
        productsInput.value = JSON.stringify(products); 
    });

    
    displayCart();
});
