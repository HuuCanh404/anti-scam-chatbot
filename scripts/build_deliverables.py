# -*- coding: utf-8 -*-
"""
Build script generating all DOCX and PDF deliverables reproducibly for:
"Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"
"""

import html
import os
import re
import subprocess
import tempfile
import textwrap
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Cm, Pt, RGBColor

ROOT_DIR = Path(__file__).resolve().parent.parent
CHROME_PATH = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


# ==============================================================================
# 1. CONTENT DEFINITIONS FOR KB1, KB2, KB3
# ==============================================================================

KB1_DOC = {
    "filename_stem": "KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen",
    "code": "KB1",
    "title": "CÁC HÌNH THỨC LỪA ĐẢO TRỰC TUYẾN & DẤU HIỆU NHẬN BIẾT TẠI VIỆT NAM",
    "subtitle": "Tài liệu Cơ sở tri thức 1 — Phục vụ Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến",
    "meta": "Cập nhật: 2025 • Nguồn chính thống: Cục ATTT (06/2023), Bộ Công an (Cục A05), NHNN (QĐ 2345)",
    "sections": [
        {
            "heading": "1. Tổng quan khung phân loại lừa đảo trực tuyến tại Việt Nam",
            "paragraphs": [
                "Theo \"Cẩm nang nhận diện và phòng chống lừa đảo trực tuyến\" do Cục An toàn thông tin (Bộ Thông tin và Truyền thông) công bố tháng 06/2023 trên Cổng Không gian mạng quốc gia (khonggianmang.vn), các thủ đoạn lừa đảo trực tuyến phổ biến tại Việt Nam được hệ thống hóa thành 3 nhóm lớn với 24 hình thức cốt lõi.",
                "Giai đoạn 2024–2025, bên cạnh 24 hình thức truyền thống, các đối tượng tội phạm công nghệ cao liên tục biến tướng theo chính sách số mới, đặc biệt là lợi dụng Quyết định 2345/QĐ-NHNN về xác thực sinh trắc học ngân hàng, giả mạo ứng dụng định danh VNeID, cài mã độc qua tệp .apk trên Android và sử dụng trí tuệ nhân tạo (Deepfake/Deepvoice). Từ ngày 01/03/2025, chức năng quản lý nhà nước về an toàn thông tin mạng đã được bàn giao về Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) — Bộ Công an."
            ],
            "callout": {
                "title": "Nguyên tắc nhận diện cốt lõi",
                "text": "Mọi kịch bản lừa đảo trực tuyến — dù biến hóa dưới vỏ bọc công nghệ nào — đều xoay quanh việc đánh vào tâm lý SỢ HÃI (đe dọa khóa SIM, khóa tài khoản, lệnh bắt giữ), KHẨN CẤP (người thân cấp cứu, chuyển nhầm tiền) hoặc THAM LAM (việc nhẹ lương cao, combo du lịch siêu rẻ, lãi suất ảo)."
            }
        },
        {
            "heading": "2. Nhóm 1 — Giả mạo thương hiệu (7 hình thức chính thống)",
            "paragraphs": [
                "Kẻ gian mạo danh uy tín của cơ quan nhà nước, ngân hàng, doanh nghiệp viễn thông, sàn thương mại điện tử hoặc hãng du lịch để tạo lòng tin và dẫn dụ nạn nhân chuyển tiền hoặc cung cấp thông tin cá nhân."
            ],
            "table": {
                "headers": ["STT", "Hình thức lừa đảo", "Thủ đoạn & Diễn biến phổ biến", "Dấu hiệu nhận diện nhanh"],
                "rows": [
                    ["1", "Combo du lịch giá rẻ", "Tạo fanpage/website giả mạo khu nghỉ dưỡng, đại lý vé máy bay, tung gói combo giảm 50–70% và yêu cầu chuyển cọc 30–100%.", "Giá thấp bất thường; chỉ nhận chuyển khoản vào tài khoản cá nhân; hối thúc chốt gấp trong ngày."],
                    ["2", "Lừa đảo 'khóa SIM'", "Gọi điện tự xưng nhà mạng thông báo thuê bao sắp bị khóa hai chiều do chưa chuẩn hóa thông tin, dụ làm theo cú pháp chuyển hướng cuộc gọi hoặc nộp phí.", "Gọi từ số di động cá nhân; yêu cầu bấm cú pháp lạ (*21*, **21*...) nhằm chiếm quyền nhận cuộc gọi/OTP."],
                    ["3", "Giả danh công ty tài chính mời vay vốn", "Quảng cáo giải ngân nhanh, không cần thế chấp, lãi suất thấp; yêu cầu nạn nhân đóng 'phí bảo hiểm khoản vay', 'phí mở hồ sơ' hoặc chứng minh số dư.", "App vay lạ ngoài kho chính thức; đòi chuyển tiền trước khi được nhận tiền vay; báo 'sai số tài khoản' để ép nộp thêm."],
                    ["4", "Giả mạo website cơ quan nhà nước, ngân hàng, doanh nghiệp", "Lập tên miền gần giống (typosquatting) giao diện y hệt cổng dịch vụ công, thuế, BHXH hoặc ngân hàng để thu thập mật khẩu và OTP.", "Đuôi tên miền lạ (.vip, .xyz, .info...) thay vì .gov.vn hoặc tên miền chính thức của ngân hàng."],
                    ["5", "Lừa đảo tin nhắn SMS Brandname giả", "Dùng trạm thu phát sóng giả (BTS giả) phát tán tin nhắn hiển thị cùng luồng tên thương hiệu ngân hàng/viễn thông kèm đường link độc hại.", "Tin nhắn thông báo trúng thưởng, tài khoản sắp hết hạn hoặc cập nhật thông tin kèm link rút gọn/tên miền lạ."],
                    ["6", "Lừa đảo bán hàng giả, hàng nhái trên sàn TMĐT", "Rao hàng chính hãng giá rẻ, dẫn dụ người mua giao dịch ngoài sàn (qua Zalo/Facebook) rồi giao hàng giả, gạch đá hoặc chặn liên lạc.", "Kêu gọi hủy đơn trên sàn để chuyển khoản trực tiếp nhằm 'giảm giá/miễn phí ship'."],
                    ["7", "Tung tin giả cuộc gọi mất tiền (như FlashAI)", "Lan truyền thông tin sai sự thật về các cuộc gọi 'nháy máy mất sạch tiền' nhằm gây hoang mang và dụ thao tác cài ứng dụng kiểm tra bảo mật giả.", "Tin đồn thiếu kiểm chứng từ nguồn báo chí chính thống; kèm link tải công cụ 'chống nghe lén' không rõ nguồn gốc."]
                ]
            }
        },
        {
            "heading": "3. Nhóm 2 — Chiếm đoạt tài khoản (5 hình thức chính thống)",
            "paragraphs": [
                "Nhóm thủ đoạn này tập trung đánh cắp quyền kiểm soát tài khoản mạng xã hội (Facebook, Zalo, Telegram) hoặc dữ liệu định danh cá nhân (CCCD) để trục lợi trực tiếp hoặc tiếp tục lừa người thân của nạn nhân."
            ],
            "table": {
                "headers": ["STT", "Hình thức lừa đảo", "Cách thức thực hiện", "Dấu hiệu nhận diện nhanh"],
                "rows": [
                    ["8", "Chiếm đoạt tài khoản MXH nhắn tin mượn tiền", "Chiếm quyền Facebook/Zalo qua link bình chọn cuộc thi, link xác minh bản quyền; sau đó nhắn tin mượn tiền hoặc nhờ chuyển khoản hộ bạn bè, người thân.", "Nhắn tin mượn tiền gấp, từ chối gọi video kiểm chứng hoặc chỉ gọi video mờ 1–2 giây rồi tắt."],
                    ["9", "Đánh cắp thông tin/ảnh CCCD vay tín dụng đen", "Dụ người dùng gửi ảnh CCCD hai mặt và ảnh chân dung (với lý do tuyển dụng, nhận quà, đăng ký thẻ) để đi mở tài khoản hoặc vay app tín dụng đen.", "Yêu cầu chụp rõ CCCD 2 mặt + video quay mặt qua Zalo/Telegram cho tổ chức không minh bạch."],
                    ["10", "Đánh cắp mã OTP Telegram và ứng dụng chat", "Gửi link đăng nhập giả mạo thông báo 'tài khoản có nguy cơ bị khóa' hoặc 'xác nhận nhóm', lừa nhập số điện thoại và mã OTP đăng nhập.", "Đường link lạ yêu cầu nhập mã đăng nhập Telegram/Zalo gửi về máy."],
                    ["11", "Lừa đảo dịch vụ 'lấy lại tài khoản MXH bị mất'", "Quảng cáo nhận khôi phục Facebook/TikTok bị hack với giá rẻ, yêu cầu đặt cọc trước hoặc gửi thông tin email/mật khẩu để chiếm đoạt thêm.", "Cam kết 'lấy lại 100% trong 15 phút', thu tiền cọc qua ví điện tử hoặc thẻ cào."],
                    ["12", "Rải link phishing & quảng cáo bẩn trên MXH", "Chạy quảng cáo bài viết giật gân, tặng quà miễn phí hoặc gắn thẻ hàng loạt để dẫn dụ người dùng bấm vào trang thu thập thông tin đăng nhập.", "Đường link yêu cầu đăng nhập lại Facebook/Google để xem nội dung hoặc nhận thưởng."]
                ]
            }
        },
        {
            "heading": "4. Nhóm 3 — Các hình thức kết hợp khác (12 hình thức chính thống)",
            "paragraphs": [
                "Đây là nhóm có mức độ thiệt hại tài chính nghiêm trọng nhất, kết hợp nhiều kịch bản thao túng tâm lý kéo dài hoặc ứng dụng công nghệ cao."
            ],
            "table": {
                "headers": ["STT", "Hình thức lừa đảo", "Kịch bản điển hình", "Dấu hiệu nhận diện nhanh"],
                "rows": [
                    ["13", "Cuộc gọi video Deepfake / Deepvoice", "Dùng AI giả khuôn mặt và giọng nói người thân/sếp gọi video ngắn chất lượng thấp vài giây, báo mất sóng rồi nhắn tin nhờ chuyển tiền gấp.", "Video giật/mờ bất thường, không tương tác tự nhiên; hối thúc chuyển khoản vào số tài khoản tên người lạ."],
                    ["14", "Giả mạo biên lai chuyển tiền thành công", "Chỉnh sửa ảnh bill ngân hàng đã chuyển khoản thành công (hoặc dùng chiêu 'lệnh chuyển tiền chờ xử lý') để lừa người bán giao hàng.", "Chỉ gửi ảnh chụp màn hình mờ/lỗi phông chữ trong khi tài khoản người bán chưa thực sự biến động số dư."],
                    ["15", "Giả danh giáo viên, y tế báo người thân cấp cứu", "Gọi điện cho phụ huynh báo con bị tai nạn nặng đang chờ mổ cấp cứu tại bệnh viện, yêu cầu chuyển tiền viện phí ngay qua số tài khoản cá nhân.", "Gây hoảng loạn tột độ; thúc ép chuyển tiền ngay không cho gọi kiểm chứng với giáo viên chủ nhiệm hoặc nhà trường."],
                    ["16", "Tuyển người mẫu nhí", "Đăng quảng cáo tuyển mẫu ảnh cho hãng thời trang, dụ phụ huynh mua trang phục đắt tiền, đóng phí tập huấn hoặc nạp tiền 'tăng lượt bình chọn'.", "Yêu cầu tham gia nhóm Telegram làm nhiệm vụ chuyển tiền 'tăng tương tác' để giữ suất."],
                    ["17", "Quảng cáo cờ bạc, cá độ, tín dụng đen chứa mã độc", "Cài cắm link/ứng dụng cờ bạc trực tuyến có mã độc theo dõi thiết bị hoặc dụ nạp tiền không cho rút.", "Cam kết 'kéo 1-1', 'tặng tiền trải nghiệm' từ trang web cờ bạc bất hợp pháp."],
                    ["18", "Đầu tư chứng khoán, tiền ảo (crypto), đa cấp giả", "Lập sàn giao dịch giả mạo chuyên gia tài chính; giai đoạn đầu cho rút tiền lãi nhỏ đều đặn, khi nạn nhân nạp tiền tỷ thì khóa tài khoản.", "Lợi nhuận cam kết cao phi lý (15–30%/tháng hoặc theo ngày), không có giấy phép của cơ quan quản lý Việt Nam."],
                    ["19", "Tuyển Cộng tác viên (CTV) online 'việc nhẹ lương cao'", "Dụ like bài viết, chốt đơn hàng ảo sàn TMĐT; nhiệm vụ đầu trả hoa hồng thật, sau ép nạp tiền đơn hàng giá trị lớn rồi báo lỗi cú pháp để chiếm đoạt.", "Lương cao không cần kỹ năng; bắt buộc nạp tiền cá nhân vào hệ thống để nhận hoa hồng."],
                    ["20", "Giả danh Công an, Viện kiểm sát, Tòa án", "Gọi điện đe dọa nạn nhân liên quan đường dây ma túy, rửa tiền hoặc phạt nguội; gửi lệnh bắt giả qua Zalo, ép chuyển tiền vào 'tài khoản tạm giữ' để chứng minh vô tội.", "Cơ quan Công an KHÔNG bao giờ làm việc qua điện thoại/Zalo và KHÔNG yêu cầu chuyển tiền xác minh."],
                    ["21", "Lừa đảo chuyển nhầm tiền vào tài khoản", "Cố ý chuyển một khoản tiền nhỏ vào tài khoản nạn nhân rồi gọi điện giả danh bên cho vay/người chuyển nhầm ép trả cả gốc lẫn lãi cắt cổ.", "Không làm việc qua ngân hàng mà yêu cầu chuyển trả vào một tài khoản thứ ba khác."],
                    ["22", "Dịch vụ 'lấy lại tiền đã bị lừa'", "Mạo danh công an mạng, luật sư, hacker mũ trắng chạy quảng cáo Facebook/Google cam kết thu hồi tiền bị lừa, yêu cầu nộp 'phí hồ sơ/phí kích hoạt' lần 2.", "Cam kết hoàn tiền 100% chỉ sau vài giờ qua tin nhắn mạng xã hội."],
                    ["23", "Lừa đảo cho số đánh đề, cá cược trực tuyến", "Quảng cáo 'soi cầu chuẩn xác', 'biết trước kết quả', thu phí mua số hoặc chia hoa hồng.", "Hứa hẹn chắc thắng trong hoạt động cờ bạc trái phép."],
                    ["24", "Bẫy tình cảm (Romance Scam / Pig Butchering)", "Tạo vỏ bọc doanh nhân/quân nhân/chuyên gia nước ngoài giàu có trên app hẹn hò, nuôi dưỡng tình cảm nhiều tuần rồi rủ đầu tư sàn ảo hoặc đóng phí hải quan nhận quà.", "Quá hoàn hảo, né tránh gặp mặt trực tiếp, sớm dẫn dắt sang đầu tư tiền hoặc nhờ đóng thuế nhận bưu kiện giá trị lớn."]
                ]
            }
        },
        {
            "heading": "5. Thủ đoạn nổi cộm cập nhật giai đoạn 2024–2025",
            "paragraphs": [
                "Ngoài 24 hình thức trên, Bộ Công an và các ngân hàng thương mại liên tục phát đi cảnh báo đối với 3 thủ đoạn bùng phát mạnh từ giữa năm 2024 đến năm 2025:"
            ],
            "bullets": [
                "Giả mạo nhân viên ngân hàng hỗ trợ cập nhật sinh trắc học (lợi dụng Quyết định 2345/QĐ-NHNN có hiệu lực từ 01/07/2024): Đối tượng gọi điện hù dọa tài khoản sẽ bị khóa nếu chưa xác thực khuôn mặt, sau đó gửi link giả mạo hoặc tệp cài đặt .apk để chiếm quyền điều khiển điện thoại và rút sạch tiền.",
                "Giả mạo cán bộ Công an, UBND, Cơ quan Thuế dụ cài app VNeID / Dịch vụ công / eTax giả (tệp .apk trên Android): Viện cớ 'kích hoạt định danh mức 2', 'cập nhật dữ liệu dân cư khi sáp nhập địa giới/bộ máy', 'hoàn thuế' hoặc 'nộp phạt nguội', đối tượng gửi tệp .apk ngoài Google Play/App Store và hướng dẫn nạn nhân bật quyền Trợ năng (Accessibility). Khi quyền này được cấp, mã độc tự động đọc trộm mã OTP và thao tác chuyển tiền ngầm.",
                "Lừa đảo tuyển dụng và Xuất khẩu lao động (XKLĐ): Quảng cáo 'visa bao đậu', 'bay nhanh chi phí thấp, lương 40–60 triệu/tháng', giả danh doanh nghiệp uy tín để phỏng vấn online rồi yêu cầu chuyển tiền đặt cọc, phí khám sức khỏe, chứng minh tài chính sau đó chặn liên lạc."
            ]
        },
        {
            "heading": "6. Tổng hợp 4 nhóm dấu hiệu nhận biết sớm (Cảnh báo đỏ)",
            "bullets": [
                "Tâm lý bất thường: Luôn tạo áp lực thời gian cực ngắn ('trong 15 phút', 'không chuyển sẽ bị bắt/khóa thẻ') hoặc hứa hẹn lợi ích phi thực tế.",
                "Kênh liên hệ bất thường: Người xưng Công an, Thuế, Ngân hàng gọi bằng số di động thông thường hoặc kết bạn Zalo, gửi văn bản/lệnh bắt dạng ảnh chụp.",
                "Đường link và tệp cài đặt bất thường: Chứa đuôi tên miền lạ (.vip, .xyz, .cc, .top), lỗi chính tả tinh vi (thay chữ 'l' bằng số '1'), link rút gọn (bit.ly, cutt.ly) hoặc yêu cầu tải tệp .apk.",
                "Yêu cầu dữ liệu cấm: Hỏi mã OTP, mật khẩu đăng nhập ngân hàng, mã PIN, ảnh CCCD hai mặt hoặc yêu cầu bật quyền Trợ năng (Accessibility) cho ứng dụng lạ."
            ]
        },
        {
            "heading": "7. Nguồn tài liệu tham khảo & Trích dẫn chính thống",
            "bullets": [
                "Cục An toàn thông tin — Bộ TT&TT (06/2023), 'Cẩm nang nhận diện và phòng chống lừa đảo trực tuyến' (3 nhóm — 24 hình thức lừa đảo), Cổng Không gian mạng quốc gia: https://khonggianmang.vn.",
                "Ngân hàng Nhà nước Việt Nam (hiệu lực 01/07/2024), Quyết định số 2345/QĐ-NHNN về giải pháp an toàn, bảo mật trong thanh toán trực tuyến và thanh toán thẻ ngân hàng.",
                "Bộ Công an (2024–2025), Các thông báo cảnh báo thủ đoạn giả mạo ứng dụng VNeID, cài mã độc .apk và giả danh hỗ trợ sinh trắc học: https://bocongan.gov.vn.",
                "Cổng Thông tin điện tử Chính phủ (28/02/2025 – 01/03/2025), Thông tin bàn giao nhiệm vụ quản lý nhà nước về an toàn thông tin mạng về Cục A05 — Bộ Công an: https://baochinhphu.vn."
            ]
        }
    ]
}

KB2_DOC = {
    "filename_stem": "KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap",
    "code": "KB2",
    "title": "NGUYÊN TẮC PHÒNG TRÁNH, BẢO MẬT & QUY TRÌNH XỬ LÝ KHẨN CẤP 4 BƯỚC",
    "subtitle": "Tài liệu Cơ sở tri thức 2 — Phục vụ Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến",
    "meta": "Cập nhật: 2025 • Nguồn chính thống: Bộ Công an (Cục A05), Cổng Không gian mạng quốc gia, NHNN",
    "sections": [
        {
            "heading": "1. Các bộ nguyên tắc phòng tránh lừa đảo chính thống tại Việt Nam",
            "paragraphs": [
                "Để giúp mọi tầng lớp người dân (từ học sinh, sinh viên đến người cao tuổi) dễ ghi nhớ và áp dụng ngay trước khi giao dịch trực tuyến, Bộ Công an và Công an các địa phương phổ biến ba bộ quy tắc ngắn gọn nhưng toàn diện sau:"
            ],
            "table": {
                "headers": ["Bộ quy tắc", "Nội dung chi tiết cần ghi nhớ", "Tình huống áp dụng thực tế"],
                "rows": [
                    ["Quy tắc '3 Không'\n(Bộ Công an)", "1. Không tin tưởng tuyệt đối (kể cả cuộc gọi video có mặt, giọng người quen hay người xưng Công an, Thuế, Ngân hàng).\n2. Không cài đặt ứng dụng từ các liên kết lạ (tuyệt đối không tải tệp .apk ngoài Google Play / App Store).\n3. Không cung cấp thông tin cá nhân và không chuyển tiền khi chưa xác minh độc lập.", "Áp dụng nhanh trong mọi cuộc gọi lạ, tin nhắn khẩn cấp hoặc lời mời qua Zalo/Facebook."],
                    ["Quy tắc '4 Không - 2 Phải'", "4 KHÔNG:\n• Không chuyển tiền khi chưa xác minh rõ.\n• Không cung cấp thông tin cá nhân / OTP / CCCD.\n• Không truy cập đường link hoặc tệp đính kèm lạ.\n• Không nghe theo cuộc gọi giả mạo đe dọa.\n\n2 PHẢI:\n• Phải cảnh giác trước lời mời lợi nhuận cao hoặc thúc ép khẩn cấp.\n• Phải xác thực lại qua kênh độc lập (hotline chính thức hoặc số điện thoại lưu sẵn của người thân).", "Áp dụng khi gặp chiêu trò giả danh người thân cấp cứu, Deepfake, đầu tư tài chính hoặc CTV online."],
                    ["Quy tắc '5 Không - 5 Luôn'\n(Cục An ninh mạng - Bộ Công an)", "5 KHÔNG: Không chia sẻ dữ liệu cá nhân; Không tiết lộ mã OTP; Không bấm link/pop-up quảng cáo đáng ngờ; Không mở file lạ; Không làm theo yêu cầu chuyển tiền của người lạ.\n\n5 LUÔN: Luôn ý thức bảo mật thông tin; Luôn đặt mật khẩu mạnh và đổi định kỳ; Luôn dùng phần mềm có bản quyền, uy tín; Luôn cập nhật kiến thức an ninh mạng; Luôn cảnh giác cao độ khi giao dịch trực tuyến.", "Áp dụng thành thói quen an toàn số lâu dài cho cá nhân và gia đình."]
                ]
            }
        },
        {
            "heading": "2. Hướng dẫn bảo mật tài khoản, thiết bị và giao dịch ngân hàng",
            "paragraphs": [
                "Bên cạnh việc nâng cao cảnh giác tâm lý, người dùng cần thiết lập các lớp phòng vệ kỹ thuật cơ bản để giảm thiểu rủi ro bị chiếm đoạt tài khoản:"
            ],
            "bullets": [
                "Đặt mật khẩu mạnh và tách biệt: Mật khẩu dài tối thiểu 12 ký tự gồm chữ hoa, chữ thường, số và ký tự đặc biệt; tuyệt đối không dùng chung một mật khẩu cho Email, Ngân hàng và Mạng xã hội.",
                "Bật xác thực hai yếu tố (2FA): Kích hoạt 2FA cho Gmail/Outlook, Facebook, Zalo (mã PIN bảo vệ 2 lớp) và ví điện tử. Ưu tiên dùng ứng dụng tạo mã (Google Authenticator, Microsoft Authenticator) và tuyệt đối không đọc mã 2FA/OTP cho bất kỳ ai.",
                "Cập nhật sinh trắc học ngân hàng đúng kênh (Quyết định 2345/QĐ-NHNN): Chỉ tự thao tác trực tiếp bên trong ứng dụng Mobile Banking chính thức cài từ Google Play / App Store hoặc đến trực tiếp quầy giao dịch ngân hàng kèm CCCD gắn chip. Ngân hàng KHÔNG bao giờ cử nhân viên gọi Zalo hoặc gửi link/.apk nhờ cập nhật hộ.",
                "Kiểm tra tên miền và hiểu đúng về ổ khóa HTTPS: Đọc kỹ tên miền gốc (phần nằm ngay trước dấu '/' đầu tiên sau https://), tránh bị đánh lừa bởi tên miền phụ như 'vietcombank.khuyenmai2025.xyz'. Tên miền cơ quan nhà nước Việt Nam luôn có đuôi '.gov.vn'. Lưu ý: biểu tượng ổ khóa HTTPS chỉ cho biết đường truyền được mã hóa, KHÔNG chứng minh trang web đó là chính chủ.",
                "Không cấp quyền Trợ năng (Accessibility) bừa bãi trên Android: Tuyệt đối từ chối cài đặt tệp .apk gửi qua Zalo/trình duyệt và không bật quyền Trợ năng cho các ứng dụng không rõ nguồn gốc."
            ]
        },
        {
            "heading": "3. Quy trình xử lý khẩn cấp 4 bước khi nghi ngờ hoặc đã sập bẫy",
            "paragraphs": [
                "Nếu bạn hoặc người thân vừa lỡ chuyển tiền cho kẻ gian, vừa bấm vào đường link lạ, lỡ cài đặt tệp .apk hoặc lỡ cung cấp mã OTP/CCCD, hãy giữ bình tĩnh và thực hiện ngay 4 bước dưới đây theo thứ tự ưu tiên:"
            ],
            "table": {
                "headers": ["Bước", "Hành động khẩn cấp", "Thao tác chi tiết cần làm ngay"],
                "rows": [
                    ["Bước 1", "Ngắt kết nối mạng & Dừng giao dịch ngay", "• Lập tức dừng mọi thao tác chuyển tiền, không nhập hay đọc thêm bất kỳ mã OTP nào.\n• Nếu lỡ cài tệp .apk lạ trên điện thoại Android: Bật ngay Chế độ máy bay / Tắt Wi-Fi và 4G để cắt quyền điều khiển từ xa của mã độc, sau đó gỡ cài đặt ứng dụng lạ (nếu không gỡ được, sao lưu dữ liệu quan trọng và khôi phục cài đặt gốc)."],
                    ["Bước 2", "Liên hệ khẩn cấp Ngân hàng & Khóa tài khoản", "• Dùng điện thoại khác (hoặc sau khi đã ngắt mã độc) gọi ngay tới số Hotline chính thức in ở mặt sau thẻ ATM hoặc trên website chính thức của ngân hàng/ví điện tử.\n• Yêu cầu khóa khẩn cấp thẻ, khóa tài khoản Internet Banking/Mobile Banking và hỗ trợ tra soát giao dịch.\n• Lập tức đổi mật khẩu các tài khoản Email, Facebook, Zalo và bật xác thực 2FA."],
                    ["Bước 3", "Thu thập & Bảo toàn toàn bộ bằng chứng", "• Chụp màn hình toàn bộ nội dung tin nhắn chat (Zalo, Telegram, Facebook, SMS), đường link giả mạo, trang cá nhân/fanpage đối tượng.\n• Ghi lại số điện thoại gọi đến, file ghi âm cuộc gọi (nếu có), số tài khoản ngân hàng người nhận tiền, biên lai và sao kê chuyển khoản có dấu xác nhận của ngân hàng."],
                    ["Bước 4", "Trình báo Cơ quan Công an & Kênh chính thống", "• Đến trực tiếp Công an xã/phường/thị trấn nơi cư trú hoặc Phòng An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (PA05) Công an tỉnh/thành phố kèm CCCD và hồ sơ chứng cứ để lập biên bản tố giác.\n• Có thể gửi phản ánh qua ứng dụng VNeID (mục Kiến nghị, phản ánh về ANTT), gọi 113 / 069.219.4053 hoặc gửi email tới tiepnhantogiactoipham@mps.gov.vn.\n• Báo cáo SĐT/tin nhắn lừa đảo miễn phí tới tổng đài 156/5656 và báo cáo link/STK lên tinnhiemmang.vn, canhbao.khonggianmang.vn, chongluadao.vn, ứng dụng nTrust."]
                ]
            },
            "callout": {
                "title": "CẢNH BÁO ĐẶC BIỆT: TRÁNH BẪY LỪA ĐẢO LẦN 2 ('DỊCH VỤ LẤY LẠI TIỀN')",
                "text": "Ngay sau khi bị lừa, nhiều nạn nhân rơi vào trạng thái tuyệt vọng và tìm kiếm trên mạng các dịch vụ quảng cáo 'Luật sư / Công an mạng / Hacker mũ trắng hỗ trợ lấy lại tiền bị lừa'. Đây là bẫy lừa đảo thứ cấp nhằm chiếm đoạt thêm 'phí hồ sơ', 'phí giải ngân'. Cơ quan Công an KHÔNG thu phí qua mạng để điều tra và KHÔNG ủy quyền cho bất kỳ cá nhân/tổ chức nào nhận tiền hộ trên mạng xã hội."
            }
        },
        {
            "heading": "4. Nguồn tài liệu tham khảo & Trích dẫn chính thống",
            "bullets": [
                "Bộ Công an (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao) & Công an các địa phương, Khuyến cáo quy tắc '3 Không', '4 Không - 2 Phải' và '5 Không - 5 Luôn': https://bocongan.gov.vn.",
                "Cục An toàn thông tin — Bộ TT&TT (06/2023), 'Cẩm nang nhận diện và phòng chống lừa đảo trực tuyến', Cổng Không gian mạng quốc gia: https://khonggianmang.vn.",
                "Ngân hàng Nhà nước Việt Nam (01/07/2024), Quyết định số 2345/QĐ-NHNN về an toàn, bảo mật trong thanh toán trực tuyến.",
                "Bộ Công an — Hướng dẫn tố giác tội phạm qua ứng dụng VNeID và hộp thư chính thức tiepnhantogiactoipham@mps.gov.vn."
            ]
        }
    ]
}

KB3_DOC = {
    "filename_stem": "KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao",
    "code": "KB3",
    "title": "HƯỚNG DẪN SỬ DỤNG CÔNG CỤ KIỂM TRA & KÊNH TRÌNH BÁO CHÍNH THỐNG TẠI VIỆT NAM",
    "subtitle": "Tài liệu Cơ sở tri thức 3 — Phục vụ Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến",
    "meta": "Cập nhật sau chuyển giao 01/03/2025 • Nguồn chính thống: Chính phủ, Bộ Công an (A05), VNCERT, VNNIC, NCA",
    "sections": [
        {
            "heading": "1. Cập nhật cơ quan chủ trì an toàn thông tin mạng (Mốc 01/03/2025)",
            "paragraphs": [
                "Khi tư vấn cho người dân về cơ quan nhà nước chịu trách nhiệm tiếp nhận và xử lý an toàn thông tin mạng tại Việt Nam, cần lưu ý mốc chuyển giao thể chế quan trọng năm 2025:",
                "Ngày 28/02/2025, Bộ Công an và Bộ Thông tin và Truyền thông đã tổ chức Lễ ký kết bàn giao nhiệm vụ quản lý nhà nước về an toàn thông tin mạng (thực hiện theo Nghị định 02/2025/NĐ-CP ngày 18/02/2025). Từ ngày 01/03/2025, Cục An toàn thông tin (Bộ TT&TT cũ) chấm dứt hoạt động; toàn bộ chức năng, nhiệm vụ quản lý nhà nước về an toàn thông tin mạng và các hệ thống kỹ thuật liên quan được chuyển giao về Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) — Bộ Công an.",
                "Các cổng tra cứu, tiếp nhận phản ánh quốc gia như khonggianmang.vn, canhbao.khonggianmang.vn, tinnhiemmang.vn và đầu số 156/5656 tiếp tục vận hành phục vụ công tác phòng, chống tội phạm mạng và tích hợp trực tiếp với ứng dụng định danh quốc gia VNeID dưới sự quản lý thống nhất của Bộ Công an."
            ]
        },
        {
            "heading": "2. Danh bạ kênh trình báo & Đường dây nóng chính thức tại Việt Nam",
            "table": {
                "headers": ["Cơ quan / Kênh tiếp nhận", "Kênh liên hệ / Đầu số / Cú pháp chính thức", "Phạm vi tiếp nhận & Ghi chú"],
                "rows": [
                    ["Bộ Công an — Cục A05 & Công an địa phương", "• Cổng TTĐT: https://bocongan.gov.vn (mps.gov.vn)\n• Email tố giác tội phạm: tiepnhantogiactoipham@mps.gov.vn\n• Ứng dụng VNeID: Mục 'Kiến nghị, phản ánh về ANTT'\n• Đường dây nóng phản ánh ANM (PA05 Hà Nội / đầu số phổ biến): 069.219.4053\n• Cục Cảnh sát Hình sự: 0692.345.860\n• PA05 TP.HCM: 069.318.7200 / 0693.187.263\n• Khẩn cấp: 113", "Tiếp nhận trình báo hành vi lừa đảo chiếm đoạt tài sản, giả mạo cơ quan nhà nước, mã độc tống tiền. Khuyến nghị đến trực tiếp Công an xã/phường nơi cư trú để lập biên bản nhanh nhất."],
                    ["Tổng đài Quốc gia 156 / 5656\n(VNCERT/CC & Bộ Công an phối hợp nhà mạng)", "• Gọi điện miễn phí: 156\n• Nhắn tin SMS miễn phí tới 156 hoặc 5656:\n  – Cuộc gọi dấu hiệu lừa đảo: LD [Số ĐT nguồn] [Nội dung phản ánh]\n  – Cuộc gọi rác: V [Số ĐT nguồn] [Nội dung]\n  – Tin nhắn rác: S [Số ĐT nguồn] [Nội dung]", "Triển khai thí điểm từ 01/11/2022, miễn phí 100% cước gọi và tin nhắn cho thuê bao di động tại Việt Nam nhằm thống kê và chặn khóa số điện thoại lừa đảo."],
                    ["Trung tâm Internet Việt Nam (VNNIC) — Tra cứu tên miền", "• Website: https://tracuutenmien.gov.vn\n• Nhắn tin SMS miễn phí: TCTM [Tên miền hoặc link website] gửi 156", "Công bố từ 03/03/2023 giúp người dân xác thực chủ thể đăng ký tên miền chính thống trước khi giao dịch."],
                    ["Cổng Cảnh báo & Hệ sinh thái Tín nhiệm mạng", "• Cổng Không gian mạng: https://khonggianmang.vn\n• Cổng Cảnh báo VN: https://canhbao.khonggianmang.vn\n• Tín nhiệm mạng (Website): https://tinnhiemmang.vn/website-lua-dao\n• Tín nhiệm mạng (Số tài khoản): https://tinnhiemmang.vn/tra-cuu-tai-khoan", "Gửi phản ánh website giả mạo, mã độc, số tài khoản ngân hàng lừa đảo và tra cứu danh sách đen đã được cơ quan chức năng kiểm duyệt."]
                ]
            }
        },
        {
            "heading": "3. Hướng dẫn từng bước sử dụng các công cụ kiểm tra an toàn",
            "paragraphs": [
                "Trước khi bấm vào bất kỳ đường link lạ nào hoặc chuyển khoản cho người bán/đối tác chưa rõ danh tính, người dân nên kiểm tra chéo theo các bước sau:"
            ],
            "bullets": [
                "Công cụ 1 — Hệ thống Tín nhiệm mạng (tinnhiemmang.vn) và mục tra cứu trên VNeID: Truy cập https://tinnhiemmang.vn/website-lua-dao để nhập tên miền cần kiểm tra, hoặc truy cập https://tinnhiemmang.vn/tra-cuu-tai-khoan để nhập số tài khoản ngân hàng trước khi chuyển tiền (hệ thống trả về trạng thái An toàn / Lừa đảo / Đang xác minh). Ngoài ra, người dùng có thể mở ứng dụng VNeID để xem tin tức cảnh báo và tra cứu website lừa đảo.",
                "Công cụ 2 — Dự án Chống Lừa Đảo (chongluadao.vn): Truy cập https://chongluadao.vn/analyze, dán đường link nghi ngờ để hệ thống quét đánh giá độ an toàn; cài đặt tiện ích mở rộng (Extension) ChongLuaDao trên trình duyệt Chrome, Cốc Cốc hoặc Microsoft Edge để tự động chặn màn hình đỏ khi lỡ bấm link độc hại; hoặc nhắn tin trực tiếp cho Zalo OA có tích xanh 'Chống Lừa Đảo' (https://zalo.me/chongluadao) để kiểm tra nhanh link/ảnh.",
                "Công cụ 3 — Tra cứu chủ thể tên miền VNNIC (tracuutenmien.gov.vn & SMS 156): Vào https://tracuutenmien.gov.vn hoặc soạn tin nhắn miễn phí 'TCTM [Tên miền]' gửi 156 để biết đơn vị sở hữu tên miền. Nếu trang tự xưng ngân hàng hoặc cơ quan nhà nước Việt Nam nhưng chủ thể đăng ký là cá nhân ở nước ngoài hoặc tên miền mới tạo vài ngày, cần dừng giao dịch ngay.",
                "Công cụ 4 — Ứng dụng phòng chống lừa đảo nTrust (Hiệp hội An ninh mạng Quốc gia - NCA): Ra mắt ngày 30/07/2024, tải miễn phí trên App Store / Google Play (thông tin chính thức tại https://ntrust.vn và https://nca.org.vn). Sau khi đăng nhập bằng số điện thoại, người dùng sử dụng các chức năng: Kiểm tra SĐT, Kiểm tra Link, Kiểm tra Số tài khoản ngân hàng, Quét mã QR trước khi mở, Quét ứng dụng độc hại trên máy và bật chế độ tự động cảnh báo cuộc gọi nghi vấn.",
                "Công cụ 5 — Cổng kiến thức 'Dấu hiệu Lừa đảo' (dauhieuluadao.com / khonggianmang.vn): Ra mắt ngày 01/04/2022 từ hợp tác giữa NCSC và Google (bản địa hóa từ Scamspotter), giúp người dân luyện tập tình huống mô phỏng và làm trắc nghiệm nâng cao kỹ năng nhận diện.",
                "Lưu ý về các trang cộng đồng độc lập (scam.vn, checkscam.vn): Các website này hỗ trợ tra cứu lịch sử tố cáo SĐT/STK từ cộng đồng nhưng dữ liệu phụ thuộc vào người dùng tự đóng góp; chỉ nên sử dụng để tham khảo chéo bổ sung, không thay thế kết luận xác minh của Cơ quan Công an."
            ]
        },
        {
            "heading": "4. Bảng tra cứu nhanh theo nhu cầu của người dùng",
            "table": {
                "headers": ["Bạn muốn kiểm tra hoặc phản ánh gì?", "Công cụ / Kênh nên dùng ngay"],
                "rows": [
                    ["Kiểm tra đường link website lạ trước khi bấm", "tinnhiemmang.vn/website-lua-dao • chongluadao.vn/analyze • tracuutenmien.gov.vn • SMS: TCTM [Tên miền] gửi 156"],
                    ["Kiểm tra số tài khoản ngân hàng trước khi chuyển tiền", "tinnhiemmang.vn/tra-cuu-tai-khoan • Ứng dụng nTrust (NCA)"],
                    ["Kiểm tra & phản ánh số điện thoại / tin nhắn nghi lừa đảo", "Gọi miễn phí 156 • Nhắn tin LD [SĐT] [Nội dung] gửi 156/5656 • Ứng dụng nTrust"],
                    ["Quét ứng dụng .apk lạ hoặc mã QR đáng ngờ", "Tính năng Quét mã QR & Quét app độc hại trong ứng dụng nTrust"],
                    ["Trình báo khi đã bị thiệt hại tài sản / đe dọa", "Công an xã/phường hoặc PA05 địa phương • Ứng dụng VNeID • 113 • 069.219.4053 • tiepnhantogiactoipham@mps.gov.vn"]
                ]
            }
        },
        {
            "heading": "5. Nguồn tài liệu tham khảo & Trích dẫn chính thống",
            "bullets": [
                "Cổng Thông tin điện tử Chính phủ (28/02/2025 – 01/03/2025), Lễ ký kết bàn giao nhiệm vụ quản lý nhà nước về an toàn thông tin mạng sang Cục A05 — Bộ Công an và Nghị định 02/2025/NĐ-CP: https://baochinhphu.vn.",
                "Báo Điện tử Chính phủ (01/11/2022), 'Triển khai thí điểm đầu số 156 tiếp nhận phản ánh về cuộc gọi rác, cuộc gọi có dấu hiệu lừa đảo': https://baochinhphu.vn.",
                "Báo Điện tử Chính phủ (03/03/2023), 'Tra cứu thông tin tên miền qua đầu số 156 giúp phòng ngừa hành vi lừa đảo' (tracuutenmien.gov.vn): https://baochinhphu.vn.",
                "Báo Điện tử Chính phủ & Báo Nhân Dân (30/07/2024), 'Hiệp hội An ninh mạng quốc gia ra mắt phần mềm phòng chống lừa đảo nTrust': https://nca.org.vn, https://ntrust.vn.",
                "Hệ sinh thái Không gian mạng Quốc gia & Cảnh báo an toàn thông tin: https://khonggianmang.vn, https://canhbao.khonggianmang.vn, https://tinnhiemmang.vn.",
                "Dự án Chống Lừa Đảo: https://chongluadao.vn và Cổng kiến thức NCSC–Google (01/04/2022): https://dauhieuluadao.com."
            ]
        }
    ]
}


# ==============================================================================
# 2. DOCX HELPERS (python-docx)
# ==============================================================================

NAVY_HEX = "0F2744"
BLUE_HEX = "1D4ED8"
LIGHT_BLUE_HEX = "EFF6FF"
ALT_ROW_HEX = "F8FAFC"
CALLOUT_BG_HEX = "FEF2F2"
CALLOUT_BORDER_HEX = "B91C1C"
BORDER_HEX = "CBD5E1"


def set_cell_shading(cell, hex_color: str):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for side, val in [("top", top), ("bottom", bottom), ("left", left), ("right", right)]:
        node = OxmlElement(f"w:{side}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, color=BORDER_HEX, sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f"</w:tblBorders>"
    )
    tblPr.append(borders)


def add_page_number_footer(section, footer_label: str):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_left = p.add_run(f"{footer_label}   |   Trang ")
    run_left.font.size = Pt(9)
    run_left.font.color.rgb = RGBColor(100, 116, 139)

    fld1 = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls("w"))
    p._p.append(fld1)

    run_mid = p.add_run(" / ")
    run_mid.font.size = Pt(9)
    run_mid.font.color.rgb = RGBColor(100, 116, 139)

    fld2 = parse_xml(r'<w:fldSimple %s w:instr="NUMPAGES"/>' % nsdecls("w"))
    p._p.append(fld2)


def configure_docx_base(doc: Document, font_name: str, footer_label: str):
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(1.8)

    normal = doc.styles["Normal"]
    normal.font.name = font_name
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), font_name)
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(30, 41, 59)
    normal.paragraph_format.line_spacing = 1.35
    normal.paragraph_format.space_after = Pt(6)

    add_page_number_footer(section, footer_label)


def add_docx_table(doc: Document, headers: list[str], rows: list[list[str]], font_name: str, parse_markdown: bool = False):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)

    # Header row
    hdr_cells = table.rows[0].cells
    trPr = table.rows[0]._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:tblHeader"))
    for idx, text in enumerate(headers):
        cell = hdr_cells[idx]
        set_cell_shading(cell, NAVY_HEX)
        set_cell_margins(cell, top=110, bottom=110, left=130, right=130)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.2
        clean_hdr = strip_md_inline(text) if parse_markdown else text
        run = p.add_run(clean_hdr)
        run.bold = True
        run.font.name = font_name
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(255, 255, 255)

    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        r_trPr = row._tr.get_or_add_trPr()
        r_trPr.append(OxmlElement("w:cantSplit"))
        bg = ALT_ROW_HEX if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            set_cell_shading(cell, bg)
            set_cell_margins(cell, top=90, bottom=90, left=130, right=130)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.25
            if parse_markdown:
                add_formatted_runs(p, val, font_name, base_size=10)
                if c_idx == 0 and len(headers) >= 3 and len(strip_md_inline(val)) <= 6:
                    for r in p.runs:
                        r.bold = True
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                run = p.add_run(val)
                run.font.name = font_name
                run.font.size = Pt(10)
                if c_idx == 0 and len(headers) >= 3 and len(val) <= 6:
                    run.bold = True
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(4)


def add_docx_callout(doc: Document, title: str, text: str, font_name: str):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.rows[0].cells[0]
    set_cell_shading(cell, CALLOUT_BG_HEX)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=160)
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="FECACA"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="FECACA"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{CALLOUT_BORDER_HEX}"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="FECACA"/>'
        f"</w:tcBorders>"
    )
    tcPr.append(tcBorders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(4)
    r_title = p.add_run(title + "\n")
    r_title.bold = True
    r_title.font.name = font_name
    r_title.font.size = Pt(10.5)
    r_title.font.color.rgb = RGBColor(153, 27, 27)

    r_body = p.add_run(text)
    r_body.font.name = font_name
    r_body.font.size = Pt(10.5)
    r_body.font.color.rgb = RGBColor(69, 10, 10)

    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(4)


def build_kb_docx(kb_data: dict, out_path: Path):
    doc = Document()
    font_name = "Segoe UI"
    configure_docx_base(doc, font_name, f"{kb_data['code']} — Trợ lý AI phòng chống lừa đảo trực tuyến")

    # Header Banner Table
    banner = doc.add_table(rows=1, cols=1)
    banner.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = banner.rows[0].cells[0]
    set_cell_shading(cell, NAVY_HEX)
    set_cell_margins(cell, top=180, bottom=180, left=220, right=220)
    bp = cell.paragraphs[0]
    bp.paragraph_format.space_after = Pt(4)
    r0 = bp.add_run(f"{kb_data['code']} • KNOWLEDGE BASE COZE\n")
    r0.bold = True
    r0.font.name = font_name
    r0.font.size = Pt(9.5)
    r0.font.color.rgb = RGBColor(147, 197, 253)

    r1 = bp.add_run(kb_data["title"] + "\n")
    r1.bold = True
    r1.font.name = font_name
    r1.font.size = Pt(15)
    r1.font.color.rgb = RGBColor(255, 255, 255)

    r2 = bp.add_run(kb_data["subtitle"] + "\n" + kb_data["meta"])
    r2.font.name = font_name
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(226, 232, 240)

    doc.add_paragraph()

    for sec in kb_data["sections"]:
        hp = doc.add_paragraph()
        hp.paragraph_format.space_before = Pt(10)
        hp.paragraph_format.space_after = Pt(5)
        hp.paragraph_format.keep_with_next = True
        hr = hp.add_run(sec["heading"])
        hr.bold = True
        hr.font.name = font_name
        hr.font.size = Pt(13)
        hr.font.color.rgb = RGBColor(15, 39, 68)

        for para_text in sec.get("paragraphs", []):
            p = doc.add_paragraph(para_text)
            p.paragraph_format.space_after = Pt(5)

        for bullet_text in sec.get("bullets", []):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(4)
            if ":" in bullet_text and bullet_text.index(":") < 80:
                lead, rest = bullet_text.split(":", 1)
                rl = p.add_run(lead + ":")
                rl.bold = True
                rl.font.name = font_name
                rr = p.add_run(rest)
                rr.font.name = font_name
            else:
                r = p.add_run(bullet_text)
                r.font.name = font_name

        if "table" in sec:
            add_docx_table(doc, sec["table"]["headers"], sec["table"]["rows"], font_name)

        if "callout" in sec:
            add_docx_callout(doc, sec["callout"]["title"], sec["callout"]["text"], font_name)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


# ==============================================================================
# 3. HTML / CHROME HEADLESS PDF RENDERING
# ==============================================================================

PDF_BASE_CSS = """
@page {
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
  @bottom-right {
    content: "Trang " counter(page) " / " counter(pages);
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 9pt;
    color: #64748b;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: FONT_FAMILY_PLACEHOLDER;
  font-size: 10.5pt;
  line-height: 1.5;
  color: #1e293b;
}
.doc-banner {
  background: #0f2744;
  color: #ffffff;
  padding: 18px 22px;
  border-radius: 10px;
  margin-bottom: 16px;
}
.doc-banner .kicker {
  font-size: 9pt;
  font-weight: 700;
  color: #93c5fd;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}
.doc-banner h1 {
  margin: 0 0 6px;
  font-size: 16pt;
  line-height: 1.3;
  color: #ffffff;
}
.doc-banner .meta {
  font-size: 9.2pt;
  color: #e2e8f0;
}
h1, h2, h3, h4 {
  color: #0f2744;
  page-break-after: avoid;
}
h2 {
  font-size: 13pt;
  margin: 16px 0 8px;
  padding-bottom: 4px;
  border-bottom: 2px solid #dbeafe;
}
h3 {
  font-size: 11.2pt;
  margin: 12px 0 6px;
  color: #1e3a8a;
}
h4 {
  font-size: 10.5pt;
  margin: 10px 0 5px;
  color: #1e40af;
}
p {
  margin: 0 0 8px;
  text-align: left;
}
ul, ol {
  margin: 4px 0 10px;
  padding-left: 20px;
}
li {
  margin-bottom: 5px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0 14px;
  font-size: 9.5pt;
}
thead {
  display: table-header-group;
}
tr {
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #cbd5e1;
  padding: 7px 9px;
  vertical-align: top;
  text-align: left;
}
th {
  background-color: #0f2744;
  color: #ffffff;
  font-weight: 700;
}
tbody tr:nth-child(even) {
  background-color: #f8fafc;
}
.callout {
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  border-left: 5px solid #b91c1c;
  border-radius: 6px;
  padding: 10px 14px;
  margin: 10px 0 14px;
  page-break-inside: avoid;
}
.callout-title {
  font-weight: 700;
  color: #991b1b;
  margin-bottom: 4px;
}
blockquote {
  background-color: #eff6ff;
  border-left: 4px solid #1d4ed8;
  margin: 8px 0 12px;
  padding: 8px 12px;
  border-radius: 0 6px 6px 0;
}
pre {
  background-color: #0f172a;
  color: #e2e8f0;
  padding: 10px 12px;
  border-radius: 6px;
  font-family: Consolas, "Courier New", monospace;
  font-size: 8.8pt;
  white-space: pre-wrap;
  word-break: break-word;
  page-break-inside: avoid;
}
code {
  background-color: #eef2f7;
  padding: 1px 4px;
  border-radius: 4px;
  font-family: Consolas, "Courier New", monospace;
  font-size: 9pt;
  color: #0f172a;
}
pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}
hr {
  border: none;
  border-top: 1px solid #cbd5e1;
  margin: 14px 0;
}
.placeholder-box {
  background-color: #fffbeb;
  border: 1px dashed #d97706;
  color: #92400e;
  padding: 6px 10px;
  border-radius: 6px;
  font-weight: 700;
  display: inline-block;
  margin: 3px 0;
}
"""


def render_html_to_pdf(html_content: str, out_pdf: Path):
    if not CHROME_PATH.exists():
        raise FileNotFoundError(f"Google Chrome not found at {CHROME_PATH}")

    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as tmp:
        tmp.write(html_content)
        tmp_path = Path(tmp.name)

    try:
        cmd = [
            str(CHROME_PATH),
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}",
            tmp_path.as_uri(),
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if res.returncode != 0 or not out_pdf.exists():
            raise RuntimeError(f"Chrome PDF failed ({res.returncode}): {res.stderr}")
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def build_kb_pdf(kb_data: dict, out_path: Path):
    css = PDF_BASE_CSS.replace("FONT_FAMILY_PLACEHOLDER", '"Segoe UI", Arial, sans-serif')
    parts = [
        '<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">',
        f"<title>{html.escape(kb_data['title'])}</title>",
        f"<style>{css}</style></head><body>",
        '<div class="doc-banner">',
        f'<div class="kicker">{html.escape(kb_data["code"])} • KNOWLEDGE BASE COZE</div>',
        f'<h1>{html.escape(kb_data["title"])}</h1>',
        f'<div class="meta">{html.escape(kb_data["subtitle"])}<br>{html.escape(kb_data["meta"])}</div>',
        "</div>",
    ]

    for sec in kb_data["sections"]:
        parts.append(f"<h2>{html.escape(sec['heading'])}</h2>")
        for p in sec.get("paragraphs", []):
            parts.append(f"<p>{html.escape(p)}</p>")

        if sec.get("bullets"):
            parts.append("<ul>")
            for b in sec["bullets"]:
                if ":" in b and b.index(":") < 80:
                    lead, rest = b.split(":", 1)
                    parts.append(f"<li><strong>{html.escape(lead)}:</strong>{html.escape(rest)}</li>")
                else:
                    parts.append(f"<li>{html.escape(b)}</li>")
            parts.append("</ul>")

        if "table" in sec:
            tbl = sec["table"]
            parts.append("<table><thead><tr>")
            for h in tbl["headers"]:
                parts.append(f"<th>{html.escape(h)}</th>")
            parts.append("</tr></thead><tbody>")
            for row in tbl["rows"]:
                parts.append("<tr>")
                for idx, val in enumerate(row):
                    formatted = html.escape(val).replace("\n", "<br>")
                    if idx == 0 and len(tbl["headers"]) >= 3 and len(val) <= 6:
                        parts.append(f"<td style='text-align:center;font-weight:700;'>{formatted}</td>")
                    else:
                        parts.append(f"<td>{formatted}</td>")
                parts.append("</tr>")
            parts.append("</tbody></table>")

        if "callout" in sec:
            co = sec["callout"]
            parts.append(
                f'<div class="callout"><div class="callout-title">{html.escape(co["title"])}</div>'
                f'<div>{html.escape(co["text"])}</div></div>'
            )

    parts.append("</body></html>")
    render_html_to_pdf("".join(parts), out_path)


# ==============================================================================
# 4. MARKDOWN -> HTML / DOCX CONVERTERS FOR COZE GUIDE & GROUP REPORT
# ==============================================================================

def inline_md_to_html(text: str) -> str:
    # Escape HTML first, protect inline code spans, then convert bold/italic cleanly
    escaped = html.escape(text)
    code_spans = []

    def _save_code(match):
        code_spans.append(f"<code>{match.group(1)}</code>")
        return f"\x00CODE{len(code_spans) - 1}\x00"

    escaped = re.sub(r"`([^`]+)`", _save_code, escaped)
    escaped = re.sub(r"\*\*((?:[^*]|\*(?!\*))+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", escaped)
    for idx, code_html in enumerate(code_spans):
        escaped = escaped.replace(f"\x00CODE{idx}\x00", code_html)
    escaped = re.sub(r"(\[CHÈN [^\]]+\]|\[ĐIỀN [^\]]+\]|\[Điền [^\]]+\]|\[MSSV\]|\[Đạt [^\]]+\])", r'<span class="placeholder-box">\1</span>', escaped)
    escaped = escaped.replace("&lt;br&gt;", "<br>")
    return escaped


def md_to_html_document(md_text: str, title: str, kicker: str, font_family: str) -> str:
    css = PDF_BASE_CSS.replace("FONT_FAMILY_PLACEHOLDER", font_family)
    lines = md_text.splitlines()
    out = [
        '<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">',
        f"<title>{html.escape(title)}</title>",
        f"<style>{css}</style></head><body>",
        '<div class="doc-banner">',
        f'<div class="kicker">{html.escape(kicker)}</div>',
        f'<h1>{html.escape(title)}</h1>',
        '<div class="meta">Dự án: Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến</div>',
        "</div>",
    ]

    i = 0
    in_ul = False
    ul_li_open = False
    ul_sub_ol = False
    in_ol = False
    ol_li_open = False
    ol_sub_ul = False

    def close_lists():
        nonlocal in_ul, ul_li_open, ul_sub_ol, in_ol, ol_li_open, ol_sub_ul
        if ol_sub_ul:
            out.append("</ul>")
            ol_sub_ul = False
        if ol_li_open:
            out.append("</li>")
            ol_li_open = False
        if in_ol:
            out.append("</ol>")
            in_ol = False
        if ul_sub_ol:
            out.append("</ol>")
            ul_sub_ol = False
        if ul_li_open:
            out.append("</li>")
            ul_li_open = False
        if in_ul:
            out.append("</ul>")
            in_ul = False

    while i < len(lines):
        line = lines[i]
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        # Skip top-level H1 already displayed in banner
        if i == 0 and stripped.startswith("# "):
            i += 1
            continue

        # Code block (supports nested code blocks inside active <ol> items)
        if stripped.startswith("```"):
            is_nested_in_ol = indent >= 2 and in_ol and ol_li_open
            if is_nested_in_ol:
                if ol_sub_ul:
                    out.append("</ul>")
                    ol_sub_ul = False
            else:
                close_lists()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code_body = textwrap.dedent("\n".join(code_lines))
            out.append("<pre><code>" + html.escape(code_body) + "</code></pre>")
            i += 1
            continue

        # Horizontal rule
        if stripped == "---":
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        # Table
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|") and "---" in lines[i + 1]:
            close_lists()
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cols = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cols)
                i += 1
            out.append("<table><thead><tr>")
            for h in headers:
                out.append(f"<th>{inline_md_to_html(h)}</th>")
            out.append("</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>")
                for c in r:
                    out.append(f"<td>{inline_md_to_html(c)}</td>")
                out.append("</tr>")
            out.append("</tbody></table>")
            continue

        # Headings
        if stripped.startswith("#### "):
            close_lists()
            out.append(f"<h4>{inline_md_to_html(stripped[5:])}</h4>")
            i += 1
            continue
        if stripped.startswith("### "):
            close_lists()
            out.append(f"<h3>{inline_md_to_html(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("## "):
            close_lists()
            out.append(f"<h2>{inline_md_to_html(stripped[3:])}</h2>")
            i += 1
            continue
        if stripped.startswith("# "):
            close_lists()
            out.append(f"<h2>{inline_md_to_html(stripped[2:])}</h2>")
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            close_lists()
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + "<br>".join(inline_md_to_html(q) for q in quote_lines) + "</blockquote>")
            continue

        # Unordered list
        if re.match(r"^[-*•]\s+", stripped):
            item_text = re.sub(r"^[-*•]\s+", "", stripped)
            if indent >= 2 and in_ol and ol_li_open:
                if not ol_sub_ul:
                    out.append("<ul>")
                    ol_sub_ul = True
                out.append(f"<li>{inline_md_to_html(item_text)}</li>")
            else:
                if in_ol:
                    close_lists()
                if ul_sub_ol:
                    out.append("</ol>")
                    ul_sub_ol = False
                if not in_ul:
                    out.append("<ul>")
                    in_ul = True
                elif ul_li_open:
                    out.append("</li>")
                    ul_li_open = False
                out.append(f"<li>{inline_md_to_html(item_text)}")
                ul_li_open = True
            i += 1
            continue

        # Ordered list
        ol_match = re.match(r"^(\d+)\.\s+", stripped)
        if ol_match:
            num = int(ol_match.group(1))
            item_text = re.sub(r"^\d+\.\s+", "", stripped)
            if indent >= 2 and in_ul and ul_li_open:
                if not ul_sub_ol:
                    out.append("<ol>" if num == 1 else f'<ol start="{num}">')
                    ul_sub_ol = True
                out.append(f"<li>{inline_md_to_html(item_text)}</li>")
            else:
                if in_ul:
                    close_lists()
                if not in_ol:
                    out.append("<ol>" if num == 1 else f'<ol start="{num}">')
                    in_ol = True
                else:
                    if ol_sub_ul:
                        out.append("</ul>")
                        ol_sub_ul = False
                    if ol_li_open:
                        out.append("</li>")
                        ol_li_open = False
                out.append(f"<li>{inline_md_to_html(item_text)}")
                ol_li_open = True
            i += 1
            continue

        # Blank line
        if not stripped:
            close_lists()
            i += 1
            continue

        # Indented continuation line inside an open ordered-list item
        if indent >= 2 and in_ol and ol_li_open:
            if ol_sub_ul:
                out.append("</ul>")
                ol_sub_ul = False
            out.append(f"<br>{inline_md_to_html(stripped)}")
            i += 1
            continue

        # Normal paragraph
        close_lists()
        out.append(f"<p>{inline_md_to_html(stripped)}</p>")
        i += 1

    close_lists()
    out.append("</body></html>")
    return "".join(out)


def strip_md_inline(text: str) -> str:
    cleaned = text.replace("<br>", "\n")
    cleaned = re.sub(r"`([^`\n]+)`", r"\1", cleaned)
    cleaned = re.sub(r"\*\*((?:[^*\n]|\*(?!\*))+?)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)", r"\1", cleaned)
    return cleaned


_INLINE_MD_PATTERN = re.compile(
    r"(`[^`\n]+`|\*\*(?:[^*\n]|\*(?!\*))+?\*\*|(?<!\*)\*(?!\*)[^*\n]+?(?<!\*)\*(?!\*))"
)
_PLACEHOLDER_PATTERN = re.compile(
    r"(\[CHÈN [^\]]+\]|\[ĐIỀN [^\]]+\]|\[Điền [^\]]+\]|\[MSSV\]|\[Đạt [^\]]+\])"
)


def _emit_inline_runs(p, text: str, font_name: str, base_size: float, bold: bool = False, italic: bool = False, color: RGBColor | None = None):
    if not text:
        return
    tokens = _INLINE_MD_PATTERN.split(text)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith("`") and tok.endswith("`") and len(tok) >= 2:
            r = p.add_run(tok[1:-1])
            r.bold = bold
            r.italic = italic
            r.font.name = "Consolas"
            r.font.size = Pt(max(base_size - 1, 9))
            r.font.color.rgb = color if color is not None else RGBColor(15, 23, 42)
        elif tok.startswith("**") and tok.endswith("**") and len(tok) >= 4:
            _emit_inline_runs(p, tok[2:-2], font_name, base_size, bold=True, italic=italic, color=color)
        elif tok.startswith("*") and tok.endswith("*") and len(tok) >= 2:
            _emit_inline_runs(p, tok[1:-1], font_name, base_size, bold=bold, italic=True, color=color)
        else:
            parts = _PLACEHOLDER_PATTERN.split(tok)
            for part in parts:
                if not part:
                    continue
                r = p.add_run(part)
                r.bold = bold
                r.italic = italic
                r.font.name = font_name
                r.font.size = Pt(base_size)
                if color is not None:
                    r.font.color.rgb = color
                elif _PLACEHOLDER_PATTERN.fullmatch(part):
                    r.bold = True
                    r.font.color.rgb = RGBColor(180, 83, 9)


def add_formatted_runs(p, text: str, font_name: str, base_size=11, bold: bool = False, italic: bool = False, color: RGBColor | None = None):
    cleaned = text.replace("<br>", "\n")
    _emit_inline_runs(p, cleaned, font_name, base_size, bold=bold, italic=italic, color=color)


def md_to_docx(md_text: str, out_path: Path, title: str, subtitle: str, font_name: str = "Times New Roman"):
    doc = Document()
    configure_docx_base(doc, font_name, "Báo cáo Đồ án — Trợ lý AI phòng chống lừa đảo trực tuyến")

    # Academic Cover Banner
    banner = doc.add_table(rows=1, cols=1)
    banner.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = banner.rows[0].cells[0]
    set_cell_shading(cell, NAVY_HEX)
    set_cell_margins(cell, top=220, bottom=220, left=240, right=240)
    bp = cell.paragraphs[0]
    bp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    bp.paragraph_format.space_after = Pt(4)
    r1 = bp.add_run(title + "\n")
    r1.bold = True
    r1.font.name = font_name
    r1.font.size = Pt(16)
    r1.font.color.rgb = RGBColor(255, 255, 255)
    r2 = bp.add_run(subtitle)
    r2.font.name = font_name
    r2.font.size = Pt(11)
    r2.font.color.rgb = RGBColor(219, 234, 254)

    doc.add_paragraph()

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if i == 0 and stripped.startswith("# "):
            i += 1
            continue
        if stripped == "---":
            i += 1
            continue

        # Code block
        if stripped.startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            r = p.add_run("\n".join(code_lines))
            r.font.name = "Consolas"
            r.font.size = Pt(9.5)
            i += 1
            continue

        # Table
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|") and "---" in lines[i + 1]:
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cols = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cols)
                i += 1
            add_docx_table(doc, headers, rows, font_name, parse_markdown=True)
            continue

        # Headings
        if stripped.startswith("#### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(strip_md_inline(stripped[5:]))
            r.bold = True
            r.font.name = font_name
            r.font.size = Pt(11.5)
            r.font.color.rgb = RGBColor(30, 64, 175)
            i += 1
            continue

        if stripped.startswith("## "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(strip_md_inline(stripped[3:]))
            r.bold = True
            r.font.name = font_name
            r.font.size = Pt(13.5)
            r.font.color.rgb = RGBColor(15, 39, 68)
            i += 1
            continue

        if stripped.startswith("### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(strip_md_inline(stripped[4:]))
            r.bold = True
            r.font.name = font_name
            r.font.size = Pt(12)
            r.font.color.rgb = RGBColor(30, 58, 138)
            i += 1
            continue

        # Bullet / Ordered item
        if re.match(r"^[-*•]\s+", stripped):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(4)
            add_formatted_runs(p, re.sub(r"^[-*•]\s+", "", stripped), font_name)
            i += 1
            continue

        if re.match(r"^\d+\.\s+", stripped):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.paragraph_format.space_after = Pt(4)
            add_formatted_runs(p, stripped, font_name)
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        add_formatted_runs(p, stripped, font_name)
        i += 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


# ==============================================================================
# 5. MAIN BUILD ENTRYPOINT
# ==============================================================================

def main():
    print("=== Building Deliverables ===")

    # 1. Build KB1, KB2, KB3 (.docx and .pdf)
    kb_dir = ROOT_DIR / "01_Phan1_Chuan_Bi_Tai_Lieu"
    for kb in (KB1_DOC, KB2_DOC, KB3_DOC):
        docx_path = kb_dir / f"{kb['filename_stem']}.docx"
        pdf_path = kb_dir / f"{kb['filename_stem']}.pdf"
        build_kb_docx(kb, docx_path)
        build_kb_pdf(kb, pdf_path)
        print(f"Built {docx_path.name} and {pdf_path.name}")

    # 2. Build Coze Guide PDF
    guide_md_path = ROOT_DIR / "02_Phan2_3_Huong_Dan_Coze" / "Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md"
    guide_pdf_path = ROOT_DIR / "02_Phan2_3_Huong_Dan_Coze" / "Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.pdf"
    guide_md = guide_md_path.read_text(encoding="utf-8")
    guide_html = md_to_html_document(
        guide_md,
        title="HƯỚNG DẪN THỰC HÀNH COZE TOÀN TẬP (PHẦN 2 & PHẦN 3)",
        kicker="COZE.COM FREE TIER • TỪ TEAM SPACE ĐẾN PUBLISH & PHÂN QUYỀN NHÓM",
        font_family='"Segoe UI", Arial, sans-serif',
    )
    render_html_to_pdf(guide_html, guide_pdf_path)
    print(f"Built {guide_pdf_path.name}")

    # 3. Build Group Report DOCX & PDF
    report_md_path = ROOT_DIR / "04_Bao_Cao_Nhom" / "Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.md"
    report_docx_path = ROOT_DIR / "04_Bao_Cao_Nhom" / "Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.docx"
    report_pdf_path = ROOT_DIR / "04_Bao_Cao_Nhom" / "Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.pdf"
    report_md = report_md_path.read_text(encoding="utf-8")

    md_to_docx(
        report_md,
        report_docx_path,
        title="BÁO CÁO ĐỒ ÁN MÔN HỌC",
        subtitle='Đề tài: Xây dựng và tích hợp "Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến" trên nền tảng Coze',
        font_name="Times New Roman",
    )
    report_html = md_to_html_document(
        report_md,
        title="BÁO CÁO ĐỒ ÁN: TRỢ LÝ AI HỖ TRỢ NHẬN DIỆN VÀ PHÒNG TRÁNH LỪA ĐẢO TRỰC TUYẾN",
        kicker="BÁO CÁO NHÓM • PHẦN 1, PHẦN 2 VÀ PHẦN 3",
        font_family='"Times New Roman", "Segoe UI", serif',
    )
    render_html_to_pdf(report_html, report_pdf_path)
    print(f"Built {report_docx_path.name} and {report_pdf_path.name}")
    print("=== Build Complete ===")


if __name__ == "__main__":
    main()
