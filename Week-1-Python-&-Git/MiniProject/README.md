# Fellowship Study & Expense Tracker

A simple utility built with Streamlit to log fellowship hours and related expenses. This project demonstrates core Python concepts including OOP, modular programming, file handling, and error handling.

## 🚀 Features

- **Study Logging**: Track time spent on various fellowship tasks.
- **Expense Tracking**: Log costs related to the fellowship.
- **Data Persistence**: Automatically saves and loads data from `data/logs.csv`.
- **Modular Design**: Logic and file handling are separated into a custom package `logger_pkg`.
- **Clean UI**: Simple dashboard for viewing logs and quick statistics.

## 📂 Project Structure

```text
MiniProject/
├── app.py                # Main Streamlit interface
├── logger_pkg/           # Custom Python package
│   ├── core.py           # OOP implementation (LogEntry, StudyLog, ExpenseLog)
│   ├── file_handler.py   # Data persistence logic
│   └── __init__.py       # Package initializer
├── data/                 # Directory for data storage
│   └── logs.csv          # CSV database
└── README.md             # Project documentation
```

## 🛠️ Requirements

- Python 3.x
- Streamlit
- Pandas

## 🏃 How to Run

1.  Navigate to the project directory:
    ```powershell
    cd "Week-1-Python-&-Git/MiniProject"
    ```
2. Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```
3. Launch the application:
    ```powershell
    streamlit run app.py
    ```

## 📝 Concepts Applied

- **Object-Oriented Programming (OOP)**: Use of base classes and inheritance for different log types.
- **Modules & Packages**: Logical separation of code into a reusable package.
- **File & Error Handling**: Robust CSV read/write operations with `try-except` blocks.
- **Streamlit Integration**: Building good enough web-based UI for data interaction.
