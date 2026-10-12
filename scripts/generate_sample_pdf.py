"""Generate sample company PDF for VedaNova Solutions."""
import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def create_vedanova_pdf():
    output_dir = Path(__file__).resolve().parent.parent / "company_docs"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = output_dir / "VedaNova_Company_Overview_and_Services.pdf"

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        leftMargin=50,
        rightMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        "VedaTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        "VedaSub",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0D9488")
    )

    h1_style = ParagraphStyle(
        "VedaH1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=14,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        "VedaBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155")
    )

    bullet_style = ParagraphStyle(
        "VedaBullet",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155"),
        leftIndent=15
    )

    story = []

    # Title & Header
    story.append(Paragraph("VedaNova Solutions", title_style))
    story.append(Paragraph("Holistic Wellness for a Better Tomorrow — Integrating Ayurveda, Technology and Research", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2563EB"), spaceAfter=15))

    # Section 1: About
    story.append(Paragraph("1. About VedaNova Solutions", h1_style))
    story.append(Paragraph(
        "VedaNova is a premier holistic wellness and healthcare technology platform. We seamlessly bridge the ancient wisdom of classical Ayurveda with cutting-edge digital health technology and clinical research. Our mission is to make individualized, preventative healthcare accessible, scientific, and actionable for modern lifestyles.",
        body_style
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Core Pillars:</b>", body_style))
    story.append(Paragraph("• <b>Individualized Care:</b> Every individual is uniquely profiled by Dosha constitution (Vata, Pitta, Kapha) and biometric data.", bullet_style))
    story.append(Paragraph("• <b>Modern Research Integration:</b> All therapies and herbal formulations are backed by lab-tested scientific efficacy.", bullet_style))
    story.append(Paragraph("• <b>Digital Tele-Wellness:</b> Continuous tracking, tele-consultations, and AI-assisted wellness routines.", bullet_style))

    # Section 2: Services
    story.append(Paragraph("2. Wellness Services & Consultation Programs", h1_style))
    story.append(Paragraph("VedaNova provides comprehensive wellness solutions tailored for individuals and corporations:", body_style))
    story.append(Spacer(1, 6))

    services_data = [
        [Paragraph("<b>Service</b>", body_style), Paragraph("<b>Description</b>", body_style), Paragraph("<b>Pricing</b>", body_style)],
        [
            Paragraph("<b>Holistic Dosha Profiling & Consultation</b>", body_style),
            Paragraph("Comprehensive 60-minute assessment with certified Ayurvedic doctors analyzing pulse, diet, stress markers, and dosha balance.", body_style),
            Paragraph("$75 / ₹2,499", body_style)
        ],
        [
            Paragraph("<b>Integrative Nutrition & Herbal Therapy</b>", body_style),
            Paragraph("Personalized gut health restoration plan with certified organic herbal formulations delivered to your doorstep.", body_style),
            Paragraph("$110 / ₹3,899 (incl. herbal kit)", body_style)
        ],
        [
            Paragraph("<b>Mental Wellness & Mindfulness Tech</b>", body_style),
            Paragraph("Guided breathwork, sleep optimization protocols, and neuro-acoustic meditation routines.", body_style),
            Paragraph("$50 / ₹1,799 / month", body_style)
        ],
        [
            Paragraph("<b>Corporate Holistic Wellness Plan</b>", body_style),
            Paragraph("Custom ergonomic assessments, employee stress resilience workshops, and quarterly wellness challenges.", body_style),
            Paragraph("Custom Enterprise Quote", body_style)
        ]
    ]

    srv_table = Table(services_data, colWidths=[150, 270, 90])
    srv_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(srv_table)
    story.append(Spacer(1, 10))

    # Section 3: How it Works
    story.append(Paragraph("3. How It Works (The 3-Step Journey)", h1_style))
    story.append(Paragraph("<b>Step 1: Digital Wellness Assessment:</b> Complete our 10-minute online questionnaire covering lifestyle, stress, digestion, and daily energy levels.", bullet_style))
    story.append(Paragraph("<b>Step 2: 1-on-1 Doctor Consultation:</b> Meet with a certified VedaNova Ayurvedic physician via secure video call for an in-depth diagnosis and treatment plan.", bullet_style))
    story.append(Paragraph("<b>Step 3: Continuous Care & Habit Tracking:</b> Receive your custom diet plan, herbal remedies, and daily guidance via the VedaNova wellness portal.", bullet_style))

    # Section 4: Policies
    story.append(Paragraph("4. Booking, Rescheduling & Refund Policy", h1_style))
    story.append(Paragraph("• <b>Rescheduling & Cancellations:</b> Appointments may be rescheduled or canceled with full refund up to 24 hours prior to the scheduled session. Cancellations within 24 hours incur a 50% cancellation fee.", bullet_style))
    story.append(Paragraph("• <b>Product Satisfaction Guarantee:</b> All unopened herbal formulations carry a 14-day 100% money-back satisfaction guarantee.", bullet_style))
    story.append(Paragraph("• <b>Support Contact:</b> Support is reachable at support@vedanovasolutions.com or through the VedaNova AI Assistant.", bullet_style))

    # Section 5: FAQs
    story.append(Paragraph("5. Frequently Asked Questions (FAQ)", h1_style))
    story.append(Paragraph("<b>Q: Are VedaNova treatments safe alongside conventional modern medicine?</b><br/>A: Yes. Our practitioners practice integrative wellness, reviewing existing prescription medications to avoid herb-drug interactions.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Q: How soon can I expect results from the holistic programs?</b><br/>A: While digestion and sleep improvements are typically noted within 7-14 days, chronic conditions like metabolic imbalance and joint stiffness generally show sustainable benefits within 6-12 weeks.", body_style))

    doc.build(story)
    print(f"Sample PDF successfully generated at: {pdf_path}")

if __name__ == "__main__":
    create_vedanova_pdf()
