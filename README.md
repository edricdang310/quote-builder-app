# EVG VPS Quote Builder

A lightweight web application for creating, managing, sharing, and printing professional VPS hosting quotes for Everest Global Joint Stock Company (EVG).

---

## 1. Quick Start

### Option A: Run locally with Python
1. Ensure **Python 3.x** is installed.
2. Open terminal in this directory and start the server:
   ```bash
   python server.py
   ```
3. Open your browser and navigate to:
   [http://localhost:8080/price/builder.html](http://localhost:8080/price/builder.html)

### Option B: Run with Docker Compose
1. Ensure **Docker** and **Docker Compose** are installed and running.
2. Start the containerized application on port `8080` in detached mode:
   ```bash
   docker compose up --build -d
   ```
3. Access the application in your browser:
   [http://localhost:8080/price/builder.html](http://localhost:8080/price/builder.html)

---

## 2. Key Features

- **General Settings**: Edit quote numbers (randomize with one click), dates, client names, and client addresses (default is blank).
- **VAT & Discount Options**:
  - Toggle 10% VAT inclusion.
  - Toggle discount column visibility. Hiding the discount column automatically updates the individual item prices to show the post-discount price for a cleaner lookup.
- **Dynamic Pricing Base**: Modify exchange rates (USD/VND) and hardware units (vCPU, RAM, SSD, HDD, IP) dynamically.
- **PDF Export**: Single-page A4 print layout optimized out-of-the-box. Ensure "Headers and footers" is disabled in browser print settings.
- **Sharing**: Generates and saves dynamic JSON configurations on the server, producing lightweight URL links to share with clients.
- **History Management**: Re-open, edit, or delete existing quotes easily from the database list at `/price/history.html`.

---

## 3. Vietnamese User Guide (Hướng dẫn sử dụng)

For detailed operational guides in Vietnamese, please refer to [Huong_dan_su_dung.md](file:///d:/Work/EVG/Kinh%20doanh/Huong_dan_su_dung.md).
