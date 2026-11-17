/**
 * Cấu hình tích hợp Coze Web SDK (Chat SDK)
 * Dự án: Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến
 *
 * HƯỚNG DẪN KÍCH HOẠT:
 * 1. Xuất bản bot (Publish v1.0.0) trên https://www.coze.com và tích chọn kênh "Chat SDK".
 * 2. Lấy bot_id từ URL trang chỉnh sửa Agent:
 *    https://www.coze.com/space/<space_id>/bot/<bot_id>
 * 3. Tạo Personal Access Token (PAT) tại: https://www.coze.com/open/oauth/pats
 *    (Chọn quyền Chat / Bot cho Team Space của nhóm).
 * 4. Thay thế 'YOUR_COZE_BOT_ID' và 'YOUR_COZE_PAT_TOKEN' bên dưới,
 *    sau đó đổi enabled: false -> enabled: true.
 *
 * CẢNH BÁO BẢO MẬT:
 * Không đẩy file chứa PAT thật lên GitHub công khai hoặc máy chủ công cộng.
 * Nếu triển khai public lâu dài, cần dùng backend cấp phát OAuth JWT thay cho PAT tĩnh.
 */
window.COZE_CHATBOT_CONFIG = {
  enabled: false,
  sdkUrl: "https://sf-cdn.coze.com/obj/unpkg-va/flow-platform/chat-app-sdk/1.2.0-beta.17/libs/oversea/index.js",
  botId: "YOUR_COZE_BOT_ID",
  token: "YOUR_COZE_PAT_TOKEN",
  title: "Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến",
  layout: "auto", // "auto" (tự chọn "mobile" / "pc" theo màn hình), "pc", hoặc "mobile"
  lang: "en"
};
