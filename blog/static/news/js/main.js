document.addEventListener('DOMContentLoaded', () => {
    const menuOpen = document.querySelector('[data-mobile-menu-open]'),
          mainMenu = document.querySelector('#main-menu'),
          header = document.querySelector('header'),
          menuExit = document.querySelector('[data-mobile-menu-exit]'),
          navLink = document.querySelectorAll('.nav-link'),
          loader = document.querySelector('.loader');

    document.body.style.overflow = 'hidden';

    function makeDisabled(){
        navLink.forEach((item) => {
            item.classList.remove('active')
        });
    }

    if (document.body.baseURI.indexOf('recommended') > 0) {
        makeDisabled();
        navLink[1].classList.add('active');
    } else if (document.body.baseURI.indexOf('about-us') > 0) {
        makeDisabled();
        navLink[2].classList.add('active');
    } else{
        makeDisabled();
        navLink[0].classList.add('active');
    }

    menuOpen.addEventListener('click', () => {
        header.style.display = "none";
        menuExit.style.display = 'block';
        mainMenu.style.display = 'block';

        const sideBar = mainMenu.querySelector('.sidebar-menu');
        sideBar.style.zIndex = '1000';
        sideBar.style.width = '100%';

        document.body.style.overflow = 'hidden';
    });

    menuExit.addEventListener('click', () => {
        mainMenu.style.display = 'none';
        header.style.display = "flex";
        document.body.style.overflow = '';
    });

    setTimeout(() => {
        document.body.style.overflow = '';
        loader.classList.add('fade');
        setTimeout(() => {
            loader.style.display = "none";
        }, 1500)
    }, 1500);
});