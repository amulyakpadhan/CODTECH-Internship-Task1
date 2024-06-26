# Text-to-Speech Conversion Application

Name: Amulya Kumar Padhan\
Company: CODTECH IT SOLUTIONS\
Domain: Machine learning\
Duration: June 1st to June 30th

## Overview
This project aims to develop a text-to-speech conversion application that allows users to input text and generate corresponding audio output. The application should support multiple languages and voices, providing users with options to customize the speech synthesis according to their preferences.

## Live Demo
The project is deployed and can be accessed at: [Text-to-Speech Converter](https://ttsconverter.pythonanywhere.com/)


## Features
- Input text for speech synthesis.
- Support for multiple languages.
- Option to choose different voices for the speech output.
- Downloadable audio files in MP3 format.
- Automatic cleanup of old audio files.

## Technologies Used
- Python 3.x
- Django 3.x or 4.x
- API for text-to-speech conversion
- HTML/CSS (Bootstrap for styling)
- JavaScript (jQuery)
- Git (for version control)
- Virtual environment tool like `venv` or `virtualenv` (recommended)

## Setup and Installation
Follow these steps to set up and run the project locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com/amulyakpadhan/CODTECH-Internship-Task1.git
cd CODTECH-Internship-Task1
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# For Windows, use: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt  # Install the required packages
```

### Step 4: Configure Django Settings
Ensure your Django settings are configured properly:

- Set ALLOWED_HOSTS to include your local development domain.
- Configure DATABASES to use a suitable database (e.g., SQLite for development).
- Ensure MEDIA_ROOT and STATIC_ROOT are properly set to handle media files and static files.

### Step 5: Run Migrations
```bash
python manage.py migrate  # Apply database migrations
```

### Step 6: Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser  # Create an admin account
```
### Step 7: Start the Django Server
```bash
python manage.py runserver  # Start the Django development server
```
Now, you can access the project by navigating to http://127.0.0.1:8000/ in your web browser.

## Usage
- Open the application in your browser.
- Enter the text you want to convert to speech.
- Select the language and voice.
- Click the "Generate Audio" button.
- The generated audio will be available for playback and download.


## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or fix.
- Make your changes and commit them with descriptive commit messages.
- Push to your fork and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
- Django: The web framework used in this project.
- Text-to-Voice API: API for text-to-speech conversion

## 🚀 About Me
I'm Amulya Kumar Padhan, a computer science student specializing in artificial intelligence and web development. This project is a demonstration of my skills and expertise in building web-based applications that incorporate advanced technologies like machine learning, deep learning, web development etc.
