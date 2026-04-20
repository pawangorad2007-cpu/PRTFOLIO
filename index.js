// ================= TYPING EFFECT =================
const roles = [
    "First-Year ENTC Student at MITAOE",
    "IoT Enthusiast",
    "Electronics Learner"
];

let i = 0;
let j = 0;
let current = "";
let isDeleting = false;

function type() {
    current = roles[i];

    if (isDeleting) {
        j--;
    } else {
        j++;
    }

    document.getElementById("typing").textContent = current.substring(0, j);

    if (!isDeleting && j === current.length) {
        isDeleting = true;
        setTimeout(type, 1200); // pause at full text
        return;
    }

    if (isDeleting && j === 0) {
        isDeleting = false;
        i = (i + 1) % roles.length;
    }

    setTimeout(type, isDeleting ? 50 : 100);
}

document.addEventListener("DOMContentLoaded", type);


// ================= SCROLL ANIMATION =================
const sections = document.querySelectorAll("section");

function revealSections() {
    const triggerBottom = window.innerHeight * 0.85;

    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;

        if (sectionTop < triggerBottom) {
            section.classList.add("show");
        }
    });
}

// Run on load + scroll
window.addEventListener("scroll", revealSections);
window.addEventListener("load", revealSections);