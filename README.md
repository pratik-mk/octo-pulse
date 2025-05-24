# 🐙  Octo Pulse – Algorithmic Trading Framework

**Octo Pulse** is a broker-agnostic algorithmic trading platform tailored for Indian financial markets. It uses a scalable architecture with the **Factory Design Pattern** to dynamically choose and integrate with different brokers such as Zerodha (Kite), Fyers, Angel One, and more.

---

## 🧠 Core Philosophy

- 🔁 **Broker Agnostic** – Plug and play any broker via standardized interfaces.
- 🏛️ **Design Pattern Driven** – Uses the Factory Pattern to dynamically create broker connectors.
- 🇮🇳 **Indian Market First** – Designed around NSE, BSE, MCX workflows, instruments, and compliance needs.
- ⚙️ **Modular Strategy Engine** – Build and deploy rule-based or AI-powered strategies.
- 📈 **Live & Backtest Ready** – Seamlessly switch between paper trading, backtesting, and live trading.

---

## 🧰 Architecture
+-------------------+
| Strategy Manager |
+-------------------+
│
▼
+-------------------+
| BrokerFactory | <----- Factory Pattern
+-------------------+
│
▼
+-------------------+
| Broker Interface |
| (Zerodha, Fyers) |
+-------------------+
│
▼
[Live Market]
