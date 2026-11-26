# Cài đặt Hồi Ức Võ Lâm

Bản beta cộng đồng đầu tiên mang mã phiên bản **v1.1.0-beta.1**. Đây là addon, không phải bộ game hoàn chỉnh.

## 1. Chuẩn bị

- JxOffline V5, V5.1 hoặc V5.2 của ACE và Mel đã chạy được bình thường (theo xác nhận của nhóm phát triển).
- Nên dùng một bản sao để chơi thử. Nếu đã cài thêm mod, cần kiểm tra những file có thể bị chép đè.
- Thoát game và sao lưu server, Client, máy ảo và dữ liệu nhân vật trước khi cài. Đừng bỏ qua bước này!

## 2. Tải một trong hai gói

- [Bản chép trực tiếp – CGPT_1.1.0-beta.1_Full.zip](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.1/CGPT_1.1.0-beta.1_Full.zip): giải nén là có thư mục `cgpt`, không cần chạy chương trình chuẩn bị.
- [Bản vá – CGPT_1.1.0-beta.1.zip](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.1/CGPT_1.1.0-beta.1.zip): tạo cùng nội dung từ bộ game có sẵn và kiểm tra dữ liệu đầu vào. Phù hợp nếu muốn đối chiếu với bộ gốc trước khi chép.

Không tải mục Source code ZIP của GitHub để cài addon. Cả hai gói đều có README riêng.

Nếu dùng bản vá, giải nén vào thư mục riêng trên Windows, chạy `Prepare-cgpt.cmd`. Chọn archive `JxserV5.tgz` gốc hoặc thư mục server sạch đã xuất ra có chứa `server1`, sau đó chọn thư mục Client (nơi có `settings`). Khi màn hình báo SUCCESS, thư mục `cgpt` xuất hiện cạnh file chuẩn bị. Chương trình không tự chép vào game. Nếu báo lỗi file thiếu hoặc không khớp, dừng lại, kiểm tra bộ gốc; không bỏ qua kiểm tra. Nếu thư mục cgpt đã tồn tại, di chuyển hoặc đổi tên nó trước khi chạy lại.

## 3. Chép addon vào game

Dừng GameServer trong launcher. Nếu dùng tab Quản lý file, giữ máy ảo hoạt động.

| Trong gói đã giải nén | Chép gộp vào |
|---|---|
| `cgpt/server1/script/` | `server1/script/` của server |
| `cgpt/server1/settings/` | `server1/settings/` của server |
| `cgpt/Client/settings/` | `settings/` của Client Windows |

Tùy bộ cài, server1 có thể nằm tại `/home/jxser/server1` hoặc `/home/jxser_new/server1`. Kiểm tra đúng thư mục đang chạy. Chép **nội dung** vào đúng thư mục, không tạo thêm cấp server1/server1 hoặc Client/Client. Giữ nguyên file và mã chữ TCVN3. Không chỉ chép một phía nếu có thay đổi bảng vật phẩm.

## 4. Vào game

Khởi động GameServer, mở game, vào **Cẩm Nang Đồng Hành → Nhận Lệnh bài Hồi Ức → Hồi Ức Võ Lâm Lệnh**. Chọn Quản lý lễ hội, mùa và sự kiện muốn chơi. Chỉ mở một sự kiện tại một thời điểm; xem [hướng dẫn chung](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/guide.html).

Bản beta có 61 bài hướng dẫn, 60 sự kiện có thể mở. Thép Tinh Luyện đang tạm khóa. Chưa kiểm chứng độc lập việc cài trên bộ sạch và chơi hết các sự kiện của chính bản phát hành này.

## 5. Nếu gặp lỗi hoặc muốn gỡ addon

Dừng game/server, dùng bản sao lưu đúng phiên bản để khôi phục. Khôi phục file không tự hoàn lại vật phẩm, kinh nghiệm hoặc tiến độ đã phát sinh; khi cần phải khôi phục cả dữ liệu nhân vật. Nếu mất đồ hoặc phát sinh thưởng bất thường, đừng thực hiện lại liên tục. [Gửi góp ý](REPORT_BUG.md).

## Kiểm tra file tải (không bắt buộc)

Đối chiếu mã SHA256 từ trang [Releases](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.1) với file tải về. Trên Windows có thể mở PowerShell tại thư mục chứa ZIP và chạy `Get-FileHash -Algorithm SHA256 .\CGPT_1.1.0-beta.1_Full.zip` (đổi tên file nếu dùng bản vá).
