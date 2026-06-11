# Hướng Dẫn Sử Dụng Công Cụ Tạo Báo Giá VPS EVG

Tài liệu này hướng dẫn cách cài đặt, khởi chạy và vận hành **Công cụ tạo báo giá VPS EVG** dành cho Công ty Cổ phần Everest Toàn Cầu.

---

## 1. Yêu cầu Hệ thống
* Máy tính đã cài đặt **Python 3.x** (để chạy server lưu trữ và quản lý lịch sử chia sẻ).
* Trình duyệt web hiện đại (Google Chrome, Microsoft Edge, Cốc Cốc, Brave,...).

---

## 2. Cách Khởi Chạy Ứng Dụng

Để sử dụng toàn bộ tính năng (đặc biệt là **Chia sẻ** và **Lịch sử**), bạn cần khởi chạy tệp tin máy chủ trung gian `server.py` theo các bước sau:

### Bước 1: Mở Terminal/CMD trong thư mục dự án
* Di chuyển vào thư mục: `d:\Work\EVG\Kinh doanh`.
* Click chuột vào thanh địa chỉ của thư mục trong Windows Explorer, gõ `cmd` rồi nhấn **Enter**; hoặc mở PowerShell và gõ lệnh:
  ```powershell
  cd "d:\Work\EVG\Kinh doanh"
  ```

### Bước 2: Chạy Python Server
* Gõ lệnh dưới đây và nhấn **Enter**:
  ```bash
  python server.py
  ```
* Màn hình Terminal sẽ hiển thị thông báo khởi chạy thành công:
  ```text
  === EVG QUOTE GENERATOR SERVER RUNNING ===
  Server is running on: http://localhost:8080
  Open in browser: http://localhost:8080/price/builder.html
  ```

### Bước 3: Truy cập vào ứng dụng
* Sao chép đường dẫn hiển thị trên màn hình Terminal hoặc click trực tiếp vào liên kết sau để mở ứng dụng trên trình duyệt:
  [http://localhost:8080/price/builder.html](http://localhost:8080/price/builder.html)

---

## 3. Hướng Dẫn Các Chức Năng Chính

### A. Thiết lập & Tạo Báo Giá (Bên trái giao diện)
* **Thông tin chung**: Nhập số báo giá (hoặc nhấn nút `🔄 Tự động` để tạo số báo giá ngẫu nhiên theo thời gian thực), ngày báo giá, thông tin khách hàng.
* **Tùy chọn Thuế VAT**: Lựa chọn hiển thị gồm VAT 10% hoặc không tính thuế VAT.
* **Cột Chiết khấu**:
  * **Có hiển thị**: Cột Chiết khấu (CK %) sẽ xuất hiện trên bảng. Đơn giá hiển thị là Đơn giá gốc.
  * **Ẩn cột CK**: Cột Chiết khấu sẽ được ẩn đi. 
    * *Quy tắc hiển thị*: Đơn giá hiển thị chuyển sang **Đơn giá sau chiết khấu** (đã giảm trừ phần trăm chiết khấu), đồng thời cột **Thành tiền** hiển thị **giá sau chiết khấu** để bảo đảm sự thống nhất và tinh tế của báo giá.
* **Thông số giá gốc**: Cho phép thay đổi tỷ giá USD/VND và đơn giá gốc của từng thông số (vCPU, RAM, SSD, HDD, IP Add-on) để tự động tính toán báo giá.
* **Danh sách VPS**:
  * Nhấn **"Thêm VPS mới"** để thêm hàng mục.
  * Tùy chỉnh thông số cấu hình phần cứng trực tiếp, bảng báo giá bên phải sẽ cập nhật tức thời theo thời gian thực.
  * Thiết lập dung lượng HDD bằng `0` nếu cấu hình gói không sử dụng ổ cứng HDD.

### B. In / Xuất File PDF
* Nhấn nút **"In / Xuất PDF"** dưới góc trái màn hình.
* Cửa sổ in mặc định của trình duyệt hiện ra.
* **Lưu ý cài đặt in**:
  * Tại phần **Destination (Máy in đích)**: Chọn **Save as PDF (Lưu dưới dạng PDF)**.
  * Tại phần **Pages (Trang)**: Chọn **All**. Giao diện đã được thiết kế tối ưu hóa A4 vừa khít **chỉ trong 1 trang**.
  * Tại phần **More Settings (Cài đặt thêm)**: **BỎ TÍCH** mục **Headers and footers (Tiêu đề đầu trang và chân trang)** để tránh dính thông tin ngày tháng, đường dẫn URL hoặc tiêu đề trang web vào bản in.
  * Nhấn **Save (Lưu)**.

### C. Chia Sẻ Báo Giá Trực Tuyến
* Nhấn nút **"Chia sẻ"** (nút màu tím) trên thanh tác vụ.
* Hệ thống sẽ tự động đóng gói toàn bộ trang báo giá dạng HTML tĩnh trên server và trả về liên kết xem trực tuyến.
* Hộp thoại chia sẻ cao cấp sẽ hiển thị:
  * Nhấn **"Sao chép liên kết"**: Sao chép nhanh đường dẫn online vào bộ nhớ đệm (Clipboard) để gửi cho khách hàng.
  * Nhấn **"Mở link"**: Mở tab trình duyệt mới để xem trực tuyến giao diện báo giá đã được đóng gói tĩnh.
  * Khách hàng khi nhận được link này cũng có thể tự nhấn nút **"Xuất file PDF"** màu vàng nổi ở góc dưới trang web để tự tải xuống bản PDF tiêu chuẩn A4.

### D. Quản Lý Lịch Sử Chia Sẻ
* Nhấn nút **"Lịch sử"** (nút màu xám đen) trên thanh tác vụ để chuyển hướng đến trang quản lý: `http://localhost:8080/price/history.html`.
* Giao diện trang Lịch sử cho phép:
  * **Xem thống kê**: Tổng số lượng file báo giá đã tạo trực tuyến và tổng dung lượng lưu trữ đang chiếm dụng trên server.
  * **Tìm kiếm**: Nhập số báo giá hoặc tên file tại ô Tìm kiếm để tìm nhanh.
  * **Xem / Xóa**:
    * Nhấn nút **"Xem"** để mở lại trang báo giá.
    * Nhấn nút **"Xóa"** để xóa vĩnh viễn tệp HTML đó trên ổ đĩa khỏi thư mục lưu trữ `Service_quote/`.
    * *Bảo vệ hệ thống*: Các file báo giá mẫu tĩnh gốc của hệ thống (ví dụ: `Báo giá dịch vụ - Danh sách VPS (SSD-HDD).html`) sẽ bị khóa chức năng Xóa (nút Xóa chuyển thành nút xám **"Mẫu"**) để tránh việc vô tình xóa mất dữ liệu gốc của bạn.
