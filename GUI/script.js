function uploadImage() {
    const formData = new FormData();
    const image = document.getElementById('image').files[0];
    formData.append('image', image);
  
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      const messageDiv = document.getElementById('message');
      messageDiv.innerHTML = data.message;
    })
    .catch(error => {
      console.error(error);
      const messageDiv = document.getElementById('message');
      messageDiv.innerHTML = 'An error occurred while uploading the image.';
    });
    console.log("SAVED image");
  }
  