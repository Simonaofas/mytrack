# mytrack
Emergency Response Tracking Web Application

## Overview

This web application is designed to track individuals in real-time during emergency situations such as evacuation, camping, and hiking. The goal is to provide a reliable and efficient system for emergency responders to locate and assist individuals in distress.

## Features

- Real-time GPS tracking of individuals.
- Emergency alert system for users to request assistance.
- User-friendly interface for both individuals and emergency responders.

## Technology Stack

- **Backend:**
  - Python with Django framework.
  - Database: PostgreSQL for storing user data.

- **Frontend:**
  - HTML, CSS, JavaScript.
  - Mapping: Integration with Google Maps API for location visualization.

## Installation

1. Clone the repository:
   ```zsh
   git clone https://github.com/your/repository.git
   ```

2. Navigate to the project directory:
   ```zsh
   cd myproject
   ```
3. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```
4. Set up and migrate the database:
   ```zsh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```zsh
   python manage.py runserver

## Google Api Activations
**Note: **
-Create and update settings.py  with  API Key information linked to your email.

GOOGLE_API_KEY = ""

RECAPTCHA_PUBLIC_KEY = ""

RECAPTCHA_PRIVATE_KEY = ""

-Don't forget to activate and enable  the following Google API's

reCAPTURE
Places API
Maps Javascript API
Directions API
Distance Matrix API
Geocoding API

## Usage

1. Access the application at [http:// http://127.0.0.1:8000.
2. SignUp for new account and Signin.
3. Create Your Profile and Update for Existing user Changes.
4. Enter Your routes adress to Navigate from origin to the  destinations.

## Contributing

Contributions are welcome!  

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview)
- [Django Documentation](https://docs.djangoproject.com/)
- ComIT




