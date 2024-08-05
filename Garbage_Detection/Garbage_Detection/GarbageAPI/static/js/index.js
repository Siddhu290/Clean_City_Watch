document.getElementById('imageUploadForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData();
    const fileInput = document.querySelector('input[type="file"]');
    const imageFile = fileInput.files[0];

    if (!imageFile) {
        alert('Please select an image to upload.');
        return;
    }

    formData.append('image', imageFile);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server here
        document.getElementById('response').textContent = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
