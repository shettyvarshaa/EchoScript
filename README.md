# Welcome to EchoScript

This is an extension that exhibits speech-to-code capabilities alongside contextual suggestions and debugging

## Prerequisites

##### Any machine with following packages installed
- nodejs
- git
- python 3.10

##### GitHub account
- Create an account on [GitHub](https://github.com/join) (if you don't already have one)
- Fork [this](https://github.com/shettyvarshaa/EchoScript) repository and then clone it to your machine
- You can refer [this](https://docs.github.com/en/get-started/quickstart/fork-a-repo) guide to understand how to fork and clone

##### NodeJs
- Download the NodeJS [prebuilt installer](https://nodejs.org/en/download/prebuilt-installer) (if you don't already have one)

## Set up locally

To set up EchoScript, follow these steps:

### 1. Clone the Repository

- Using HTTPS

```bash
git clone https://github.com/shettyvarshaa/EchoScript
```

- Using SSH

```bash
git clone git@github.com:shettyvarshaa/EchoScript
```
### 2. To set up server-side:

2.1 Navigate to the `backend` directory

2.2 Create a virtual environment

- For **Windows**

```bash
python -m venv venv
```

- For **Mac** and **Linux**

```bash
python3 -m venv venv
```


2.3 Activate the virtual environment

- For **Git Bash**
```bash
source ./venv/Scripts/activate
```

- For **Command-prompt**
```cmd
.\venv\Scripts\activate
```

- For **Powershell**
```cmd
.\venv\Scripts\Activate.ps1
```

- For Bash (Ubuntu Terminal)
```bash
source ./venv/bin/activate
```

2.4 Install the Dependencies for the backend

- For Windows

```cmd
pip install -r requirements.txt
```

- For Mac or Linux

```bash
pip3 install -r requirements.txt
```

### 3. To run the application:
3.1 To run the server-side, navigate to `backend` directory

```bash
cd backend
```

3.2 Start the local server

```bash
python main.py
```

3.3 To run the client-side, navigate to `echoscript/extension.js`.

3.4 Press `F5` to open a new window with your extension loaded.

3.5 Run your command from the command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `EchoScript`.

3.6 Say `start coding` to start voice commands.

3.7 Try out this query `find a java code for simple calculator from stack overflow `. (working on the logic to render it for generalized queries)
