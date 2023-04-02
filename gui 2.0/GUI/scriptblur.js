function uploadImageblur() {
    const formData = new FormData();
    const image = document.getElementById('images').files[0];
    formData.append('images', image);
  
    fetch('/uploadblur', {
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
    const x = document.getElementById("removing");
    x.style.display = "block";
    console.log("done");
  }
  