# PASSWORD LOCKER

## Description

A simple python program which runs on the terminal it securely stores your user's account credentials for various pages and also generates passwords for a user's new page account.

## Features

- The program utilizes two classes:- Account and Credential.
- The program authenticates accounts to see their credentials.
- Contains docstrings to document methods and functions.
- Contains a test class for all the classes testing each individual method in a class.
- Program saves data on exiting to use during next launch

## User Stories

- A user can create a password locker account with my details, a login username and password.
- A user can store my already existing account credentials in the application.
- A user can create new account credentials in the application.
- A user has the option of putting in a password that he/she want to use for the new credential account.
- A user can view various account credentials and their passwords in the application
- A user can delete credentials account that he/she no longer needs in the application.

## Requirements

- This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
- Once python is installed, install the folowing external libraries using pip:
  - **`pip3 install pyperclip`**
  - **`pip3 install termcolor`**
  - **`pip3 install unittest`**

## Short-codes and Keywords

- Short-codes:
  - **ln**: Logs the user in
  - **xx/ex**: Closes the application
  - **sc**: Save existing page credentials
  - **cc**:Create new page credentials
  - **dc**: Display all credentials saved
  - **fc**: Find credential saved by page name
  - **cp**: Copy pagename credential password to clipboard
  - **dl**:Delete page credential
  - **lgo**: Log out

A very interactive search web app that uses a simple forms to get users and their repository at GitHub.

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/HASSAN1A/Password-Locker/issues/new) by including your search query and the expected result.
If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/HASSAN1A/Password-Locker). Please include sample queries and their corresponding results.

## Built with

1. Python 3.8.2
2. Python libraries used:
   - pyperclip
   - random (inbuilt)
   - time (inbuilt)
   - pickles (inbuilt)
   - termcolor
   - unittest

## Setup/Installation

First make sure you have installed the required modules from above as well as have python 3.8 installed in your computer.
Here is a run through of how to set up the application:

- **Step 1** : Clone this repository using \*\*`## Technologies Used
- Python 3.8.2
- Python libraries used:
  _ pyperclip
  _ random
  _ time
  _ pickles
  _ termcolor
  _ unittest
  `\*\*, or downloading a ZIP file of the code.
- **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
- **Step 3** : Open the terminal, go to the project directory and run the following commands: **`chmod +x run.py`** and **`./run.py`** respectively to launch the program.

## Team

[Hassan Juma ](https://github.com/HASSAN1A)

## [License](https://github.com/HASSAN1A/Password-Locker/blob/master/LICENSE.md)

[MIT](https://github.com/HASSAN1A/Password-Locker/blob/master/LICENSE.md) © [Hassan Juma](https://github.com/HASSAN1A)
