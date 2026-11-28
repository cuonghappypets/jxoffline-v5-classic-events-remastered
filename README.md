# JxCER — JXOffline Classic Events Remastered

**Dự án Phục dựng các sự kiện/lễ hội Võ Lâm Truyền Kỳ xưa** (2005–2010), trên nền tảng JxOffline V5.

![Hồi Ức Võ Lâm — JxOffline V5 Classic Events Remastered, banner minh họa của dự án](assets/readme/cover.jpg)

**JxOffline V5 (by ACE) · Beta cộng đồng 5.1 — Classic Event Experience** (phiên bản phát hành: v1.1.0-beta.5.1)

Thư mục gói addon: `cuonghappypets_cgpt`

**Trạng thái dự án: bảo trì và tiếp nhận góp ý cộng đồng.** Beta 5.1 là mốc hiện tại; chưa mở đợt phát triển nội dung mới.

**Nền tảng JxOffline V5:** ACE và Mel.

**Bộ cài WSL2:** Võ Duy Khánh (VDK).

**Cảm ơn:** Tiểu Âu và các anh em dev đi trước đã để lại mã nguồn và tư liệu quý giá.

**Nhóm phục dựng addon:** **CGPT — Classic Game Preservation Team** (Cường + Chat GPT).

## Bắt đầu tại đây

**Addon là phần bổ sung sự kiện, không phải bộ game đầy đủ.** Anh em cần có JxOffline V5, V5.1 hoặc V5.2 chạy được trước khi cài.

- [Bản chép trực tiếp — CGPT_1.1.0-beta.5.1_Full.zip](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.5.1/CGPT_1.1.0-beta.5.1_Full.zip): cho người mới, giải nén có thư mục cuonghappypets_cgpt.
- [Đang chơi đúng Beta 5? Tải bản cập nhật](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.5.1/CGPT_1.1.0-beta.5.1_Update_from_beta.5.zip): 16 file (10 Server, 6 Client), kiểm PRE trước khi cài.
- [Beta 5 — bản lưu trữ có chỉnh tỷ lệ drop](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5): cũng là bước trung gian nếu đang dùng Beta 4.
- **[Hướng dẫn chi tiết cách cài đặt, cấu hình kết nối và cập nhật addon](INSTALL.md)**.
- **[Hướng dẫn chép file từ Windows sang server bằng WinSCP](INSTALL.md#chép-file-từ-windows-sang-server-bằng-winscp-sftp)**.
- [Mở cẩm nang 62 sự kiện](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/) · [Gửi góp ý](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/issues).

Chưa có game? Xem mục [Cài JxV5 bằng bộ cài WSL2 của VDK](#cài-jxv5-bằng-bộ-cài-wsl2-của-vdk). Đã chơi được game gốc? Chuyển thẳng đến mục [Cài đặt và đồng bộ addon](#cài-đặt-và-đồng-bộ-addon).

**Đừng tải mục Source code (zip) trên GitHub để cài addon.** Dùng đúng file CGPT có liên kết tải ở trên.

## Một chút hồi ức Võ Lâm

Chào anh em!

Không biết còn bao nhiêu anh em nhớ những ngày chạy khắp bản đồ săn trái cây làm Mâm Ngũ Quả, những mùa Trung Thu gom nguyên liệu làm lồng đèn, hay những lần thức khuya chỉ để kiếm thêm vài vật phẩm đổi thưởng. Thời ấy, niềm vui chơi Võ Lâm đôi khi cũng chỉ đơn giản như vậy.

Nhờ có bản JxOffline V5 của hai bác ACE và Mel, mình cùng ông dev CGPT đã tranh thủ vài ngày đào bới, chắp vá và chế cháo để phục dựng lại những sự kiện Võ Lâm Truyền Kỳ giai đoạn 2005–2010. Đến nay, addon có **62 sự kiện trong danh mục, 61 sự kiện có thể mở**, từ Tết Nguyên Đán, Trung Thu, Giáng Sinh, Valentine, các ngày lễ trong năm, sinh nhật Võ Lâm cho đến những hoạt động đặc biệt khác.

## Có gì trong addon?

Các sự kiện được chia thành những nhóm lễ hội để anh em dễ tìm và chủ động trải nghiệm. Addon bổ sung **Hồi Ức Võ Lâm Lệnh**, với hai nhóm **Quản lý sự kiện** và **Quản lý tính năng** (các hoạt động nguyên bản). Khi có sự kiện đang mở, mục đầu tiên là **Quản lý sự kiện hiện tại**: đóng (ngừng săn và đổi thưởng) hoặc tạm dừng (ngừng săn, vẫn đổi thưởng). Khi không có sự kiện đang mở, mục này tự ẩn. Thích đón Tết giữa tháng Bảy hay chơi Trung Thu vào đêm giao thừa cũng được. :)))

**Từ Beta2:** NPC Thượng Sứ Lễ Hội tập trung các tuyến đổi thưởng tại Tương Dương, giữa cổng Nha Môn dưới bậc thang. Các NPC và tuyến đặc thù vẫn giữ riêng. Hệ thống đổi theo số lượng bổ sung thông báo riêng về vật phẩm thực tế đã sử dụng và nhận được khi đọc được dữ liệu giao dịch.

**Kế thừa từ Beta 5:** Beta 5 — Item Quality of Life Update: sửa 12 vật phẩm thiếu hình ảnh, chuẩn hóa xếp chồng 25 ID và biên tập 115 mô tả. STT trong Lệnh bài trùng với cẩm nang online; ID kỹ thuật không đổi.

**Từ Beta 4:** Beta 4 bổ sung các bãi luyện công cấp cao, trong đó có Tu Luyện Cốc 90–180, và chỉnh tỷ lệ mặc định xuống 2% ở nhóm thấp và 5% ở nhóm cao (90/110/119 theo file drop), mỗi lượt trúng rơi một món. Điều kiện riêng và các nguồn rơi đặc thù vẫn giữ nguyên.

Nhằm bảo toàn trải nghiệm các sự kiện cổ điển của Võ Lâm Truyền Kỳ, từ Beta 5.1 JxCER ngừng cung cấp và hỗ trợ tính năng tùy chỉnh tỷ lệ rơi vật phẩm sự kiện trong menu công cộng. Anh em có nhu cầu sử dụng tính năng này vẫn có thể tải [Beta 5](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/tag/v1.1.0-beta.5); tính năng sẽ không còn được duy trì, sửa lỗi hoặc cập nhật trong các phiên bản tiếp theo.

Nếu đang dùng Beta 5 và từng chỉnh tỷ lệ drop, trước khi cập nhật hãy chọn Khôi phục tỷ lệ mặc định (2% – 5%) và mở lại menu xác nhận. Bản 5.1 chỉ ẩn các nút điều chỉnh, không tự ghi đè cấu hình Relay đã lưu. Nếu đã dùng bản thử Auto trước đó, hãy tắt Auto và xác nhận trước khi nâng cấp. Không chỉnh DB thủ công.

Fix Bug Auto là chế độ tương thích thử nghiệm, mặc định OFF trên cài đặt mới; chỉ bật nếu thực sự gặp vấn đề nhặt đồ. Hiện chỉ hỗ trợ Tết 2009 (STT 42, ID #21). Khi bật, hộp quà 1 ô thay cho vật phẩm rơi trực tiếp và khi nhặt chuyển thành đúng vật phẩm đã chọn, không thay tỷ lệ hay tự mở rương thưởng. Chưa xác nhận tương thích MelAuto hoặc các Auto khác trong game thực tế. Khi OFF, giữ cơ chế rơi trực tiếp của Beta 5.

Hồi Ức Võ Lâm Lệnh → Quản lý sự kiện → Quản lý vật phẩm sự kiện: xem danh sách bản đồ, kiểm tra bản đồ hiện tại, Fix Bug Auto và quay lại. Với Relay chưa khởi tạo, mục Auto có bước xác nhận khởi tạo riêng, không đổi tỷ lệ; chọn lại Auto sau khi khởi tạo thành công.

**Từ Beta3:** Lễ hội chiến công (30/4/2007), Ghép người tuyết (Giáng sinh 2006), nhánh Tân Bản Cổ của Sinh nhật 2009; bổ sung nhánh đổi lệnh bài và đèn kéo quân đặc biệt của Trung thu 2006, cân bằng vật liệu #35/#36/#40/#41 và ẩn #02 khỏi danh mục. Các ngày 30/4 và 25/12 là mốc tham chiếu dịp lễ, chưa xác minh lịch mở chính thức.

Đợt nâng cấp này đã đối chiếu 30 sự kiện từ tư liệu của Tiểu Âu: giữ nguyên 17, nâng cấp 6, phục dựng thêm 2 và tạm gác 5. JxCER tiếp thu có chọn lọc, giữ bản sắc từng lễ hội và điều chỉnh khi cần cho trải nghiệm offline, LAN nhỏ.

Cẩm nang HTML trực tuyến có 62 bài trong danh mục, tổng hợp thể lệ, cách tham gia, vật phẩm, công thức, phần thưởng và tư liệu lịch sử còn tìm được.

Dự án chỉ tập trung vào phục dựng lễ hội, tôn trọng game gốc và ý đồ của các tác giả JxOffline V5. Đây là addon cộng đồng phi thương mại, không phải sản phẩm chính thức của nhà phát hành. Kho mã không đính kèm bộ game đầy đủ, tài khoản, cơ sở dữ liệu hoặc dữ liệu lưu nhân vật, cũng như mã và tài nguyên chưa rõ quyền phân phối.

## Hình ảnh những mùa lễ hội

| Trung Thu Lồng Đèn | Mâm Ngũ Quả |
| :---: | :---: |
| ![Banner minh họa Trung Thu Lồng Đèn](assets/readme/mid-autumn-poster.jpg) | ![Banner minh họa Mâm Ngũ Quả](assets/readme/tet-poster.jpg) |

*Hai banner minh họa gợi nhớ không khí lễ hội năm xưa, không phải ảnh chụp trong game.*

| Lồng đèn tại Chu Tiên trấn | Săn nguyên liệu tại Khóa Lang động |
| :---: | :---: |
| ![Cảnh lồng đèn trong game](assets/readme/lanterns-ingame.jpg) | ![Cảnh đánh quái và nhặt nguyên liệu trong game](assets/readme/materials-ingame.jpg) |

*Ảnh chụp trong quá trình chơi thử, cắt khung để tập trung vào cảnh sự kiện.*

## Vài lời về bản beta

Phần quan trọng nhất mình muốn chia sẻ là addon này mới được thực hiện trong vài ngày, với chút ký ức còn sót lại sau gần hai thập kỷ và lượng mã nguồn, dữ liệu ít ỏi mà Tiểu Âu cùng các anh em dev đi trước đã để lại.

Có sự kiện còn tương đối đầy đủ dữ liệu, nhưng cũng có sự kiện chỉ còn vài đoạn script, vài vật phẩm hoặc một bài viết cũ. Những cơ chế bị thất lạc phải được suy luận, tái tạo và chế cháo thêm để có thể hoạt động. Cái gì tìm được căn cứ thì cố gắng giữ đúng; phần chưa đủ tư liệu vẫn có thể khác với nguyên bản.

Những sự kiện quen thuộc như **Trung Thu Lồng Đèn** và **Mâm Ngũ Quả** hiện đã tương đối ổn. Tuy nhiên, điều đó không có nghĩa là mọi sự kiện đã được kiểm thử gameplay đầy đủ hay phục dựng chính xác như ngày xưa. Bản beta được giữ để anh em chơi thử và góp ý. Nhóm sẽ tập trung tiếp nhận phản hồi trước khi mở lại đợt phát triển. Addon hướng đến JxOffline V5, V5.1 và V5.2 của ACE và Mel. Bản Beta 5.1 có 63 ID kỹ thuật, 62 sự kiện trong danh mục và 61 có thể mở. Trung thu PGaming (#02) được lưu trữ, giữ ghi nhận tác giả; Thép Tinh Luyện (#52) vẫn tạm khóa để kiểm tra rủi ro nhận thưởng.

Mình muốn giữ ổn định số lượng sự kiện hiện tại, tập trung sửa lỗi và điều chỉnh dựa trên trải nghiệm thực tế thay vì tiếp tục mở rộng sang những sự kiện sau năm 2010. Nếu thu xếp được thời gian, mình có thể thử khả năng tương thích với bản Võ Lâm Offline 1-click cho anh em máy yếu hơn. **Bản 1-click chưa được xác nhận tương thích**, chưa có lịch phát hành riêng.

## Cộng đồng Vozer Truyền Kỳ Vui Vẻ

Anh em có thể tham gia [Discord Vozer Truyền Kỳ Vui Vẻ](https://discord.gg/B7WEFRDwT) để tải bản JxV5 gốc, trao đổi kinh nghiệm cài đặt và thảo luận cùng Mel, ACE và cộng đồng người chơi.

## Cài JxV5 bằng bộ cài WSL2 của VDK

**Chỉ làm phần này nếu anh em chưa có JxV5 chạy được.** Nếu đã vào game bình thường, không cần cài lại game gốc hay nâng cấp lên V5.2.

1. Tải [bộ cài WSL2 của bác Võ Duy Khánh](https://drive.google.com/file/d/1DAgjb3Ari2zednom28EDCt2Biu0xkLqK/view?usp=drive_link). Tải thêm bộ Server (`.tgz`) và Client JxV5 (bộ file để mở game trên Windows) từ cộng đồng Vozer Truyền Kỳ Vui Vẻ ở trên.
2. Chạy `VLTK-Server.exe` để khởi tạo lần đầu. Sang tab **Quản lý file**, tải file Server `.tgz` lên đúng vị trí theo hướng dẫn bộ cài rồi giải nén tại chỗ.
3. Trở lại tab **Bảng điều khiển**, chọn `jxser` ở cạnh nút **Khởi động**, rồi bấm **Khởi động** để chạy Server. Nếu dùng thư mục server khác, chọn đúng thư mục đó.
4. Khi Server đã khởi động, chạy `Game.exe` trong thư mục Client để vào game.

Kiểm tra game gốc hoạt động bình thường trước khi cài addon CGPT. Nếu chưa vào được game, hãy hỏi cộng đồng về bộ cài trước; addon không thay thế hoặc sửa lỗi cài đặt của game gốc. Bộ cài WSL2 và game gốc là các sản phẩm riêng, không nằm trong gói addon CGPT.

## Cài đặt và đồng bộ addon

**[Tải CGPT Community Beta 5.1 — bản chép trực tiếp](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases/download/v1.1.0-beta.5.1/CGPT_1.1.0-beta.5.1_Full.zip)** — tải file `CGPT_1.1.0-beta.5.1_Full.zip`, không phải Source code (zip).

Người mới chọn Full.zip; anh em đã cài đúng Beta 5 chọn gói Update ở đầu trang. Chỉ cần một gói phù hợp; cả hai cần cập nhật Server và Client. Nếu đang ở phiên bản cũ hơn, xem [các bản phát hành trước](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases). Nếu game có mod riêng, kiểm tra checksum trước khi ghi đè.

> **[Hướng dẫn chi tiết cách cài đặt, cấu hình kết nối và cập nhật addon](INSTALL.md)** — có hướng dẫn sao lưu, chép đúng thư mục, đồng bộ Client và khôi phục khi gặp lỗi.
>
> Nếu cần chuyển file từ Windows sang Linux, xem **[Cách chép file bằng WinSCP (SFTP)](INSTALL.md#chép-file-từ-windows-sang-server-bằng-winscp-sftp)** (địa chỉ, cổng kết nối, tài khoản và cách chép file từng bước).

### Bước 1 — Sao lưu và giải nén

1. Có bộ **JxOffline V5, V5.1 hoặc V5.2 của ACE và Mel**, chơi được bình thường. Không bắt buộc nâng cấp lên V5.2. Các bản mod khác cần đối chiếu xung đột trước khi cài.
2. Thoát game, dừng GameServer và sao lưu server, Client và dữ liệu nhân vật. Nếu sao chép cả file đĩa máy ảo, tắt hẳn môi trường Linux trước khi sao chép. Nên thử trên bản sao trước.
3. Tải bản `CGPT_1.1.0-beta.5.1_Full.zip` từ Releases và giải nén vào thư mục riêng. Thư mục `cuonghappypets_cgpt` đã có sẵn. Nếu đang dùng đúng Beta 5, xem mục cập nhật bên dưới.

### Bước 2 — Chép file vào server và Client

Thư mục `cuonghappypets_cgpt` có cấu trúc `cuonghappypets_cgpt/server1/` và `cuonghappypets_cgpt/Client/` (chỉ các file cần thiết cho lễ hội). Đọc ghi chú tương thích của chính gói đó trước khi chép.

| Thư mục nguồn trong gói | Thư mục đích trong game |
| --- | --- |
| `cuonghappypets_cgpt/server1/script/` | `server1/script/` trên server Linux |
| `cuonghappypets_cgpt/server1/settings/` | `server1/settings/` trên server Linux |
| `cuonghappypets_cgpt/Client/settings/` | `settings/` trong thư mục Client Windows |

**Server** là phần game chạy trên Linux. **Client** là thư mục game trên Windows có file `Game.exe`.

1. Bật môi trường Linux (WSL2 hoặc máy ảo) để chép file, nhưng chưa khởi động GameServer. Dùng tab **Quản lý file** của VDK hoặc WinSCP. Xác định đúng thư mục server đang sử dụng: ví dụ `/home/jxser/server1` hoặc `/home/jxser_new/server1`.
2. Chép **gộp nội dung** hai thư mục `script` và `settings` vào server theo bảng trên. Không xóa file khác hoặc thay cả thư mục game. Ví dụ, chép nội dung `cuonghappypets_cgpt/server1/script/` vào `/home/jxser/server1/script/` nếu đang dùng thư mục server đó. Không tạo thêm cấp `server1/server1`, `script/script` hoặc `settings/settings`. Giữ nguyên file và mã chữ TCVN3.
3. Chép riêng nội dung `cuonghappypets_cgpt/Client/settings/` vào `settings/` của Client trên Windows. Không chép Client lên Linux. Không tạo thêm cấp `Client/Client`. Những thay đổi bảng vật phẩm cần đồng bộ cả hai phía.

#### Chép file từ Windows sang server bằng WinSCP

[WinSCP](https://winscp.net/) là chương trình giúp anh em kéo thả file từ Windows sang Linux mà không cần gõ lệnh.

**[Xem hướng dẫn WinSCP từng bước — thông số kết nối và cách chép file](INSTALL.md#chép-file-từ-windows-sang-server-bằng-winscp-sftp).**

Mở WinSCP, kết nối theo bảng thông số trong hướng dẫn trên. Khung trái là file Windows, khung phải là file Linux. Mở thư mục `cuonghappypets_cgpt/server1` ở bên trái và đúng thư mục `server1` ở bên phải. Chọn hai thư mục `script` và `settings`, chép sang phải ở chế độ **Binary** để giữ nguyên file. Chỉ ghi đè các file cần cập nhật sau khi đã sao lưu, không dùng chế độ đồng bộ có xóa file đích. Chờ chép xong và đóng WinSCP.

Vẫn phải chép riêng phần Client trên Windows theo dòng Client trong bảng bên trên. Nếu WinSCP không kết nối được, xem hướng dẫn chi tiết, không mở cổng ra Internet chỉ để chép file cục bộ.

### Bước 3 — Khởi động lại và vào sự kiện

Khởi động lại GameServer, mở game. Vào **Cẩm Nang Đồng Hành → Nhận Lệnh bài Hồi Ức → Hồi Ức Võ Lâm Lệnh**. Dùng lệnh bài để vào **Quản lý sự kiện**, chọn mùa và sự kiện muốn chơi. Mục **Quản lý tính năng** dành cho các hoạt động nguyên bản.

Chỉ mở một sự kiện tại một thời điểm. [Xem hướng dẫn chung trong cẩm nang](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/guide.html) nếu chưa biết bắt đầu từ đâu.

### Cập nhật bản mới hoặc gỡ addon

Từ đúng Beta 5 lên Beta 5.1, chọn gói Update, kiểm tra PRE/POST.sha256 và chép cả Server lẫn Client. Nếu đang ở Beta 4, nâng lên Beta 5 trước. Không hạ cấp bảng stack khi còn chồng vật phẩm mới chưa được xử lý an toàn; khôi phục file không hoàn tác dữ liệu nhân vật.

- Với bản cập nhật nhỏ, sao lưu các file sẽ thay, dừng GameServer, chép đúng các file cập nhật server/client được cung cấp cho phiên bản đang dùng rồi khởi động lại. Không lấy gói cập nhật của bản khác ghép vào.
- Nếu lỗi, dừng game và GameServer và dùng gói khôi phục đúng phiên bản hoặc bản sao lưu. Khôi phục file không hoàn tác vật phẩm, EXP hoặc tiến độ đã phát sinh; nếu cần khôi phục cả dữ liệu, dùng bản sao lưu đầy đủ.
- Nếu bộ game đã được tùy chỉnh, không chép đè bảng vật phẩm hoặc script dùng chung khi chưa đối chiếu xung đột. Addon chỉ thay đổi những phần cần thiết để tích hợp sự kiện.

**[Đọc hướng dẫn cập nhật và khôi phục chi tiết](INSTALL.md#5-cập-nhật-addon).**

### Trạng thái bộ cài

Beta 5 đã chơi thử đại diện: Hồng Bảo Rương hiển thị và gom được chồng 72 chiếc. Bản tích hợp qua 618/618 ca hồi quy drop/menu, 100/100 ca chọn vật phẩm Tết 2009, 5/5 ca callback rương, 25/25 ca callback nhóm stacking và 200 lượt kiểm tra xác suất Đào Vạn Thọ trong Lua giả lập. Đã đối chiếu 458 ID ứng viên đang hoạt động qua 6 profile và 2 biến thể (5.496 lượt); không còn đường dẫn sprite thiếu trong tập kiểm tra. Chưa xác nhận mọi sprite render, tự gom khi nhặt, tiêu hao một đơn vị, lưu qua restart hoặc cài mới trên mọi nền tảng. Sau reload/restart, kiểm tra lại sự kiện và tỷ lệ; đã ghi nhận trường hợp về Mâm ngũ quả. #02 lưu trữ, #52 vẫn tạm khóa.

Beta 5.1 đã qua 22 nhóm kiểm thử Lua giả lập, gồm 200 tổ hợp lựa chọn vật phẩm ON/OFF; tính năng Fix Bug Auto chưa được xác minh native.

## Cẩm nang và góp ý

[![Giao diện cẩm nang Hồi Ức Võ Lâm](assets/readme/handbook.jpg)](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/)

*Bấm vào ảnh để mở cẩm nang và tìm sự kiện muốn chơi.*

Anh em nào có thời gian thì tải gói beta về chơi thử nhé! Không cần test hết các sự kiện đâu, cứ chọn những sự kiện mình từng chơi và còn nhớ là quý lắm rồi.

Nếu thấy cơ chế chưa đúng, tỷ lệ rơi đồ hoặc phần thưởng chưa hợp lý, gặp bug hay đơn giản là nhớ một chi tiết khác với bản phục dựng, anh em cứ thoải mái góp ý. Không cần biết lập trình hay đọc source; đôi khi chỉ một câu *“Hồi đó tôi nhớ sự kiện này không phải chơi như vậy…”* cũng đã là một manh mối rất quý.

JxCER hoàn toàn phi thương mại, không nhận donate hay mời cà phê. Anh em chơi thử và chia sẻ góp ý là sự hỗ trợ quý nhất đối với dự án.

<p align="center">
  <img src="assets/readme/community-poster.jpg" width="720" alt="Tranh minh họa hội quán Võ Lâm — Anh em vào test phụ một tay nhé!" />
</p>

- [Cẩm nang Hồi Ức Võ Lâm – 62 sự kiện](https://cuonghappypets.github.io/jxoffline-v5-classic-events-remastered/)
- [Hướng dẫn chi tiết cách cài đặt, cấu hình kết nối và cập nhật addon](INSTALL.md) (bao gồm cách gỡ addon)
- [Cách chép file bằng WinSCP (SFTP)](INSTALL.md#chép-file-từ-windows-sang-server-bằng-winscp-sftp)
- [Những thay đổi qua các phiên bản](CHANGELOG.md)
- [Danh sách sự kiện để anh em chơi thử](COMMUNITY_UAT.md)
- [Mẫu báo lỗi](REPORT_BUG.md)
- [Gửi góp ý qua GitHub Issues](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/issues)
- [Releases – tải gói addon](https://github.com/cuonghappypets/jxoffline-v5-classic-events-remastered/releases)

Cẩm nang giữ nội dung chi tiết và liên kết nguồn; các icon vật phẩm chỉ là minh họa, không phải hình gốc trong game.

## Lời cảm ơn

Đặc biệt cảm ơn hai bác **ACE và Mel** đã làm nên nền tảng JxOffline V5 để anh em có cơ hội trở lại Võ Lâm. Cảm ơn bác **Võ Duy Khánh (VDK)** đã chia sẻ bộ cài WSL2, giúp anh em thuận tiện hơn khi cài đặt và trải nghiệm game. Cảm ơn **Tiểu Âu** và các anh em dev đi trước đã để lại những đoạn source và tư liệu quý giá cho cộng đồng. Nếu không có công sức của mọi người, chắc cũng chẳng có addon này. :D

Gần hai mươi năm đã qua, mã nguồn có thể thất lạc, tư liệu có thể không còn, nhưng đâu đó trong ký ức mỗi anh em vẫn còn một mảnh Võ Lâm ngày ấy.

Hy vọng chúng ta có thể cùng nhau nhặt nhạnh những mảnh ký ức đó, ghép lại thành một Hồi Ức Võ Lâm trọn vẹn hơn.

Chúc anh em chơi game vui vẻ!
