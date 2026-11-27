

import pandas as pd
from datetime import datetime
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_csv_report(results):
    safe_results = []

    for index, item in enumerate(results, start=1):
        safe_results.append({
            "Sample ID": f"PASS-{index:03d}",
            "Strength": item.get("strength", "N/A"),
            "Complexity Score": item.get("score", "N/A"),
            "Estimated Entropy": item.get("entropy", "N/A"),
            "Findings": "; ".join(item.get("feedback", []))
        })

    df = pd.DataFrame(safe_results)

    return df.to_csv(index=False).encode("utf-8")


def generate_pdf_report(results):
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=35,
        leftMargin=35,
        topMargin=35,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph(
            "Password Security Audit Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "Assessment Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "This report summarizes password complexity "
            "assessment results from synthetic test samples. "
            "Plaintext passwords are not included.",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    table_data = [[
        "Sample ID",
        "Strength",
        "Score",
        "Entropy"
    ]]

    for index, item in enumerate(results, start=1):
        table_data.append([
            f"PASS-{index:03d}",
            str(item.get("strength", "N/A")),
            str(item.get("score", "N/A")),
            str(item.get("entropy", "N/A"))
        ])

    table = Table(
        table_data,
        repeatRows=1,
        colWidths=[90, 110, 90, 110]
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    ]))

    content.append(table)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Recommendation: Use long, unique passwords and "
            "a password manager. Enable multi-factor authentication "
            "where available. Avoid reusing passwords.",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Note: Complexity and theoretical entropy are "
            "educational indicators, not guarantees of password security.",
            styles["Italic"]
        )
    )

    document.build(content)

    buffer.seek(0)

    return buffer.getvalue()
