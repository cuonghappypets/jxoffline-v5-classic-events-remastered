# JxOffline V5 Classic Events Remastered

**JxOffline V5 (by ACE) · Community Beta**

Addon: `cgpt`

- **Phát triển addon:** CGPT (ChatGPT) — dev chính, phục dựng sự kiện và triển khai mã nguồn.
- **Kiểm thử gameplay và góp ý:** [cuonghappypets](https://github.com/cuonghappypets) — trải nghiệm thực tế, định hướng tính năng và hỗ trợ hoàn thiện addon.
- **Nền tảng JxOffline V5:** ACE và Mel.

Dự án phục dựng 61 lễ hội Võ Lâm Truyền Kỳ giai đoạn 2005–2010 trên môi trường JX Offline V5.2. Bản beta cộng đồng đang chuẩn bị; chưa có gói cài công khai, chưa xác nhận tương thích bản sạch, chưa có 61/61 native gameplay PASS. Mỗi người chơi có thể đóng góp bằng cách chọn vài sự kiện từng trải nghiệm và ghi lỗi có thể tái hiện.

## Phạm vi addon cộng đồng

Tôn trọng game gốc và ý đồ của các tác giả JxOffline V5. Addon chỉ phục dựng lễ hội và bổ sung Hồi Ức Võ Lâm Lệnh với hai nhóm **Quản lý lễ hội** và **Quản lý tính năng** (các hoạt động nguyên bản). Trong Quản lý lễ hội, mục đầu dùng để quản lý sự kiện hiện tại: tạm dừng nhưng vẫn cho đổi thưởng, hoặc đóng và ngừng đổi thưởng. Không bao gồm mod cấp tiền, điểm, trang bị hay chỉnh tốc độ luyện kỹ năng.

Không đính kèm full game, tài khoản, DB/save, mã/asset chưa có quyền phân phối. Gói cài, phạm vi tương thích và license sẽ chỉ được công bố sau khi kiểm duyệt. Không tự nhận là sản phẩm chính thức của nhà phát hành.

## Cài đặt và đồng bộ addon

> **Hiện trạng:** chưa có gói cài công khai. Các bước dưới đây mô tả cách sử dụng gói `cgpt` khi được phát hành, không phải hướng dẫn lấy mã từ repo tài liệu hiện tại để cài ngay. Không dùng gói addon cá nhân hoặc bản ghép chưa duyệt thay thế.

### Chuẩn bị

1. Có bộ **JxOffline V5 của ACE và Mel**, đã cập nhật V5.1 và V5.2, chơi được bình thường. Chưa xác nhận tương thích V5.0/V5.1 hoặc bản mod khác.
2. Thoát game, tắt GameServer và sao lưu toàn bộ server, client, ảnh đĩa máy ảo và dữ liệu nhân vật. Nên thử trên bản sao trước.
3. Khi gói addon được công bố, tải đúng phiên bản từ mục Releases và giải nén vào thư mục riêng. Không chép đè cả bộ game.

### Đồng bộ lần đầu

Gói dự kiến có cấu trúc `cgpt/server1/` và `cgpt/Client/` (chỉ các file cần thiết cho lễ hội). Đọc ghi chú tương thích của chính gói đó trước khi chép.

| Thư mục trong gói | Vị trí trong game |
| --- | --- |
| `cgpt/server1/script/` | `server1/script/` trên server Linux |
| `cgpt/server1/settings/` | `server1/settings/` trên server Linux |
| `cgpt/Client/settings/` | `settings/` trong thư mục Client Windows |

4. Dừng game stack trong launcher, giữ máy ảo hoạt động để sử dụng tab **Quản lý file**. Xác nhận đúng thư mục server đang dùng: tùy bộ cài có thể là `/home/jxser/server1` hoặc `/home/jxser_new/server1`. Không chép nhầm profile. Chép gộp nội dung server vào đúng `server1`, giữ nguyên đường dẫn và mã TCVN3.
5. Chép gộp nội dung `Client/` vào thư mục client thực tế. Không tạo thêm một cấp `Client/Client`. Những thay đổi bảng vật phẩm cần đồng bộ cả hai phía; nếu bản cập nhật chỉ có Lua server thì không cần chép client.
6. Khởi động lại GameServer, mở game. Trong **Cẩm Nang Đồng Hành**, nhận **Hồi Ức Võ Lâm Lệnh** (một lệnh bài quản lý). Dùng lệnh để vào Quản lý lễ hội hoặc Quản lý tính năng. Khi thử lễ hội, mở một sự kiện, kiểm tra thông báo và trạng thái trước khi tham gia.

### Cập nhật bản mới hoặc gỡ addon

- Với bản cập nhật nhỏ, sao lưu các file sẽ thay, dừng GameServer, chép đúng delta server/client được cung cấp cho phiên bản đang dùng rồi khởi động lại. Không lấy delta của bản khác ghép vào.
- Nếu lỗi, dừng game/server và dùng bản rollback đúng phiên bản hoặc khôi phục backup. Rollback file không hoàn tác vật phẩm, EXP hoặc tiến độ đã phát sinh; nếu cần khôi phục cả dữ liệu, dùng backup đầy đủ.
- Nếu bộ game đã chỉnh mod, không chép đè bảng item hoặc script dùng chung khi chưa đối chiếu xung đột. Addon cộng đồng không thay các chức năng nguyên bản ngoài phần tích hợp sự kiện, không cấp tiền/điểm/đồ miễn phí.

### Trạng thái bộ cài

Đã tách mã quản lý lễ hội khỏi bản mod cá nhân và đối chiếu các tuyến tích hợp với archive game gốc. Còn phải hoàn thành bản ghép bảng vật phẩm sự kiện và thử trên JX V5.2 sạch. Không phát tán bảng item nguyên khối từ bản private: chúng có thay đổi giới hạn stack và các dữ liệu ngoài phạm vi lễ hội. Nghiệm thu gameplay do cộng đồng cùng đóng góp; các ca chưa thử không được ghi PASS. Thép Tinh Luyện (ID52) còn tình huống thiếu ô hành trang/stack cần kiểm tra, chưa khuyến nghị giao dịch trên nhân vật có dữ liệu quan trọng.

## Cẩm nang và góp ý

- [Cẩm nang chi tiết 61 sự kiện (HTML)](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/)
- [Danh sách kiểm thử](COMMUNITY_UAT.md)
- [Mẫu báo lỗi](REPORT_BUG.md)

Cẩm nang công khai gồm 61 bài chi tiết, giữ nội dung và liên kết nguồn; không kèm ảnh hoặc sprite game. Gói addon chưa phát hành.

## Lời cảm ơn

Đặc biệt cảm ơn **ACE và Mel**, những người đã làm nên bản JxOffline V5 để anh em có cơ hội trở lại Võ Lâm. Nếu không có công sức của hai anh, addon phục dựng lễ hội này cũng không có nền tảng để ra đời. CGPT là addon cộng đồng độc lập, không phải bản phát hành chính thức của ACE hay Mel.
