document.addEventListener('DOMContentLoaded', function() {
    // Get the common modal
    const commonModal = document.querySelector('.modal-common');

    // Get the buttons that open the common modal
    const createEmployeeButton = document.querySelector('.create-employee');
    const editEmployeeButtons = document.querySelectorAll('.edit-employee');
    const deleteEmployeeButtons = document.querySelectorAll('.delete-employee');

    // Get the cancel button for the common modal
    const cancelCommonButton = commonModal.querySelector('.cancel-button');

    // Get the modal title element
    const modalTitle = commonModal.querySelector('.modal-title');

    // Flag to track whether a create or edit modal is open
    let createEditModalOpen = false;

    // Function to open the common modal
    function openCommonModal(title, action, formElement, customClass) {
        modalTitle.textContent = title; // Set the modal title
        commonModal.style.display = 'block';
        if (customClass) {
            commonModal.classList.add(customClass); // Add the custom class
        }

        if (action && formElement) {
            formElement.action = action; // Set the form action URL if action and formElement are provided
        }

        // Set the flag to true when a create or edit modal is open
        createEditModalOpen = true;
    }

    // Function to close the common modal
    function closeCommonModal() {
        commonModal.style.display = 'none';

        // Reset the flag when the common modal is closed
        createEditModalOpen = false;
    }

    // Add click event listener to open the common modal for creating an employee
    if (createEmployeeButton) {
        createEmployeeButton.addEventListener('click', function() {
            // Use Django URL tag to generate the action URL
            const createEmployeeURL = "{% url 'employee-create' %}";
            openCommonModal('Create Employee', createEmployeeURL, null, 'employee-form-modal');
        });
    }

    // Add click event listeners to open the common modal for editing an employee
    if (editEmployeeButtons) {
        editEmployeeButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                if (!createEditModalOpen) { // Check if a create or edit modal is already open
                    const title = button.getAttribute('data-modal-title');
                    const editEmployeeURL = button.getAttribute('data-edit-url');

                    // Fetch the employee details and populate the form fields
                    fetch(editEmployeeURL)
                        .then(response => response.json())
                        .then(data => {
                            document.querySelector('[name="first_name"]').value = data.first_name;
                            document.querySelector('[name="last_name"]').value = data.last_name;
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });

                    openCommonModal(title, editEmployeeURL, null, 'employee-form-modal');
                }
            });
        });
    }

    // Function to open the delete confirmation modal
    function openDeleteConfirmationModal(title, action, formElement, customClass) {
        modalTitle.textContent = title; // Set the modal title
        commonModal.style.display = 'block';
        if (customClass) {
            commonModal.classList.add(customClass); // Add the custom class
        }

        if (action && formElement) {
            formElement.action = action; // Set the form action URL if action and formElement are provided
        }
    }

    // Function to open the delete confirmation modal
    function openDeleteConfirmation(employeeId, deleteEmployeeURL) {
        if (!createEditModalOpen) { // Check if a create or edit modal is already open
            const deleteForm = document.getElementById('deleteEmployeeForm');
            if (deleteForm) {
                // Set the form action URL and open the delete confirmation modal
                openDeleteConfirmationModal('Confirm Deletion', deleteEmployeeURL, deleteForm, 'delete-confirmation-modal');
            } else {
                console.error('Delete form not found.');
            }
        }
    }

    // Add click event listeners to open the delete confirmation modal
    if (deleteEmployeeButtons) {
        deleteEmployeeButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const employeeId = button.getAttribute('data-id');
                const deleteEmployeeURL = button.getAttribute('data-delete-url');
                openDeleteConfirmation(employeeId, deleteEmployeeURL);
            });
        });
    }

    // Add click event listener to close the common modal when "Cancel" is clicked
    if (cancelCommonButton) {
        cancelCommonButton.addEventListener('click', function() {
            closeCommonModal();
        });
    }
});
