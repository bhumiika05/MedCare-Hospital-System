(function () {
    "use strict";

    var navToggle = document.querySelector(".nav-toggle");
    var navPanel = document.querySelector(".nav-panel");
    var header = document.querySelector(".site-header");
    var navLinks = document.querySelectorAll(".nav-link, .login-btn");

    function setNavOpen(open) {
        if (!navToggle || !navPanel) return;
        navToggle.setAttribute("aria-expanded", open ? "true" : "false");
        navPanel.classList.toggle("is-open", open);
        document.body.style.overflow = open ? "hidden" : "";
    }

    if (navToggle && navPanel) {
        navToggle.addEventListener("click", function () {
            var isOpen = navToggle.getAttribute("aria-expanded") === "true";
            setNavOpen(!isOpen);
        });

        navLinks.forEach(function (link) {
            link.addEventListener("click", function () {
                if (window.matchMedia("(max-width: 768px)").matches) {
                    setNavOpen(false);
                }
            });
        });

        document.addEventListener("keydown", function (e) {
            if (e.key === "Escape") {
                setNavOpen(false);
            }
        });
    }

    if (header) {
        window.addEventListener(
            "scroll",
            function () {
                header.classList.toggle("is-scrolled", window.scrollY > 8);
            },
            { passive: true }
        );
    }

    var welcomeBtn = document.querySelector("[data-welcome]");
    if (welcomeBtn) {
        welcomeBtn.addEventListener("click", function () {
            alert("Welcome to MedCare!");
        });
    }
})();
