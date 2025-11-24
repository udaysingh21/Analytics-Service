# Contributing to Analytics Service (Python)

Thank you for contributing to the Analytics microservice!  
This service is part of the larger **Volunteer Resource Management System (VRMS)**.

Before contributing, please **read the main VRMS contribution guide**:

**Main Contribution Guide:**  
[CONTRIBUTING.md](https://github.com/udaysingh21/Volunteer-Resource-Management-System/blob/main/CONTRIBUTING.md)

---

## Tech Stack

- Python 3.10+
- FastAPI / Flask / Django (depending on actual implementation)
- PostgreSQL (or chosen DB)
- Docker (recommended)
- Poetry/pip requirements

---

## Running the Service

### 1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
# OR if using Poetry:
poetry install
```

### 3. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your local configuration
```


### 4. Start the service
```bash
# For FastAPI:
uvicorn main:app --reload

# For Flask:
flask run

# For Django:
python manage.py runserver
```

---

## 🔧 Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful commit messages
- Add docstrings to functions and classes
- Use type hints where applicable
- Keep business logic in service layer, not in route handlers
- Write unit tests for new features

---

## How to Contribute

### 1. Create a feature branch
```bash
git checkout -b feature/my-change
```

### 2. Make your changes

### 3. Commit and push
```bash
git commit -am "Describe your change"
git push origin feature/my-change
```

### 5. Open a Pull Request

Open a Pull Request in this microservice's repo, **not** in VRMS.

---

## Updating in VRMS (Submodule Pointer)

After your PR is merged, update the VRMS meta-repository:
```bash
cd ../VRMS
git add analytics-service
git commit -m "Update submodule pointer for analytics-service"
git push
```

---

**Thank you again for contributing!**