document.addEventListener("DOMContentLoaded", function () {
    const showCreateModalButton = document.getElementById("show-create-modal");
    const createModal = document.getElementById("create-modal");

    const closeModal = () => {
        createModal.style.display = "none";
    };

    showCreateModalButton.addEventListener("click", function () {
        createModal.style.display = "block";
    });

    const createForm = document.getElementById("create-form");

    createForm.addEventListener("submit", function (event) {
        event.preventDefault();
        fetch("{% url 'employee-list-create' %}", {
            method: "POST",
            body: new FormData(createForm),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                createModal.style.display = "none";
                createForm.reset();
            }
        });
    });

    // Close modal when clicking outside of it
    window.addEventListener("click", function (event) {
        if (event.target === createModal) {
            closeModal();
        }
    });

    // Close modal when pressing the "Esc" key
    window.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });
});
