document.addEventListener("DOMContentLoaded", function () {
    const showCreateModalButton = document.getElementById("show-create-modal");
    const createModal = document.getElementById("create-modal");
    const overlay = document.getElementById("overlay");

    const closeModal = () => {
        createModal.style.display = "none";
        overlay.style.display = "none";
    };

    showCreateModalButton.addEventListener("click", function () {
        createModal.style.display = "block";
        overlay.style.display = "block";
    });

    const closeCreateModalButton = document.getElementById("close-create-modal");

    closeCreateModalButton.addEventListener("click", function () {
        closeModal();
    });

    overlay.addEventListener("click", function () {
        closeModal();
    });

    // Close modal when pressing the "Esc" key
    window.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });
});
