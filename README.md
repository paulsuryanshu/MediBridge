# MediBridge

MediBridge is a web application aimed at transforming rural healthcare through AI-driven diagnostics, providing accessible and efficient healthcare solutions for underserved communities.

## Live Demo

Check out the live demo of [**MediBridge**](https://paulsmedibridge.netlify.app/).

## Features

- **AI Diagnostics**: Offers healthcare diagnostics powered by AI, specifically targeted to meet the needs of rural areas.
- **Image Slider**: Highlights services with a dynamic image carousel.
- **Testimonials**: Features client feedback to build trust and credibility.
- **Contact Form**: Easy-to-use form for users to get in touch with the MediBridge team.

## Project Structure

         MediBridge/
         │
         ├── static/                    # Static assets
         │   ├── images/                # Images used across the application
         │   ├── css/                   # Stylesheets for the web pages
         │   └── js/                    # JavaScript files for interactive features
         ├── templates/                 # HTML templates
         │   ├── index.html             # Main homepage
         │   ├── about.html             # About MediBridge's mission and team
         │   ├── services.html          # Detailed services page
         │   ├── contact.html           # Contact page
         │   └── testimonials.html      # Testimonials page
         ├── README.md                  # Project documentation
         └── app.py                     # Main Flask application file (if using backend)


## Technologies Used

- **HTML5** - Structure and content
- **CSS3** - Styling, animations, and layout
- **JavaScript** - Dynamic elements and interactions
- **Flask** - (Optional) For backend and AI model integration
- **Machine Learning** - Pre-trained models for health diagnostics

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/paulsuryanshu/MediBridge.git
2. Navigate to the project directory:
   ```bash
   cd MediBridge
3. If using a backend:
   
   Set up a virtual environment (optional but recommended):
      ```bash
      python3 -m venv venv
      source venv/bin/activate  # For Linux/Mac
      venv\Scripts\activate     # For Windows
          
Install the required packages:
      
      
      pip install -r requirements.txt
      
4. Frontend-only option:
      ```bash
      
      Open index.html directly in your browser.
5. Backend with Flask:
   
     Run the application:
   
         
   
          python app.py

      Open your browser and go to http://127.0.0.1:5000.