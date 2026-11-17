(function () {
  "use strict";

  var SCENARIOS = {
    police: {
      risk: "Rủi ro RẤT CAO — Giả danh Cơ quan Công an / Viện kiểm sát / Thuế",
      title: "Cuộc gọi đe dọa liên quan vụ án hoặc yêu cầu chuyển tiền xác minh",
      signs: [
        "Gọi bằng số di động cá nhân hoặc tài khoản Zalo lạ, gửi hình 'lệnh bắt' hoặc 'quyết định khởi tố' qua mạng.",
        "Đe dọa giữ bí mật tuyệt đối, không được nói với gia đình và thúc ép chuyển tiền vào 'tài khoản tạm giữ' để chứng minh vô tội.",
        "Hoặc xưng cán bộ Thuế/Công an yêu cầu cài ứng dụng lạ ngoài Google Play/App Store để hoàn thuế, nộp phạt nguội."
      ],
      actions: [
        "Ngắt cuộc gọi ngay lập tức; tuyệt đối KHÔNG chuyển tiền, KHÔNG cung cấp CCCD, OTP hay cài đặt tệp .apk.",
        "Ghi nhớ: Cơ quan Công an, Viện kiểm sát, Tòa án KHÔNG làm việc qua điện thoại/Zalo và KHÔNG bao giờ yêu cầu người dân chuyển tiền xác minh.",
        "Xác minh trực tiếp tại Công an xã/phường nơi cư trú hoặc phản ánh số điện thoại gọi tới đầu số miễn phí 156."
      ]
    },
    biometric: {
      risk: "Rủi ro RẤT CAO — Chiếm quyền điện thoại qua tệp .apk / Giả mạo sinh trắc học",
      title: "Giả danh ngân hàng hỗ trợ sinh trắc học (QĐ 2345) hoặc kích hoạt VNeID",
      signs: [
        "Gọi điện dọa khóa tài khoản nếu chưa cập nhật sinh trắc học khuôn mặt theo Quyết định 2345/QĐ-NHNN.",
        "Gửi đường link lạ qua SMS/Zalo hoặc gửi tệp cài đặt .apk trên Android yêu cầu cấp quyền Trợ năng (Accessibility).",
        "Đòi hỏi nhập mật khẩu ngân hàng, mã PIN hoặc đọc mã OTP qua điện thoại."
      ],
      actions: [
        "Việc cập nhật sinh trắc học CHỈ thực hiện trực tiếp trong ứng dụng Mobile Banking chính thức hoặc tại quầy giao dịch ngân hàng với CCCD gắn chip.",
        "Nếu đã lỡ tải hoặc cài file .apk lạ: lập tức ngắt Wi-Fi/4G (bật chế độ máy bay), gỡ ứng dụng lạ, gọi hotline ngân hàng khóa tài khoản.",
        "Trình báo qua ứng dụng VNeID chính thức, tổng đài 156 hoặc Công an địa phương."
      ]
    },
    ctv: {
      risk: "Rủi ro CAO — Lừa đảo tuyển Cộng tác viên (CTV) online",
      title: "Mời chào 'việc nhẹ lương cao', thả tim, chốt đơn ảo nhận hoa hồng",
      signs: [
        "Nhiệm vụ ban đầu rất dễ (like video, đánh giá sản phẩm) và được trả tiền thật 20.000–100.000đ để tạo lòng tin.",
        "Sau đó dụ tham gia nhóm Telegram/Zalo nâng cấp nhiệm vụ, yêu cầu nạp số tiền ngày càng lớn để hưởng hoa hồng 15–30%.",
        "Khi nạp tiền lớn, đối tượng báo 'lỗi cú pháp/sai hệ thống', liên tục ép nạp thêm tiền mới được rút."
      ],
      actions: [
        "Dừng ngay lập tức mọi thao tác nạp thêm tiền — kẻ lừa đảo sẽ không bao giờ cho rút tiền gốc nếu bạn tiếp tục nạp.",
        "Lưu toàn bộ ảnh chụp đoạn chat Telegram/Zalo, số tài khoản ngân hàng nhận tiền và sao kê chuyển khoản.",
        "Báo cáo số tài khoản lừa đảo lên tinnhiemmang.vn/tra-cuu-tai-khoan và trình báo Công an nơi gần nhất."
      ]
    },
    deepfake: {
      risk: "Rủi ro RẤT CAO — Cuộc gọi video Deepfake / Deepvoice giả người thân",
      title: "Người thân hoặc sếp gọi video ngắn chất lượng mờ nhờ chuyển tiền gấp",
      signs: [
        "Cuộc gọi video chỉ kéo dài vài giây, hình ảnh hơi giật, ánh sáng thiếu tự nhiên rồi tự ngắt với lý do 'mạng yếu'.",
        "Sau đó nhắn tin hối thúc chuyển tiền gấp (cấp cứu, trả nợ, mua hàng hộ) vào một số tài khoản ngân hàng tên người lạ."
      ],
      actions: [
        "KHÔNG chuyển tiền ngay dù nhìn thấy mặt hoặc nghe đúng giọng nói người quen.",
        "Chủ động gọi lại vào số điện thoại chính chủ đã lưu trong danh bạ hoặc hỏi một câu kiểm chứng riêng tư chỉ hai người biết.",
        "Cảnh báo ngay cho người thân bị mạo danh để họ đổi mật khẩu và cảnh giác bạn bè xung quanh."
      ]
    },
    travel: {
      risk: "Rủi ro CAO — Giả mạo Combo du lịch giá rẻ & 'Dịch vụ lấy lại tiền'",
      title: "Bán vé máy bay/resort giảm giá 50–70% hoặc quảng cáo thu hồi tiền bị lừa",
      signs: [
        "Fanpage có nhiều tương tác ảo, giả mạo tên khách sạn/resort nổi tiếng, yêu cầu chuyển khoản đặt cọc 50–100% để giữ khuyến mãi.",
        "Sau khi chuyển tiền, đối tượng chặn liên lạc hoặc đòi đóng thêm phí xuất hóa đơn.",
        "Xuất hiện các trang quảng cáo 'luật sư/công an mạng hỗ trợ lấy lại tiền bị lừa' yêu cầu đóng phí hồ sơ trước."
      ],
      actions: [
        "Kiểm tra tên miền website trên tracuutenmien.gov.vn hoặc gửi tin nhắn TCTM [Tên miền] tới 156; kiểm tra STK tại tinnhiemmang.vn.",
        "Tuyệt đối tránh bẫy lừa đảo lần 2 từ các dịch vụ 'lấy lại tiền bị lừa' trên mạng xã hội.",
        "Liên hệ ngân hàng hỗ trợ tra soát và nộp hồ sơ tố giác trực tiếp cho Cơ quan Công an."
      ]
    }
  };

  function renderScenario(key) {
    var box = document.getElementById("scenario-output");
    var data = SCENARIOS[key];
    if (!box || !data) {
      return;
    }

    var signsHtml = data.signs.map(function (item) {
      return "<li>" + item + "</li>";
    }).join("");

    var actionsHtml = data.actions.map(function (item) {
      return "<li>" + item + "</li>";
    }).join("");

    box.innerHTML =
      '<span class="risk-tag">' + data.risk + "</span>" +
      "<h3>" + data.title + "</h3>" +
      '<p style="margin:6px 0;font-weight:700;color:#0f2744;">Dấu hiệu nhận biết:</p>' +
      '<ul class="scenario-list">' + signsHtml + "</ul>" +
      '<p style="margin:6px 0;font-weight:700;color:#047857;">Hành động khuyến nghị:</p>' +
      '<ul class="scenario-list">' + actionsHtml + "</ul>";
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function setupScenarioTabs() {
    var buttons = document.querySelectorAll(".scenario-btn");
    var outputBox = document.getElementById("scenario-output");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (other) {
          other.classList.remove("active");
          other.setAttribute("aria-selected", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-selected", "true");
        if (outputBox && btn.id) {
          outputBox.setAttribute("aria-labelledby", btn.id);
        }
        renderScenario(btn.getAttribute("data-scenario"));
      });
    });
    renderScenario("police");
  }

  function isRawIpHostname(hostname) {
    if (!hostname) {
      return false;
    }
    if (hostname.indexOf(":") !== -1 || (hostname.charAt(0) === "[" && hostname.charAt(hostname.length - 1) === "]")) {
      return true;
    }
    return /^\d{1,3}(\.\d{1,3}){3}$/.test(hostname);
  }

  function matchesDomainOrSubdomain(hostname, domain) {
    return hostname === domain || hostname.slice(-(domain.length + 1)) === "." + domain;
  }

  function parseCandidateUrl(raw) {
    if (!raw || /\s|[<>"'`]/.test(raw)) {
      return { ok: false, reason: "Đầu vào không phải là đường link hoặc tên miền hợp lệ (chứa khoảng trắng hoặc ký tự đặc biệt)." };
    }
    if (/^(javascript|data|vbscript):/i.test(raw)) {
      return { ok: false, dangerousScheme: true, reason: "Đường dẫn sử dụng giao thức nguy hiểm (javascript:/data:/vbscript:) — tuyệt đối không mở." };
    }
    var hasScheme = /^[a-zA-Z][a-zA-Z0-9+.-]*:\/\//.test(raw);
    if (hasScheme && !/^https?:\/\//i.test(raw)) {
      return { ok: false, reason: "Chỉ hỗ trợ kiểm tra đường dẫn web bắt đầu bằng http:// hoặc https://." };
    }
    var candidate = hasScheme ? raw : "https://" + raw;
    try {
      var parsed = new URL(candidate);
      var hostname = (parsed.hostname || "").toLowerCase().replace(/\.$/, "");
      if (!hostname) {
        return { ok: false, reason: "Không xác định được tên miền từ đường dẫn đã nhập." };
      }
      var isIp = isRawIpHostname(hostname);
      if (!isIp) {
        if (hostname.indexOf(".") === -1 || /^\.|\.\./.test(hostname) || !/\.[a-z0-9-]{2,}$/i.test(hostname)) {
          return { ok: false, reason: "Tên miền chưa đúng định dạng (ví dụ hợp lệ: https://dichvucong.gov.vn hoặc vietcombank.com.vn)." };
        }
      }
      return { ok: true, parsed: parsed, hostname: hostname, isIp: isIp, explicitHttp: /^http:\/\//i.test(raw) };
    } catch (e) {
      return { ok: false, reason: "Đường link hoặc tên miền không đúng cú pháp URL." };
    }
  }

  function setupUrlChecker() {
    var form = document.getElementById("url-check-form");
    var input = document.getElementById("url-input");
    var resultBox = document.getElementById("url-result");
    if (!form || !input || !resultBox) {
      return;
    }

    var SHORTENERS = ["bit.ly", "tinyurl.com", "cutt.ly", "rb.gy", "t.co", "goo.gl", "is.gd", "shorturl.at"];
    var OFFICIAL_BANKS = [
      { kw: "vietcombank", domains: ["vietcombank.com.vn"] },
      { kw: "bidv", domains: ["bidv.com.vn"] },
      { kw: "techcombank", domains: ["techcombank.com", "techcombank.com.vn"] },
      { kw: "mbbank", domains: ["mbbank.com.vn"] },
      { kw: "vietinbank", domains: ["vietinbank.vn"] },
      { kw: "agribank", domains: ["agribank.com.vn"] },
      { kw: "acb", domains: ["acb.com.vn"], wordBoundaryOnly: true },
      { kw: "vpbank", domains: ["vpbank.com.vn"] },
      { kw: "tpbank", domains: ["tpb.vn", "tpbank.vn"] },
      { kw: "sacombank", domains: ["sacombank.com.vn"] }
    ];
    var TYPO_PATTERNS = [
      /vne1d/i,
      /vietc0mbank/i,
      /b0congan/i,
      /dichvuc0ng/i,
      /techc0mbank/i,
      /sac0mbank/i,
      /b1dv/i,
      /agrib4nk/i,
      /vietinb4nk/i,
      /ch1nhphu/i,
      /\.g0v\.vn$/i
    ];

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var raw = (input.value || "").trim();
      resultBox.className = "url-result show";

      if (!raw) {
        resultBox.classList.add("warn");
        resultBox.textContent = "Vui lòng nhập một đường link hoặc tên miền để kiểm tra sơ bộ.";
        return;
      }

      var check = parseCandidateUrl(raw);
      if (!check.ok) {
        resultBox.classList.add(check.dangerousScheme ? "danger" : "warn");
        resultBox.textContent = check.reason;
        return;
      }

      var parsed = check.parsed;
      var hostname = check.hostname;
      var pathname = (parsed.pathname || "").toLowerCase();
      var fullLower = parsed.href.toLowerCase();
      var warnings = [];

      if (check.isIp) {
        warnings.push("Đường link dùng địa chỉ IP trực tiếp (" + escapeHtml(hostname) + ") thay cho tên miền chính thức — dấu hiệu rủi ro cao của trang giả mạo hoặc phát tán mã độc.");
      }

      if (pathname.slice(-4) === ".apk" || /\.apk(\b|$|\?|#)/i.test(fullLower)) {
        warnings.push("Đường link trỏ tới tệp cài đặt .apk ngoài kho ứng dụng chính thức — nguy cơ cao chứa mã độc đánh cắp OTP/chiếm quyền điện thoại.");
      }

      if (check.explicitHttp) {
        warnings.push("Sử dụng giao thức http:// không mã hóa dữ liệu.");
      }

      if (/\.(vip|xyz|cc|top|tk|click|cfd|icu|buzz)$/i.test(hostname)) {
        warnings.push("Sử dụng đuôi tên miền lạ thường gặp trong các chiến dịch giả mạo (.xyz, .vip, .cc, .top, .tk, .click...).");
      }

      if (SHORTENERS.some(function (domain) { return matchesDomainOrSubdomain(hostname, domain); })) {
        warnings.push("Là đường link rút gọn che giấu địa chỉ đích thực tế.");
      }

      if (/\.gov\.vn\./i.test(hostname)) {
        warnings.push("Tên miền '" + escapeHtml(hostname) + "' chèn '.gov.vn' vào giữa để đánh lừa thị giác, nhưng tên miền gốc thực sự KHÔNG phải .gov.vn.");
      }

      var isOfficialGov =
        matchesDomainOrSubdomain(hostname, "gov.vn") ||
        matchesDomainOrSubdomain(hostname, "chinhphu.vn") ||
        matchesDomainOrSubdomain(hostname, "baochinhphu.vn");

      if (/(vneid|dichvucong|bocongan|chinhphu|tongcucthue|gdt|thue|bhxh|toaan|vienkiemsat)/i.test(hostname) && !isOfficialGov) {
        warnings.push("Tên miền '" + escapeHtml(hostname) + "' chứa từ khóa cơ quan nhà nước/dịch vụ công nhưng không thuộc tên miền chính thức .gov.vn — cần hết sức cảnh giác giả mạo.");
      }

      OFFICIAL_BANKS.forEach(function (bank) {
        var boundaryRegex = new RegExp("(^|[.-])" + bank.kw + "([.-]|$)", "i");
        var matchedKw = bank.wordBoundaryOnly
          ? boundaryRegex.test(hostname)
          : (hostname.indexOf(bank.kw) !== -1 || boundaryRegex.test(hostname));
        if (matchedKw) {
          var isOfficialBank = bank.domains.some(function (d) {
            return matchesDomainOrSubdomain(hostname, d);
          });
          if (!isOfficialBank) {
            warnings.push("Tên miền '" + escapeHtml(hostname) + "' chứa từ khóa ngân hàng (" + bank.kw + ") nhưng KHÔNG khớp tên miền chính thức (" + bank.domains.join(", ") + ") — nguy cơ cao trang giả mạo.");
          }
        }
      });

      if (TYPO_PATTERNS.some(function (re) { return re.test(hostname); })) {
        warnings.push("Phát hiện dấu hiệu giả mạo chữ cái bằng số (typosquatting) trong tên miền '" + escapeHtml(hostname) + "'.");
      }

      if (warnings.length > 0) {
        resultBox.classList.add("danger");
        resultBox.innerHTML =
          "<strong>Cảnh báo phát hiện " + warnings.length + " dấu hiệu nghi vấn (tên miền đích: <code>" + escapeHtml(hostname) + "</code>):</strong><ul style='margin:6px 0 0;padding-left:18px;'>" +
          warnings.map(function (w) { return "<li>" + w + "</li>"; }).join("") +
          "</ul><div style='margin-top:8px;'>Khuyến nghị: Không bấm link hoặc nhập mật khẩu; hãy kiểm tra lại tại <code>tinnhiemmang.vn</code>, <code>chongluadao.vn/analyze</code> hoặc nhắn <code>TCTM [Tên miền]</code> gửi <code>156</code>.</div>";
      } else {
        resultBox.classList.add("ok");
        resultBox.innerHTML =
          "<strong>Chưa phát hiện dấu hiệu hình thức bất thường rõ rệt (tên miền đích: <code>" + escapeHtml(hostname) + "</code>).</strong> Tuy nhiên, không nên chủ quan — luôn đối chiếu tên miền gốc chính thức qua <code>tracuutenmien.gov.vn</code>, <code>tinnhiemmang.vn</code> hoặc ứng dụng <code>nTrust</code> trước khi đăng nhập hay chuyển tiền.";
      }
    });
  }

  function initCozeSdkIfConfigured() {
    var cfg = window.COZE_CHATBOT_CONFIG;
    var statusBox = document.getElementById("coze-status-box");
    var statusTitle = document.getElementById("coze-status-title");
    var statusDesc = document.getElementById("coze-status-desc");
    var statusPill = document.getElementById("coze-status-pill");

    if (!cfg || !statusBox) {
      return;
    }

    var botId = typeof cfg.botId === "string" ? cfg.botId.trim() : "";
    var token = typeof cfg.token === "string" ? cfg.token.trim() : "";
    var hasValidBot = Boolean(botId) && botId !== "YOUR_COZE_BOT_ID";
    var hasValidToken = Boolean(token) && token !== "YOUR_COZE_PAT_TOKEN";

    if (cfg.enabled !== true || !hasValidBot || !hasValidToken) {
      statusBox.className = "status-box pending";
      statusTitle.textContent = "Trạng thái tích hợp Coze: Chờ cấu hình bot_id & token";
      statusPill.textContent = "Chưa kích hoạt SDK";
      return;
    }

    statusBox.className = "status-box ready";
    statusTitle.textContent = "Trạng thái tích hợp Coze: Đã cấu hình — Đang nạp Web SDK";
    statusDesc.textContent = "Đang kết nối tới Bot ID " + botId + ". Bong bóng chat Trợ lý AI sẽ hiển thị ở góc dưới bên phải.";
    statusPill.textContent = "Đã bật SDK";

    var resolvedLayout = cfg.layout === "auto"
      ? (window.innerWidth < 768 ? "mobile" : "pc")
      : (cfg.layout || "pc");

    var script = document.createElement("script");
    script.src = cfg.sdkUrl;
    script.async = true;
    script.onload = function () {
      if (window.CozeWebSDK && typeof window.CozeWebSDK.WebChatClient === "function") {
        new window.CozeWebSDK.WebChatClient({
          config: {
            bot_id: botId
          },
          auth: {
            type: "token",
            token: token,
            onRefreshToken: function () {
              return token;
            }
          },
          componentProps: {
            title: cfg.title || "Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"
          },
          ui: {
            base: {
              layout: resolvedLayout,
              lang: cfg.lang || "en"
            }
          }
        });
        statusTitle.textContent = "Trạng thái tích hợp Coze: Đang hoạt động trực tuyến";
        statusPill.textContent = "Đã kết nối";
      }
    };
    script.onerror = function () {
      statusBox.className = "status-box pending";
      statusTitle.textContent = "Không tải được Coze Web SDK từ CDN";
      statusDesc.textContent = "Vui lòng kiểm tra kết nối Internet hoặc cập nhật lại sdkUrl từ tab Publish -> Chat SDK -> Installation trên coze.com.";
      statusPill.textContent = "Lỗi kết nối SDK";
    };
    document.body.appendChild(script);
  }

  document.addEventListener("DOMContentLoaded", function () {
    setupScenarioTabs();
    setupUrlChecker();
    initCozeSdkIfConfigured();
  });
})();
