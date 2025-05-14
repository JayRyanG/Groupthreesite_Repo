setTimeout(() => {
    const successToastMessage = document.getElementById('toast-success')
    if (successToastMessage) {
        successToastMessage.style.display = 'none'
    }
}, 3000)