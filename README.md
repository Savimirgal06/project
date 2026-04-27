# project
# Competitor Pricing Dashboard

This project is a **Competitor Price Tracker** designed to help suppliers and businesses monitor market prices for cloud services and hardware. It scrapes competitor data, calculates a competitive "Recommended Price" (5% lower than the market rate), and visualizes the distribution through a modern web dashboard.

---

## 🚀 Features

* **Automated Data Collection:** A Python-based scraper that generates market data with timestamps.
* **Dynamic Pricing Logic:** Automatically calculates a recommended price at a 5% discount relative to competitors.
* **Modern Web Dashboard:** Built with Flask and styled with a dark-themed, responsive CSS layout.
* **Data Visualization:** Integrates `Chart.js` to show average price distributions across different product categories.
* **Real-time CSV Processing:** Reads and processes `market_data.csv` on each page load to ensure the UI is up to date.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Frontend:** HTML5, CSS3 (Inter font), Jinja2 Templates
* **Visualization:** Chart.js
* **Storage:** CSV (Flat-file database)

---

## 📂 Project Structure

```text
├── app.py              # Main Flask application (Server)
├── scraper.py          # Script to simulate/scrape market data
├── market_data.csv     # Generated data file (Auto-created)
└── template/
    └── frontend.html   # Dashboard UI with Chart.js integration
```

---

## ⚙️ Installation & Setup

1.  **Install dependencies:**
    Ensure you have Python installed. You will need Flask:
    ```bash
    pip install flask
    ```


2. **Generate the initial data:**
    Run the scraper to create the `market_data.csv` file:
    ```bash
    python scraper.py
    ```

3. **Run the application:**
    ```bash
    python app.py
    ```

4. **View the Dashboard:**
    Open your browser and navigate to `http://127.0.0.1:8080`.

---


## 📊 How it Works

1.  **Scraping:** `scraper.py` compiles a list of products (Cloud Storage, Managed Databases, etc.) from various sources like AWS, Google Cloud, and Azure.
2.  **Calculation:** Inside `app.py`, the system iterates through the CSV. For every competitor price found, it applies the formula:
    $$Recommended\ Price = Price \times 0.95$$
3.  **Aggregation:** The application calculates the average price per product category to populate the bar chart on the frontend.
4.  **Visualization:** `frontend.html` renders a table for granular data and a bar chart for high-level market overview.

---

## 📝 License
This project is for educational/portfolio purposes. Feel free to modify the scraping logic in `scraper.py` to target real-world APIs or web endpoints.
