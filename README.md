# Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến

Gói tài liệu, cơ sở tri thức (Knowledge Base), hướng dẫn thực hành trên nền tảng **Coze (`coze.com` — gói Free bằng tài khoản Google)**, trang web tích hợp và báo cáo nhóm hoàn chỉnh cho đồ án/bài tập lớn môn học (ví dụ: *AI căn bản*).

- **Tên Chatbot chuẩn (Canonical Agent Name):** `Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến`
- **3 Chức năng cốt lõi:**
  1. **Nhận diện dấu hiệu lừa đảo trực tuyến:** Phân tích tin nhắn, cuộc gọi, đường link, tệp cài đặt (`.apk`), tài khoản mạng xã hội và kịch bản giao dịch dựa trên hệ thống phân loại chính thống tại Việt Nam.
  2. **Phòng tránh và xử lý khẩn cấp:** Hướng dẫn các bộ nguyên tắc phòng ngừa (*3 Không*, *4 Không - 2 Phải*, *5 Không - 5 Luôn*), bảo mật tài khoản/sinh trắc học đúng kênh và quy trình ứng phó khẩn cấp 4 bước khi nghi ngờ hoặc đã chuyển tiền/cài mã độc.
  3. **Hướng dẫn công cụ kiểm tra & kênh trình báo chính thống:** Hướng dẫn sử dụng chi tiết `tinnhiemmang.vn`, `chongluadao.vn`, `tracuutenmien.gov.vn`, ứng dụng `nTrust`, `canhbao.khonggianmang.vn`, `VNeID`, đầu số `156`/`5656`, `113` và kênh tiếp nhận của **Cục A05 — Bộ Công an** (tiếp nhận chức năng quản lý nhà nước về an toàn thông tin từ Cục An toàn thông tin từ ngày **01/03/2025**).

---

## 1. Cấu trúc thư mục gói sản phẩm

```text
anti_scam_chatbot/
├── README.md                                            # Tổng quan & kế hoạch triển khai 7 ngày
├── 01_Phan1_Chuan_Bi_Tai_Lieu/                          # Phần 1: Persona/Prompt & 3 tài liệu Knowledge Base
│   ├── Persona_Va_Prompt_Coze.md                        # Tài liệu giải thích vai trò, ràng buộc & bản Prompt đầy đủ
│   ├── Persona_Va_Prompt_Coze_Paste.txt                 # Văn bản thuần (plain text) dán trực tiếp vào Coze
│   ├── KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.docx        # Kiến thức 1: 24 hình thức + thủ đoạn 2024–2025 (DOCX)
│   ├── KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.pdf         # Kiến thức 1 (PDF sẵn sàng upload Coze)
│   ├── KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.docx# Kiến thức 2: Nguyên tắc phòng tránh & 4 bước khẩn cấp (DOCX)
│   ├── KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.pdf # Kiến thức 2 (PDF sẵn sàng upload Coze)
│   ├── KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.docx      # Kiến thức 3: Công cụ tra cứu & kênh trình báo VN (DOCX)
│   └── KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.pdf       # Kiến thức 3 (PDF sẵn sàng upload Coze)
├── 02_Phan2_3_Huong_Dan_Coze/                           # Phần 2 & 3: Hướng dẫn thao tác chi tiết trên coze.com
│   ├── Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md             # Hướng dẫn từng bước (Team Space -> Publish -> Chia sẻ)
│   └── Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.pdf            # Bản PDF dễ đọc / in ấn cho cả nhóm
├── 03_Website_Tich_Hop/                                 # Phần 3: Website tĩnh giới thiệu & nhúng Coze Chat SDK
│   ├── index.html                                       # Trang chủ tiếng Việt (có slot comment embed trực tiếp)
│   ├── styles.css                                       # Giao diện responsive, không phụ thuộc CDN ngoài
│   ├── coze-config.js                                   # File cấu hình bot_id, token (PAT), title để bật SDK
│   └── app.js                                           # Logic tương tác kiểm tra kịch bản & khởi tạo Coze Web SDK
├── 04_Bao_Cao_Nhom/                                     # Báo cáo nộp môn học hoàn chỉnh (Phần 1, 2, 3)
│   ├── Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.md         # Nguồn Markdown báo cáo
│   ├── Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.docx       # Bản Word để nhóm chèn ảnh chụp màn hình & điền tên thành viên
│   └── Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.pdf        # Bản PDF chuẩn học thuật
└── scripts/                                             # Script tự động tạo tài liệu và kiểm thử chất lượng
    ├── build_deliverables.py                            # Sinh lại toàn bộ file .docx và .pdf từ nội dung chuẩn
    └── verify_deliverables.py                           # Kiểm tra DOCX, trích xuất text PDF & kiểm thử web bằng Playwright
```

---

## 2. Hướng dẫn chạy nhanh (Quick Start)

### Bước 1: Chuẩn bị tài khoản & chạy thử Website tại máy cá nhân
1. Mở thư mục `01_Phan1_Chuan_Bi_Tai_Lieu/` để kiểm tra 3 tệp Knowledge Base (`.pdf` hoặc `.docx`) và tệp `Persona_Va_Prompt_Coze_Paste.txt`.
2. Mở thư mục `02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md` (hoặc `.pdf`) và thực hiện lần lượt từ **Bước 1 đến Bước 9** trên `https://www.coze.com`.
3. Chạy thử trang web tích hợp ở máy cá nhân bằng Python (không cần cài Node.js):
   ```powershell
   cd C:\Users\canhn\teamwork_projects\anti_scam_chatbot\03_Website_Tich_Hop
   python -m http.server 8080 --bind 127.0.0.1
   ```
   Sau đó mở trình duyệt tại `http://127.0.0.1:8080`.
4. Sau khi Publish bot phiên bản `1.0.0` lên **Chat SDK**, cập nhật `botId` và `token` (PAT) vào `03_Website_Tich_Hop/coze-config.js` (đặt `enabled: true`) để kích hoạt bong bóng chat Coze trực tiếp trên website.

### Bước 2: Chạy bộ kiểm tra tự động (nếu nhóm chỉnh sửa nội dung)
```powershell
python C:\Users\canhn\teamwork_projects\anti_scam_chatbot\scripts\build_deliverables.py
python C:\Users\canhn\teamwork_projects\anti_scam_chatbot\scripts\verify_deliverables.py
```

---

## 3. Kế hoạch triển khai nhóm trong 1 tuần (7 ngày)

Kế hoạch thiết kế cho nhóm **3–5 sinh viên** (phù hợp giới hạn ~5 thành viên cộng tác trên **Team Space** gói Free của Coze) và phù hợp hạn mức **10 Coze Credits/ngày** của gói Free:

| Ngày | Mục tiêu chính | Công việc chi tiết & Phân công gợi ý | Sản phẩm đầu ra / Nghiệm thu |
|---|---|---|---|
| **Ngày 1** | Khởi tạo Team Space & Rà soát Phần 1 | • Trưởng nhóm đăng nhập `coze.com` bằng Google, tạo **Team Space** (`+ New team`), mời tất cả thành viên và nâng quyền lên **Administrator**.<br>• Cả nhóm đọc rà soát `Persona_Va_Prompt_Coze_Paste.txt` và 3 file `KB1`, `KB2`, `KB3`. | Team Space đã đủ thành viên với quyền `Administrator`; chụp ảnh màn hình minh chứng phân quyền. |
| **Ngày 2** | Tạo Agent & Tối ưu Persona/Prompt | • Thực hiện `Development -> + Create -> Create agent` với tên chuẩn `Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến`.<br>• Dán `Persona_Va_Prompt_Coze_Paste.txt` vào `Persona & Prompt`, bấm **`Optimize`** (Auto-Optimize Prompt), rà soát giữ nguyên ranh giới an toàn & quy tắc chọn công cụ. | Agent hoàn thiện Persona & Prompt; chụp ảnh trước/sau khi nhấn `Optimize`. |
| **Ngày 3** | Nạp Knowledge Base & Thêm Plugins | • Vào `Skills -> Knowledge -> Text`, upload `KB1`, `KB2`, `KB3` (PDF), chọn `Automatic Segmentation` & `Automatic Recall`.<br>• Thêm plugin **`Google Web Search`** (hoặc `Bing Web Search` dự phòng) và plugin tạo ảnh (**`DALLE 3`** — lưu ý 10 credits/lần, có thể thêm `Stable Diffusion` 1 credit/lần để dự phòng). | KB đã chuyển trạng thái hoàn tất index; Plugins hiển thị trong `Skills`; chọn mô hình `Gemini 1.5 Flash` (0.25 credits/lần) để tiết kiệm credit khi test. |
| **Ngày 4** | Kiểm thử Q&A & Web Search trên `Preview & Debug` | • Chạy **5 test prompt Knowledge Base Q&A** + **3 test prompt Google Search** từ `Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md`.<br>• Mở khung **Trace/Process** kiểm tra bot có truy xuất đúng KB hoặc gọi Google Search không; tinh chỉnh prompt nếu cần. | Ghi kết quả thực tế vào bảng kiểm thử; chụp ảnh Trace KB retrieval và Google Search. |
| **Ngày 5** | Kiểm thử tạo ảnh & Xuất bản v1.0.0 | • Chạy **2 test prompt tạo ảnh** (lưu ý `DALLE 3` tiêu tốn 10 credits/lần — thực hiện đầu ngày khi credit vừa reset hoặc dùng `Stable Diffusion`).<br>• Bấm **`Publish`** phát hành bản `1.0.0` kèm Changelog tiếng Việt; kích hoạt kênh **`Chat SDK`** (và **`Messenger`** nếu nhóm có Fanpage test). | Bot xuất bản thành công bản `1.0.0`; lấy được `bot_id`, URL Chat SDK và PAT tại `coze.com/open/oauth/pats`. |
| **Ngày 6** | Tích hợp Website & Kiểm tra chéo | • Điền `botId`, `token` vào `03_Website_Tich_Hop/coze-config.js` (`enabled: true`).<br>• Chạy web local qua `python -m http.server`, test chat thực tế trên giao diện web; thành viên khác kiểm tra thử khả năng cùng chỉnh sửa prompt/KB trên Team Space. | Video/ảnh chụp website hiển thị nút chat Coze hoạt động ổn định; xác nhận 100% thành viên sửa được bot. |
| **Ngày 7** | Hoàn thiện Báo cáo & Tổng duyệt nộp bài | • Mở `04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.docx`, điền thông tin nhóm, chèn ảnh chụp màn hình, `bot_id`, link & kết quả chạy 10 test prompts vào các vị trí `[CHÈN ...]` đã đánh dấu.<br>• Xuất lại PDF và kiểm tra chéo 4 tiêu chí trước khi nộp. | Báo cáo nhóm hoàn chỉnh (`.docx` & `.pdf`) + slide/demo sẵn sàng trình bày. |

> **Lưu ý bảo mật khi nộp bài:** Tuyệt đối **không** đẩy file `coze-config.js` chứa Personal Access Token (PAT) thật lên GitHub/repository công khai. Khi demo trực tiếp hoặc nộp mã nguồn tĩnh, hãy thu hồi PAT cũ hoặc đổi `token` về giá trị giữ chỗ sau khi quay video/chụp ảnh minh chứng.
