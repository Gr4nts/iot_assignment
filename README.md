# iot_assignment
This repository is for Assignment 1 of Programming Internet of Things using the Raspberry Pi and sensehat.
The code reads temperature from a sensehat over the course of a week and then prints it to a web interface read from a file, it also sends notifications to the user if the temperature is under or over 20 degrees. 
The third file is for the bluetooth rasberry pi that picks up devices in its proximity and sends messages to it

# Create.py is the creation of the database where the temperature are stored
# Crontask.py is reading of the sensehat and the Raspberry pi, into the database
# notification.py is the used with pushbullet and notifies the user when the temperatureß
