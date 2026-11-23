(function () {
    "use strict";

    var nav = document.getElementById("nav");
    var burger = document.getElementById("navBurger");
    if (!nav || !burger) return;

    var thresholdValue = nav.getAttribute("data-scrolled-threshold");
    var threshold = thresholdValue === null ? 8 : Number(thresholdValue);
    if (!Number.isFinite(threshold)) threshold = 8;

    burger.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        burger.setAttribute("aria-expanded", open ? "true" : "false");
    });

    function updateScrollState() {
        nav.classList.toggle("scrolled", window.scrollY > threshold);
    }

    updateScrollState();
    window.addEventListener("scroll", updateScrollState, { passive: true });
})();
