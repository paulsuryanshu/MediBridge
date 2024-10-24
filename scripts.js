// Scroll-to-Top functionality
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.onscroll = function () {
    let scrollTopBtn = document.getElementById('scrollTopBtn');
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollTopBtn.classList.add('show');
    } else {
        scrollTopBtn.classList.remove('show');
    }
};

let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function changeSlide(n) {
    showSlide(currentSlide += n);
}

function showSlide(n) {
    if (n >= slides.length) {
        currentSlide = 0;
    } 
    if (n < 0) {
        currentSlide = slides.length - 1;
    }
    slides.forEach((slide) => slide.classList.remove('active'));
    slides[currentSlide].classList.add('active');
}

// Auto-play functionality (Optional)
setInterval(() => {
    changeSlide(1);
}, 5000); // Change image every 5 seconds

// Testimonial Slider functionality
const testimonials = [
    { text: "This service has transformed healthcare in my rural community.", author: "- Dr. A" },
    { text: "AI diagnostics have made it easier to detect diseases early.", author: "- Nurse B" },
    { text: "We can now provide quality healthcare even in remote areas.", author: "- Health Worker C" }
];
let currentTestimonial = 0;

function updateTestimonial() {
    document.getElementById('testimonial-text').innerText = testimonials[currentTestimonial].text;
    document.getElementById('testimonial-author').innerText = testimonials[currentTestimonial].author;
}

function prevTestimonial() {
    currentTestimonial = (currentTestimonial === 0) ? testimonials.length - 1 : currentTestimonial - 1;
    updateTestimonial();
}

function nextTestimonial() {
    currentTestimonial = (currentTestimonial === testimonials.length - 1) ? 0 : currentTestimonial + 1;
    updateTestimonial();
}

// JavaScript for Hero Pop-Up
function openHero() {
    document.getElementById("hero-popup").style.display = "flex";
}

function closeHero() {
    document.getElementById("hero-popup").style.display = "none";
}

// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Add scroll event listener for parallax effect
    window.addEventListener("scroll", function() {
        const heroSection = document.querySelector(".hero-section");
        const scrollPosition = window.scrollY;
        const viewportHeight = window.innerHeight;
        
        // Apply parallax-like effect by modifying hero section position
        if (scrollPosition < viewportHeight) {
            heroSection.style.transform = `translateY(${scrollPosition * 0.5}px)`;
            heroSection.style.opacity = 1 - scrollPosition / viewportHeight;
        }
    });
    
    // Open hero pop-up automatically when the page loads
    openHero(); // This will automatically open the pop-up
});

// Contact Form Validation
document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;

    let isValid = true;
    
    if (name === "") {
        document.getElementById('nameError').innerText = "Name is required";
        isValid = false;
    } else {
        document.getElementById('nameError').innerText = "";
    }

    if (email === "") {
        document.getElementById('emailError').innerText = "Email is required";
        isValid = false;
    } else {
        document.getElementById('emailError').innerText = "";
    }

    if (message === "") {
        document.getElementById('messageError').innerText = "Message is required";
        isValid = false;
    } else {
        document.getElementById('messageError').innerText = "";
    }

    if (isValid) {
        alert("Form submitted successfully!");
    }
});
