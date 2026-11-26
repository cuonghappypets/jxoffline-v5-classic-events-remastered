# Hướng dẫn cài đặt, cấu hình kết nối và cập nhật Hồi Ức Võ Lâm

Bản beta cộng đồng đầu tiên mang mã phiên bản **v1.1.0-beta.1**. Đây là addon (phần bổ sung sự kiện), không phải bộ game hoàn chỉnh. Nếu chưa có game gốc chạy được, xem [cách cài JxV5 bằng bộ cài WSL2 của VDK](README.md#cài-jxv5-bằng-bộ-cài-wsl2-của-vdk) trước.

## 1. Chuẩn bị

- JxOffline V5, V5.1 hoặc V5.2 của ACE và Mel đã chạy được bình thường (theo xác nhận của nhóm phát triển).
- Nên dùng một bản sao để chơi thử. Nếu đã cài thêm mod, cần kiểm tra những file có thể bị chép đè.
- Thoát game, dừng GameServer và sao lưu server, Client, máy ảo và dữ liệu nhân vật trước khi cài. Nếu sao chép cả file đĩa máy ảo, tắt hẳn môi trường Linux trước khi sao chép. Đừng bỏ qua bước này!

## 2. Tải một trong hai gói

**Người mới nên chọn bản chép trực tiếp (Full.zip).** Chỉ cần tải một gói, giải nén vào thư mục riêng trên Windows, không giải nén đè trực tiếp vào game.

- [Bản chép trực tiếp – CGPT_1.1.0-beta.1_Full.zip](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.1/CGPT_1.1.0-beta.1_Full.zip): giải nén là có thư mục `cgpt`, không cần chạy chương trình chuẩn bị.
- [Bản vá – CGPT_1.1.0-beta.1.zip](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.1/CGPT_1.1.0-beta.1.zip): tạo cùng nội dung từ bộ game có sẵn và kiểm tra dữ liệu đầu vào. Phù hợp nếu muốn đối chiếu với bộ gốc trước khi chép.

Không tải mục **Source code (zip)** của GitHub để cài addon. Cả hai gói đều có README riêng.

Nếu dùng bản vá, giải nén vào thư mục riêng trên Windows, chạy `Prepare-cgpt.cmd`. Chọn file nén `JxserV5.tgz` gốc hoặc thư mục server sạch đã xuất ra có chứa `server1`, sau đó chọn thư mục Client (nơi có `settings`). Khi màn hình báo SUCCESS, thư mục `cgpt` xuất hiện cạnh file chuẩn bị. Chương trình không tự chép vào game. Nếu báo lỗi file thiếu hoặc không khớp, dừng lại, kiểm tra bộ gốc; không bỏ qua kiểm tra. Nếu thư mục cgpt đã tồn tại, di chuyển hoặc đổi tên nó trước khi chạy lại.

## 3. Chép addon vào game

Server là phần game chạy trên Linux; Client là thư mục game trên Windows có file `Game.exe`.

Bật môi trường Linux (WSL2 hoặc máy ảo) để chép file, nhưng giữ GameServer ở trạng thái dừng. Có thể dùng tab **Quản lý file** của VDK hoặc WinSCP.

| Trong gói đã giải nén | Chép gộp vào |
|---|---|
| `cgpt/server1/script/` | `server1/script/` của server |
| `cgpt/server1/settings/` | `server1/settings/` của server |
| `cgpt/Client/settings/` | `settings/` của Client Windows |

Tùy bộ cài, server1 có thể nằm tại `/home/jxser/server1` hoặc `/home/jxser_new/server1`. Kiểm tra đúng thư mục đang chạy. Chép **nội dung** vào đúng thư mục, không tạo thêm cấp server1/server1 hoặc Client/Client. Ví dụ, nếu server nằm tại `/home/jxser/server1`, chép nội dung `cgpt/server1/script/` vào `/home/jxser/server1/script/`. Chép gộp, không xóa các file khác hoặc tạo thêm cấp `script/script`, `settings/settings`. Giữ nguyên file và mã chữ TCVN3. Chép riêng phần Client trên Windows, không chép Client lên Linux. Không chỉ chép một phía nếu có thay đổi bảng vật phẩm.

### Chép file từ Windows sang server bằng WinSCP (SFTP)

Nếu không dùng tab **Quản lý file**, anh em có thể dùng [WinSCP](https://winscp.net/) để chép file. Thoát game, sao lưu và dừng GameServer trong chương trình quản lý; giữ Linux (WSL2 hoặc máy ảo) chạy để kết nối.

1. Mở WinSCP, tạo phiên kết nối mới với các thông số:

   | Mục | Giá trị |
   |---|---|
   | File protocol | SFTP |
   | Host name | `127.0.0.1` |
   | Port number | `22` |
   | User name | Tài khoản SSH của bộ cài Linux (ví dụ `root` nếu bộ cài dùng tài khoản này) |
   | Password | `123456` nếu bộ cài vẫn dùng mật khẩu mặc định |

2. Bấm **Login**. Khi kết nối lần đầu, kiểm tra máy chủ và khóa SSH đúng với máy Linux cục bộ trước khi xác nhận.
3. Khung bên trái là file Windows; khung bên phải là file trên server Linux. Mở thư mục addon đã giải nén ở bên trái và đúng thư mục `server1` đang sử dụng ở bên phải (ví dụ `/home/jxser/server1` hoặc `/home/jxser_new/server1`).
4. Chọn hai thư mục `script` và `settings` trong `cgpt/server1/`, chép sang thư mục `server1` trên Linux. Chọn chế độ truyền **Binary** để giữ nguyên mã chữ TCVN3 và nội dung file. Chép gộp các thư mục, chỉ xác nhận ghi đè file cần cập nhật sau khi đã sao lưu; không xóa file khác trên server.
5. Chép riêng nội dung `cgpt/Client/settings/` vào `settings/` của Client trên Windows, như bảng ở trên. Kiểm tra đường dẫn và file đã chép xong, đóng WinSCP rồi khởi động lại GameServer.

Nếu không kết nối được, kiểm tra Linux đã chạy, dịch vụ SSH và cổng 22 của bộ cài có hoạt động hay không; không mở cổng ra Internet chỉ để chép file cục bộ. Mật khẩu trên chỉ dành cho cấu hình mặc định được nêu ở đây; nếu đã đổi, dùng mật khẩu hiện tại. Không dùng mật khẩu mặc định cho máy chủ mở ra mạng, không lưu hoặc chia sẻ mật khẩu cá nhân.

## 4. Vào game

Khởi động GameServer, mở game, vào **Cẩm Nang Đồng Hành → Nhận Lệnh bài Hồi Ức → Hồi Ức Võ Lâm Lệnh**. Chọn Quản lý lễ hội, mùa và sự kiện muốn chơi. Chỉ mở một sự kiện tại một thời điểm; xem [hướng dẫn chung](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/guide.html).

Bản beta có 61 bài hướng dẫn, 60 sự kiện có thể mở. Thép Tinh Luyện đang tạm khóa. Chưa kiểm chứng độc lập việc cài trên bộ sạch và chơi hết các sự kiện của chính bản phát hành này.

## 5. Cập nhật addon

Khi có bản cập nhật mới, không cần cài lại game gốc nếu game đang hoạt động bình thường.

1. Tải đúng gói cập nhật dành cho phiên bản addon và bộ game anh em đang dùng. Đọc hướng dẫn đi kèm gói; không lấy file cập nhật của phiên bản khác ghép vào.
2. Thoát game, dừng GameServer và sao lưu các file sắp thay cùng dữ liệu nhân vật.
3. Giữ Linux hoạt động để chép các file phía server vào đúng thư mục đang dùng, bằng tab Quản lý file hoặc WinSCP như mục 3. Chỉ chép những file mà gói cập nhật yêu cầu; không xóa file khác.
4. Nếu gói cập nhật có phần Client, chép phần đó vào thư mục game trên Windows. Nếu chỉ cập nhật Lua trên server thì không cần chép lại Client.
5. Kiểm tra chép xong, đóng WinSCP nếu đang dùng, khởi động lại GameServer và vào game kiểm tra. Nếu game đã cài thêm mod, cần đối chiếu các file dùng chung trước khi ghi đè.

## 6. Nếu gặp lỗi hoặc muốn gỡ addon

Dừng game/server, dùng bản sao lưu đúng phiên bản để khôi phục. Khôi phục file không tự hoàn lại vật phẩm, kinh nghiệm hoặc tiến độ đã phát sinh; khi cần phải khôi phục cả dữ liệu nhân vật. Nếu mất đồ hoặc phát sinh thưởng bất thường, đừng thực hiện lại liên tục. [Gửi góp ý](REPORT_BUG.md).

## Kiểm tra file tải (không bắt buộc)

Đối chiếu mã SHA256 từ trang [Releases](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.1) với file tải về. Trên Windows có thể mở PowerShell tại thư mục chứa ZIP và chạy `Get-FileHash -Algorithm SHA256 .\CGPT_1.1.0-beta.1_Full.zip` (đổi tên file nếu dùng bản vá).
