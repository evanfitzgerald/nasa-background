
import requests, shutil, subprocess, datetime

# enter nasa api key
api_key = '2yBfvfL62Je5l47lynCx7Vcd7hdzwlKpvxzzAthg'

# enter where you want the photos to be stored
filename = '/Users/evandfitz/Desktop/Personal/Projects/nasa-background/'

# http request
url = 'https://api.nasa.gov/planetary/apod?api_key=' + api_key
response = requests.get(url)

# lets use know if our http request was sucessful
if response.status_code == 200:

    # data from the request
    data = response.text

    # current date, used for naming file
    now = datetime.datetime.now()
    date = str(now.month) + '-' + str(now.day) + '-' + str(now.year)
    filename = filename + date + '.jpg'

    # parsing data to get url of photo
    response = requests.get(data[data.find('https:'):data.find('.jpg')] + '.jpg', stream=True)

    # checks if the 'photo of the day' is a youtube clip instead
    if 'youtube' in data[data.find('https:'):data.find('.jpg')]:
        print('video found, no changes made')

    else:
        # downloading photo
        photo = open(filename, 'wb')
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, photo)
        del response

        # changes the background image
        SCRIPT = """osascript -e 'tell application "Finder" to set desktop picture to """ + '"' +filename+ '"' +""" as POSIX file'"""
        subprocess.Popen(SCRIPT, shell=True)

        # to make this process run during a login, see steps on using the automator in macOS

# lets us know if there is an error with the http request
else:
    print('error with request')
