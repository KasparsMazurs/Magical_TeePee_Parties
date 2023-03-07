document.querySelectorAll('.nav-link').forEach
(link => {
    if(link.href === window.location.href) {
        link.setAttribute('ria-current', 'page')
    }
})