function uploadImage() {
    const formData = new FormData();
    const image = document.getElementById('image').files[0];
    formData.append('image', image);
  
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(
      ()=>{
        console.log("SAVED image and removed shadow");
        const x = document.getElementById("removing");
        x.style.display = "block";
        console.log("done");
      }
    )
    .catch(error => {
      console.error(error);
      const messageDiv = document.getElementById('message');
      messageDiv.innerHTML = 'An error occurred while uploading the image.';
    });
    
  }
  