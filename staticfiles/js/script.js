window.onload = function () {
    var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (isMobile) {
        document.getElementById("mobileMessage").style.display = "block";
        document.getElementById("registrationForm").style.display = "none";
    }

    // Disable zooming
    document.addEventListener(
        "wheel",
        function (event) {
            if (event.ctrlKey === true) {
                event.preventDefault();
            }
        },
        { passive: false }
    );
}
function preventDefault(e) {
    e.preventDefault();
}
function preventDefault(e) {
    e.preventDefault();
}

// Function to prevent default behavior
function preventDefault(e) {
    e.preventDefault();
}
// Disable right-click
document.addEventListener('contextmenu', function (event) {
    event.preventDefault();
    showFunnyWarningModalRightClick('Right-clicking is disabled!');
});
//Disable Shortcuts
document.addEventListener('keydown', function (event) {
    // Detecting F12 key
    if (event.keyCode == 123) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Ctrl+Shift+I (Linux)
    else if (event.ctrlKey && event.shiftKey && event.keyCode == 73) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Cmd+Option+I (macOS)
    else if (event.metaKey && event.altKey && event.keyCode == 73) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Cmd+Shift+c (macOS)
    else if (event.metaKey && event.shiftKey && event.keyCode == 67) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Ctrl+Shift+C (Linux)
    else if (event.ctrlKey && event.shiftKey && event.keyCode == 67) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Cmd+Option+C (macOS)
    else if (event.metaKey && event.altKey && event.keyCode == 67) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Ctrl+Shift+J (Linux)
    else if (event.ctrlKey && event.shiftKey && event.keyCode == 74) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Cmd+Option+J (macOS)
    else if (event.metaKey && event.altKey && event.keyCode == 74) {
        event.preventDefault();
        showFunnyWarningModal('Inspect shortcut is disabled!');
    }
    // Detecting Ctrl+U (Windows/Linux)
    else if (event.ctrlKey && event.keyCode == 85) {
        event.preventDefault();
        showFunnyWarningModal('Viewing source code is disabled!');
    }
    // Detecting Cmd+Option+U (macOS)
    else if (event.metaKey && event.altKey && event.keyCode == 85) {
        event.preventDefault();
        showFunnyWarningModal('Viewing source code is disabled!');
    }
});

function showFunnyWarningModal() {
    var modal = document.getElementById("funnyWarningModal");
    modal.style.display = "block";
}

function showFunnyWarningModalRightClick() {
    var modal = document.getElementById("funnyWarningModalRightClick");
    modal.style.display = "block";
}





function closeModal() {
    var modal = document.getElementById("funnyWarningModal");
    modal.style.display = "none";
}

function closeModalRightClick() {
    var modal = document.getElementById("funnyWarningModalRightClick");
    modal.style.display = "none";
}