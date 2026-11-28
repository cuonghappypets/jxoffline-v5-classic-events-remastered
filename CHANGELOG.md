# Lịch sử phát hành

## Beta cộng đồng 5.1 — v1.1.0-beta.5.1 · 28/11/2026

Nhằm bảo toàn trải nghiệm các sự kiện cổ điển của Võ Lâm Truyền Kỳ, từ Beta 5.1 JxCER ngừng cung cấp và hỗ trợ tính năng tùy chỉnh tỷ lệ rơi vật phẩm sự kiện trong menu công cộng. Anh em có nhu cầu sử dụng tính năng này vẫn có thể tải [Beta 5](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5); tính năng sẽ không còn được duy trì, sửa lỗi hoặc cập nhật trong các phiên bản tiếp theo.

Nếu đang dùng Beta 5 và từng chỉnh tỷ lệ drop, trước khi cập nhật hãy chọn Khôi phục tỷ lệ mặc định (2% – 5%) và mở lại menu xác nhận. Bản 5.1 chỉ ẩn các nút điều chỉnh, không tự ghi đè cấu hình Relay đã lưu. Nếu đã dùng bản thử Auto trước đó, hãy tắt Auto và xác nhận trước khi nâng cấp. Không chỉnh DB thủ công.

Fix Bug Auto là chế độ tương thích thử nghiệm, mặc định OFF trên cài đặt mới; chỉ bật nếu thực sự gặp vấn đề nhặt đồ. Hiện chỉ hỗ trợ Tết 2009 (STT 42, ID #21). Khi bật, hộp quà 1 ô thay cho vật phẩm rơi trực tiếp và khi nhặt chuyển thành đúng vật phẩm đã chọn, không thay tỷ lệ hay tự mở rương thưởng. Chưa xác nhận tương thích MelAuto hoặc các Auto khác trong game thực tế. Khi OFF, giữ cơ chế rơi trực tiếp của Beta 5.

Đã kiểm tra trên đúng payload Beta 5.1: 22 nhóm kiểm thử Lua giả lập, gồm 200 tổ hợp lựa chọn vật phẩm ON/OFF, menu public/private, Relay và callback. Chưa kiểm thử native: pickup, marker, lưu qua restart, tương thích Auto thực tế và trường hợp túi đầy. Nếu có lỗi hoặc hộp bị khóa, tắt chế độ, giữ backup/log và báo lỗi; không ép mở lại. Đây vẫn là bản beta.

- Full 288 file; Update từ đúng Beta 5 gồm 16 file, cả Server và Client. [Tải Beta 5.1](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5.1).

## Beta cộng đồng 5 — v1.1.0-beta.5 · 28/11/2026

- **Hình ảnh:** 12 vật phẩm từng thiếu sprite (9 Tết 2009, 3 Đào Vạn Thọ) được trỏ về tài nguyên có sẵn trong Client. Hai bánh đào dùng hình thay thế, không khẳng định đúng hình gốc.
- **Xếp chồng:** chuẩn hóa 25 ID trong 437 ID magic/quest đã rà soát. Giữ nguyên 255 ID có giới hạn dương và 157 ID còn lại do rủi ro/thiếu căn cứ. Không bật đồng loạt cho vật phẩm riêng trạng thái, hạn dùng hay cơ chế tiêu hao đặc biệt.
- **Mô tả:** 115 vật phẩm được biên tập tiếng Việt có dấu theo công dụng trong Lua; giữ tên và ID để tránh ảnh hưởng bộ lọc Auto.
- **Tra cứu:** STT 01–62 trong Hồi Ức Võ Lâm Lệnh khớp [cẩm nang online](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/). Ví dụ 09 là Đào Vạn Thọ (ID15), 42 là Tết 2009 (ID21). ID kỹ thuật, thể lệ, phần thưởng và số sự kiện giữ nguyên.
- **Drop:** giữ cải tiến Beta 4 (2%/5% mặc định, 0–100% tùy chỉnh, một món mỗi lượt trúng với drop thường). Tỷ lệ 0–100% chỉ áp dụng nguồn rơi thường. Đào Vạn Thọ (STT 09, ID #15) và các sự kiện đặc thù giữ cơ chế riêng. Đào Vạn Thọ cấp 80+, bốn map Tứ Đại Phong Cảnh, tỷ lệ 25% riêng. Tết 2009 rơi trực tiếp vật phẩm gốc, không cần hộp trung gian.


- Full 286 file; Update từ Beta 4 ổn định 29 file, cần cả Server và Client. Đã chơi thử đại diện: Hồng Bảo Rương hiển thị và gom được chồng 72 chiếc. Bản tích hợp qua 618/618 ca hồi quy drop/menu, 100/100 ca chọn vật phẩm Tết 2009, 5/5 ca callback rương, 25/25 ca callback nhóm stacking và 200 lượt kiểm tra xác suất Đào Vạn Thọ trong Lua giả lập. Đã đối chiếu 458 ID ứng viên đang hoạt động qua 6 profile và 2 biến thể (5.496 lượt); không còn đường dẫn sprite thiếu trong tập kiểm tra. Chưa xác nhận mọi sprite render, tự gom khi nhặt, tiêu hao một đơn vị, lưu qua restart hoặc cài mới trên mọi nền tảng. Sau reload/restart, kiểm tra lại sự kiện và tỷ lệ; đã ghi nhận trường hợp về Mâm ngũ quả.
- [Tải bản Beta 5](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5)

## Beta cộng đồng 4 — v1.1.0-beta.4 · 28/11/2026

Bản cập nhật theo phản hồi người chơi, gom toàn bộ cải tiến ngày 28/11 vào một bản duy nhất.

- Bổ sung 19 ID map cấp cao, gồm Tu Luyện Cốc 90–180 và các bãi luyện công trên cấp 100.
- Tỷ lệ rơi thường mặc định: 2% nhóm thấp, 5% nhóm cao (90/110/119 theo file drop), mỗi lượt trúng đúng một vật phẩm. Giữ điều kiện riêng và nguồn đặc thù.
- Hồi Ức Võ Lâm Lệnh → Quản lý sự kiện → Quản lý vật phẩm sự kiện (sau Kỳ duyên giang hồ): chỉnh tỷ lệ 0–100%, bỏ công tắc bật/tắt riêng, xem map theo sự kiện đang mở, khôi phục mặc định 2%/5%/1. Không chỉnh số lượng.
- Danh sách map quản lý trong config.lua; chỉ đọc maplist khi xem thông tin, không đọc khi farm. Thiết lập áp dụng chung server offline. Nếu Relay chưa xác nhận, mở lại kiểm tra, không gửi lặp.
- Giữ nguyên 62 mục/61 sự kiện có thể mở, #02 lưu trữ, #52 tạm khóa.


- Cập nhật ổn định cùng ngày: Đã kiểm tra native đại diện Trung thu 2006 tại Tần Lăng: 100%, ba lần tạo một vật phẩm và có nhặt item. Bản sạch qua 618/618 ca hồi quy giả lập và 33.693 đối chiếu map/sự kiện. Chưa kiểm thử native toàn bộ bản sạch, lưu tỷ lệ/trạng thái sự kiện qua restart, hiệu năng hoặc cài mới trên từng nền. Sau reload/restart, kiểm tra lại sự kiện đang mở và tỷ lệ trước khi farm; đã ghi nhận trường hợp quay về Mâm ngũ quả. Update từ Beta3: 38 Lua; từ Beta4 consolidated cũ: 2 Lua; Client không đổi.
- [Tải bản cập nhật](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.4)

## Beta cộng đồng 3 — v1.1.0-beta.3 · 27/11/2026

- Bổ sung ID62 Lễ hội chiến công: đổi điểm Tống Kim tích lũy thật, mua Công trạng lệnh, ghép Túi quà may mắn và đổi hoa lấy EXP. Không thêm điểm Tống Kim giả hoặc nguồn rơi từ quái.
- Bổ sung ID63 Ghép người tuyết: hộp quà, sáu nguyên liệu, ba công thức; thời lượng nhân đôi EXP cá nhân 10/30/60 phút là điều chỉnh offline, cần thêm trải nghiệm thực tế.
- Sinh nhật 2009 (#51) có thêm nhánh Thiên Tứ Bảo Rương, ghép Tân Bản Cổ; giữ Nhím Báo Phú. Trung thu 2006 (#27) bổ sung cơ hội nhận mảnh tranh khi ghép đèn, đổi 10 lệnh bài lấy vật phẩm kỹ năng/tiềm năng và đổi 10 đèn kéo quân đặc biệt; không thêm nguồn mảnh Dã Tẩu chưa xác minh.
- Cân bằng nguyên liệu #27, #35, #36, #40, #41; giữ tỷ lệ rơi thường 10/20% và một vật phẩm mỗi lượt trúng theo điều kiện riêng.
- Lưu trữ Trung thu PGaming (#02), giữ ID và ghi nhận nguồn; #52 Thép Tinh Luyện vẫn khóa. Tổng 63 ID kỹ thuật, 62 mục trong cẩm nang, 61 có thể mở.
- Full và Update từ beta.2 dùng thư mục gói `cuonghappypets_cgpt`; cả hai cần cập nhật server và Client. Update gồm 43 file, 36 file rollback và 7 đường dẫn mới. Đã kiểm thử mock tích hợp và owner chấp nhận chơi thử nhanh bản private; chưa xác nhận cài mới bản công khai trên từng nền tảng hoặc tất cả tuyến sự kiện.

[Xem file tải và ghi chú phát hành](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.3)

## Beta cộng đồng 2 — v1.1.0-beta.2 · 27/11/2026

- Điều chỉnh 32 tuyến rơi nguyên liệu thường: 10% nhóm quái 10–80, 20% nhóm 90 tại bãi hợp lệ; mỗi lượt trúng một món. Giữ điều kiện riêng (Tết 2006/2007 chỉ nhóm 90, Quốc khánh 2007 từ nhóm 50) và nguồn đặc thù.
- Gom các tuyến đổi thưởng tại Tương Dương về Thượng Sứ Lễ Hội, bổ sung số lượng nguyên liệu hiện có, điều hướng và tên sự kiện trong thoại. Giữ NPC/hoạt động đặc thù.
- Quản lý sự kiện hiện tại chỉ xuất hiện khi có event đang mở; Đóng, Tạm dừng, Quay lại. Thông báo riêng sau đổi thưởng theo số lượng khi đọc được thay đổi thực tế.
- Giữ 60 sự kiện có thể mở; ID52 Thép Tinh Luyện vẫn khóa. Không thêm mod cá nhân.
- Gói Full cho người mới và Update từ beta.1 chỉ có 79 Lua server; Client giữ nguyên. Đã chơi thử đại diện ở UAT cá nhân; bản cộng đồng chưa được nghiệm thu toàn bộ trên từng nền tảng.

[Xem file tải và ghi chú phát hành](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.2)

## Beta cộng đồng đầu tiên — v1.1.0-beta.1 · 26/11/2026

- Phục dựng các lễ hội Võ Lâm giai đoạn 2005–2010, cẩm nang 61 sự kiện.
- 60 sự kiện có thể mở; Thép Tinh Luyện tạm khóa để kiểm tra thêm.
- Hồi Ức Võ Lâm Lệnh giúp mở, tạm dừng (vẫn đổi thưởng) và đóng sự kiện.
- Hai cách cài: bản chép trực tiếp và bản vá tạo file từ bộ game gốc. Cùng nội dung addon.
- Bản beta còn cần anh em chơi thử, góp ý thể lệ, phần thưởng và lỗi. Khả năng tương thích V5/V5.1/V5.2 do nhóm phát triển xác nhận; chưa nghiệm thu độc lập toàn bộ bản phát hành.

[Xem file tải và ghi chú phát hành](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.1)

## Cẩm nang trực tuyến

Đã biên tập lời hướng dẫn, giữ bảng công thức, phần thưởng và tư liệu đối chiếu; bổ sung biểu tượng minh họa vật phẩm. Lượt biên tập cuối tập trung vào ngôn ngữ dành cho người chơi, thuật ngữ, tiêu đề và tham chiếu tài liệu. Cập nhật cẩm nang không đồng nghĩa với thay đổi thể lệ trong addon.

Sau Beta3, dự án chuyển sang bảo trì và tiếp nhận góp ý. Giữ ổn định số lượng sự kiện, không mở rộng sau năm 2010; chỉ sửa lỗi và điều chỉnh có căn cứ thực tế. Thử nghiệm bản 1-click là hướng cân nhắc riêng, chưa có xác nhận tương thích hoặc lịch triển khai.
