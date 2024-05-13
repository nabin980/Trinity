function showUserList() {
    var userListContent = document.getElementById("userListContent");
    if (userListContent.style.display === "none") {
        userListContent.style.display = "block";
    } else {
        userListContent.style.display = "none";
    }
}

function openEmailPopup(email, requestId) {
    var modal = document.getElementById('emailModal_' + requestId);
    var recipientField = modal.querySelector('.recipient-field');

    // Set the value of the recipient field to the clicked email
    recipientField.value = email;

    // Show the modal
    modal.style.display = 'block';
}


function closeEmailPopup(requestId) {
    var modal = document.getElementById('emailModal_' + requestId);
    
    // Hide the modal
    modal.style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form").forEach(form => {
        form.addEventListener("submit", function (event) {
            // event.preventDefault();

            const isEmailSent = true; // Replace this with your actual email sending logic

            if (isEmailSent) {
                const modalOverlay = document.getElementById("modalOverlay");
                const popupMessage = document.getElementById("popupMessage");

                popupMessage.textContent = "Email sent successfully";
                modalOverlay.style.display = "block";

                setTimeout(() => {
                    modalOverlay.style.display = "none";
                }, 5000); // Adjust the time the message stays visible (in milliseconds)
            }
        });
    });
});


function closePopup() {
    const modalOverlay = document.getElementById("modalOverlay");
    document.body.classList.remove("blur-background");
    modalOverlay.style.display = "none";
}


//  TOASTS 
const sendEmailButton = document.getElementById("sendEmailButton");
const toast = document.querySelector(".toast");
const closeIcon = document.getElementById("close");
const progress = document.querySelector(".progress");

let timer1, timer2;

sendEmailButton.addEventListener("click", () => {
    toast.classList.add("active");
    progress.classList.add("active");

    timer1 = setTimeout(() => {
        toast.classList.remove("active");
    }, 5000); // 5 seconds for toast to disappear

    timer2 = setTimeout(() => {
        progress.classList.remove("active");
    }, 5300); // 5.3 seconds for progress bar to disappear
});

closeIcon.addEventListener("click", () => {
    toast.classList.remove("active");
    setTimeout(() => {
        progress.classList.remove("active");
    }, 300);

    clearTimeout(timer1);
    clearTimeout(timer2);
});



