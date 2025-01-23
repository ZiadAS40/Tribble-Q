
![Tribble-Q Logo](app/static/Images/logo.png)

## Table of Contents

- [Introduction](#tribble-q)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)


## Introduction

Tribble-Q is a web application designed for professors to create quizzes for their students, grade them, and access various features such as IQ tests.

## Features

- Create and manage quizzes
- Grade student submissions
- Access IQ tests and other assessment tools
- Real-time quiz analytics
- Secure student authentication


## Getting Started

Follow these steps to set up and run the project in a virtual environment.

### Prerequisites

- Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the Repository**

    First, clone the repository to your local machine:

    ```bash
    git clone https://github.com/ZiadAS40/Tribble-Q.git
    ```

2. **Navigate to the Project Directory**

    Change the directory to your project folder:

    ```bash
    cd Tribble-Q
    ```

3. **Create a Virtual Environment**

    Create a virtual environment to manage dependencies:

    ```bash
    python3 -m venv venv
    ```

    This creates a folder named `venv` in your project directory, which contains the virtual environment.

4. **Activate the Virtual Environment**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Install the Required Packages**

    With the virtual environment activated, install the necessary packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Project**

    After the installation is complete, you can run your project:

    ```bash
    python3 -m run
    ```

### Deactivation

When you're done working in the virtual environment, you can deactivate it:

```bash
deactivate
```

### Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Register and log in.
3. Try some quizzes.
4. Go the subscription section.
5. Subscripe in the first one and enter the promocode 'QQQ100'.
6. you can also make pouplate files and make quizzes 'see populate_quizzeis.py for reference'
7. you can populate with 
    ```bash
    python3 -m your_file
    ```
    