# Bảng Tra Cứu và Quy Tắc Tính Giá Dịch Vụ EVG

Tài liệu này tổng hợp các thuộc tính và quy tắc tính giá của các dịch vụ từ dữ liệu nội bộ để phục vụ cho các lần lập báo giá tiếp theo.

---

## 1. Cloud-VPS & VPS Dedicated
Tỷ giá áp dụng: **26,500 VND/USD**
Thuế VAT: **10%** (chưa bao gồm trong giá gốc)

### 1.1. Công thức tính giá cấu hình Cloud-VPS (chưa VAT)
$$\text{Giá gốc (USD)} = (\text{vCPU} \times 3) + (\text{RAM (GB)} \times 3.5) + (\text{SSD (GB)} \times 0.1) + (\text{HDD (GB)} \times 0.06) + (\text{IP Add-on} \times 3)$$
$$\text{Giá gốc (VND)} = \text{Giá gốc (USD)} \times 26,500$$

### 1.2. Chính sách giảm giá (Discount) theo thời hạn hợp đồng
1. **Giảm giá mặc định hàng tháng (Monthly Discount):** 
   - Hầu hết các gói hoặc cấu hình tùy chọn: **20%**
   - Riêng gói `e.medium` (4 Core - 8 GB RAM - 50 GB SSD): **30%**
2. **Khấu trừ thanh toán trước (giảm tiếp trên giá sau khi chiết khấu tháng):**
   - Thanh toán **3 tháng**: Giảm thêm **15%** (Nhân hệ số `0.85`)
   - Thanh toán **6 tháng**: Giảm thêm **20%** (Nhân hệ số `0.80`)
   - Thanh toán **12 tháng**: Giảm thêm **25%** (Nhân hệ số `0.75`)

### 1.3. Bảng giá các cấu hình VPS mẫu (Chưa VAT)
| Tên gói | vCPU | RAM (GB) | SSD (GB) | Giá gốc (VND/tháng) | Chiết khấu tối đa | Giá sau CK (VND/tháng) | 3 tháng (VND/tháng) | 6 tháng (VND/tháng) | 12 tháng (VND/tháng) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **e.tiny** | 1.0 | 2.0 | 50.0 | 397,500 | 20% | 318,000 | 270,300 | 254,400 | 238,500 |
| **e.small** | 2.0 | 4.0 | 50.0 | 662,500 | 20% | 530,000 | 450,500 | 424,000 | 397,500 |
| **e.medium** | 4.0 | 8.0 | 50.0 | 1,192,500 | 30% | 834,750 | 709,537.5 | 667,800 | 626,062.5 |
| **e.medium+** | 8.0 | 8.0 | 50.0 | 1,510,500 | 20% | 1,208,400 | 1,027,140 | 966,720 | 906,300 |
| **e.large** | 8.0 | 16.0 | 100.0 | 2,385,000 | 20% | 1,908,000 | 1,621,800 | 1,526,400 | 1,431,000 |
| **e.huge** | 16.0 | 32.0 | 100.0 | 4,505,000 | 20% | 3,604,000 | 3,063,400 | 2,883,200 | 2,703,000 |

### 1.4. VPS Dedicated (Thuê máy chủ riêng)
| Gói | Cấu hình | Giá USD/tháng | Giá VND/tháng |
| :--- | :--- | :---: | :---: |
| **D32** | 32GB RAM ECC, 2x E5-2680v3, 2x240G + 2x480G SSD, 500Mbps unmeter, 2 IPv4 | 250 | 6,625,000 |
| **D64** | 64GB RAM ECC, 2x E5-2680v3, 2x240G + 2x960G SSD, 500Mbps unmeter, 2 IPv4 | 350 | 9,275,000 |
| **D128** | 128GB RAM ECC, 2x E5-2680v3, 2x240G + 4x960G SSD, 500Mbps unmeter, 2 IPv4 | 400 | 10,600,000 |

---

## 2. Dịch vụ vStorage (Lưu trữ)
| Dung lượng gói | Đơn giá/GB/tháng (VND) | Ghi chú |
| :--- | :---: | :--- |
| **<= 1 TB** (1,000 GB) | 950 | Hỗ trợ mã hóa AES 256 |
| **<= 5 TB** (5,000 GB) | 900 | Hỗ trợ mã hóa AES 256 |
| **<= 10 TB** (10,000 GB) | 850 | Hỗ trợ mã hóa AES 256 |
| **<= 50 TB** (50,000 GB) | 800 / 750 | Hỗ trợ mã hóa AES 256 |
| **>= 100 TB** (100,000 GB) | 700 | Hỗ trợ mã hóa AES 256 |

---

## 3. Dịch vụ CDN
### 3.1. CDN theo dung lượng (Traffic/GB)
*Gói lớn giảm dần đơn giá từ 750 VND/GB xuống còn 100 VND/GB tùy thuộc sản lượng cam kết hàng tháng.*
- **Dưới 10 TB:** 750 VND/GB (Giá gói: < 7,500,000 VND)
- **10 TB - 50 TB:** 400 VND/GB
- **50 TB - 150 TB:** 250 VND/GB
- **150 TB - 500 TB:** 168 VND/GB
- **500 TB - 1,024 TB:** 125 VND/GB
- **Trên 1,024 TB:** 105 VND/GB (hoặc 100 VND/GB cho > 4,096 TB)

### 3.2. CDN theo gói năm (12 tháng sử dụng)
- **CDN-T (5 TB):** 2,525,000 VND/gói
- **CDN-S (20 TB):** 8,200,000 VND/gói
- **CDN-M (50 TB):** 15,750,000 VND/gói (Free 50GB storage/tháng)
- **CDN-MPLUS (100 TB):** 22,000,000 VND/gói (Free 100GB storage/tháng)
- **CDN-L (200 TB):** 25,000,000 VND/gói (Free 200GB storage/tháng)
- **CDN-H (500 TB):** 54,000,000 VND/gói (Free 500GB storage/tháng)
- **CDN-V (1,000 TB):** 86,000,000 VND/gói (Free 1000GB storage/tháng)

---

## 4. Dịch vụ Transcode
### 4.1. Transcode offline (VND/phút) - Cam kết tối thiểu 5,000 phút
- **360p:** 129.25 VND
- **480p:** 141.00 VND
- **720p:** 188.00 VND
- **1080p:** 235.00 VND

### 4.2. Live Transcode (VND/phút) - Cam kết tối thiểu 5,000 phút
- **360p:** 70.74 VND
- **480p:** 70.74 VND
- **720p:** 141.48 VND
- **1080p:** 275.10 VND

---

## 5. Dedicated Storage & Colocation
Tỷ giá áp dụng: **23,500 VND/USD**

### 5.1. Thuê tủ đĩa riêng (Dedicated Storage) - Chưa VAT
- **S20T** (Chasis 2x2.5 + 12x3.5, 2x240GB SSD + 2x10TB HDD, 16GB RAM): **350 USD** (~8,225,000 VND/tháng)
- **S40T** (Chasis 2x2.5 + 12x3.5, 2x240GB SSD + 4x10TB HDD, 32GB RAM): **500 USD** (~11,750,000 VND/tháng)
- **S80T** (Chasis 2x2.5 + 12x3.5, 2x240GB SSD + 8x10TB HDD, 64GB RAM): **770 USD** (~18,095,000 VND/tháng)
- **S120T** (Chasis 2x2.5 + 12x3.5, 2x240GB SSD + 12x10TB HDD, 128GB RAM): **1,095 USD** (~25,732,500 VND/tháng)

### 5.2. Chỗ đặt máy chủ (Colocation) - Chưa VAT
- **COLO-01 Standard** (1U Rack, 400W Power, 300Mbps Uplink, 2 IPv4): **106 USD** (~2,491,000 VND/tháng)
- **COLO-02 Standard** (2U Rack, 400W Power, 300Mbps Uplink, 2 IPv4): **110 USD** (~2,585,000 VND/tháng)
- **COLO-03 VIP** (1U Rack, 400W Power, 500Mbps Uplink, 2 IPv4): **116 USD** (~2,726,000 VND/tháng)
- **COLO-04 VIP** (2U Rack, 400W Power, 500Mbps Uplink, 2 IPv4): **120 USD** (~2,820,000 VND/tháng)
