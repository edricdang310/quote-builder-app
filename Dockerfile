FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép toàn bộ mã nguồn vào container
COPY . /app/

# Expose cổng 8080
EXPOSE 8080

# Cài đặt biến môi trường PORT mặc định
ENV PORT=8080

# Khởi chạy server Python (sử dụng cờ -u để không bị hoãn ghi log)
CMD ["python", "-u", "server.py"]
