# clocTech
Email Sending Using Python (CLOC Script)
The whole point of this exercise is to count lines of code by scanning files of code, languages found, coments, number of files, etc... within a folder/file

Scope
The file scanning of a specific file can count the files and deploy the data within the file with a chart of explination. While using Python on the other hand. The code will allow the file that has collected all the data of cloc and sent the file to a designated email with proof of the documentation of cloc.

Steps
In order for the process of the cloc to be sent to an email using Python, there are some things that need to be handled before succefully finishing the production.

Go to your gmail that the email will be sent to and go to the "Manage Your Google Account" button
Go to "Security"
Click the toggle button that will "Allow less secure apps" to be ON
Use the Python code to send the file over to an email
After running the cloc and received teh data of cloc, then start up the Python code to send the email
Troubleshoot a problem
If the email was not received, double check if "Allow less secure apps" is ON. If it is off, the email will not go through
Python code was written on Visual Studio Code. If it does not run try running the source code on Terminal
If cloc is not recognized, make sure the cloc file is within the folder that you are using to catpure and send your data
If the file you are trying to send is not sending it to the email while running the Python code, make sure you type the correct file name of the cloc data correctly or "Copy the path" of the file and use that instead
