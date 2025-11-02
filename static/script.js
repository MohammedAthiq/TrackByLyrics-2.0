document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.querySelector(".theme-toggle");

    // Apply saved theme globally
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme === "dark") {
        document.body.classList.add("dark");
        if (toggleButton) toggleButton.textContent = "☀️ Light Mode";
    } else {
        document.body.classList.remove("dark");
        if (toggleButton) toggleButton.textContent = "🌙 Dark Mode";
    }

    // Toggle theme on click and save preference
    if (toggleButton) {
        toggleButton.addEventListener("click", () => {
            document.body.classList.toggle("dark");
            const isDark = document.body.classList.contains("dark");
            toggleButton.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
            localStorage.setItem("theme", isDark ? "dark" : "light");
        });
    }
});