# 📦 Smart Inventory Optimization Tool (Prototype)

**Smart Inventory** is a data-driven web application designed to help businesses optimize stock levels by predicting future product demand.

Built as a rapid prototype, this tool utilizes **Machine Learning (Linear Regression)** to analyze historical sales trends and forecast upcoming inventory requirements, helping to reduce overstocking and stockouts.

## 🚀 Key Features
* **📂 Drag-and-Drop Interface:** Easily upload historical sales data via CSV.
* **🤖 Automated ML Training:** Instantly trains a Linear Regression model for *each* unique product in the dataset.
* **📅 Next-Month Forecasting:** Predicts exact sales units for the upcoming month based on previous trends.
* **📊 Interactive Dashboard:** Built with Streamlit for a responsive and user-friendly experience.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Processing:** Pandas
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Language:** Python 3.x

## 📂 Project Structure
* `app.py`: The main application script that launches the Streamlit dashboard.
* `model.py`: Contains the logic for training the Linear Regression model and making predictions.
* `utils.py`: Helper functions for handling data ingestion (CSV loading).
* `data.csv`: A sample dataset provided for testing the application.

## ⚙️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/BhupinderrSingh/Smart-Inventory-Tool.git](https://github.com/BhupinderrSingh/Smart-Inventory-Tool.git)
    cd Smart-Inventory-Tool
    ```

2.  **Install Dependencies**
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

4.  **How to Use**
    * The app will open in your browser (usually at `http://localhost:8501`).
    * Upload the `data.csv` file included in this repo.
    * View the real-time predictions for each product.

## 🔮 Future Roadmap
* **Visualization:** Adding line charts to visualize sales trends vs. predictions.
* **Advanced Algorithms:** Implementing ARIMA or LSTM for more complex time-series forecasting.
* **Database Support:** Integrating SQL support to save predictions permanently.

---
**Developed by Bhupinder Singh**
