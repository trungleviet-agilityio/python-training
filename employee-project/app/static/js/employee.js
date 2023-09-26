document.addEventListener("DOMContentLoaded", function () {
    const showModalButtons = document.querySelectorAll(".edit-employee, .create-employee");
    const closeModalButtons = document.querySelectorAll(".close, #close-employee-modal, #close-delete-modal");
    const overlay = document.getElementById("overlay");
    const modals = document.querySelectorAll(".modal");
    const deleteButtons = document.querySelectorAll(".delete-employee");

    showModalButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const modalId = button.getAttribute("data-modal-id");
            const modal = document.getElementById(modalId);
            modal.style.display = "block";
            overlay.style.display = "block";
        });
    });

    closeModalButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            modals.forEach(function (modal) {
                modal.style.display = "none";
            });
            overlay.style.display = "none";
        });
    });

    // Close modals when clicking the overlay
    overlay.addEventListener("click", function () {
        modals.forEach(function (modal) {
            modal.style.display = "none";
        });
        overlay.style.display = "none";
    });

    // Close modals when pressing the "Esc" key
    window.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            modals.forEach(function (modal) {
                modal.style.display = "none";
            });
            overlay.style.display = "none";
        }
    });

    // Handle delete button click
    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const employeeId = button.getAttribute("data-id");
            if (confirm("Are you sure you want to delete this employee?")) {
                // Send a DELETE request to the server
                fetch(`/employee/${employeeId}/`, {
                    method: "DELETE",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"), // Ensure you have a function to get the CSRF token
                    },
                })
                .then(response => {
                    if (response.ok) {
                        // Reload the page to reflect the updated employee list
                        location.reload();
                    } else {
                        // Handle errors if needed
                    }
                });
            }
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});
