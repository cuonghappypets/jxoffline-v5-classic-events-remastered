# Community UAT — 61 sự kiện

Mỗi người chọn 1–3 sự kiện mình từng chơi, dùng clone test và báo kết quả có bằng chứng. Không cần chơi tất cả. Ưu tiên lỗi mất đồ, duplicate, sai EXP/thưởng, crash, quota và lưu trạng thái. 
- Smoke chung trước khi phân phối: mở Hồi Ức Lệnh, nhóm mùa, nút đóng/chỉ đổi thưởng nhanh, xác nhận/hủy, chuyển trạng thái Relay, banner, một event mở, relog/restart.
- ID52 ưu tiên cao: chưa cho thử giao dịch rủi ro trên dữ liệu thật, kiểm đủ chỗ trước, điều tra gộp stack/thiếu chỗ trên clone phục hồi được. Grade9 HOLD.
- Chỉ PASS toàn event khi có các ca bắt buộc (route, điều kiện, producer, tiêu thụ, thưởng, giới hạn, persistence); nhánh chưa chạy ghi NOT_TESTED / BLOCKED. Mọi test trên RC10 trước đây chỉ có bằng chứng entry, giao diện, chặn đồng mở; không tính là full PASS. 
- Mẫu REPORT_BUG.md. Ma trận kỹ thuật nội bộ đã được giữ; trạng thái beta riêng bên dưới không tự nhận PASS.



| ID | Sự kiện | Native gameplay toàn event |
|---:|---|---|
| 01 | Tết 2006 - Mâm ngũ quả | NOT_TESTED |
| 02 | Trung thu PGaming | NOT_TESTED |
| 03 | Tết 2007 - Pháo giao thừa | NOT_TESTED |
| 04 | Trung thu 2005 - Minh Nguyệt trấn | NOT_TESTED |
| 05 | Giáng sinh 2007 - Người tuyết | NOT_TESTED |
| 06 | Trung thu 2007 - Làm bánh | NOT_TESTED |
| 07 | Nhất tự vi sư 2006 | NOT_TESTED |
| 08 | Valentine 2007 - Hoa hồng | NOT_TESTED |
| 09 | Vu Lan 2006 - Liên hoa | NOT_TESTED |
| 10 | Hàn thực 2007 - Bánh chay | NOT_TESTED |
| 11 | Valentine 2008 - Tín vật | NOT_TESTED |
| 12 | Quốc tế Lao động 2005 - Sát Thủ Huyền Giản | NOT_TESTED |
| 13 | Sinh nhật Võ Lâm 2006 - 1 tuổi | NOT_TESTED |
| 14 | Quốc khánh Việt Nam 2006 | NOT_TESTED |
| 15 | Kỷ niệm Kiếm Hiệp 3 năm - Đào Vạn Thọ | NOT_TESTED |
| 16 | Sinh nhật Võ Lâm 2007 - 2 tuổi | NOT_TESTED |
| 17 | Mật đồ thần bí 2007 | NOT_TESTED |
| 18 | Nhà giáo Việt Nam 2007 - Tôn sư trọng đạo | NOT_TESTED |
| 19 | Tết 2008 - Bánh chưng | NOT_TESTED |
| 20 | Sinh nhật Võ Lâm 2008 - Phong Hỏa Liên Thành | NOT_TESTED |
| 21 | Tết 2009 - Hồng bao, ngũ quả, pháo hoa | NOT_TESTED |
| 22 | Tết 2008 - Hái lộc đầu xuân | NOT_TESTED |
| 23 | Giáng sinh 2007 - Tìm thiếu nữ | NOT_TESTED |
| 24 | Quốc khánh Kiếm Hiệp 2006 | NOT_TESTED |
| 25 | Quốc tế Phụ nữ 2008 - Tặng hoa | NOT_TESTED |
| 26 | Quốc khánh Việt Nam 2007 | NOT_TESTED |
| 27 | Trung thu 2006 - Lồng đèn cổ điển | NOT_TESTED |
| 28 | Triệu hồi Mãnh Tướng 2007 | NOT_TESTED |
| 29 | Ươm mầm may mắn 2008 | NOT_TESTED |
| 30 | Tứ hải giai huynh đệ 2008 | NOT_TESTED |
| 31 | Bắc Đẩu luyện đan 2008 | NOT_TESTED |
| 32 | Tây Sơn Cư 10 năm 2005 | NOT_TESTED |
| 33 | 30-4-2008 - Lá cờ chiến thắng | NOT_TESTED |
| 34 | 30-4-2008 - Diệt sơn tặc | NOT_TESTED |
| 35 | Quốc khánh 2008 - Dưỡng Sinh Bí Phổ | NOT_TESTED |
| 36 | Trung thu 2008 - Thưởng nguyệt | NOT_TESTED |
| 37 | Nhà giáo 2008 - Đáp tạ ân sư | NOT_TESTED |
| 38 | Giáng sinh 2008 - Bánh kem | NOT_TESTED |
| 39 | Valentine 2009 - Cây tình nhân | NOT_TESTED |
| 40 | 30-4-2009 - Chế bầu rượu | NOT_TESTED |
| 41 | Quốc khánh 2009 - Chiếc mũ hòa bình | NOT_TESTED |
| 42 | Tết 2010 - Cây mai ngày Tết | NOT_TESTED |
| 43 | Giáng sinh 2009 - Trang trí cây thông | NOT_TESTED |
| 44 | 30-4-2009 - Chinh phục Fansipan | NOT_TESTED |
| 45 | 30-4-2010 - Đơm mầm hạnh phúc | NOT_TESTED |
| 46 | Quốc tế Phụ nữ 2009 - Tặng trang sức | NOT_TESTED |
| 47 | Đả Hổ 2010 - Hoa Sen Cận | NOT_TESTED |
| 48 | Trung thu 2010 - Lồng đèn bươm bướm | NOT_TESTED |
| 49 | Nhà giáo 2009 - Đố hoa đăng | NOT_TESTED |
| 50 | Tết 2009 - Phúc Lộc Thọ | NOT_TESTED |
| 51 | Sinh nhật 2009 - Nhím Báo Phú | NOT_TESTED |
| 52 | 30-4-2010 - Thép Tinh Luyện | NOT_TESTED — HOLD giao dịch |
| 53 | Lễ tình nhân 2006 - Lễ vật tình nhân | NOT_TESTED |
| 54 | Nhà giáo 2010 - Báo đáp ân sư | NOT_TESTED |
| 55 | Nguyên đán 2006 - Chiếu thư Minh Chủ | NOT_TESTED |
| 56 | Nguyên đán 2007 - Quà kinh nghiệm | NOT_TESTED |
| 57 | Thần Toán Tử 2010 | NOT_TESTED |
| 58 | 30-4-2010 - Chiến sĩ | NOT_TESTED |
| 59 | Ngũ Sắc Kết Tinh 2010 - Tam sắc | NOT_TESTED |
| 60 | World Cup 2010 - Bóng da, bóng hoàng kim | NOT_TESTED |
| 61 | Thất Thành Đại Chiến 2010 - Tiểu Tự Khung | NOT_TESTED |
