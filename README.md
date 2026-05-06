# 🚀 Automation Testing Framework (Playwright + Python)

## 📌 Overview

This project is a scalable **Automation Testing Framework** built using **Playwright + Python + Pytest**, designed to support both UI and API testing with CI/CD integration.

The framework follows best practices for:

* Maintainability
* Scalability
* Reusability
* CI/CD readiness

---

## 🎯 Key Features

* ✅ End-to-End UI automation (Checkout flow)
* ✅ Page Object Model (POM)
* ✅ Config-driven environment (dev/staging)
* ✅ Pytest-based test structure
* ✅ Allure reporting integration
* ✅ CI/CD ready (GitHub Actions)
* ✅ Scalable architecture for multi-team usage

---

## 🧱 Project Structure

```
automation-framework/
│
├── config/                # Environment configs
├── core/                  # Core framework (config, base, utils)
│
├── ui/
│   ├── pages/             # Page Object Models
│   └── tests/             # UI test cases
│
├── api/
│   ├── services/          # API service layer
│   └── tests/             # API test cases
│
├── reports/               # Test reports (ignored in git)
│
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```
git clone https://github.com/bichvt233/fv-automation-framework.git
cd fv-automation-framework
```

---

### 2. Create virtual environment

#### Windows (CMD):

```
python -m venv venv
venv\Scripts\activate
```

#### PowerShell:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
playwright install
```

---

## ▶️ Run Tests

### Run all tests

```
pytest -s -v --env=staging
```

---

### Run specific test type

```
pytest -m smoke
pytest -m ui
pytest -m api
```

---

### Run tests in parallel

```
pytest -n 4
```

---

## 📊 Test Report (Allure)

### Generate report

```
pytest --alluredir=reports
```

### View report

```
allure serve reports
```

---

## 🧪 Test Coverage

### UI Automation

* Login
* Add product to cart
* Checkout flow
* Order completion validation

### API Automation (extendable)

* Service-based testing structure
* Ready for scaling

---

## ⚙️ Configuration

Environment configs are stored in:

```
config/staging.env
```

Example:

```
BASE_URL=https://www.saucedemo.com
```

---

## 🔁 CI/CD Integration

This project is designed to integrate with **GitHub Actions**:

### CI Flow:

* Run smoke tests on Pull Request
* Run full regression on merge
* Generate and store test reports

---

## 🧠 Design Principles

* Separation of concerns (UI / API / Core)
* Reusable components (service layer, page objects)
* Config-driven execution
* CI-first testing mindset

---

## 📈 Future Improvements

* Add API test coverage
* Add performance testing (k6/JMeter)
* Dockerize test execution
* Integrate test analytics dashboard
* Implement flaky test detection

---

## 👤 Author

**Vũ Thị Bích**

---

## 💡 Notes

This framework is built as a **real-world scalable solution**, not just a demo project.
It can be extended for enterprise-level automation across multiple teams.

---
