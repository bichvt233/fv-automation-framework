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
├── config/
├── core/
│
├── ui/
│   ├── pages/
│   └── tests/
│
├── api/
│   ├── services/
│   └── tests/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧪 Example Test Flow (Checkout)

* Login with standard user
* Add product to cart
* Navigate to cart
* Proceed to checkout
* Fill user information
* Complete order
* Verify success message

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

---

## 🔁 CI/CD

The framework is designed to integrate with CI pipelines:

* Run smoke tests on Pull Requests
* Run full regression on merge
* Generate test reports automatically

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
