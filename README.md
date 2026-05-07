# 🚀 QA Automation Framework (Playwright + Python)

## 📌 Overview

This project demonstrates a **scalable automation testing framework** built with Playwright + Python, designed to support UI and API testing with CI/CD integration.

The focus is not just on writing test cases, but on building a **maintainable and scalable automation system** for real-world usage.

---

## 🧠 Business Problem

Manual regression testing is:

* Time-consuming
* Error-prone
* Hard to scale across teams

Especially for critical flows like **checkout**, where failures directly impact revenue.

---

## 💡 Solution

I designed and implemented a **modular automation framework** that:

* Automates end-to-end checkout flow
* Uses Page Object Model for maintainability
* Separates UI / API / Core layers
* Supports environment-based configuration
* Integrates with CI/CD for continuous testing

---

## 📈 Impact

* ⏱ Reduced regression testing time significantly
* 🔁 Enabled repeatable and reliable test execution
* ⚙️ Made automation scalable across multiple teams
* 🚀 Supported CI/CD pipeline for faster feedback

---

## 🏗️ Architecture

```text
Test Layer (UI/API)
        ↓
Page Objects / Service Layer
        ↓
Core Framework (config, utils)
        ↓
CI/CD (GitHub Actions)
```

---

## 🧱 Project Structure

```text
automation-framework/
│
├── .github/
│   └── workflows/
│       ├── pr-tests.yml        # Smoke tests on Pull Requests
│       └── regression.yml      # Full regression on push to main + daily schedule
│
├── config/
│   └── staging.env             # Environment variables (BASE_URL, etc.)
│
├── core/
│   ├── base_page.py            # Base Page Object with common actions
│   └── config.py               # Environment config loader
│
├── ui/
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── tests/
│       ├── test_checkout.py
│       └── data/
│           └── checkout_data.py
│
├── api/
│   ├── services/
│   └── tests/
│       ├── test_login_api.py
│       └── data/
│           └── api_data.py
│
├── conftest.py                 # Fixtures, hooks, Allure screenshot on failure
├── pytest.ini                  # Pytest config & markers
├── requirements.txt
└── README.md
```

---

## 🧪 Example Test Flows

### UI — Checkout (E2E)

* Login with standard user
* Add product to cart
* Navigate to cart
* Proceed to checkout
* Fill user information
* Complete order
* Verify success message

### API — Login

* Send POST request to login endpoint
* Verify response status 200

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/bichvt233/fv-automation-framework.git
cd fv-automation-framework

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
playwright install
```

---

## ▶️ Run Tests

```bash
pytest -s -v --env=staging
```

---

## 📊 Test Report

```bash
pytest --alluredir=reports
allure serve reports
```

> Note: `allure-pytest` is required for report generation. Install via `pip install allure-pytest`.

---

## 🔁 CI/CD (GitHub Actions)

The framework includes two GitHub Actions workflows in `.github/workflows/`:

| Workflow | Trigger | Description |
|----------|---------|-------------|
| `pr-tests.yml` | Pull Request to `main` | Runs smoke tests (`-m smoke`) with parallel execution |
| `regression.yml` | Push to `main` + Daily at 2AM UTC | Runs full regression suite with parallel execution |

Both workflows:
* Install dependencies + Playwright browsers
* Run tests with `--env=staging --browser chromium`
* Generate and upload Allure reports as artifacts

---

## ⭐ Highlights

* Scalable automation architecture
* Clean separation of concerns
* CI/CD-ready framework
* Real-world E2E flow implementation

---

## 👤 About Me

I am a QA Engineer with strong experience in:

* Automation strategy
* Framework design
* CI/CD integration

This project reflects my approach to building **quality engineering systems**, not just test cases.

---
