# Lịch sử phát hành

## Beta cộng đồng 4 — v1.1.0-beta.4 · 28/11/2026

Beta 4 bổ sung 19 ID map cấp cao, gồm Tu Luyện Cốc 90–180. Mặc định 10% nhóm thấp, 20% nhóm cao (90/110/119 theo file drop), một vật phẩm mỗi lượt trúng; giữ nguồn đặc thù và điều kiện riêng. Owner xác nhận farm tại Tu Luyện Cốc ngày 28/11/2026, chưa nghiệm thu mọi map/nền tảng.

RC02 là gói thử nghiệm tùy chọn sau Beta 4 chính: Lệnh bài → Quản lý sự kiện → Quản lý vật phẩm sự kiện (sau Kỳ duyên giang hồ), xem tên map, chỉnh tỷ lệ/số lượng, bật/tắt và reset. Chưa nghiệm thu native Relay, giao diện và lưu qua restart; chỉ thử trên bản sao offline.

- 8.455/8.455 ca mô phỏng RC01; 8.701/8.701 ca mô phỏng RC02. Full và Update chính là RC01; RC02 tùy chọn.
- [Tải và ghi chú phát hành](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.4)

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
