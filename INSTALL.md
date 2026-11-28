# Hướng dẫn cài đặt, cấu hình kết nối và cập nhật Hồi Ức Võ Lâm

Bản beta cộng đồng hiện tại của **JxCER — JXOffline Classic Events Remastered (Dự án Phục dựng các sự kiện/lễ hội Võ Lâm Truyền Kỳ xưa)** mang mã phiên bản **v1.1.0-beta.5.1**. Đây là addon (phần bổ sung sự kiện), không phải bộ game hoàn chỉnh. Nếu chưa có game gốc chạy được, xem [cách cài JxV5 bằng bộ cài WSL2 của VDK](README.md#cài-jxv5-bằng-bộ-cài-wsl2-của-vdk) trước.

## 1. Chuẩn bị

- JxOffline V5, V5.1 hoặc V5.2 của ACE và Mel đã chạy được bình thường. Đây là phạm vi nền tảng hướng đến; chưa nghiệm thu độc lập việc cài mới Beta 5.1 trên từng bản. Bản 1-click chưa được xác nhận tương thích.
- Nên dùng một bản sao để chơi thử. Nếu đã cài thêm mod, cần kiểm tra những file có thể bị chép đè.
- Thoát game, dừng GameServer và sao lưu server, Client, máy ảo và dữ liệu nhân vật trước khi cài. Nếu sao chép cả file đĩa máy ảo, tắt hẳn môi trường Linux trước khi sao chép. Đừng bỏ qua bước này!

## 2. Tải đúng gói

- [Bản chép trực tiếp — CGPT_1.1.0-beta.5.1_Full.zip](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.5.1/CGPT_1.1.0-beta.5.1_Full.zip): cho người mới, giải nén có thư mục cuonghappypets_cgpt.
- [Đang chơi đúng Beta 5? Tải bản cập nhật](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.5.1/CGPT_1.1.0-beta.5.1_Update_from_beta.5.zip): 16 file (10 Server, 6 Client), kiểm PRE trước khi cài.
- [Beta 5 — bản lưu trữ có chỉnh tỷ lệ drop](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5): cũng là bước trung gian nếu đang dùng Beta 4.

Chỉ cần một gói phù hợp. Không tải mục **Source code (zip)** của GitHub để cài addon. Giải nén vào thư mục riêng, không giải nén đè trực tiếp vào game. Nếu dùng gói Update, đọc README.md trong gói, sao lưu và đối chiếu PRE.sha256 trước khi chép. Nếu không chắc đang dùng đúng Beta 5 hoặc đã có mod riêng, dừng để đối chiếu.

**Trước khi nâng cấp từ Beta 5:** nếu từng chỉnh drop, khôi phục mặc định 2% – 5% và xác nhận trong menu cũ. Beta 5.1 không tự thay đổi cấu hình đã lưu.

## 3. Chép addon vào game

Cả Full.zip và Update Beta 5.1 đều cần đồng bộ Server và Client. Không đổi tên thư mục game; thư mục `cuonghappypets_cgpt` chỉ là thư mục chứa file addon đã giải nén.

Server là phần game chạy trên Linux; Client là thư mục game trên Windows có file `Game.exe`.

Bật môi trường Linux (WSL2 hoặc máy ảo) để chép file, nhưng giữ GameServer ở trạng thái dừng. Có thể dùng tab **Quản lý file** của VDK hoặc WinSCP.

| Trong gói đã giải nén | Chép gộp vào |
|---|---|
| `cuonghappypets_cgpt/server1/script/` | `server1/script/` của server |
| `cuonghappypets_cgpt/server1/settings/` | `server1/settings/` của server |
| `cuonghappypets_cgpt/Client/settings/` | `settings/` của Client Windows |

Tùy bộ cài, server1 có thể nằm tại `/home/jxser/server1` hoặc `/home/jxser_new/server1`. Kiểm tra đúng thư mục đang chạy. Chép **nội dung** vào đúng thư mục, không tạo thêm cấp server1/server1 hoặc Client/Client. Ví dụ, nếu server nằm tại `/home/jxser/server1`, chép nội dung `cuonghappypets_cgpt/server1/script/` vào `/home/jxser/server1/script/`. Chép gộp, không xóa các file khác hoặc tạo thêm cấp `script/script`, `settings/settings`. Giữ nguyên file và mã chữ TCVN3. Chép riêng phần Client trên Windows, không chép Client lên Linux. Không chỉ chép một phía nếu có thay đổi bảng vật phẩm.

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
4. Chọn hai thư mục `script` và `settings` trong `cuonghappypets_cgpt/server1/`, chép sang thư mục `server1` trên Linux. Chọn chế độ truyền **Binary** để giữ nguyên mã chữ TCVN3 và nội dung file. Chép gộp các thư mục, chỉ xác nhận ghi đè file cần cập nhật sau khi đã sao lưu; không xóa file khác trên server.
5. Với Full (hoặc gói có Client), chép riêng nội dung `cuonghappypets_cgpt/Client/settings/` vào `settings/` của Client trên Windows, như bảng ở trên. Kiểm tra đường dẫn và file đã chép xong, đóng WinSCP rồi khởi động lại GameServer.

Nếu không kết nối được, kiểm tra Linux đã chạy, dịch vụ SSH và cổng 22 của bộ cài có hoạt động hay không; không mở cổng ra Internet chỉ để chép file cục bộ. Mật khẩu trên chỉ dành cho cấu hình mặc định được nêu ở đây; nếu đã đổi, dùng mật khẩu hiện tại. Không dùng mật khẩu mặc định cho máy chủ mở ra mạng, không lưu hoặc chia sẻ mật khẩu cá nhân.

## 4. Vào game

Khởi động GameServer, mở game, vào **Cẩm Nang Đồng Hành → Nhận Lệnh bài Hồi Ức → Hồi Ức Võ Lâm Lệnh**. Chọn Quản lý sự kiện, mùa và sự kiện muốn chơi. Chỉ mở một sự kiện tại một thời điểm; xem [hướng dẫn chung](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/guide.html).

Bản Beta 5.1 có 63 ID kỹ thuật, 62 bài trong danh mục, 61 sự kiện có thể mở. Trung thu PGaming (#02) được lưu trữ; người chơi có thể xem bài lưu trữ nhưng không mở sự kiện này trong Beta 5.1. Gặp Thượng Sứ Lễ Hội ở Tương Dương, ngay giữa cổng Nha Môn dưới bậc thang. Khi có sự kiện đang mở, vào Quản lý sự kiện hiện tại để tạm dừng hoặc đóng; muốn đóng hẳn sự kiện đã tạm dừng, chọn sự kiện trong nhóm mùa. Thép Tinh Luyện đang tạm khóa. Beta 5 đã có lượt chơi thử đại diện; các thay đổi Beta 5.1 mới kiểm thử giả lập, chưa nghiệm thu trong game. Chưa kiểm chứng độc lập việc cài mới bản cộng đồng trên từng nền tảng và chơi hết các tuyến sự kiện.

## 5. Cập nhật addon

Kế thừa Beta 5 — Item Quality of Life Update: sửa 12 vật phẩm thiếu hình ảnh, chuẩn hóa xếp chồng 25 ID và biên tập 115 mô tả. STT trong Lệnh bài trùng với cẩm nang online; ID kỹ thuật không đổi. Đào Vạn Thọ (STT 09, ID #15) và các sự kiện đặc thù giữ cơ chế riêng.

Chọn đúng gói Update theo phiên bản đang chơi. Dừng GameServer, sao lưu, kiểm tra PRE.sha256 và NEW_PATHS.txt; nếu lệch thì dừng. Chép gộp server1 và Client, không chép rollback. Đối chiếu BASELINE.sha256 khi cần, kiểm PRE của cả hai phía. Kiểm tra POST.sha256 rồi khởi động. Beta 4 bổ sung các bãi luyện công cấp cao, trong đó có Tu Luyện Cốc 90–180, và chỉnh tỷ lệ mặc định xuống 2% ở nhóm thấp và 5% ở nhóm cao (90/110/119 theo file drop), mỗi lượt trúng rơi một món. Điều kiện riêng và các nguồn rơi đặc thù vẫn giữ nguyên.

Nhằm bảo toàn trải nghiệm các sự kiện cổ điển của Võ Lâm Truyền Kỳ, từ Beta 5.1 JxCER ngừng cung cấp và hỗ trợ tính năng tùy chỉnh tỷ lệ rơi vật phẩm sự kiện trong menu công cộng. Anh em có nhu cầu sử dụng tính năng này vẫn có thể tải [Beta 5](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5); tính năng sẽ không còn được duy trì, sửa lỗi hoặc cập nhật trong các phiên bản tiếp theo.

Nếu đang dùng Beta 5 và từng chỉnh tỷ lệ drop, trước khi cập nhật hãy chọn Khôi phục tỷ lệ mặc định (2% – 5%) và mở lại menu xác nhận. Bản 5.1 chỉ ẩn các nút điều chỉnh, không tự ghi đè cấu hình Relay đã lưu. Nếu đã dùng bản thử Auto trước đó, hãy tắt Auto và xác nhận trước khi nâng cấp. Không chỉnh DB thủ công.

Fix Bug Auto là chế độ tương thích thử nghiệm, mặc định OFF trên cài đặt mới; chỉ bật nếu thực sự gặp vấn đề nhặt đồ. Hiện chỉ hỗ trợ Tết 2009 (STT 42, ID #21). Khi bật, hộp quà 1 ô thay cho vật phẩm rơi trực tiếp và khi nhặt chuyển thành đúng vật phẩm đã chọn, không thay tỷ lệ hay tự mở rương thưởng. Chưa xác nhận tương thích MelAuto hoặc các Auto khác trong game thực tế. Khi OFF, giữ cơ chế rơi trực tiếp của Beta 5.

Hồi Ức Võ Lâm Lệnh → Quản lý sự kiện → Quản lý vật phẩm sự kiện: xem danh sách bản đồ, kiểm tra bản đồ hiện tại, Fix Bug Auto và quay lại. Với Relay chưa khởi tạo, mục Auto có bước xác nhận khởi tạo riêng, không đổi tỷ lệ; chọn lại Auto sau khi khởi tạo thành công.

Beta 5 đã chơi thử đại diện: Hồng Bảo Rương hiển thị và gom được chồng 72 chiếc. Bản tích hợp qua 618/618 ca hồi quy drop/menu, 100/100 ca chọn vật phẩm Tết 2009, 5/5 ca callback rương, 25/25 ca callback nhóm stacking và 200 lượt kiểm tra xác suất Đào Vạn Thọ trong Lua giả lập. Đã đối chiếu 458 ID ứng viên đang hoạt động qua 6 profile và 2 biến thể (5.496 lượt); không còn đường dẫn sprite thiếu trong tập kiểm tra. Chưa xác nhận mọi sprite render, tự gom khi nhặt, tiêu hao một đơn vị, lưu qua restart hoặc cài mới trên mọi nền tảng. Sau reload/restart, kiểm tra lại sự kiện và tỷ lệ; đã ghi nhận trường hợp về Mâm ngũ quả.

1. Tải đúng gói cập nhật dành cho phiên bản addon và bộ game anh em đang dùng. Đọc hướng dẫn đi kèm gói; không lấy file cập nhật của phiên bản khác ghép vào.
2. Thoát game, dừng GameServer và sao lưu các file sắp thay cùng dữ liệu nhân vật.
3. Giữ Linux hoạt động để chép các file phía server vào đúng thư mục đang dùng, bằng tab Quản lý file hoặc WinSCP như mục 3. Chỉ chép những file mà gói cập nhật yêu cầu; không xóa file khác.
4. Nếu gói cập nhật có phần Client, chép phần đó vào thư mục game trên Windows. Nếu chỉ cập nhật Lua trên server thì không cần chép lại Client.
5. Kiểm tra chép xong, đóng WinSCP nếu đang dùng, khởi động lại GameServer và vào game kiểm tra. Nếu game đã cài thêm mod, cần đối chiếu các file dùng chung trước khi ghi đè.

## 6. Nếu gặp lỗi hoặc muốn gỡ addon

Trước khi quay về Beta 5: tắt Fix Bug Auto, xác nhận OFF, thu nhặt/mở hết hộp thử nghiệm 30642 hợp lệ qua game. Nếu còn hộp bị khóa, dừng và giữ bản sao để kiểm tra. Dừng server, kiểm POST.sha256; chép rollback đúng đường dẫn và chỉ bỏ hai file mới trong NEW_PATHS.txt nếu đúng checksum và không tồn tại trước khi cài. Kiểm PRE.sha256. Khôi phục file không hoàn tác dữ liệu nhân vật; không hạ cấp bảng stack nếu còn chồng vật phẩm không tương thích. Không sửa DB thủ công. [Gửi góp ý](REPORT_BUG.md).

## Kiểm tra file tải (không bắt buộc)

Đối chiếu mã SHA256 từ trang [Releases](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5.1) với file tải về. Trên Windows có thể mở PowerShell tại thư mục chứa ZIP và chạy `Get-FileHash -Algorithm SHA256 .\CGPT_1.1.0-beta.5.1_Full.zip` (đổi tên file nếu dùng gói Update).
