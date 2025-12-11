document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault(); // Prevent page reload

      let isValid = true;
      let message = "Please fill in all required fields.";

      // Generic field checks
      const nameInput = document.getElementById("name");
      const emailInput = document.getElementById("email");
      const messageInput = document.getElementById("message");
      const interestInput = document.getElementById("interest");

      if (nameInput && nameInput.value.trim() === "") isValid = false;
      if (emailInput && emailInput.value.trim() === "") isValid = false;
      if (messageInput && messageInput.value.trim() === "") isValid = false;
      if (interestInput && interestInput.value === "") isValid = false;

      if (!isValid) {
        alert(message);
        return;
      }

      // Success message — you can change per page
      alert("Form submitted successfully!");
      form.reset(); // Clear the form
    });
  }
});
