document.addEventListener('DOMContentLoaded', function() {
    // This code will run after the DOM is fully loaded.

    // Get the common modal
    const commonModal = document.querySelector('.modal-common');

    // Get the buttons that open the common modal
    const createEmployeeButton = document.querySelector('.create-employee');
    const editEmployeeButtons = document.querySelectorAll('.edit-employee');

    // Get the cancel button for the common modal
    const cancelCommonButton = commonModal.querySelector('.cancel-button');

    // Get the modal title element
    const modalTitle = commonModal.querySelector('.modal-title');

    // Function to open the common modal with a specific title and action URL
    function openCommonModal(title, action) {
        modalTitle.textContent = title; // Set the modal title
        commonModal.style.display = 'block';

        // Move the form initialization here to retrieve it when the modal is displayed
        const form = commonModal.querySelector('#employeeForm');

        if (action) {
            form.action = action; // Set the form action URL if action is provided
        }
    }

    // Function to close the common modal
    function closeCommonModal() {
        commonModal.style.display = 'none';
    }

    // Add click event listener to open the common modal for creating an employee
    if (createEmployeeButton) {
        createEmployeeButton.addEventListener('click', function() {
            // Use Django URL tag to generate the action URL
            const createEmployeeURL = "{% url 'employee-create' %}";
            openCommonModal('Create Employee', createEmployeeURL);
        });
    }

    // Add click event listeners to open the common modal for editing an employee
    if (editEmployeeButtons) {
        editEmployeeButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const title = button.getAttribute('data-modal-title');
                const employeeId = button.getAttribute('data-id');
                
                // Use Django URL tag to generate the action URL with employee ID
                const editEmployeeURL = "{% url 'employee-edit' 0 %}".replace('0', employeeId);
                openCommonModal(title, editEmployeeURL);
            });
        });
    }

    // Add click event listener to close the common modal
    if (cancelCommonButton) {
        cancelCommonButton.addEventListener('click', closeCommonModal);
    }
});
