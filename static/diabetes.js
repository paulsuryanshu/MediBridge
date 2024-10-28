// Scroll to Top Button functionality
const scrollTopBtn = document.getElementById('scrollTopBtn');

// Show or hide the scroll to top button based on scroll position
window.onscroll = function() {
    handleScroll();
};

function handleScroll() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        scrollTopBtn.style.display = "block";
    } else {
        scrollTopBtn.style.display = "none";
    }
}

// Scroll to the top of the document when the button is clicked
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Sticky navigation bar functionality (optional: change style on scroll)
window.addEventListener('scroll', function() {
    const navbar = document.getElementById('navbar');
    if (window.pageYOffset > 50) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }
});

// Basic form validation
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    const age = document.getElementById('age').value;
    const sex = document.getElementById('sex').value;
    const cp = document.getElementById('cp').value;
    const trestbps = document.getElementById('trestbps').value;
    const chol = document.getElementById('chol').value;
    const fbs = document.getElementById('fbs').value;
    const restecg = document.getElementById('restecg').value;
    const thalach = document.getElementById('thalach').value;
    const exang = document.getElementById('exang').value;
    const oldpeak = document.getElementById('oldpeak').value;
    const slope = document.getElementById('slope').value;
    const ca = document.getElementById('ca').value;
    const thal = document.getElementById('thal').value;

    // Simple validation for numerical fields
    if (isNaN(age) || age <= 0) {
        alert('Please enter a valid age.');
        event.preventDefault();
        return false;
    }
    
    // Add other validations as needed
    if (isNaN(sex) || (sex !== '0' && sex !== '1')) {
        alert('Please enter a valid sex (0 for female, 1 for male).');
        event.preventDefault();
        return false;
    }

    // Validate chest pain type
    if (isNaN(cp) || cp < 1 || cp > 4) {
        alert('Chest Pain Type must be between 1 and 4.');
        event.preventDefault();
        return false;
    }

    // Continue validations for other fields if necessary
    // ...

    // If all validations pass, allow the form submission
    return true;
});
