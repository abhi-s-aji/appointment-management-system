document.addEventListener("DOMContentLoaded", function() {
    const currentUrl = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(link => {
        const linkUrl = link.getAttribute('href');

        if (linkUrl === '/' && currentUrl === '/') {
            link.classList.add('active-tab');
        } else if (linkUrl !== '/' && currentUrl.includes(linkUrl)) {
            link.classList.add('active-tab');
        } else {
            link.classList.remove('active-tab');
        }
    });
});