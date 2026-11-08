# Stock Market Trading & Portfolio Simulator 📈💼

A comprehensive financial engine and trading portfolio simulator built in Python using core **Object-Oriented Programming (OOP)** principles. The application models a live stock market floor, allowing traders to execute buy/sell orders, track average cost dynamics, manage assets, and simulate daily market fluctuations via automated randomized algorithms.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Market Price Generator:** Implements realistic end-of-day market scenarios using randomized floating-point changes between `-5.0%` and `+5.0%` across listed symbols (AAPL, TSLA, MSFT, AMZN).
*   **Intelligent Portfolio Ledger:** Automatically recalculates a trader's **Average Buying Price** upon multiple fractional stock purchases, preventing cost basis mismatches.
*   **Live PnL Engine:** Evaluates active stock positions against shifting market prices to render clear profit/loss breakdowns (e.g., `+$50.5` or `-$12.2`) in real-time.
*   **Financial Integrity System:** Features wallet state controllers that validate sufficient starting funds and current item holdings before allowing transactions to clear.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This codebase focuses on extreme modularity, component composition, and relational isolation:
*   **Classes & Blueprints:** Decoupled cleanly into four cohesive modules: `Stock` (ticker & price history host), `Portfolio` (quantity & cost ledger), `User` (trader state controller), and `MarketSimulator` (main orchestrator loop).
*   **Deep Aggregation / Composition:** Illustrates solid architecture design where the `MarketSimulator` class embeds a custom `User` instance, which recursively maps out a structural `Portfolio` node interacting closely with dictionaries of dynamic `Stock` objects.
*   **Advanced Data Tracking:** Utilizes internal state lists (`price_history`) inside individual stock items to seamlessly pave the way for tracking performance curves over multi-day iterations.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd stock-market-simulator-oop
    ```
3.  **Run the interactive market simulation loop:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Standard library utilities (`random` is bundled natively with Python setups).
