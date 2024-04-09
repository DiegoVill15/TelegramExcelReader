# Excel Query Telegram Bot

## Overview
The ExcelQueryTelegramBot is a Python-based Telegram bot designed to provide an interactive interface for querying and retrieving data from Excel sheets. By integrating with the Telegram API, it offers users the ability to perform searches and get information directly in their chat windows, making data access simpler and more intuitive.

## Features
- **Data Querying**: Users can send commands to search for specific data within an Excel sheet, such as IDs, names, or job titles.
- **Flexible Searches**: Supports various query types, allowing for a broad range of data retrieval operations.
- **User-friendly**: Offers an easy-to-use interface for non-technical users to access complex Excel data.

## Technologies Used
- Python
- `pandas` for data manipulation and analysis.
- `python-telegram-bot` for interacting with the Telegram API.

## Getting Started

### Prerequisites
- Python 3.6+
- Pip package manager

### Installation
1. Clone the repository:
```bash
git clone https://github.com/DiegoVill15/TelegramExcelReader.git
```
2. Install the required packages:
```bash
pip install pandas python-telegram-bot
```
3. Set up your Telegram bot token and Excel file path in the script.

### Usage
- Ensure you have an Excel file ready in the repository. An example file `EXCEL_PRUEBA.xlsx` is included for demonstration purposes.
- Update the `RUTA_EXCEL` and `NOMBRE_HOJA` variables in the script to match your Excel file's path and the sheet name you want to query.
- Run the bot with: python TelegramExcelReader.py
- Send commands through your Telegram bot to query data from your specified Excel sheet.
