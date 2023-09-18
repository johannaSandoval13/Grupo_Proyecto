window.addEventListener("scroll", function () {
    const header = document.getElementById("main-header");
    if (window.scrollY > 100) {
        header.classList.add("header-hidden");
    } else {
        header.classList.remove("header-hidden");
    }
});