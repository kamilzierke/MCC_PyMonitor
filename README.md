# MCC_PyMonitor
Very simple Flask app to read data from the MegaCell Charger

![obraz](https://github.com/kamilzierke/MCC_PyMonitor/assets/67487992/4cd35a3c-606b-4830-a03f-6d4f37fb1a8d)

To run the provided Python code with Flask, Pandas, and socket communication, you will need to have Python installed on your system, along with the Flask and Pandas libraries. 
First donwload both files. Edit the main.py file with notepad and change the line 

    server_address = ('192.168.1.x', 8886)

To contain your MCC IP address.


Here's a simplified instruction set for both PowerShell on Windows and Bash on Unix-based systems (like Linux or macOS) for running the script.

For Windows (PowerShell):

  Install Python from the official website: python.org.
  Open PowerShell and install Flask and Pandas using pip (Python's package installer):
  
    pip install Flask pandas

Go to the folder with downloaded main.py and template/index.html files/folders.
Holding shift right click on the empty space in the folder and chose "Open Powershell window here"
Run the app:

    python main.py

For Unix-based systems (Bash):

  Install Python using your distribution's package manager, for example, on Ubuntu:

    sudo apt update
    sudo apt install python3 python3-pip

Install Flask and Pandas using pip:

    pip3 install Flask pandas

Go to the folder with downloaded main.py and template/index.html
Run the script:

    python3 main.py

General Notes:

Ensure you have network access to the IP f your device on port 8886, as specified in your Python script.
Place the index.html file inside a templates folder in the same directory as your main.py.
The Python script will start a Flask web server on http://localhost:5000. Open this URL in a web browser to view the application.

The script will listen for UDP packets on port 8886 and update the web page with the received data. 
Make sure the device sending the data is configured to send to the correct IP address and port.

No virtualization is needed, and these instructions are for running the code directly on your local machine's operating system.
