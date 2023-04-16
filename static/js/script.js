// Create pop up for likes if not registered
const likeBtn = document.getElementById('like-btn');
const message = document.getElementById('message');

likeBtn.addEventListener('click', () => {
  message.classList.add('click');
});