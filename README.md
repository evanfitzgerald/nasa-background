# nasa-background
Updates your background everyday based on NASA's Astromony photo of the day using their open API. 

<p align = "center">
<img src = "9-5-2019.jpg" width=600 height=400 alt="" </p> 

## Installation

Requirements: Python 3.X+ 

```
git clone https://github.com/evanfitzgerald/nasa-background.git

pip3 install -r requirements.txt
```
### Getting an API key & File Storage

After cloning the projects files and installing the requirements you must request to get an API key for access to NASA's API. 
[(click here)](https://api.nasa.gov/index.html#apply-for-an-api-key)

Next, find a directory to store the files and edit the following in the potd.py file:

```
# enter nasa api key
api_key = 'enter_the_api_key_here'

# enter where you want the photos to be stored
filename = 'enter_the_directory_here'
```

## Usage
In order to run the file:
```
cd wherever_the_directory_is

python3 potd.py
```
### Automator
If you have macOS the automator is a good solution to automate the process of manually running the file everyday. 

To use the Automator: 

1. Start automator and select Application.
2. Add 'Run Shell Script' to the workflow.
3. Add the following to the script.
```
python ~/directory_of_choice/potd.py
```
4. Go to System Preferences > Users & Groups > Login Items and then add the application you made with the Automator.
 
## Liscense

See the [LICENSE](https://github.com/evanfitzgerald/nasa-background/blob/master/LICENSE) file for license rights and limitations.
