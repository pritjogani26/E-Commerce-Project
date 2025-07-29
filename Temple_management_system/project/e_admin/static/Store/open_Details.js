function openProductDetails(name, price, description, details, imgSrc) {
    document.getElementById("productName").textContent = name;
    document.getElementById("productPrice").textContent = price;
    document.getElementById("productDescription").textContent = description;
    document.querySelector(".product-image img").src = imgSrc;
    document.getElementById("details").textContent = details;
    document.getElementById("productDetails").style.display = "block";
    // document.body.style.background = "black";
}

function closeProductDetails() {
    document.getElementById("productDetails").style.display = "none";
}