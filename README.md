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

Especially for critical flows like **login** and **checkout**, where failures directly impact user experience and revenue.

---

## 💡 Solution

I designed and implemented a **modular automation framework** that:

* Automates end-to-end checkout flow
* Tests login with multiple user types (valid, locked, problem, performance, error, visual)
* Tests API login endpoint
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
│       ├── pr-tests.yml            # Smoke tests on Pull Requests
│       └── regression.yml          # Full regression on push to main + daily schedule
│
├── config/
│   └── staging.env                 # Environment variables (BASE_URL, etc.)
│
├── core/
│   ├── base_page.py                # Base Page Object with common actions
│   └── config.py                   # Environment config loader
│
├── ui/
│   ├── pages/                      ← Page Objects (HOW to interact)
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── tests/                      ← Test scenarios (WHAT to verify)
│       ├── test_login.py           # 6 login test cases (valid, locked, problem, perf, error, visual)
│       ├── test_checkout.py        # E2E checkout flow
│       └── data/
│           └── test_data.py        # Test data for UI tests
│
├── api/
│   ├── services/
│   └── tests/
│       ├── test_login_api.py       # API login test (reqres.in)
│       └── data/
│           └── api_data.py         # Test data for API tests
│
├── conftest.py                     # Fixtures, hooks, Allure screenshot on failure
├── pytest.ini                      # Pytest config & markers (smoke, ui, api, regression)
├── requirements.txt
└── README.md
```

---

## 🧪 Test Flows

### UI — Login (6 Test Cases)

| # | Test Case | User | Expected |
|---|-----------|------|----------|
| TC1 | Valid login | `standard_user` | Redirect to Products page |
| TC2 | Locked out user | `locked_out_user` | Error message displayed |
| TC3 | Problem user | `problem_user` | Login OK, product images may be broken |
| TC4 | Performance glitch user | `performance_glitch_user` | Login OK but slow (>1s) |
| TC5 | Error user | `error_user` | Login OK, some features may error |
| TC6 | Visual user | `visual_user` | Login OK, UI may be misaligned |

### UI — Checkout (E2E)

* Login with standard user
* Verify 6 products displayed
* Add first product to cart
* Navigate to cart
* Proceed to checkout
* Fill user information
* Complete order
* Verify success message

### API — Login (reqres.in)

* Send POST request to `/api/login` with API key header
* Verify response status 200
* Verify token is returned and not empty

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
# Run all tests
pytest --env=staging

# Run only UI tests
pytest -m ui --env=staging

# Run only smoke tests
pytest -m smoke --env=staging

# Run only API tests
pytest -m api --env=staging

# Run a specific test file
pytest ui/tests/test_login.py -v
pytest ui/tests/test_checkout.py -v
pytest api/tests/test_login_api.py -v
```

---

## 📊 Test Report

```bash
pytest --alluredir=reports --env=staging
allure serve reports
```

> Note: `allure-pytest` is included in `requirements.txt`. Screenshots are automatically attached on test failure.

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
* Deploy Allure report to GitHub Pages

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.12 | Programming language |
| Playwright | 1.55.0 | Browser automation |
| Pytest | 8.4.1 | Test framework |
| Allure | 2.16.0 | Test reporting |
| Requests | 2.32.3 | API testing |
| GitHub Actions | — | CI/CD |

---

## ⭐ Highlights

* Scalable automation architecture with Page Object Model
* Clean separation of concerns (UI / API / Core)
* Multi-user login test coverage (6 user types)
* E2E checkout flow with full verification
* API test integration
* CI/CD-ready with Allure reporting & GitHub Pages
* Automatic screenshot capture on test failure

---

## 👤 About Me

I am a QA Engineer with strong experience in:

* Automation strategy
* Framework design
* CI/CD integration

This project reflects my approach to building **quality engineering systems**, not just test cases.

---
