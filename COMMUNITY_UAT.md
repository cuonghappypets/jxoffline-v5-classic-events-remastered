# Anh em cùng chơi thử

## Beta 5.1 — Classic Event Experience

Đã kiểm tra trên đúng payload Beta 5.1: 22 nhóm kiểm thử Lua giả lập, gồm 200 tổ hợp lựa chọn vật phẩm ON/OFF, menu public/private, Relay và callback. Chưa kiểm thử native: pickup, marker, lưu qua restart, tương thích Auto thực tế và trường hợp túi đầy. Nếu có lỗi hoặc hộp bị khóa, tắt chế độ, giữ backup/log và báo lỗi; không ép mở lại. Đây vẫn là bản beta.

- Kiểm tra menu public chỉ có tra cứu bản đồ, kiểm tra map hiện tại, Fix Bug Auto và quay lại; không còn nút chỉnh tỷ lệ.
- Tết 2009 (STT 42): OFF giữ vật phẩm trực tiếp. ON thử với bản sao game, kiểm đúng một vật phẩm gốc, không mở rương bên trong, kiểm manual pickup, túi đầy, tắt lại, relogin/restart. Không dùng nếu không gặp lỗi tương thích.
- Kiểm tra STT 09 Đào Vạn Thọ và STT 11 Trung thu 2006 không bị thay đổi cơ chế. Báo đúng phiên bản, STT, bản đồ, Auto, tình trạng túi và ảnh trước/sau; giữ backup nếu có lỗi.

Nếu đang dùng Beta 5 và từng chỉnh tỷ lệ drop, trước khi cập nhật hãy chọn Khôi phục tỷ lệ mặc định (2% – 5%) và mở lại menu xác nhận. Bản 5.1 chỉ ẩn các nút điều chỉnh, không tự ghi đè cấu hình Relay đã lưu. Nếu đã dùng bản thử Auto trước đó, hãy tắt Auto và xác nhận trước khi nâng cấp. Không chỉnh DB thủ công.

[Báo lỗi](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/issues)


Các mục Beta 5 và Beta 4 dưới đây là hướng dẫn kiểm thử lịch sử, không áp dụng các nút tùy chỉnh drop cho Beta 5.1.

## Beta 5 — Item Quality of Life Update

Chọn một vài sự kiện, không cần thử hết 61. Ghi phiên bản game và addon, STT, map, cấp, cách tái hiện và số lượng trước/sau.
- STT42 (Tết 2009): nhặt trực tiếp Lam/Hồng/Lục, Hồng hiển thị và gom đúng, mở một rương từ chồng giảm đúng một, nhận đúng chữ Lộc.
- STT09 (Đào Vạn Thọ): cấp 80+, bốn map riêng; kiểm đường cát và hai bánh đào, 25% không theo thiết lập 100%.
- STT11 (Trung thu 2006): dùng một lồng đèn/bánh từ chồng và kiểm hiệu ứng/EXP. Kiểm dấu tiếng Việt của mô tả.
- STT19 (Lễ hội chiến công): kiểm ghép và mở túi, số lượng giảm/tăng đúng.
- Relogin/restart, kiểm số lượng, tỷ lệ và sự kiện đang mở. Nếu mất/nhân đôi vật phẩm, dừng và giữ backup.

Đã chơi thử đại diện: Hồng Bảo Rương hiển thị và gom được chồng 72 chiếc. Bản tích hợp qua 618/618 ca hồi quy drop/menu, 100/100 ca chọn vật phẩm Tết 2009, 5/5 ca callback rương, 25/25 ca callback nhóm stacking và 200 lượt kiểm tra xác suất Đào Vạn Thọ trong Lua giả lập. Đã đối chiếu 458 ID ứng viên đang hoạt động qua 6 profile và 2 biến thể (5.496 lượt); không còn đường dẫn sprite thiếu trong tập kiểm tra. Chưa xác nhận mọi sprite render, tự gom khi nhặt, tiêu hao một đơn vị, lưu qua restart hoặc cài mới trên mọi nền tảng. Sau reload/restart, kiểm tra lại sự kiện và tỷ lệ; đã ghi nhận trường hợp về Mâm ngũ quả.

Các số STT bên dưới khớp cẩm nang và Lệnh bài; ID kỹ thuật giữ nguyên.

## Beta 4 — kiểm thử theo phản hồi

Beta 4 bổ sung các bãi luyện công cấp cao, trong đó có Tu Luyện Cốc 90–180, và chỉnh tỷ lệ mặc định xuống 2% ở nhóm thấp và 5% ở nhóm cao (90/110/119 theo file drop), mỗi lượt trúng rơi một món. Điều kiện riêng và các nguồn rơi đặc thù vẫn giữ nguyên.

Anh em có thể tự chỉnh trong game: Hồi Ức Võ Lâm Lệnh → Quản lý sự kiện → Quản lý vật phẩm sự kiện (sau Kỳ duyên giang hồ). Chỉnh tỷ lệ 0–100% cho từng nhóm, 0% là tắt nhóm đó; bỏ công tắc bật/tắt riêng và chỉnh số lượng. Cấu hình OFF cũ giữ 0/0; Khôi phục mặc định đưa về 2%/5%, một vật phẩm mỗi lượt trúng. Nếu Relay chưa có module, khởi tạo và đợi xác nhận trước khi chỉnh; không gửi lặp khi chưa xác nhận. Danh sách và thông tin map xét sự kiện đang mở, không đọc maplist trong lúc farm. Thiết lập áp dụng chung cho server offline; danh sách map vẫn nằm trong config.lua.

Đã kiểm tra native đại diện Trung thu 2006 tại Tần Lăng: 100%, ba lần tạo một vật phẩm và có nhặt item. Bản sạch qua 618/618 ca hồi quy giả lập và 33.693 đối chiếu map/sự kiện. Chưa kiểm thử native toàn bộ bản sạch, lưu tỷ lệ/trạng thái sự kiện qua restart, hiệu năng hoặc cài mới trên từng nền. Sau reload/restart, kiểm tra lại sự kiện đang mở và tỷ lệ trước khi farm; đã ghi nhận trường hợp quay về Mâm ngũ quả.

Ưu tiên Tu Luyện Cốc 80/90/120/180 và map cao; thử menu với 100%/1 món, 0%, reset, kiểm tra đúng sự kiện và restart. Ghi nhận kết quả thực tế và phiên bản đang dùng.


Chọn 1–3 sự kiện mình từng chơi, dùng bản sao game để trải nghiệm. Không cần chơi hết 61 sự kiện có thể mở. Cùng kiểm tra cách mở sự kiện, tìm NPC, săn nguyên liệu, chế tạo/đổi thưởng, số lượt và tiến độ sau khi đăng nhập lại.

Ưu tiên báo lỗi mất đồ, nhận thưởng lặp, sai kinh nghiệm, sai phần thưởng hoặc game bị treo. Nếu chỉ chơi thử một phần, cứ kể lại đúng phần đó. Không cần kết luận cả sự kiện hoạt động tốt nếu chưa thử hết.

Owner đã chấp nhận lượt chơi thử nhanh Beta3 trên bộ UAT private ngày 27/11/2026. Bản cộng đồng chưa được xác nhận cài mới trên từng nền tảng hoặc chơi hết các tuyến. Ưu tiên thử #27 (mảnh tranh, đổi lệnh bài và đèn đặc biệt), #35/#36/#40/#41 (nguyên liệu), #51 (Tân Bản Cổ), #62 (điểm Tống Kim thật) và #63 (vật phẩm, stack và buff người tuyết), đồng thời kiểm tra Thượng Sứ Lễ Hội và chuyển trạng thái. 63 ID kỹ thuật; danh mục có 62 mục, 61 có thể mở. #02 Trung thu PGaming đã lưu trữ; #52 Thép Tinh Luyện vẫn tạm khóa. Các mục chưa xác nhận đầy đủ không có nghĩa là sự kiện hỏng; chỉ là chưa có đủ kết quả chơi thử của chính bản phát hành này.

[Mẫu góp ý và báo lỗi](REPORT_BUG.md) · [Cẩm nang](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/)

| STT | ID | Sự kiện | Tình trạng chơi thử đầy đủ |
|---:|---:|---|---|
| 05 | 01 | Tết 2006 - Mâm ngũ quả | Chưa xác nhận đầy đủ |
| 16 | 03 | Tết 2007 - Pháo giao thừa | Chưa xác nhận đầy đủ |
| 02 | 04 | Trung thu 2005 - Minh Nguyệt trấn | Chưa xác nhận đầy đủ |
| 25 | 05 | Giáng sinh 2007 - Người tuyết | Chưa xác nhận đầy đủ |
| 23 | 06 | Trung thu 2007 - Làm bánh | Chưa xác nhận đầy đủ |
| 13 | 07 | Nhất tự vi sư 2006 | Chưa xác nhận đầy đủ |
| 17 | 08 | Valentine 2007 - Hoa hồng | Chưa xác nhận đầy đủ |
| 08 | 09 | Vu Lan 2006 - Liên hoa | Chưa xác nhận đầy đủ |
| 18 | 10 | Hàn thực 2007 - Bánh chay | Chưa xác nhận đầy đủ |
| 30 | 11 | Valentine 2008 - Tín vật | Chưa xác nhận đầy đủ |
| 01 | 12 | Quốc tế Lao động 2005 - Sát Thủ Huyền Giản | Chưa xác nhận đầy đủ |
| 07 | 13 | Sinh nhật Võ Lâm 2006 - 1 tuổi | Chưa xác nhận đầy đủ |
| 10 | 14 | Quốc khánh Việt Nam 2006 | Chưa xác nhận đầy đủ |
| 09 | 15 | Kỷ niệm Kiếm Hiệp 3 năm - Đào Vạn Thọ | Chưa xác nhận đầy đủ |
| 20 | 16 | Sinh nhật Võ Lâm 2007 - 2 tuổi | Chưa xác nhận đầy đủ |
| 27 | 17 | Mật đồ thần bí 2007 | Chưa xác nhận đầy đủ |
| 24 | 18 | Nhà giáo Việt Nam 2007 - Tôn sư trọng đạo | Chưa xác nhận đầy đủ |
| 28 | 19 | Tết 2008 - Bánh chưng | Chưa xác nhận đầy đủ |
| 34 | 20 | Sinh nhật Võ Lâm 2008 - Phong Hỏa Liên Thành | Chưa xác nhận đầy đủ |
| 42 | 21 | Tết 2009 - Hồng bao, ngũ quả, pháo hoa | Chưa xác nhận đầy đủ |
| 29 | 22 | Tết 2008 - Hái lộc đầu xuân | Chưa xác nhận đầy đủ |
| 26 | 23 | Giáng sinh 2007 - Tìm thiếu nữ | Chưa xác nhận đầy đủ |
| 12 | 24 | Quốc khánh Kiếm Hiệp 2006 | Chưa xác nhận đầy đủ |
| 31 | 25 | Quốc tế Phụ nữ 2008 - Tặng hoa | Chưa xác nhận đầy đủ |
| 22 | 26 | Quốc khánh Việt Nam 2007 | Chưa xác nhận đầy đủ |
| 11 | 27 | Trung thu 2006 - Lồng đèn cổ điển | Chưa xác nhận đầy đủ |
| 21 | 28 | Triệu hồi Mãnh Tướng 2007 | Chưa xác nhận đầy đủ |
| 39 | 29 | Ươm mầm may mắn 2008 | Chưa xác nhận đầy đủ |
| 40 | 30 | Tứ hải giai huynh đệ 2008 | Chưa xác nhận đầy đủ |
| 41 | 31 | Bắc Đẩu luyện đan 2008 | Chưa xác nhận đầy đủ |
| 04 | 32 | Tây Sơn Cư 10 năm 2005 | Chưa xác nhận đầy đủ |
| 32 | 33 | 30-4-2008 - Lá cờ chiến thắng | Chưa xác nhận đầy đủ |
| 33 | 34 | 30-4-2008 - Diệt sơn tặc | Chưa xác nhận đầy đủ |
| 35 | 35 | Quốc khánh 2008 - Dưỡng Sinh Bí Phổ | Chưa xác nhận đầy đủ |
| 36 | 36 | Trung thu 2008 - Thưởng nguyệt | Chưa xác nhận đầy đủ |
| 37 | 37 | Nhà giáo 2008 - Đáp tạ ân sư | Chưa xác nhận đầy đủ |
| 38 | 38 | Giáng sinh 2008 - Bánh kem | Chưa xác nhận đầy đủ |
| 44 | 39 | Valentine 2009 - Cây tình nhân | Chưa xác nhận đầy đủ |
| 46 | 40 | 30-4-2009 - Chế bầu rượu | Chưa xác nhận đầy đủ |
| 49 | 41 | Quốc khánh 2009 - Chiếc mũ hòa bình | Chưa xác nhận đầy đủ |
| 52 | 42 | Tết 2010 - Cây mai ngày Tết | Chưa xác nhận đầy đủ |
| 51 | 43 | Giáng sinh 2009 - Trang trí cây thông | Chưa xác nhận đầy đủ |
| 47 | 44 | 30-4-2009 - Chinh phục Fansipan | Chưa xác nhận đầy đủ |
| 53 | 45 | 30-4-2010 - Đơm mầm hạnh phúc | Chưa xác nhận đầy đủ |
| 45 | 46 | Quốc tế Phụ nữ 2009 - Tặng trang sức | Chưa xác nhận đầy đủ |
| 54 | 47 | Đả Hổ 2010 - Hoa Sen Cận | Chưa xác nhận đầy đủ |
| 60 | 48 | Trung thu 2010 - Lồng đèn bươm bướm | Chưa xác nhận đầy đủ |
| 50 | 49 | Nhà giáo 2009 - Đố hoa đăng | Chưa xác nhận đầy đủ |
| 43 | 50 | Tết 2009 - Phúc Lộc Thọ | Chưa xác nhận đầy đủ |
| 48 | 51 | Sinh nhật 2009 - Nhím Báo Phú / Tân Bản Cổ | Chưa xác nhận đầy đủ |
| 55 | 52 | 30-4-2010 - Thép Tinh Luyện | Tạm khóa trong beta |
| 06 | 53 | Lễ tình nhân 2006 - Lễ vật tình nhân | Chưa xác nhận đầy đủ |
| 61 | 54 | Nhà giáo 2010 - Báo đáp ân sư | Chưa xác nhận đầy đủ |
| 03 | 55 | Nguyên đán 2006 - Chiếu thư Minh Chủ | Chưa xác nhận đầy đủ |
| 15 | 56 | Nguyên đán 2007 - Quà kinh nghiệm | Chưa xác nhận đầy đủ |
| 58 | 57 | Thần Toán Tử 2010 | Chưa xác nhận đầy đủ |
| 56 | 58 | 30-4-2010 - Chiến sĩ | Chưa xác nhận đầy đủ |
| 62 | 59 | Ngũ Sắc Kết Tinh 2010 - Tam sắc | Chưa xác nhận đầy đủ |
| 57 | 60 | World Cup 2010 - Bóng da, bóng hoàng kim | Chưa xác nhận đầy đủ |
| 59 | 61 | Thất Thành Đại Chiến 2010 - Tiểu Tự Khung | Chưa xác nhận đầy đủ |
| 19 | 62 | 30-4-2007 - Lễ hội chiến công | Chưa xác nhận đầy đủ |
| 14 | 63 | Giáng sinh 2006 - Ghép người tuyết | Chưa xác nhận đầy đủ |
