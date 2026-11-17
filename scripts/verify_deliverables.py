# -*- coding: utf-8 -*-
"""
Automated verification suite for:
"Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"
"""

import functools
import http.server
import re
import socketserver
import threading
from pathlib import Path

from docx import Document
from pypdf import PdfReader
from playwright.sync_api import sync_playwright

ROOT_DIR = Path(__file__).resolve().parent.parent
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CANONICAL_NAME = "Trợ lý AI hỗ trợ nhận diện và phòng tránh lừa đảo trực tuyến"

REQUIRED_FILES = [
    "README.md",
    "01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze.md",
    "01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze_Paste.txt",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.docx",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.pdf",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.docx",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.pdf",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.docx",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.pdf",
    "02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md",
    "02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.pdf",
    "03_Website_Tich_Hop/index.html",
    "03_Website_Tich_Hop/styles.css",
    "03_Website_Tich_Hop/coze-config.js",
    "03_Website_Tich_Hop/app.js",
    "04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.md",
    "04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.docx",
    "04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.pdf",
    "scripts/build_deliverables.py",
    "scripts/verify_deliverables.py",
]

DOCX_FILES = [
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.docx",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.docx",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.docx",
    "04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.docx",
]

PDF_FILES = [
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB1_Cac_Hinh_Thuc_Lua_Dao_Truc_Tuyen.pdf",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB2_Nguyen_Tac_Phong_Tranh_Va_Xu_Ly_Khan_Cap.pdf",
    "01_Phan1_Chuan_Bi_Tai_Lieu/KB3_Cong_Cu_Kiem_Tra_Va_Kenh_Trinh_Bao.pdf",
    "02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.pdf",
    "04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.pdf",
]


def has_vietnamese_diacritics(text: str) -> bool:
    return any(ch in text for ch in "ăâđêôơưĂÂĐÊÔƠƯáàảãạéèẻẽẹíìỉĩịóòỏõọúùủũụýỳỷỹỵ")


def verify_required_files():
    print("[1/5] Checking required file layout...")
    for rel in REQUIRED_FILES:
        p = ROOT_DIR / rel
        assert p.exists(), f"Missing file: {p}"
        assert p.stat().st_size > 0, f"Empty file: {p}"
    print(f"  OK: All {len(REQUIRED_FILES)} files present and non-empty.")


def verify_consistency():
    print("[2/5] Checking cross-deliverable consistency...")
    targets = [
        "README.md",
        "01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze.md",
        "01_Phan1_Chuan_Bi_Tai_Lieu/Persona_Va_Prompt_Coze_Paste.txt",
        "02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md",
        "03_Website_Tich_Hop/index.html",
        "04_Bao_Cao_Nhom/Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.md",
    ]
    for rel in targets:
        content = (ROOT_DIR / rel).read_text(encoding="utf-8")
        assert CANONICAL_NAME in content, f"Canonical agent name missing in {rel}"
        for token in ("156", "tinnhiemmang.vn", "chongluadao.vn", "nTrust", "VNeID"):
            assert token in content, f"Expected token '{token}' missing in {rel}"
        assert "Lorem ipsum" not in content and "TODO" not in content, f"Placeholder/TODO text found in {rel}"

    # Verify >= 8 Vietnamese test prompts (T1..T10) in Coze guide
    guide_text = (ROOT_DIR / "02_Phan2_3_Huong_Dan_Coze/Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.md").read_text(encoding="utf-8")
    for idx in range(1, 11):
        assert f"**T{idx}**" in guide_text, f"Missing test prompt T{idx} in Coze guide"
    print("  OK: Agent name, core channels, and 10 Vietnamese test prompts verified.")


def verify_docx_files():
    print("[3/5] Verifying DOCX files with python-docx...")
    for rel in DOCX_FILES:
        p = ROOT_DIR / rel
        doc = Document(str(p))
        chunks = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
        for tbl in doc.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    for cp in cell.paragraphs:
                        if cp.text.strip():
                            chunks.append(cp.text.strip())
        full_text = "\n".join(chunks)
        assert len(full_text) > 1000, f"DOCX text too short in {rel}: {len(full_text)} chars"
        assert has_vietnamese_diacritics(full_text), f"No Vietnamese diacritics found in {rel}"
        assert "`" not in full_text, f"Leaked backtick found in {rel}"

        if rel.endswith("Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.docx"):
            assert "**" not in full_text, f"Leaked '**' bold marker found in {rel}"
            italic_leaks = re.findall(r"(?<!\*)\*(?!\*)[^*\n]+(?<!\*)\*(?!\*)", full_text)
            assert not italic_leaks, f"Leaked '*...*' italic markers in {rel}: {italic_leaks[:5]}"

        print(f"  OK: {rel} ({len(doc.paragraphs)} paragraphs, {len(doc.tables)} tables, {len(full_text)} chars)")


def verify_pdf_files():
    print("[4/5] Verifying PDF files with pypdf...")
    for rel in PDF_FILES:
        p = ROOT_DIR / rel
        reader = PdfReader(str(p))
        num_pages = len(reader.pages)
        assert num_pages >= 2, f"PDF page count unexpectedly low in {rel}: {num_pages}"
        total_chars = 0
        pages_text = []
        for idx, page in enumerate(reader.pages):
            txt = (page.extract_text() or "").strip()
            assert len(txt) > 50, f"Page {idx + 1} in {rel} has too little extracted text ({len(txt)} chars)"
            assert has_vietnamese_diacritics(txt), f"Page {idx + 1} in {rel} missing Vietnamese diacritics"
            assert "#### " not in txt, f"Leaked '#### ' heading on page {idx + 1} in {rel}"
            pages_text.append(txt)
            total_chars += len(txt)

        joined_text = re.sub(r"\s+", " ", "\n".join(pages_text))
        if rel.endswith("Huong_Dan_Thuc_Hanh_Coze_Toan_Tap.pdf"):
            for expected_step in (
                "1. Hạn mức Coze Credits",
                "2. Hạn mức Web SDK",
                "3. Giới hạn cộng tác",
                "1. Truy cập",
                "2. Tại thanh bên trái",
                "3. Điền thông tin",
                "4. Chắc chắn rằng",
                "1. Tại cột giữa",
                "2. Thêm Plugin tìm kiếm web",
                "3. Thêm Plugin tạo ảnh",
                "4. Kiểm tra lại",
                "1. Sau khi kiểm thử",
                "2. Điền thông tin phát hành",
                "3. Ở phần chọn kênh",
                "4. Bấm Publish",
            ):
                assert expected_step in joined_text, f"Ordered-list step '{expected_step}' missing/reset in {rel}"

        if rel.endswith("Bao_Cao_Du_An_Tro_Ly_AI_Chong_Lua_Dao.pdf"):
            for expected_item in (
                "1. Vai trò",
                "2. Ba chức năng",
                "3. Giọng điệu",
                "4. Quy tắc định tuyến",
                "5. Quy trình phản hồi chuẩn",
                "6. Ranh giới an toàn nghiêm ngặt",
                "1. KB1_",
                "2. KB2_",
                "3. KB3_",
            ):
                assert expected_item in joined_text, f"Ordered-list item '{expected_item}' missing/reset in {rel}"

        print(f"  OK: {rel} ({num_pages} pages, {total_chars} extracted chars)")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def verify_webpage_playwright():
    print("[5/5] Verifying 03_Website_Tich_Hop over HTTP with Playwright + Chrome headless...")
    web_dir = ROOT_DIR / "03_Website_Tich_Hop"
    handler = functools.partial(QuietHandler, directory=str(web_dir))

    with socketserver.TCPServer(("127.0.0.1", 0), handler) as httpd:
        port = httpd.server_address[1]
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        base_url = f"http://127.0.0.1:{port}/index.html"

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
                for vp_name, viewport in [("desktop", {"width": 1280, "height": 800}), ("mobile", {"width": 360, "height": 740})]:
                    context = browser.new_context(viewport=viewport)
                    page = context.new_page()
                    console_errors = []
                    page_errors = []
                    failed_requests = []
                    bad_statuses = []
                    dialogs = []

                    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
                    page.on("pageerror", lambda err: page_errors.append(str(err)))
                    page.on("requestfailed", lambda req: failed_requests.append(f"{req.url}: {req.failure}"))
                    page.on("response", lambda resp: bad_statuses.append(f"{resp.status} {resp.url}") if resp.status >= 400 else None)
                    page.on("dialog", lambda dlg: (dialogs.append(dlg.message), dlg.dismiss()))

                    page.goto(base_url, wait_until="networkidle")

                    h1_text = page.locator("h1").inner_text().strip()
                    assert CANONICAL_NAME in h1_text, f"Unexpected H1 on {vp_name}: {h1_text}"

                    status_title = page.locator("#coze-status-title").inner_text().strip()
                    assert "Chờ cấu hình" in status_title, f"Unexpected Coze status on {vp_name}: {status_title}"

                    # Check .header-inner horizontal padding >= 16px
                    hdr_pad = page.evaluate("""() => {
                        const el = document.querySelector('.header-inner');
                        const cs = getComputedStyle(el);
                        return { left: parseFloat(cs.paddingLeft), right: parseFloat(cs.paddingRight) };
                    }""")
                    assert hdr_pad["left"] >= 16 and hdr_pad["right"] >= 16, (
                        f".header-inner horizontal padding too small on {vp_name}: {hdr_pad}"
                    )

                    # Check nav anchor clicks do not leave target <h2> occluded by .site-header
                    nav_targets = ["#chuc-nang", "#kiem-tra-nhanh", "#khan-cap", "#cong-cu", "#tich-hop-coze"]
                    for target_id in nav_targets:
                        page.locator(f'nav.nav-links a[href="{target_id}"]').click()
                        page.wait_for_function(
                            """() => new Promise(resolve => {
                                let lastY = window.scrollY;
                                let stableCount = 0;
                                let elapsed = 0;
                                const timer = setInterval(() => {
                                    elapsed += 80;
                                    if (Math.abs(window.scrollY - lastY) < 1) {
                                        stableCount += 1;
                                        if (stableCount >= 3 && elapsed >= 240) {
                                            clearInterval(timer);
                                            resolve(true);
                                        }
                                    } else {
                                        stableCount = 0;
                                        lastY = window.scrollY;
                                    }
                                    if (elapsed >= 3000) {
                                        clearInterval(timer);
                                        resolve(true);
                                    }
                                }, 80);
                            })"""
                        )
                        metrics = page.evaluate(
                            """(sel) => {
                                const header = document.querySelector('.site-header');
                                const h2 = document.querySelector(sel + ' h2');
                                const hStyle = getComputedStyle(header);
                                const headerRect = header.getBoundingClientRect();
                                const h2Rect = h2.getBoundingClientRect();
                                return {
                                    position: hStyle.position,
                                    headerBottom: headerRect.bottom,
                                    h2Top: h2Rect.top,
                                    h2Bottom: h2Rect.bottom,
                                    vh: window.innerHeight
                                };
                            }""",
                            target_id,
                        )
                        if metrics["position"] in ("sticky", "fixed"):
                            assert metrics["h2Top"] >= metrics["headerBottom"] - 1, (
                                f"Target {target_id} h2 occluded by sticky header on {vp_name}: {metrics}"
                            )
                        assert metrics["h2Top"] >= 0 and metrics["h2Bottom"] <= metrics["vh"], (
                            f"Target {target_id} h2 not cleanly visible in viewport on {vp_name}: {metrics}"
                        )

                    # Check ARIA tablist contract & interactive scenario tabs
                    aria_initial = page.evaluate("""() => {
                        const tablist = document.querySelector('.scenario-tabs[role="tablist"]');
                        const tabs = Array.from(document.querySelectorAll('.scenario-btn'));
                        const panel = document.querySelector('#scenario-output[role="tabpanel"]');
                        return {
                            hasTablist: Boolean(tablist),
                            hasTabpanel: Boolean(panel),
                            tabCount: tabs.length,
                            validTabs: tabs.every(t => t.getAttribute('role') === 'tab' && t.getAttribute('aria-controls') === 'scenario-output'),
                            selectedStates: tabs.map(t => ({ id: t.dataset.scenario, selected: t.getAttribute('aria-selected') }))
                        };
                    }""")
                    assert aria_initial["hasTablist"] and aria_initial["hasTabpanel"], f"ARIA tablist/tabpanel missing on {vp_name}: {aria_initial}"
                    assert aria_initial["tabCount"] == 5 and aria_initial["validTabs"], f"ARIA tab roles invalid on {vp_name}: {aria_initial}"
                    assert aria_initial["selectedStates"][0]["selected"] == "true", f"Initial active tab aria-selected!=true on {vp_name}"
                    assert all(s["selected"] == "false" for s in aria_initial["selectedStates"][1:]), f"Inactive tabs aria-selected!=false on {vp_name}"

                    page.locator('button[data-scenario="biometric"]').click()
                    out_text = page.locator("#scenario-output").inner_text()
                    assert "2345" in out_text and ".apk" in out_text, f"Biometric scenario failed on {vp_name}"
                    assert page.locator('button[data-scenario="biometric"]').get_attribute("aria-selected") == "true"
                    assert page.locator('button[data-scenario="police"]').get_attribute("aria-selected") == "false"

                    page.locator('button[data-scenario="deepfake"]').click()
                    out_text_df = page.locator("#scenario-output").inner_text()
                    assert "Deepfake" in out_text_df, f"Deepfake scenario failed on {vp_name}"
                    assert page.locator('button[data-scenario="deepfake"]').get_attribute("aria-selected") == "true"

                    # Test URL checker adversarial & legitimate cases
                    url_cases = [
                        ("http://vneid-capnhat.vip/app.apk", ["danger"], ["Cảnh báo phát hiện", ".apk"]),
                        ("https://vneid-phishing.com/?next=dichvucong.gov.vn", ["danger"], ["Cảnh báo phát hiện"]),
                        ("https://vneid.gov.vn.scam.com", ["danger"], ["Cảnh báo phát hiện"]),
                        ("https://103.45.67.89/login", ["danger"], ["Cảnh báo phát hiện"]),
                        ("<script>alert(1)</script>", ["warn", "danger"], []),
                        ("https://www.vietcombank.com.vn", ["ok"], ["Chưa phát hiện dấu hiệu"]),
                    ]
                    for test_url, allowed_classes, required_substrings in url_cases:
                        page.locator("#url-input").fill(test_url)
                        page.locator('#url-check-form button[type="submit"]').click()
                        res_class = page.locator("#url-result").get_attribute("class") or ""
                        res_text = page.locator("#url-result").inner_text()
                        assert any(cls in res_class.split() for cls in allowed_classes), (
                            f"URL '{test_url}' expected class in {allowed_classes}, got '{res_class}' on {vp_name}"
                        )
                        if "ok" not in allowed_classes:
                            assert "ok" not in res_class.split(), f"URL '{test_url}' falsely returned 'ok' on {vp_name}"
                        for sub in required_substrings:
                            assert sub in res_text, f"URL '{test_url}' missing '{sub}' in result on {vp_name}: {res_text}"

                    # Check horizontal overflow
                    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
                    assert not overflow, f"Horizontal overflow detected on {vp_name} viewport"

                    assert not dialogs, f"Unexpected JS alert/dialog on {vp_name}: {dialogs}"
                    assert not console_errors, f"Console errors on {vp_name}: {console_errors}"
                    assert not page_errors, f"Page errors on {vp_name}: {page_errors}"
                    assert not failed_requests, f"Failed requests on {vp_name}: {failed_requests}"
                    assert not bad_statuses, f"HTTP >= 400 responses on {vp_name}: {bad_statuses}"
                    print(f"  OK: {vp_name} ({viewport['width']}x{viewport['height']}) — 0 console errors, 0 page errors, 0 failed requests, nav/ARIA/URL checks passed.")
                    context.close()
                browser.close()
        finally:
            httpd.shutdown()


def main():
    verify_required_files()
    verify_consistency()
    verify_docx_files()
    verify_pdf_files()
    verify_webpage_playwright()
    print("=== ALL VERIFICATION CHECKS PASSED ===")


if __name__ == "__main__":
    main()
