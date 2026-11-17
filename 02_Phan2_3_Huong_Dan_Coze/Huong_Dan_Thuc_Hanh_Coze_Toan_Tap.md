# Hướng Dẫn Thực Hành Coze Toàn Tập (Phần 2 & Phần 3)

**Dự án:** Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến  
**Nền tảng:** `https://www.coze.com` (Phiên bản quốc tế — gói **Free Plan** đăng nhập bằng tài khoản Google)  
**Phạm vi tài liệu:** Hướng dẫn đầy đủ từ khởi tạo Team Space, tạo Agent, nạp Knowledge Base (`KB1`–`KB3`), cấu hình Plugins, kiểm thử trên `Preview & Debug` (10 test prompts tiếng Việt), xuất bản phiên bản `1.0.0`, tích hợp lên Website & Facebook Messenger, đến chia sẻ quyền **chỉnh sửa chung cho toàn bộ thành viên nhóm**.

---

## Tổng quan tài nguyên gói Coze Free cần lưu ý trước khi bắt đầu

1. **Hạn mức Coze Credits miễn phí:** Mỗi tài khoản Free được cấp **10 Coze Credits/ngày** (làm mới hằng ngày).
   - Chi phí mô hình gợi ý khi test: `Gemini 1.5 Flash` (**0,25 credits/lượt**), `GPT-4o-mini` (**1 credit/lượt**), `GPT-4o` (2–5 credits/lượt).
   - **Lưu ý cực kỳ quan trọng về Plugin tạo ảnh:** **`DALLE 3` tiêu tốn 10 credits/lần gọi** — tức chỉ 1 lần tạo ảnh bằng `DALLE 3` sẽ dùng hết hạn mức 10 credits/ngày của gói Free! Trong khi đó **`Stable Diffusion` chỉ tốn 1 credit/lần** và `Leonardo` tốn 2,5 credits/lần.
   - **Chiến lược tiết kiệm cho nhóm:** Chọn mô hình **`Gemini 1.5 Flash`** (hoặc `GPT-4o-mini`) để chạy toàn bộ bài test hỏi đáp KB và Google Search; thực hiện test `DALLE 3` vào đầu ngày mới (hoặc dùng `Stable Diffusion` làm phương án dự phòng nếu đã dùng hết credit trong ngày).
2. **Hạn mức Web SDK & API miễn phí:** Coze cung cấp hạn mức miễn phí ban đầu **100 lượt gọi Web SDK (Chat SDK)** và **30 lượt gọi API** trước khi cần nạp Coze Tokens.
3. **Giới hạn cộng tác Team Space gói Free:** Tối đa khoảng **5 thành viên cộng tác** và **3 bot/workflow dùng chung** trong một Team Space — vừa đủ cho một nhóm sinh viên 3–5 người.

---

## BƯỚC 1: Đăng nhập `coze.com` và Tạo Team Space (Không dùng Personal Workspace)

### Vì sao KHÔNG được dùng Personal Workspace?
- `Personal Workspace` được tạo mặc định cho riêng từng tài khoản cá nhân và **không cho phép mời thành viên khác vào cùng chỉnh sửa**.
- Để tất cả thành viên trong nhóm đều có thể mở, sửa Persona/Prompt, cập nhật Knowledge Base, thêm Plugin và Publish lại bot, trưởng nhóm **bắt buộc phải tạo một Team Space**.

### Thao tác chi tiết
1. Truy cập `https://www.coze.com` và bấm **Sign in / Get Started** -> chọn **Continue with Google** bằng tài khoản Google của trưởng nhóm.
2. Tại thanh bên trái (hoặc menu chọn Workspace ở góc trên bên trái), bấm vào tên Workspace hiện tại -> chọn **`+ New team`**.
3. Điền thông tin tạo Team Space:
   - **Team Name:** `Nhom AI Phong Chong Lua Dao` (hoặc tên nhóm môn học).
   - **Description:** `Không gian làm việc chung xây dựng Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến`.
   - **Avatar:** Chọn biểu tượng chiếc khiên / ảnh đại diện phù hợp -> bấm **`Confirm`**.
4. Chắc chắn rằng giao diện đang đứng đúng trong **Team Space** vừa tạo trước khi chuyển sang Bước 2.

---

## BƯỚC 2: Tạo Agent (`Development -> + Create -> Create agent`)

1. Ở thanh điều hướng bên trái của Team Space, chọn **`Development`**.
2. Bấm nút **`+ Create`** -> chọn **`Create agent`** (lưu ý: giao diện Coze hiện gọi là *Agent*, còn trong URL và mã tích hợp Web SDK vẫn dùng tham số `bot_id`).
3. Điền đầy đủ thông tin khởi tạo:
   - **Agent Name (Tên Agent):**
     ```text
     Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến
     ```
   - **Agent Function Description (Mô tả chức năng Agent):**
     ```text
     Trợ lý AI tiếng Việt giúp người dân, sinh viên và người cao tuổi nhận diện dấu hiệu lừa đảo trực tuyến, nắm vững nguyên tắc phòng tránh và xử lý khẩn cấp 4 bước, đồng thời hướng dẫn sử dụng các công cụ kiểm tra và kênh trình báo chính thống tại Việt Nam (156, VNeID, Bộ Công an A05, tinnhiemmang.vn, chongluadao.vn, nTrust).
     ```
   - **Icon / Avatar:** Tải ảnh đại diện nhóm thiết kế hoặc bấm **AI Generate** để Coze tạo biểu tượng chiếc khiên bảo vệ an toàn mạng.
4. Bấm **`Confirm`** để mở màn hình thiết lập 3 cột (**Arrangement / Develop**):
   - **Cột trái:** `Persona & Prompt`
   - **Cột giữa:** `Skills` (Plugins, Workflows, Knowledge, Memory...)
   - **Cột phải:** `Preview & Debug`

---

## BƯỚC 3: Thiết lập `Persona & Prompt` và Sử dụng nút `Optimize` (Auto-Optimize Prompt)

1. Mở tệp `01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze_Paste.txt` trong gói tài liệu của nhóm.
2. Sao chép toàn bộ nội dung (`Ctrl + A` -> `Ctrl + C`) và dán vào khung **`Persona & Prompt`** ở cột bên trái trên Coze.
3. Nhấn nút **`Optimize`** (Auto-Optimize Prompt — biểu tượng cây đũa thần ở góc ô Prompt). Coze sẽ dùng LLM tự động cấu trúc lại prompt thành các mục chuẩn (`# Role`, `## Skills`, `## Constraints`).
4. **Rà soát bắt buộc sau khi `Optimize`:** Đọc kỹ bản Coze vừa tối ưu để đảm bảo **không bị mất** 4 yếu tố cốt lõi sau (nếu bị rút gọn quá mức, hãy chỉnh tay bổ sung lại):
   - Tên chuẩn: `Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến`.
   - Đủ 3 chức năng cốt lõi: nhận diện dấu hiệu lừa đảo; phòng tránh & xử lý khẩn cấp 4 bước; hướng dẫn công cụ kiểm tra & kênh trình báo (`156`, `5656`, `113`, `VNeID`, `tinnhiemmang.vn`, `chongluadao.vn`, `tracuutenmien.gov.vn`, `nTrust`).
   - Ranh giới an toàn: không thay thế cơ quan công an, tuyệt đối không đòi OTP/mật khẩu/PIN/số thẻ/CCCD thật.
   - Quy tắc định tuyến công cụ: ưu tiên Knowledge Base cho kiến thức chuẩn; chỉ gọi `Google Web Search` khi hỏi tin tức/cảnh báo mới; chỉ gọi plugin tạo ảnh (`DALLE 3`/`Stable Diffusion`) khi người dùng chủ động yêu cầu vẽ poster/minh họa.
5. Ở thanh chọn mô hình phía trên cột giữa/trái, chọn **`Gemini 1.5 Flash`** (0,25 credits/lượt) hoặc **`GPT-4o-mini`** (1 credit/lượt) để tiết kiệm credit trong giai đoạn kiểm thử.

---

## BƯỚC 4: Nạp Cơ sở tri thức (`Skills -> Knowledge -> Text`)

### Giới hạn Knowledge Base trên Coze cần biết
- Định dạng văn bản hỗ trợ: `.pdf`, `.docx`, `.doc`, `.txt` (nếu tài liệu có bảng biểu nên ưu tiên `.pdf` hoặc `.docx`).
- Dung lượng: tối đa **2 GB/tháng** và **10 GB tổng dung lượng**; tối đa **100–300 tệp** trong một Knowledge Base; mỗi đoạn (segment) tối đa **5.000 ký tự**, tối đa **10.000 đoạn/tệp**.

### Thao tác upload 3 tài liệu `KB1`, `KB2`, `KB3`
1. Tại cột giữa **`Skills`**, tìm mục **`Knowledge`** -> bấm biểu tượng **`+`** -> chọn **`Create Knowledge`** (hoặc chọn Knowledge có sẵn trong Team Space).
2. Chọn loại **`Text`** -> đặt tên Knowledge Base: `Kien_Thuc_Phong_Chong_Lua_Dao_VN` -> bấm **`Confirm`**.
3. Chọn nguồn **`Local Document`** -> bấm **Upload** và tải lên cả 3 tệp PDF (hoặc DOCX) từ thư mục `01_Phan1_Chuan_Bi_Tai_Lieu\`:
   - `KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.pdf`
   - `KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.pdf`
   - `KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.pdf`
4. Ở bước cấu hình cắt đoạn (**Segmentation** — lưu ý Coze khóa lựa chọn này ngay sau lần upload đầu tiên):
   - Chọn **`Automatic Segmentation`** (khuyến nghị vì 3 file PDF đã trình bày rõ từng đề mục và bảng biểu, Coze tự nhận diện đoạn văn và bảng mạch lạc).
5. Chờ trạng thái xử lý của cả 3 file chuyển sang **`Completed / Success`** (100%).
6. Quay lại màn hình `Develop` của Agent, trong mục `Knowledge`:
   - Đặt chế độ truy xuất (**Recall Mode**) là **`Automatic Recall`** (hoặc kiểm tra `Recall Strategy`: *Semantic + Full-text*) để bot tự động tra cứu KB cho mọi câu hỏi về lừa đảo.

---

## BƯỚC 5: Thêm Plugins (`Google Web Search` và Tạo ảnh `DALLE 3` / `Stable Diffusion`)

1. Tại cột giữa **`Skills`**, tìm mục **`Plugins`** -> bấm biểu tượng **`+`**.
2. **Thêm Plugin tìm kiếm web:**
   - Gõ từ khóa `Google Web Search` (hoặc `Google Search`) vào ô tìm kiếm trong Plugin Store.
   - Chọn plugin chính thức **`Google Web Search`** -> bấm **`Add`**.
   - *(Phương án dự phòng)*: Nếu tại thời điểm thực hành plugin `Google Web Search` bị giới hạn khu vực hoặc yêu cầu API key riêng, nhóm có thể thêm **`Bing Web Search`** (chi phí 1 credit/lượt) để thay thế.
3. **Thêm Plugin tạo ảnh minh họa:**
   - Tiếp tục tìm từ khóa `DALLE 3` trong Plugin Store -> chọn plugin **`DALLE 3`** -> bấm **`Add`**.
   - *(Khuyến nghị tiết kiệm Credit cho gói Free)*: Nhóm nên bấm **`Add`** thêm **`Stable Diffusion`** (chỉ tốn **1 credit/lần**) làm lựa chọn thứ hai trong trường hợp đã dùng hết 10 credits/ngày với `DALLE 3`.
4. Kiểm tra lại cột **`Skills -> Plugins`** đã hiển thị đầy đủ cả Plugin tìm kiếm web và Plugin tạo ảnh.

---

## BƯỚC 6: Kiểm thử trên `Preview & Debug` (Trace & Bộ 10 Test Prompts Tiếng Việt)

Ở cột bên phải **`Preview & Debug`**, nhóm tiến hành chat kiểm thử trực tiếp. Sau mỗi câu trả lời, bấm vào thanh trạng thái mở rộng (**Process / Trace**) phía trên câu trả lời của bot để kiểm tra xem:
- Câu hỏi kiến thức nền có gọi đúng **Knowledge Base** (`KB1`–`KB3`) hay không?
- Câu hỏi tin tức/cập nhật mới có kích hoạt **`Google Web Search`** hay không?
- Câu hỏi tạo poster/ảnh có kích hoạt **`DALLE 3`** (hoặc `Stable Diffusion`) hay không?

### Bảng 10 Test Prompts Tiếng Việt Chuẩn (3 Nhóm)

#### Nhóm A — Hỏi đáp bám sát Knowledge Base (5 Prompts)

| Mã | Prompt test tiếng Việt (Copy dán vào Preview & Debug) | Công cụ kỳ vọng | Tiêu chí đánh giá đạt (Acceptance Criteria) |
|---|---|---|---|
| **T1** | *Tôi nhận được cuộc gọi tự xưng là Công an điều tra nói tôi liên quan đường dây rửa tiền, gửi hình lệnh bắt qua Zalo và yêu cầu chuyển tiền vào "tài khoản tạm giữ" để chứng minh vô tội. Đây có phải lừa đảo không và tôi nên làm gì?* | Knowledge Base (`KB1`, `KB2`, `KB3`) | Kết luận ngay đây là **lừa đảo mạo danh cơ quan công an/Viện kiểm sát/Tòa án** (thuộc Nhóm 3 trong 24 hình thức); khẳng định công an không làm việc/bắt chuyển tiền qua Zalo; hướng dẫn ngắt liên lạc, không chuyển tiền và gọi `113` / `156` / Công an địa phương. |
| **T2** | *Có người gọi xưng nhân viên ngân hàng nói tài khoản của tôi sắp bị khóa vì chưa cập nhật sinh trắc học theo QĐ 2345, họ gửi cho tôi một đường link và bảo tải file .apk để xác thực. Tôi lỡ bấm tải file .apk về máy Android rồi thì phải xử lý khẩn cấp thế nào?* | Knowledge Base (`KB1`, `KB2`) | Nhận diện đúng thủ đoạn giả mạo cập nhật sinh trắc học (QĐ 2345/QĐ-NHNN) và mã độc `.apk`; đưa ngay **Quy trình 4 bước khẩn cấp** (ngắt Wi-Fi/4G, gỡ app lạ/khôi phục cài đặt gốc nếu cần -> gọi hotline chính thức ngân hàng khóa thẻ/tài khoản, đổi mật khẩu -> lưu bằng chứng -> trình báo Công an/VNeID/`156`); **không** đòi người dùng gửi OTP hay mật khẩu. |
| **T3** | *Mẹ tôi mới chuyển khoản nhầm 5 triệu đồng cho một trang bán combo du lịch giá rẻ trên Facebook rồi bị họ chặn liên lạc. Mẹ tôi thấy trên mạng có quảng cáo dịch vụ "công an mạng hỗ trợ lấy lại tiền bị lừa", có nên thuê không?* | Knowledge Base (`KB1`, `KB2`, `KB3`) | Cảnh báo dứt khoát dịch vụ "lấy lại tiền bị lừa" là **lừa đảo lần 2** (hình thức số 22); trấn an không đổ lỗi; hướng dẫn giữ sao kê, đoạn chat, STK lừa đảo -> gọi ngân hàng hỗ trợ tra soát -> trình báo Công an xã/phường/PA05 hoặc qua VNeID, gửi `tinnhiemmang.vn`. |
| **T4** | *Hãy giải thích ngắn gọn quy tắc "3 Không" và "4 Không - 2 Phải" để tôi gửi cho ông bà lớn tuổi trong gia đình dễ nhớ.* | Knowledge Base (`KB2`) | Trình bày rõ ràng, dễ đọc, đúng nội dung **3 Không** (Không tin tuyệt đối; Không cài app từ link lạ; Không cung cấp thông tin cá nhân/chuyển tiền) và **4 Không - 2 Phải**, ngôn ngữ gần gũi cho người cao tuổi. |
| **T5** | *Trước khi chuyển tiền mua hàng online, tôi muốn tự kiểm tra xem đường link website và số tài khoản ngân hàng của người bán có dấu hiệu lừa đảo hay không thì dùng những công cụ nào của Việt Nam và thao tác ra sao?* | Knowledge Base (`KB3`) | Hướng dẫn từng bước ít nhất 3 công cụ chính thống: `tinnhiemmang.vn/website-lua-dao` & `tinnhiemmang.vn/tra-cuu-tai-khoan`, `chongluadao.vn/analyze`, `tracuutenmien.gov.vn` (hoặc SMS `TCTM [Tên miền]` gửi `156`), ứng dụng `nTrust` của NCA. |

#### Nhóm B — Tìm kiếm thông tin thời sự qua Plugin `Google Web Search` (3 Prompts)

| Mã | Prompt test tiếng Việt | Công cụ kỳ vọng | Tiêu chí đánh giá đạt |
|---|---|---|---|
| **T6** | *Hãy tìm kiếm thông tin mới nhất trên web về việc chuyển giao chức năng quản lý nhà nước về an toàn thông tin từ Cục An toàn thông tin sang Bộ Công an năm 2025 để tôi biết cơ quan nào đang chủ trì hiện nay.* | `Google Web Search` (+ `KB3`) | Trace hiển thị có gọi plugin tìm kiếm web; trả lời chính xác mốc bàn giao **28/02/2025** / hiệu lực từ **01/03/2025** chuyển sang **Cục A05 — Bộ Công an**, kèm dẫn nguồn báo chí/cổng `.gov.vn`. |
| **T7** | *Hãy tra cứu trên Google các cảnh báo lừa đảo trực tuyến nổi bật gần đây tại Việt Nam (như giả mạo thuế, hoàn thuế, phạt nguội hoặc AI Deepfake) và tóm tắt ngắn gọn kèm nguồn trích dẫn.* | `Google Web Search` | Trace xác nhận gọi `Google Web Search`; tóm tắt được các cảnh báo cập nhật mới và dẫn rõ tên báo/cổng chính thống (`bocongan.gov.vn`, `baochinhphu.vn`, `vnexpress.net`, `tuoitre.vn`...). |
| **T8** | *Tôi thấy một trang web lạ có tên miền kết thúc bằng .vip tự xưng là cổng hỗ trợ kích hoạt VNeID. Hãy tìm kiếm thông tin xác minh tên miền cổng dịch vụ công và VNeID chính thức tại Việt Nam.* | `Google Web Search` (+ `KB3`) | Kết hợp tìm kiếm xác nhận cổng cơ quan nhà nước Việt Nam dùng đuôi `.gov.vn` (như `bocongan.gov.vn`, `dichvucong.gov.vn`) và ứng dụng VNeID chỉ tải trên App Store/Google Play chính thức; cảnh báo tên miền `.vip` là dấu hiệu giả mạo. |

#### Nhóm C — Tạo ảnh minh họa qua Plugin tạo ảnh (`DALLE 3` / `Stable Diffusion`) (2 Prompts)

> **Nhắc nhở ngân sách Credit:** Hãy thực hiện Nhóm C khi tài khoản còn đủ **10 credits** (nếu dùng `DALLE 3`) hoặc chuyển sang `Stable Diffusion` (1 credit/lần) nếu trong ngày đã dùng hết credit cho Nhóm A & B.

| Mã | Prompt test tiếng Việt | Công cụ kỳ vọng | Tiêu chí đánh giá đạt |
|---|---|---|---|
| **T9** | *Hãy tạo một poster minh họa phong cách hiện đại, thân thiện với chủ đề tuyên truyền phòng tránh lừa đảo trực tuyến, hình chiếc khiên bảo vệ điện thoại và thông điệp an toàn số (sử dụng hình ảnh trực quan, không chữ rườm rà).* | `DALLE 3` (hoặc `Stable Diffusion`) | Trace xác nhận gọi thành công plugin tạo ảnh; trả về ảnh minh họa hiển thị rõ trên khung chat, đúng chủ đề an toàn mạng, không chứa nội dung phản cảm. |
| **T10** | *Hãy vẽ một hình minh họa cảnh báo người dùng lớn tuổi cẩn thận trước cuộc gọi giả mạo và đường link độc hại, tông màu xanh dương - cam dễ nhìn.* | `DALLE 3` (hoặc `Stable Diffusion`) | Trace xác nhận gọi plugin tạo ảnh; ảnh minh họa tạo thành công, phù hợp sử dụng làm tư liệu truyền thông/slide thuyết trình của nhóm. |

---

## BƯỚC 7: Xuất bản Chatbot phiên bản `1.0.0` (`Publish`)

1. Sau khi kiểm thử đạt yêu cầu ở Bước 6, bấm nút **`Publish`** ở góc trên bên phải màn hình `Develop`.
2. Điền thông tin phát hành:
   - **Version:** `1.0.0`
   - **Changelog (Nhật ký phiên bản — mẫu tiếng Việt gợi ý):**
     ```text
     Phiên bản 1.0.0 — Phát hành chính thức Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến:
     - Hoàn thiện Persona & Prompt tiếng Việt theo 3 chức năng cốt lõi và ranh giới an toàn.
     - Tích hợp 3 tài liệu Knowledge Base chuẩn (24 hình thức lừa đảo + thủ đoạn 2024-2025, nguyên tắc 3 Không / 4 Không - 2 Phải / quy trình khẩn cấp 4 bước, hướng dẫn công cụ tinnhiemmang.vn / chongluadao.vn / nTrust / 156 / VNeID / Bộ Công an A05).
     - Kết nối plugin Google Web Search và tạo ảnh minh họa (DALLE 3 / Stable Diffusion).
     - Kiểm thử thành công 10 kịch bản tiếng Việt trên Preview & Debug.
     ```
3. Ở phần chọn kênh phát hành bên dưới, tích chọn **`Chat SDK`** (và **`Messenger`** nếu nhóm muốn triển khai song song lên Fanpage).
4. Bấm **`Publish`** để hoàn tất xuất bản.

---

## BƯỚC 8: Tích hợp Chatbot lên Website (`Chat SDK`) và Facebook Messenger

### Phương án A: Tích hợp lên Website của nhóm (`03_Website_Tich_Hop/`)

1. **Lấy `bot_id`:** Mở trang chi tiết Agent trên `coze.com`, nhìn thanh địa chỉ trình duyệt có dạng:
   `https://www.coze.com/space/<space_id>/bot/<bot_id>`
   -> Chuỗi số `<bot_id>` ở cuối URL chính là `bot_id` của chatbot.
2. **Tạo Personal Access Token (PAT) để demo môn học:**
   - Truy cập `https://www.coze.com/open/oauth/pats` (hoặc vào ảnh đại diện góc dưới trái -> **API Management / Authorization** -> **Personal Access Tokens**).
   - Bấm **`Add Token`** -> đặt tên `Web_Demo_AntiScam`, chọn thời hạn (ví dụ 30 ngày), tích quyền **Chat / Bot** cho Workspace của nhóm -> bấm **`Confirm`**.
   - **Sao chép ngay mã PAT** (bắt đầu bằng `pat_...`) vì Coze chỉ hiển thị đầy đủ một lần duy nhất.
3. **Kiểm tra mã nhúng trên Coze:** Tại màn hình **`Publish -> Chat SDK -> Installation`**, kiểm tra phiên bản URL `<script src="...">` mới nhất (ví dụ `https://sf-cdn.coze.com/obj/unpkg-va/flow-platform/chat-app-sdk/1.2.0-beta.17/libs/oversea/index.js`).
4. **Cấu hình vào trang web có sẵn trong gói sản phẩm:**
   - Mở tệp `03_Website_Tich_Hop/coze-config.js`.
   - Sửa `enabled: false` thành `enabled: true`.
   - Dán `botId` và `token` (PAT) vào đúng hai trường tương ứng (và cập nhật `sdkUrl` nếu Coze hiển thị phiên bản mới hơn).
   - Chạy server cục bộ bằng lệnh:
     ```powershell
     cd C:\Users\canhn\teamwork_projects\anti_scam_chatbot\03_Website_Tich_Hop
     python -m http.server 8080 --bind 127.0.0.1
     ```
   - Mở `http://127.0.0.1:8080` trên Chrome: góc dưới bên phải sẽ xuất hiện nút bong bóng chat của **Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến**.

> **Cảnh báo bảo mật cực kỳ quan trọng:**  
> Phiên bản `Web SDK` hiện đại bắt buộc dùng `auth: { type: 'token' }` (kiểu cũ `unauth` đã ngừng hỗ trợ). Khi demo cục bộ trong môn học, dùng PAT trực tiếp trong `coze-config.js` rất tiện lợi, nhưng **tuyệt đối không đẩy file chứa PAT thật lên GitHub công khai hoặc hosting công cộng** vì người khác có thể đọc mã nguồn và dùng ké hạn mức token của bạn (nếu đưa lên môi trường thật phải cấp phát OAuth JWT từ backend).

### Phương án B: Tích hợp lên Facebook Messenger (Tùy chọn mở rộng)

1. Chuẩn bị 01 **Facebook Fanpage** (dùng để demo môn học) và đăng nhập `https://developers.facebook.com/` (**Meta for Developers**).
2. Chọn **My Apps -> Create App -> Other -> Business** -> đặt tên ứng dụng -> tại bảng điều khiển ứng dụng, thêm sản phẩm **`Messenger`**.
3. Trong mục **Messenger -> Settings -> Webhooks -> Add Callback URL**:
   - **Callback URL:** `https://api.coze.com/adapter/messenger/webhook`
   - **Verify Token:** `coze`
   - Tích chọn các quyền sự kiện tin nhắn (`messages`, `messaging_postbacks`).
4. Liên kết Fanpage thử nghiệm và bấm **Generate Token** để lấy **Page Access Token**, đồng thời lấy **App ID** và **App Secret** trong *App Settings -> Basic*.
5. Quay lại Coze tại giao diện **`Publish`** -> mục *Publish to social platforms* -> bấm **`Configure`** ở dòng **`Messenger`** -> dán các thông số từ Meta -> **`Save`** -> tích chọn **`Messenger`** và bấm **`Publish`**.

---

## BƯỚC 9: Chia sẻ quyền chỉnh sửa cho toàn bộ thành viên nhóm (Phân biệt rõ với link chỉ chat)

Đây là yêu cầu bắt buộc ở Phần 3 để **mọi thành viên trong nhóm đều có thể cùng mở vào chỉnh sửa Prompt, Knowledge Base, Plugins và Publish lại bot**.

### Cách làm đúng: Mời vào Team Space & Nâng quyền lên `Administrator`

1. Đảm bảo nhóm đang ở trong **Team Space** đã tạo ở Bước 1.
2. Trên thanh điều hướng bên trái, vào **`Space Configuration`** (hoặc biểu tượng bánh răng cài đặt của Team Space) -> chọn tab **`Members`**.
3. Thực hiện một trong hai cách mời thành viên:
   - **Cách 1 (Mời trực tiếp):** Bấm **`+ Add member`** -> nhập chính xác Coze Username / Nickname hoặc email tài khoản Google đã đăng ký Coze của từng bạn trong nhóm -> gửi lời mời (hiệu lực 7 ngày).
   - **Cách 2 (Dùng link mời vào Team):** Bấm biểu tượng **Share** -> bật **Space Sharing Link** -> sao chép đường link (hiệu lực 7 ngày) gửi vào nhóm chat của lớp để các bạn tự bấm tham gia.
4. **Bước quyết định — Nâng vai trò từ `Member` lên `Administrator`:**
   - Ngay khi thành viên vào Team Space, mặc định Coze gán vai trò **`Member`**.
   - Theo cơ chế phân quyền của Coze: **`Member`** chỉ có toàn quyền chỉnh sửa/xóa tài nguyên **do chính tài khoản đó tạo**, không được tự do sửa/xóa hay quản trị bot do trưởng nhóm tạo.
   - Trưởng nhóm (`Owner`) **bắt buộc** phải bấm vào cột **Role** bên cạnh tên từng thành viên trong `Space Configuration > Members` và đổi từ `Member` -> **`Administrator`**.
   - Với quyền **`Administrator`**, mọi thành viên trong nhóm đều có quyền mở Agent, chỉnh sửa `Persona & Prompt`, thêm/xóa tệp trong `Knowledge Base`, cấu hình `Plugins` và bấm `Publish`.

### Bảng phân biệt quyền chỉnh sửa Team Space và các đường link chỉ xem / chỉ chat

| Hình thức chia sẻ | Ai thao tác được? | Có sửa được Prompt / KB / Plugins của bot nhóm không? | Kết luận sử dụng cho bài tập nhóm |
|---|---|---|---|
| **Team Space + Vai trò `Administrator`** | Các thành viên trong Team Space | **CÓ — Toàn quyền cùng chỉnh sửa, kiểm thử và Publish phiên bản mới** | **BẮT BUỘC DÙNG** cho yêu cầu cộng tác nhóm. |
| **Team Space + Vai trò `Member`** | Thành viên trong Team Space | **Hạn chế** (chỉ quản lý bot tự tạo, không toàn quyền sửa/xóa tài nguyên của bạn khác) | Không đủ — cần nâng lên `Administrator`. |
| **Coze Store — Private Configuration** | Người nhận link chat | **KHÔNG** — Chỉ được phép **chat thử** với bot, không thấy Prompt/KB. | Chỉ dùng để gửi giảng viên hoặc người dùng trải nghiệm chat. |
| **Coze Store — Public Configuration** | Người dùng cộng đồng | **KHÔNG sửa bot gốc** — Chỉ cho phép **Duplicate** (nhân bản sang workspace riêng), và thường bị chặn nếu bot có Knowledge Base riêng tư. | Không dùng để làm việc nhóm trên cùng một bot. |
