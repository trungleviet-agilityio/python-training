document.addEventListener('DOMContentLoaded', function() {
    // Get the common modal
    const commonModal = document.querySelector('.modal-common');

    // Get the buttons that open the common modal
    const createEmployeeButton = document.querySelector('.create-employee');
    const editEmployeeButtons = document.querySelectorAll('.edit-employee');

    // Get the cancel button for the common modal
    const cancelCommonButton = commonModal.querySelector('.cancel-button');

    // Get the modal title element
    const modalTitle = commonModal.querySelector('.modal-title');

    // Function to open the common modal with a specific title
    function openCommonModal(title) {
        modalTitle.textContent = title; // Set the modal title
        commonModal.style.display = 'block';
    }

    // Function to close the common modal
    function closeCommonModal() {
        commonModal.style.display = 'none';
    }

    // Add click event listener to open the common modal for creating an employee
    createEmployeeButton.addEventListener('click', function() {
        openCommonModal('Create Employee'); // Set the title
    });

    // Add click event listeners to open the common modal for editing an employee
    editEmployeeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            openCommonModal('Update Employee'); // Set the title
        });
    });

    // Add click event listener to close the common modal
    cancelCommonButton.addEventListener('click', closeCommonModal);
});
