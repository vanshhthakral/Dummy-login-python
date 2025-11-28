// dashboard.js

function logout() {
    // Clear stored username if you use it
    localStorage.removeItem("demoUsername");
    // Go back to login page
    window.location.href = "index.html";
}

// Optional: show username from localStorage if set by login page
document.addEventListener("DOMContentLoaded", () => {
    const label = document.getElementById("usernameLabel");
    const stored = localStorage.getItem("demoUsername");
    if (stored && label) {
        label.textContent = stored;
    }
});
