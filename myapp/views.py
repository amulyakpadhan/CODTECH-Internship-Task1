import os
import datetime
import requests
from django.conf import settings
from django.shortcuts import render
from .forms import TextToSpeechForm

def index(request):
    if request.method == 'POST':
        form = TextToSpeechForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            language_code = form.cleaned_data['language_code']
            voice_code = form.cleaned_data['voice_code']

            # Define API request parameters
            url = "http://api.voicerss.org/"
            params = {
                'key': 'c6c26ba0732446648551a35dec8eb712',  # Replace with your actual API key
                'hl': language_code,
                'c': 'MP3',
                'src': text,
                'v': voice_code
            }

            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                # Generate a unique filename based on the current timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                audio_filename = f"audio_{timestamp}.mp3"
                audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
                with open(audio_path, 'wb') as audio_file:
                    audio_file.write(response.content)
                audio_url = os.path.join(settings.MEDIA_URL, audio_filename)
                return render(request, 'index.html', {'form': form, 'audio_url': audio_url})

            else:
                return render(request, 'index.html', {'form': form, 'error': 'API request failed: ' + response.text})
    else:
        form = TextToSpeechForm()

    return render(request, 'index.html', {'form': form})


def cleanup_old_audio_files():
    # Define the threshold for old audio files (e.g., files older than 7 days)
    threshold_date = datetime.datetime.now() - datetime.timedelta(days=7)

    # Iterate over the files in the media folder
    for filename in os.listdir(settings.MEDIA_ROOT):
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.isfile(file_path):
            # Get the creation time of the file
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            # Check if the file is older than the threshold date
            if creation_time < threshold_date:
                # Delete the file
                os.remove(file_path)

def schedule_audio_cleanup():
    # Schedule the cleanup task to run periodically (e.g., daily)
    cleanup_old_audio_files()

# Call the schedule_audio_cleanup function when this module is imported
schedule_audio_cleanup()

def about(request):
    return render(request, 'about.html')