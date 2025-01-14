# CashFlow

CashFlow is a Django-based web application designed to manage and track financial transactions.

## Getting Started

Follow the instructions below to set up and run the project locally.

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment module (optional but recommended)

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   
2. Navigate to the project directory:
   ```bash
   cd cashFlow

3. Create a virtual environment:
   ```bash
   python -m venv env

4. Activate the virtual environment:
On Windows:
   ```bash
    .\env\Scripts\activate
On macOS/Linux:

    source env/bin/activate

5. Install the required dependencies:
   ```bash
    pip install -r requirements.txt

6. Navigate to the Django project directory:
    ```bash
    cd cash_flow_django
7. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
8. Start the development server:
    ```bash
    python manage.py runserver
9. Open your web browser and go to: http://127.0.0.1:8000/

Ensure your Python version matches the project's requirements.
Always activate the virtual environment before running commands for this project.
If you encounter any issues, refer to the Django documentation.

### License
This project is licensed under the MIT License
