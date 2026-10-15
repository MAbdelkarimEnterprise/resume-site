from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import HRFlowable

F = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("Serif", F + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-I", F + "LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Sans", F + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-B", F + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-I", F + "LiberationSans-Italic.ttf"))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-B", italic="Sans-I", boldItalic="Sans-B")

NAVY = HexColor("#14213D"); BURG = HexColor("#6B1D2F"); SOFT = HexColor("#55607A"); RULE = HexColor("#C9CCD6")

name = ParagraphStyle("name", fontName="Serif", fontSize=24, leading=27, textColor=BURG, alignment=1)
contact = ParagraphStyle("contact", fontName="Sans", fontSize=8.8, leading=12, textColor=SOFT, alignment=1)
sec = ParagraphStyle("sec", fontName="Sans-B", fontSize=9.2, leading=11, textColor=BURG, spaceBefore=11, spaceAfter=1)
org = ParagraphStyle("org", fontName="Sans-B", fontSize=10.4, leading=13.4, textColor=NAVY)
right = ParagraphStyle("right", parent=org, fontName="Sans", alignment=2, textColor=SOFT, fontSize=9)
role = ParagraphStyle("role", fontName="Sans-I", fontSize=9.7, leading=12.6, textColor=NAVY)
bullet = ParagraphStyle("bullet", fontName="Sans", fontSize=9.6, leading=12.8, textColor=NAVY, leftIndent=11, bulletIndent=2, spaceBefore=1.2)
line = ParagraphStyle("line", fontName="Sans", fontSize=9.6, leading=13.2, textColor=NAVY)

W = letter[0] - 2 * 0.6 * inch

def header_row(left, r):
    t = Table([[Paragraph(left, org), Paragraph(r, right)]], colWidths=[W * 0.68, W * 0.32])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("VALIGN", (0, 0), (-1, -1), "BOTTOM")]))
    return t

def section(title):
    return [Paragraph(title.upper(), sec), HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=1, spaceAfter=3)]

def bl(items):
    return [Paragraph(x, bullet, bulletText="•") for x in items]

def entry(left, r, role_txt, items):
    parts = [header_row(left, r)]
    if role_txt:
        parts.append(Paragraph(role_txt, role))
    parts += bl(items)
    parts.append(Spacer(1, 6))
    return KeepTogether(parts)

story = []
story.append(Paragraph("Mahmoud El Walid Abdelkarim", name))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "Grand Rapids, MI | Cairo, Egypt &nbsp;·&nbsp; mw.abdelkarim@gmail.com &nbsp;·&nbsp; +1 (779) 445-4980<br/>"
    "<link href='https://www.linkedin.com/in/mahmoud-abdelkarim-b443b4326'>linkedin.com/in/mahmoud-abdelkarim-b443b4326</link> &nbsp;·&nbsp; "
    "<link href='https://www.mahmoudabdelkarim.com'>mahmoudabdelkarim.com</link>", contact))

story += section("Education")
story.append(entry("Grand Valley State University <font name='Sans' color='#55607A'>· Allendale, MI</font>", "Expected 2028",
    "B.S. Artificial Intelligence, Minor in Business · GPA 3.8 · Honors College",
    ["NCAA Division II Swim &amp; Dive student-athlete: <b>2026 NCAA All-American</b> (7th, 100 back, 46.85) and "
     "<b>2026 GLIAC Champion</b> (100 back), plus GLIAC relay titles in the 200 medley and 400 free."]))

story += section("Experience")
story.append(entry("Rowad Modern Engineering (RME) <font name='Sans' color='#55607A'>· Cairo, Egypt</font>", "Jun – Jul 2026",
    "AI Integration Intern, Strategy &amp; PMO", [
    "Designed and shipped <b>RME Intelligence</b>, an internal AI operating system for a major construction "
    "contractor, now live with <b>38 users across 5 construction projects</b>.",
    "Built <b>13 domain modules</b> end to end in Next.js, TypeScript, Prisma and PostgreSQL, including BOQ, IPC, Tender, "
    "Specification, Variation, Claims &amp; Delay, Knowledge Graph, AI Assistant and Analytics.",
    "Engineered LLM extraction pipelines that turn bills of quantities, payment certificates, tenders and specifications into "
    "structured, queryable data, cutting manual takeoff and certification review <b>from hours to minutes</b>.",
    "Architected the document pipeline as a staged async workflow behind a provider-agnostic AI and OCR layer, with role-based "
    "access control, a Vitest suite, and a knowledge-graph retrieval layer for natural-language queries across the portfolio.",
    "Built the executive dashboard leadership uses for portfolio decisions: contract vs. certified position, pending IPC value, "
    "claims exposure, forecast margin and automated risk flags.",
    "Partnered with Flex Labs to map departmental processes and run stakeholder interviews, converting findings into scoped "
    "product requirements; delivered PMO dashboards and board packs.",
]))
story.append(entry("Emerge Capital <font name='Sans' color='#55607A'>· Dubai (Remote)</font>", "Exposure Program",
    "Venture Builder", [
    "Supported market research, pitch content and product ideation for portfolio ventures across AI and Web3.",
]))

story += section("Startups")
story.append(entry("Founder &amp; Engineer <font name='Sans' color='#55607A'>· Independent AI ventures</font>", "2024 – Present", None, [
    "<b>FINU</b>: AI money assistant for spending analysis, autopilot savings and putting idle cash to work; secured "
    "<b>$200K in Google Gemini credits</b>. Built the marketing and demo site on Next.js and Vercel.",
    "<b>FORGE</b> (in development): training app combining WHOOP recovery, strain and sleep data with lift logging and an AI nutrition coach.",
    "<b>NYX</b> (nyxsystem.online): autonomous AI product with a tiered subscription model on a Netlify and Resend stack.",
    "<b>AI automation for SMEs</b>: designed and prototyped AI receptionists with LLMs and voice APIs, handling booking, intake "
    "and follow-up for gyms, clinics and restaurants across Egypt and the MENA region.",
]))

story += section("Skills")
for k, v in [
    ("AI &amp; ML", "LLM integration, RAG and retrieval pipelines, document extraction, agentic workflows, knowledge graphs, prompt engineering, OpenAI and Anthropic APIs"),
    ("Languages", "Python, TypeScript, JavaScript, SQL"),
    ("Full-stack", "Next.js, React, Tailwind CSS, Prisma ORM, PostgreSQL, REST APIs, Vitest, Git"),
    ("Infrastructure", "Vercel, Netlify, Docker, AWS, GCP"),
    ("Product", "Requirements gathering, process mapping, PMO and portfolio reporting, market research, financial modeling"),
    ("Spoken", "Arabic (native), English (fluent)"),
]:
    story.append(Paragraph(f"<b>{k}:</b> {v}", line))

doc = SimpleDocTemplate("/home/claude/site/resume.pdf", pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                        topMargin=0.5 * inch, bottomMargin=0.45 * inch,
                        title="Mahmoud El Walid Abdelkarim — Resume", author="Mahmoud El Walid Abdelkarim",
                        subject="Resume", keywords="AI engineer, software engineering, LLM, RAG, Next.js, TypeScript, Python")
doc.build(story)
