# JxOffline V5 Classic Events Remastered

**JxOffline V5 (by ACE) · Community Beta**

Addon: `cgpt`

- **Phát triển addon:** **CGPT — Classic Game Preservation Team** (Cường + Chat GPT).
- **Nền tảng JxOffline V5:** ACE và Mel.

## Một chút hồi ức Võ Lâm

Chào anh em!

Không biết còn bao nhiêu anh em nhớ những ngày chạy khắp bản đồ săn trái cây làm Mâm Ngũ Quả, những mùa Trung Thu gom nguyên liệu làm lồng đèn, hay những lần thức khuya chỉ để kiếm thêm vài vật phẩm đổi thưởng. Thời ấy, niềm vui chơi Võ Lâm đôi khi cũng chỉ đơn giản như vậy.

Nhờ có bản JxOffline V5 của hai bác ACE và Mel, mình cùng ông dev CGPT đã tranh thủ vài ngày đào bới, chắp vá và chế cháo để phục dựng lại những sự kiện Võ Lâm Truyền Kỳ giai đoạn 2005–2010. Đến nay, addon đã tập hợp được **61 sự kiện**, từ Tết Nguyên Đán, Trung Thu, Giáng Sinh, Valentine, các ngày lễ trong năm, sinh nhật Võ Lâm cho đến những hoạt động đặc biệt khác.

## Có gì trong addon?

Các sự kiện được chia thành những nhóm lễ hội để anh em dễ tìm và chủ động trải nghiệm. Addon bổ sung **Hồi Ức Võ Lâm Lệnh**, với hai nhóm **Quản lý lễ hội** và **Quản lý tính năng** (các hoạt động nguyên bản). Mục đầu của Quản lý lễ hội cho phép quản lý sự kiện hiện tại: tạm dừng nhưng vẫn cho đổi thưởng, hoặc đóng và ngừng đổi thưởng. Thích đón Tết giữa tháng Bảy hay chơi Trung Thu vào đêm giao thừa cũng được. :)))

Kèm theo addon là cẩm nang HTML với 61 bài viết, tổng hợp thể lệ, cách tham gia, vật phẩm, công thức, phần thưởng và tư liệu lịch sử còn tìm được.

Dự án chỉ tập trung vào phục dựng lễ hội, tôn trọng game gốc và ý đồ của các tác giả JxOffline V5. Đây là addon cộng đồng phi thương mại, không phải sản phẩm chính thức của nhà phát hành. Repo không đính kèm full game, tài khoản, DB/save hay mã và tài nguyên chưa rõ quyền phân phối.

## Vài lời về bản beta

Phần quan trọng nhất mình muốn chia sẻ là addon này mới được thực hiện trong vài ngày, với chút ký ức còn sót lại sau gần hai thập kỷ và lượng mã nguồn, dữ liệu ít ỏi mà PGaming cùng các anh em dev đi trước đã để lại.

Có sự kiện còn tương đối đầy đủ dữ liệu, nhưng cũng có sự kiện chỉ còn vài đoạn script, vài vật phẩm hoặc một bài viết cũ. Những cơ chế bị thất lạc phải được suy luận, tái tạo và chế cháo thêm để có thể hoạt động. Cái gì tìm được căn cứ thì cố gắng giữ đúng; phần chưa đủ tư liệu vẫn có thể khác với nguyên bản.

Những sự kiện quen thuộc như **Trung Thu Lồng Đèn** và **Mâm Ngũ Quả** hiện đã tương đối ổn. Tuy nhiên, điều đó không có nghĩa là cả 61 sự kiện đã được kiểm thử gameplay đầy đủ hay phục dựng chính xác như ngày xưa. Bản beta vẫn đang được hoàn thiện; khả năng tương thích với bộ V5.2 sạch cũng chưa được xác nhận.

## Cài đặt và đồng bộ addon

> **Hiện trạng:** chưa có gói cài công khai. Các bước dưới đây mô tả cách sử dụng gói `cgpt` khi được phát hành, không phải hướng dẫn lấy mã từ repo tài liệu hiện tại để cài ngay.

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
- Nếu bộ game đã được tùy chỉnh, không chép đè bảng item hoặc script dùng chung khi chưa đối chiếu xung đột. Addon chỉ thay đổi những phần cần thiết để tích hợp sự kiện.

### Trạng thái bộ cài

Đã đối chiếu các tuyến tích hợp với archive game gốc. Còn phải hoàn thành bản ghép bảng vật phẩm sự kiện và thử trên JX V5.2 sạch. Nghiệm thu gameplay do cộng đồng cùng đóng góp; các ca chưa thử không được ghi PASS. Thép Tinh Luyện (ID52) còn tình huống thiếu ô hành trang/stack cần kiểm tra, chưa khuyến nghị giao dịch trên nhân vật có dữ liệu quan trọng.

## Cẩm nang và góp ý

Anh em nào có thời gian thì chơi thử khi gói beta được phát hành nhé! Không cần test hết 61 sự kiện đâu, cứ chọn những sự kiện mình từng chơi và còn nhớ là quý lắm rồi.

Nếu thấy cơ chế chưa đúng, tỷ lệ rơi đồ hoặc phần thưởng chưa hợp lý, gặp bug hay đơn giản là nhớ một chi tiết khác với bản phục dựng, anh em cứ thoải mái góp ý. Không cần biết lập trình hay đọc source; đôi khi chỉ một câu *“Hồi đó tôi nhớ sự kiện này không phải chơi như vậy…”* cũng đã là một manh mối rất quý.

- [Cẩm nang Hồi Ức Võ Lâm – 61 sự kiện](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/)
- [Danh sách kiểm thử](COMMUNITY_UAT.md)
- [Mẫu báo lỗi](REPORT_BUG.md)
- [Gửi góp ý qua GitHub Issues](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/issues)
- [Releases – nơi công bố gói addon khi sẵn sàng](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases)

Cẩm nang công khai giữ nội dung chi tiết và liên kết nguồn, không kèm ảnh hoặc sprite game. Hiện chưa có gói cài công khai trên GitHub.

## Lời cảm ơn

Đặc biệt cảm ơn hai bác **ACE và Mel** đã làm nên nền tảng JxOffline V5 để anh em có cơ hội trở lại Võ Lâm. Cảm ơn **PGaming** và các anh em dev đi trước đã để lại những đoạn source và tư liệu quý giá cho cộng đồng. Nếu không có công sức của mọi người, chắc cũng chẳng có addon này. :D

Gần hai mươi năm đã qua, mã nguồn có thể thất lạc, tư liệu có thể không còn, nhưng đâu đó trong ký ức mỗi anh em vẫn còn một mảnh Võ Lâm ngày ấy.

Hy vọng chúng ta có thể cùng nhau nhặt nhạnh những mảnh ký ức đó, ghép lại thành một Hồi Ức Võ Lâm trọn vẹn hơn.

Chúc anh em chơi game vui vẻ!
