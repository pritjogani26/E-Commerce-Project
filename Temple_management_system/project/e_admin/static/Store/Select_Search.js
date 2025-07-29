document.addEventListener("DOMContentLoaded", function() {
    const filterSelect = document.getElementById("filter");
    const itemBoxes = document.querySelectorAll(".item-box");
    const searchInput = document.getElementById("search");
    const searchIcon = document.querySelector(".search_icon");

    // Function to filter item boxes based on search input
    function filterBySearch() {
        const searchValue = searchInput.value.trim().toLowerCase();
        itemBoxes.forEach(function(itemBox) {
            const itemName = itemBox.querySelector(".item-title").textContent.trim().toLowerCase();
            if (itemName.includes(searchValue)) {
                itemBox.style.display = "block";
            } else {
                itemBox.style.display = "none";
            }
        });
    }

    // Event listener for search icon click
    searchIcon.addEventListener("click", function() {
        filterBySearch();
    });

    // Event listener for filter select change
    filterSelect.addEventListener("change", function() {
        const selectedOption = this.value;
        if (selectedOption === "All") {
            itemBoxes.forEach(function(itemBox) {
                itemBox.style.display = "block";
            });
            searchInput.value = ""; // Clear search input
        } else {
            itemBoxes.forEach(function(itemBox) {
                if (itemBox.classList.contains(selectedOption)) {
                    itemBox.style.display = "block";
                } else {
                    itemBox.style.display = "none";
                }
            });
            searchInput.value = ""; // Clear search input
        }
    });

    // Event listener for search input keyup (to perform search on enter press)
    searchInput.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            filterSelect.value = "All";
            filterBySearch();
        }
    });

    // Event listener for search input change (to perform search while typing)
    searchInput.addEventListener("input", function() {
        filterSelect.value = "All";
        filterBySearch();
    });
});