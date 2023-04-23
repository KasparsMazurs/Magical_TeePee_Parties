// Create pop up for likes if not registered
document.addEventListener('click', event => {
  if (event.target.classList.contains('like-btn')) {
    event.target.nextElementSibling.classList.add('click');
  }
});