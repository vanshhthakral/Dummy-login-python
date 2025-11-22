// app.js
// Frontend behaviour for the dummy login system demo.

// ⚠ Matches the insecure credentials in config.py (for demo only)
const DEMO_USERNAME = "admin";
const DEMO_PASSWORD = "Admin@123";

const form = document.getElementById("loginForm");
const messageEl = document.getElementById("message");

function showMessage(text, type) {
    messageEl.textContent = text;
    messageEl.classList.remove("message--error", "message--success");

    if (type === "success") {
        messageEl.classList.add("message--success");
    } else {
        messageEl.classList.add("message--error");
    }
}

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    if (username === DEMO_USERNAME && password === DEMO_PASSWORD) {
        showMessage("Login successful! Redirecting...", "success");

        // Store session data
        localStorage.setItem("username", username);

        setTimeout(() => {
            window.location.href = "dashboard.html";
        }, 1000);
    } else {
        showMessage("Invalid credentials. Try admin / Admin@123.", "error");
    }
});
