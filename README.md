# Installation Guide for CentralHub
## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- **python3+** - [Python installation guide](https://realpython.com/installing-python/) for windows
- **git** - [Git installation guide](https://www.simplilearn.com/tutorials/git-tutorial/git-installation-on-windows) for windows

## Installation Steps


1. **Clone the repository:**
    ```commandline
    git clone --branch backend https://github.com/juniper06/CentralHub.git
    cd CentralHub
    ```

2. **Create Virtual Environment**
   
   **_NOTE:_**: if you haven't installed virtual environment in python or skip this command if you already installed
    ```commandline
     pip install virtualenv
     ```
3.   **Activate Virtual Environment**
     ```commandline
     python -m venv .venv
     ```
     ```commandline
     .venv\Scripts\activate
     ```
         
4. **Install Django**
   ```commandline
   pip install django
   ```
   
5. **Setup before run the server**
   1. ```commandline
      python manage.py migrate
      ```
   2. ```commandline
      python manage.py createsuperuser
      ```

6. **Run the Server**
   ```commandline
   python manage.py runserver
   ```