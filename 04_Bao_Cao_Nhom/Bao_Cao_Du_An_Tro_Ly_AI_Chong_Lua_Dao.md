# BÁO CÁO ĐỒ ÁN MÔN HỌC

**ĐỀ TÀI:** XÂY DỰNG VÀ TÍCH HỢP **"TRỢ LÝ AI HỖ TRỢ NHẬN DIỆN VÀ PHÒNG TRÁNH LỪA ĐẢO TRỰC TUYẾN"** TRÊN NỀN TẢNG COZE

---

## THÔNG TIN NHÓM THỰC HIỆN

- **Môn học:** `[ĐIỀN TÊN MÔN HỌC — Ví dụ: Trí tuệ nhân tạo căn bản]`
- **Giảng viên hướng dẫn:** `[ĐIỀN HỌ TÊN GIẢNG VIÊN]`
- **Lớp / Học kỳ:** `[ĐIỀN LỚP / HỌC KỲ — NĂM HỌC]`
- **Danh sách thành viên nhóm:**

| STT | Họ và tên | Mã số sinh viên | Vai trò & Công việc phụ trách |
|---|---|---|---|
| 1 | `[Điền họ tên Thành viên 1]` | `[MSSV]` | Nhóm trưởng: Tạo Team Space, phân quyền Administrator, tổng hợp Phần 1 & 2 |
| 2 | `[Điền họ tên Thành viên 2]` | `[MSSV]` | Biên soạn & kiểm chuẩn dữ liệu Knowledge Base (`KB1`, `KB2`, `KB3`) |
| 3 | `[Điền họ tên Thành viên 3]` | `[MSSV]` | Thiết lập Persona/Prompt, Plugins và chạy kiểm thử 10 kịch bản trên Coze |
| 4 | `[Điền họ tên Thành viên 4]` | `[MSSV]` | Tích hợp Web SDK lên trang web (`03_Website_Tich_Hop`), hoàn thiện Báo cáo |

---

## MỤC LỤC TÓM TẮT

1. **Giới thiệu đề tài & Mục tiêu dự án**
2. **Phần 1: Chuẩn bị tài liệu, thiết kế Persona & Prompt và xây dựng Knowledge Base**
3. **Phần 2: Thiết lập Chatbot trên Coze, cấu hình Knowledge Base, Plugins và Kiểm thử**
4. **Phần 3: Xuất bản phiên bản 1.0.0, Tích hợp Website / Messenger và Phân quyền chỉnh sửa nhóm**
5. **Kết luận & Hướng phát triển**
6. **Tài liệu tham khảo**

---

## 1. GIỚI THIỆU ĐỀ TÀI & MỤC TIÊU DỰ ÁN

### 1.1. Lý do chọn đề tài
Tại Việt Nam, cùng với sự phát triển mạnh mẽ của thanh toán số, dịch vụ công trực tuyến (VNeID) và mạng xã hội, các thủ đoạn lừa đảo trực tuyến ngày càng gia tăng về tần suất và mức độ tinh vi. Bên cạnh 24 hình thức lừa đảo phổ biến đã được cơ quan chức năng tổng hợp, giai đoạn 2024–2025 xuất hiện hàng loạt biến thể mới như giả mạo nhân viên ngân hàng hỗ trợ cập nhật sinh trắc học theo **Quyết định 2345/QĐ-NHNN**, giả mạo cán bộ Công an/Thuế dụ cài đặt tệp `.apk` chứa mã độc mang tên `VNeID` hoặc `Dịch vụ công`, hay lừa đảo bằng cuộc gọi video **Deepfake / Deepvoice**. Người dân — đặc biệt là sinh viên và người cao tuổi — thường thiếu một kênh hỏi đáp tức thời, bình tĩnh và đáng tin cậy để kiểm tra dấu hiệu nghi vấn trước khi bấm link hoặc chuyển tiền.

Từ thực tiễn đó, nhóm lựa chọn xây dựng chatbot mang tên chuẩn **"Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"** trên nền tảng **Coze (`coze.com` — gói miễn phí)** kết hợp cơ sở tri thức tiếng Việt chuẩn hóa từ nguồn chính thống và tích hợp lên website giới thiệu riêng.

### 1.2. Mục tiêu và 3 chức năng cốt lõi của Chatbot
Trợ lý AI được thiết kế xoay quanh **3 chức năng cốt lõi**:
1. **Nhận diện dấu hiệu lừa đảo trực tuyến:** Phân tích tin nhắn, cuộc gọi, đường link, tệp cài đặt (`.apk`) và kịch bản giao dịch; đối chiếu với hệ thống phân loại lừa đảo tại Việt Nam để chỉ ra điểm bất thường và mức độ rủi ro.
2. **Phòng tránh và xử lý khẩn cấp:** Hướng dẫn các bộ nguyên tắc phòng ngừa chính thống (*3 Không*, *4 Không - 2 Phải*, *5 Không - 5 Luôn*), bảo mật 2FA/sinh trắc học đúng kênh và quy trình ứng phó khẩn cấp 4 bước khi đã lỡ chuyển tiền hoặc cài mã độc.
3. **Hướng dẫn công cụ kiểm tra và kênh trình báo chính thống:** Chỉ dẫn từng bước tra cứu qua `tinnhiemmang.vn`, `chongluadao.vn`, `tracuutenmien.gov.vn`, ứng dụng `nTrust`, `canhbao.khonggianmang.vn`, và liên hệ đúng kênh tiếp nhận (`156`, `5656`, `113`, `VNeID`, **Cục A05 — Bộ Công an**, email `tiepnhantogiactoipham@mps.gov.vn`).

### 1.3. Tổng hợp các tệp sản phẩm trong dự án

| Phần | Tên tệp sản phẩm trong dự án | Vai trò |
|---|---|---|
| Tổng quan | `README.md` | Tổng quan gói sản phẩm, sơ đồ thư mục và kế hoạch triển khai nhóm 7 ngày |
| Phần 1 | `01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze.md` & `Persona_Va_Prompt_Coze_Paste.txt` | Mô tả thiết kế và bản văn bản thuần dán trực tiếp vào `Persona & Prompt` trên Coze |
| Phần 1 | `01_Phan1_Chuan_Bi_Tai_Lieu/KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.docx` & `.pdf` | Tri thức 1: 3 nhóm — 24 hình thức lừa đảo (Cục ATTT) + biến thể 2024–2025 |
| Phần 1 | `01_Phan1_Chuan_Bi_Tai_Lieu/KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.docx` & `.pdf` | Tri thức 2: Nguyên tắc phòng ngừa, bảo mật & Quy trình khẩn cấp 4 bước |
| Phần 1 | `01_Phan1_Chuan_Bi_Tai_Lieu/KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.docx` & `.pdf` | Tri thức 3: Danh bạ cơ quan sau chuyển giao 01/03/2025 & hướng dẫn công cụ tra cứu |
| Phần 2 & 3 | `02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md` & `.pdf` | Tài liệu hướng dẫn thực hành đầy đủ 9 bước trên Coze và bộ 10 test prompts |
| Phần 3 | `03_Website_Tich_Hop/index.html`, `styles.css`, `coze-config.js`, `app.js` | Website tiếng Việt giới thiệu dự án và tích hợp Coze Web SDK |
| Phần 4 | `04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.md`, `.docx`, `.pdf` | Báo cáo nhóm hoàn chỉnh phục vụ nộp bài và thuyết trình |

---

## 2. PHẦN 1: CHUẨN BỊ TÀI LIỆU, THIẾT KẾ PERSONA & PROMPT VÀ XÂY DỰNG KNOWLEDGE BASE

### 2.1. Thiết kế Persona & Prompt (`Persona_Va_Prompt_Coze.md`)
Để đảm bảo chatbot trả lời chính xác, an toàn và biết lựa chọn đúng công cụ khi vận hành trên Coze, nhóm thiết kế tệp `01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze_Paste.txt` với 6 khối quy định chặt chẽ:
1. **Vai trò & Đối tượng phục vụ:** Định danh rõ tên chatbot *"Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"*, phục vụ người dân phổ thông, học sinh/sinh viên, người cao tuổi và người giao dịch trực tuyến tại Việt Nam.
2. **Ba chức năng cốt lõi:** Gắn chặt 3 nhóm nhiệm vụ nhận diện — phòng tránh/xử lý khẩn cấp — hướng dẫn công cụ/trình báo.
3. **Giọng điệu giao tiếp:** Bình tĩnh, khách quan, chia bước ngắn gọn dễ hiểu, tuyệt đối **không phán xét hay đổ lỗi** cho người dùng khi họ lỡ chuyển tiền hoặc bấm link lạ.
4. **Quy tắc định tuyến công cụ (Tool Routing):**
   - Ưu tiên tra cứu **Knowledge Base** trước đối với mọi câu hỏi về thủ đoạn, quy tắc phòng tránh, quy trình 4 bước và danh bạ công cụ/đầu số Việt Nam.
   - Chỉ gọi plugin **`Google Web Search`** khi người dùng hỏi tin tức/cảnh báo mới phát sinh (năm 2025–2026) hoặc cần kiểm chứng thông tin thời sự, và phải trích dẫn nguồn chính thống.
   - Chỉ gọi plugin tạo ảnh (**`DALLE 3`** / **`Stable Diffusion`**) khi người dùng chủ động yêu cầu vẽ poster/infographic tuyên truyền.
5. **Quy trình phản hồi chuẩn:** Phân biệt rõ cấu trúc trả lời cho tình huống nghi ngờ (Mức độ rủi ro -> Dấu hiệu bất thường -> Hành động ngay -> Công cụ kiểm tra) và tình huống khẩn cấp (đưa ngay 4 bước xử lý lên đầu).
6. **Ranh giới an toàn nghiêm ngặt:** Tuyệt đối không yêu cầu người dùng nhập mã OTP, mật khẩu, mã PIN, số thẻ/CVV hay ảnh/số CCCD thật vào khung chat; khẳng định rõ chatbot chỉ hỗ trợ tham khảo ban đầu, không thay thế Cơ quan Công an hay tư vấn pháp lý chính thức.

### 2.2. Xây dựng 3 tài liệu Knowledge Base tiếng Việt chuẩn hóa
Toàn bộ tri thức được nhóm nghiên cứu, đối chiếu từ các nguồn chính thống của Việt Nam và biên soạn thành 3 tệp độc lập (đều có bản `.docx` và `.pdf` sạch Unicode, trình bày cấu trúc đề mục và bảng biểu rõ ràng để Coze phân đoạn chính xác):

1. **`KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.pdf` (`.docx`):**
   - Trình bày đầy đủ **3 nhóm — 24 hình thức lừa đảo trực tuyến** theo *Cẩm nang nhận diện và phòng chống lừa đảo trực tuyến* (Cục An toàn thông tin, 06/2023): Nhóm 1 — Giả mạo thương hiệu (7 hình thức); Nhóm 2 — Chiếm đoạt tài khoản (5 hình thức); Nhóm 3 — Các hình thức kết hợp khác (12 hình thức, gồm Deepfake, giả danh Công an/VKS/Tòa án, CTV online, đầu tư tài chính/crypto, bẫy tình cảm...).
   - Bổ sung nhóm thủ đoạn bùng phát giai đoạn **2024–2025**: Lợi dụng **Quyết định 2345/QĐ-NHNN** (hiệu lực 01/07/2024) để lừa hỗ trợ sinh trắc học; giả danh Công an/Thuế/UBND gửi file **`.apk`** giả mạo `VNeID` hoặc `Dịch vụ công` chiếm quyền Trợ năng (Accessibility); và lừa đảo tuyển dụng/xuất khẩu lao động (XKLĐ).
   - Tổng hợp 4 nhóm dấu hiệu nhận biết chung (tạo khẩn cấp/sợ hãi/tham lam; giả mạo cơ quan chức năng qua điện thoại/Zalo; tên miền sai chính tả/đuôi lạ/link rút gọn; đòi OTP/mật khẩu/cấp quyền ứng dụng lạ).

2. **`KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.pdf` (`.docx`):**
   - Hệ thống hóa đầy đủ 3 bộ nguyên tắc phòng ngừa chính thống đang được Bộ Công an và Công an các địa phương tuyên truyền: **"3 Không"**, **"4 Không - 2 Phải"**, và **"5 Không - 5 Luôn"**.
   - Hướng dẫn thực hành bảo mật cá nhân: mật khẩu mạnh, xác thực 2 yếu tố (2FA) bằng ứng dụng tạo mã, quy tắc cập nhật sinh trắc học **chỉ qua app ngân hàng chính thức hoặc tại quầy giao dịch**, cách đọc tên miền gốc và hiểu đúng về biểu tượng ổ khóa HTTPS.
   - Quy trình **ứng phó khẩn cấp 4 bước** khi nghi ngờ hoặc đã sập bẫy: *Bước 1: Ngắt mạng & dừng giao dịch (gỡ app `.apk` lạ)* -> *Bước 2: Gọi hotline chính thức ngân hàng khóa thẻ/tài khoản & đổi mật khẩu* -> *Bước 3: Thu thập, chụp màn hình bảo toàn bằng chứng* -> *Bước 4: Trình báo Công an địa phương/PA05/VNeID/`156`*, kèm cảnh báo dứt khoát **tránh bẫy lừa đảo lần 2 từ các dịch vụ "lấy lại tiền bị lừa"**.

3. **`KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.pdf` (`.docx`):**
   - Cập nhật **bối cảnh thể chế mới nhất tại Việt Nam**: Ngày **28/02/2025**, Bộ Công an và Bộ TT&TT đã ký kết bàn giao nhiệm vụ quản lý nhà nước về an toàn thông tin mạng; từ **01/03/2025**, Cục An toàn thông tin chấm dứt hoạt động và chuyển giao nhiệm vụ về **Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) — Bộ Công an**.
   - Danh bạ kênh trình báo chính thức: Tổng đài/SMS miễn phí **`156`** và **`5656`** (kèm các cú pháp `LD`, `V`, `S`, `TCTM`), khẩn cấp **`113`**, đường dây nóng **`069.219.4053`**, Cục CSHS **`0692.345.860`**, ứng dụng **VNeID** (mục Kiến nghị, phản ánh về ANTT), hộp thư **`tiepnhantogiactoipham@mps.gov.vn`**, và Công an xã/phường/PA05 địa phương.
   - Hướng dẫn thao tác từng bước các công cụ kiểm tra chính thống: **`tinnhiemmang.vn`** (tra cứu website lừa đảo & STK ngân hàng), **`chongluadao.vn`** (phân tích link, extension trình duyệt, Zalo OA *Chống Lừa Đảo*), **`tracuutenmien.gov.vn`** (VNNIC), ứng dụng **`nTrust`** của Hiệp hội An ninh mạng Quốc gia (NCA, ra mắt 30/07/2024), cổng **`canhbao.khonggianmang.vn`**, **`dauhieuluadao.com`** và lưu ý giới hạn khi tham khảo các trang cộng đồng như `scam.vn`/`checkscam.vn`.

---

## 3. PHẦN 2: THIẾT LẬP CHATBOT TRÊN COZE, KNOWLEDGE BASE, PLUGINS & KIỂM THỬ

Toàn bộ quy trình thao tác chi tiết được nhóm chuẩn hóa trong tài liệu `02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md` (`.pdf`). Dưới đây là kết quả triển khai thực tế của nhóm trên `https://www.coze.com`:

### 3.1. Tạo Team Space & Khởi tạo Agent
- Nhóm đăng nhập `coze.com` bằng tài khoản Google (gói **Free Plan** — hạn mức **10 Coze Credits/ngày**).
- Tạo **Team Space** (`+ New team`) thay vì dùng *Personal Workspace* để đảm bảo cả nhóm có thể cùng cộng tác và chỉnh sửa trên một không gian chung.
- Thực hiện `Development -> + Create -> Create agent` với:
  - **Agent Name:** `Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến`
  - **Agent Function Description:** Đúng như mô tả đã chuẩn bị ở Phần 1.
- `[CHÈN ẢNH CHỤP MÀN HÌNH 1: Giao diện tạo Team Space và hộp thoại Create Agent trên coze.com]`

### 3.2. Dán `Persona & Prompt` và Tối ưu bằng `Optimize` (Auto-Optimize Prompt)
- Nhóm dán toàn bộ nội dung từ `01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze_Paste.txt` vào khung **`Persona & Prompt`**.
- Bấm nút **`Optimize`** để Coze tự động tái cấu trúc prompt, sau đó rà soát lại để giữ nguyên tên trợ lý, 3 chức năng cốt lõi, quy tắc định tuyến công cụ và ranh giới không thu thập OTP/mật khẩu/CCCD.
- Chọn mô hình LLM tiết kiệm credit (`Gemini 1.5 Flash` — 0,25 credits/lượt hoặc `GPT-4o-mini` — 1 credit/lượt) cho giai đoạn kiểm thử.
- `[CHÈN ẢNH CHỤP MÀN HÌNH 2: Khung Persona & Prompt sau khi nhấn nút Optimize trên Coze]`

### 3.3. Tích hợp Knowledge Base (`Skills -> Knowledge -> Text`)
- Trong cột giữa `Skills`, nhóm tạo Knowledge Base dạng **`Text`** và tải lên 3 tệp PDF: `KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.pdf`, `KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.pdf`, và `KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.pdf`.
- Lựa chọn chiến lược phân đoạn **`Automatic Segmentation`** và chế độ truy xuất **`Automatic Recall`** để bot tự động đối chiếu tri thức nội bộ trên mọi câu hỏi của người dùng.
- `[CHÈN ẢNH CHỤP MÀN HÌNH 3: Danh sách 3 tài liệu KB1, KB2, KB3 ở trạng thái Completed trong Knowledge Base]`

### 3.4. Cấu hình Plugins (`Google Web Search` & Image Generation)
- Trong `Skills -> Plugins`, nhóm nhấn `+` để tìm và thêm:
  1. **`Google Web Search`** (hoặc `Bing Web Search` làm phương án dự phòng) để tra cứu các cảnh báo lừa đảo mới nhất năm 2025–2026 và tin tức chuyển giao cơ quan quản lý an toàn mạng.
  2. **`DALLE 3`** để tạo poster/hình minh họa tuyên truyền phòng chống lừa đảo (nhóm lưu ý rõ trong hướng dẫn rằng `DALLE 3` tiêu tốn **10 credits/lần gọi** trên gói Free nên nhóm lên kế hoạch test đầu ngày và tích hợp thêm **`Stable Diffusion`** — 1 credit/lần làm lựa chọn dự phòng).
- `[CHÈN ẢNH CHỤP MÀN HÌNH 4: Cột Skills hiển thị Knowledge Base và các Plugins đã thêm thành công]`

### 3.5. Kết quả Kiểm thử trên `Preview & Debug` (Bộ 10 Test Prompts Tiếng Việt)
Nhóm thực hiện kiểm thử trực tiếp trên khung **`Preview & Debug`** với đầy đủ **10 kịch bản kiểm thử tiếng Việt** (vượt mức tối thiểu 8 kịch bản), kết hợp mở hộp kiểm tra **Process / Trace** để xác minh đúng công cụ được gọi:

| Mã | Nhóm kiểm thử | Nội dung Test Prompt tóm tắt | Công cụ ghi nhận trên Trace | Kết quả thực tế của nhóm |
|---|---|---|---|---|
| **T1** | KB Q&A | Cuộc gọi giả danh Công an gửi lệnh bắt qua Zalo, đòi chuyển tiền chứng minh vô tội | Knowledge Base (`KB1`, `KB2`, `KB3`) | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T2** | KB Q&A | Giả mạo ngân hàng cập nhật sinh trắc học QĐ 2345, lỡ tải file `.apk` trên Android | Knowledge Base (`KB1`, `KB2`) | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T3** | KB Q&A | Mất tiền mua combo du lịch, hỏi có nên thuê dịch vụ "lấy lại tiền bị lừa" | Knowledge Base (`KB1`, `KB2`, `KB3`) | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T4** | KB Q&A | Giải thích quy tắc "3 Không" và "4 Không - 2 Phải" cho ông bà lớn tuổi | Knowledge Base (`KB2`) | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T5** | KB Q&A | Cách tự kiểm tra link website và STK ngân hàng trước khi chuyển tiền | Knowledge Base (`KB3`) | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T6** | Web Search | Tra cứu việc chuyển giao nhiệm vụ ATTT từ Cục ATTT sang Bộ Công an (2025) | `Google Web Search` | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T7** | Web Search | Tìm các cảnh báo lừa đảo mới gần đây tại Việt Nam (thuế, phạt nguội, Deepfake) | `Google Web Search` | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T8** | Web Search | Xác minh tên miền cổng dịch vụ công / VNeID chính thức vs tên miền `.vip` lạ | `Google Web Search` | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T9** | Image Gen | Tạo poster hiện đại hình chiếc khiên bảo vệ điện thoại, tuyên truyền an toàn số | `DALLE 3` / `Stable Diffusion` | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |
| **T10** | Image Gen | Vẽ hình minh họa cảnh báo người lớn tuổi trước cuộc gọi và link giả mạo | `DALLE 3` / `Stable Diffusion` | `[Đạt / Ghi chú thực tế sau khi chạy trên Coze]` |

- `[CHÈN BẢNG / ẢNH CHỤP MÀN HÌNH 5: Kết quả chạy thực tế các câu hỏi Knowledge Base + Trace truy xuất KB]`
- `[CHÈN ẢNH CHỤP MÀN HÌNH 6: Kết quả chạy Google Web Search và ảnh minh họa tạo thành công từ DALLE 3 / Stable Diffusion]`

---

## 4. PHẦN 3: XUẤT BẢN PHIÊN BẢN `1.0.0`, TÍCH HỢP WEBSITE / MESSENGER VÀ PHÂN QUYỀN CHỈNH SỬA NHÓM

### 4.1. Xuất bản phiên bản `1.0.0` (`Publish`)
- Nhóm nhấn **`Publish`**, đặt số phiên bản **`1.0.0`**, điền Changelog tiếng Việt mô tả các thành phần hoàn thiện (Persona/Prompt, 3 file Knowledge Base, Google Web Search & Image Generation, 10 test cases) và chọn kênh phát hành **`Chat SDK`** (và **`Messenger`** nếu triển khai Fanpage).
- Thông tin bot sau khi xuất bản:
  - **Bot ID:** `[CHÈN BOT_ID SAU KHI PUBLISH — lấy từ URL https://www.coze.com/space/<space_id>/bot/<bot_id>]`
  - **Link Coze (nếu có chia sẻ):** `[CHÈN LINK / MÃ NHÚNG CHAT SDK SAU KHI PUBLISH]`
- `[CHÈN ẢNH CHỤP MÀN HÌNH 7: Giao diện Publish phiên bản 1.0.0 và tab Chat SDK -> Installation]`

### 4.2. Tích hợp lên Website giới thiệu (`03_Website_Tich_Hop/`)
Nhóm thiết kế một trang web tĩnh hoàn chỉnh bằng HTML5, CSS3 và JavaScript thuần (`03_Website_Tich_Hop/index.html`, `styles.css`, `coze-config.js`, `app.js`), không phụ thuộc thư viện hay font CDN ngoài để đảm bảo hiển thị tiếng Việt ổn định trên cả máy tính và điện thoại.

Trang web cung cấp các khối chức năng trực quan cho người dùng cuối:
- Giới thiệu mục tiêu và 3 chức năng cốt lõi của **"Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"**.
- Bộ công cụ tương tác nhanh **Kiểm tra kịch bản nghi ngờ** (mô phỏng các tình huống phổ biến như giả danh Công an, file `.apk` sinh trắc học/VNeID, CTV online, combo du lịch giá rẻ) giúp người dùng nhận diện nhanh trước khi chat sâu với AI.
- Bảng **Quy trình xử lý khẩn cấp 4 bước** và danh mục **Công cụ kiểm tra & Kênh trình báo chính thống** (`156`, `5656`, `113`, `VNeID`, `tinnhiemmang.vn`, `chongluadao.vn`, `tracuutenmien.gov.vn`, `nTrust`).
- Khối **Tích hợp Coze Chat SDK** tách riêng cấu hình tại `03_Website_Tich_Hop/coze-config.js` (`window.COZE_CHATBOT_CONFIG`): người quản trị chỉ cần thay `botId`, `token` (PAT tạo tại `coze.com/open/oauth/pats`) và đặt `enabled: true` là `app.js` tự động nạp `CozeWebSDK.WebChatClient` và hiển thị cửa sổ chat ngay trên trang web. Khi chưa điền token (`enabled: false`), trang web vẫn vận hành sạch sẽ không lỗi console để phục vụ kiểm thử giao diện.
- **Ghi chú bảo mật:** Nhóm tuân thủ nguyên tắc không công khai Personal Access Token (PAT) lên kho mã nguồn công cộng; khi chạy chấm điểm trực tiếp tại lớp mới bật cấu hình cục bộ trên localhost.
- `[CHÈN ẢNH CHỤP MÀN HÌNH 8: Giao diện Website tích hợp hiển thị bong bóng chat Trợ lý AI hoạt động thực tế]`

### 4.3. Phương án tích hợp mở rộng lên Facebook Messenger
Trong tài liệu hướng dẫn (`02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md`), nhóm cũng đã trình bày đầy đủ quy trình kết nối **Facebook Fanpage** thông qua **Meta for Developers** (sản phẩm *Messenger*, Webhook Callback URL `https://api.coze.com/adapter/messenger/webhook`, Verify Token `coze`, Page Access Token) và kích hoạt kênh **`Messenger`** trong mục *Publish to social platforms* trên Coze.
- `[CHÈN ẢNH CHỤP MÀN HÌNH 9 (Tùy chọn nếu nhóm triển khai Messenger): Cấu hình Webhook trên Meta và chat thử qua Fanpage]`

### 4.4. Cấu hình chia sẻ quyền chỉnh sửa cho toàn bộ thành viên nhóm
Để đáp ứng yêu cầu mọi thành viên trong nhóm đều cùng chỉnh sửa được chatbot:
1. Nhóm sử dụng **Team Space** (không dùng Personal Workspace).
2. Nhóm trưởng truy cập **`Space Configuration > Members`**, mời toàn bộ thành viên qua `+ Add member` (hoặc Space Sharing Link có hiệu lực 7 ngày).
3. Nhóm trưởng chủ động chuyển vai trò (**Role**) của từng thành viên từ **`Member`** lên **`Administrator`**. Nhờ vậy, tất cả thành viên đều có quyền chỉnh sửa `Persona & Prompt`, cập nhật `Knowledge Base`, quản lý `Plugins` và `Publish` phiên bản mới.
4. Nhóm phân biệt rõ trong tài liệu: đường link từ **Coze Store — Private Configuration** chỉ cho phép người ngoài *chat thử*, còn **Public Configuration** chỉ cho phép *Duplicate* thành bản sao riêng (không sửa được bot gốc và bị hạn chế nếu dùng Knowledge Base riêng tư).
- `[CHÈN ẢNH CHỤP MÀN HÌNH 10: Danh sách thành viên trong Space Configuration > Members với vai trò Administrator]`

---

## 5. KẾT LUẬN & HƯỚNG PHÁT TRIỂN

### 5.1. Kết luận
Sau quá trình triển khai theo kế hoạch 7 ngày, nhóm đã xây dựng hoàn chỉnh hệ thống sản phẩm gồm: bộ Persona & Prompt tiếng Việt chuẩn hóa, 3 tài liệu Knowledge Base bám sát thực tiễn Việt Nam (cập nhật cả giai đoạn chuyển giao sang Cục A05 — Bộ Công an từ 01/03/2025 và các thủ đoạn 2024–2025), tài liệu hướng dẫn thực hành Coze 9 bước kèm 10 test cases, trang web tích hợp Coze Web SDK và báo cáo nhóm hoàn chỉnh. Giải pháp chứng minh nền tảng Coze gói miễn phí hoàn toàn khả thi để sinh viên xây dựng các trợ lý AI phục vụ cộng đồng có tính thực tiễn cao.

### 5.2. Hạn chế và hướng phát triển
- **Hạn mức gói miễn phí:** Gói Coze Free giới hạn 10 credits/ngày (đặc biệt `DALLE 3` tốn 10 credits/lần) và 100 lượt Web SDK miễn phí ban đầu; trong tương lai nếu triển khai diện rộng cho người dân cần nâng cấp gói trả phí hoặc kết nối máy chủ backend cấp phát OAuth JWT để bảo mật token.
- **Mở rộng đa kênh & dữ liệu thời gian thực:** Tích hợp thêm Zalo OA (thông qua API trung gian), tự động cập nhật nguồn RSS/cảnh báo từ `canhbao.khonggianmang.vn` và bổ sung tính năng kiểm tra ảnh chụp màn hình tin nhắn trực tiếp bằng mô hình đa phương thức (Multimodal Vision).

---

## 6. TÀI LIỆU THAM KHẢO

1. **Cục An toàn thông tin (Bộ TT&TT)** (06/2023), *Cẩm nang nhận diện và phòng chống lừa đảo trực tuyến* (3 nhóm — 24 hình thức lừa đảo trực tuyến), Cổng Không gian mạng quốc gia `https://khonggianmang.vn`.
2. **Cổng Thông tin điện tử Chính phủ (`baochinhphu.vn` / `chinhphu.vn`) & Bộ Công an (`bocongan.gov.vn`)** (28/02/2025 – 01/03/2025), Thông tin bàn giao nhiệm vụ quản lý nhà nước về an toàn thông tin mạng từ Bộ TT&TT (Cục ATTT) sang **Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) — Bộ Công an** và Nghị định `02/2025/NĐ-CP`.
3. **Ngân hàng Nhà nước Việt Nam** (hiệu lực 01/07/2024), *Quyết định số 2345/QĐ-NHNN* về triển khai các giải pháp an toàn, bảo mật trong thanh toán trực tuyến và thanh toán thẻ ngân hàng; cùng các khuyến cáo phòng chống giả mạo sinh trắc học trên `https://bocongan.gov.vn`.
4. **Báo Điện tử Chính phủ (`baochinhphu.vn`)** (01/11/2022 & 03/03/2023), *Triển khai đầu số 156 tiếp nhận phản ánh cuộc gọi rác, cuộc gọi có dấu hiệu lừa đảo* và *Tra cứu thông tin tên miền qua đầu số 156 (`TCTM` / `https://tracuutenmien.gov.vn`)*.
5. **Hiệp hội An ninh mạng Quốc gia (NCA) & Báo Nhân Dân** (30/07/2024), *Ra mắt ứng dụng phòng chống lừa đảo nTrust*, `https://nca.org.vn` và `https://ntrust.vn`.
6. **Hệ sinh thái Tín nhiệm mạng & Cảnh báo an toàn thông tin Việt Nam**, `https://tinnhiemmang.vn/website-lua-dao`, `https://tinnhiemmang.vn/tra-cuu-tai-khoan`, `https://canhbao.khonggianmang.vn`, và cổng kiến thức NCSC–Google `https://dauhieuluadao.com` (ra mắt 01/04/2022).
7. **Dự án Chống Lừa Đảo (ChongLuaDao)**, Công cụ phân tích liên kết & tiện ích trình duyệt, `https://chongluadao.vn` (`chongluadao.vn/analyze`).
8. **Coze Platform Documentation (`coze.com/docs`)**, Tài liệu hướng dẫn về *Team Space & Role Permissions*, *Knowledge Base*, *Plugins*, *Web SDK (`CozeWebSDK.WebChatClient`)* và *Messenger Integration*.
