window.addEventListener('scroll', function() {
    var header = document.getElementById('header');
    if (window.pageYOffset > 50) {
        header.classList.add('scrolling');
    } else {
        header.classList.remove('scrolling');
    }
});
document.querySelector('.file-input').addEventListener('change', function(event) {
  var file = event.target.files[0];
  var formData = new FormData();
  formData.append('file', file);

  fetch('/upload/', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
});

