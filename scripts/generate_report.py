import sys
import json
from fpdf import FPDF
import matplotlib.pyplot as plt
import os

# COLORS
PRIMARY_COLOR = (0, 51, 102) # Navy Blue
ACCENT_COLOR = (204, 0, 0)   # Dark Red
TEXT_COLOR = (50, 50, 50)    # Dark Grey

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.set_text_color(*PRIMARY_COLOR)
        self.cell(0, 10, 'SOVEREIGN BOARDROOM: EXECUTIVE BRIEF', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(*PRIMARY_COLOR)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.set_text_color(*TEXT_COLOR)
        self.multi_cell(0, 6, body)
        self.ln()

def create_chart(value, label, filename, max_val=100):
    """Creates a simple gauge-like bar chart."""
    fig, ax = plt.subplots(figsize=(4, 1))
    ax.barh([0], [max_val], color='#e0e0e0', height=0.5) # Background
    color = 'green' if value > max_val/2 else 'red'
    ax.barh([0], [value], color=color, height=0.5) # Value
    ax.set_xlim(0, max_val)
    ax.axis('off')
    plt.text(0, 0.6, f"{label}: {value}", fontsize=12, fontweight='bold')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def generate_pdf(data_json, output_path="report.pdf"):
    # Sanitize input to avoid UnicodeEncodeError (FPDF default font is latin-1)
    data_json = data_json.replace("₹", "Rs. ")
    data = json.loads(data_json)
    pdf = PDFReport()
    pdf.add_page()
    
    # TITLE SECTION
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f"AUDIT TARGET: {data.get('ticker', 'UNKNOWN')}", 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Verdict: {data.get('verdict', 'N/A')}", 0, 1, 'L')
    pdf.ln(5)

    # 1. THE BOTTOM LINE
    pdf.chapter_title("1. THE BOTTOM LINE")
    pdf.chapter_body(data.get('bottom_line', 'No data provided.'))

    # 2. ELI5 EXPLANATION
    pdf.chapter_title("2. THE 'ELI5' (WHY IT MATTERS)")
    pdf.chapter_body(data.get('eli5', 'No data provided.'))

    # 3. ANALYST REPORTS (The Deep Dive)
    pdf.chapter_title("3. ANALYST REPORTS")
    
    # Technical Analyst (Engine)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, "Technical Analyst (Price & Momentum):", 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6, data.get('technical_analysis', 'N/A'))
    pdf.ln(3)

    # Fundamental Analyst
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, "Fundamental Analyst (Quality & Value):", 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6, data.get('fundamental_analysis', 'N/A'))
    pdf.ln(3)

    # Macro Strategist (Architect)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, "Macro Strategist (The Weather):", 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6, data.get('macro_analysis', 'N/A'))
    pdf.ln(5)

    # CHARTS (Visuals)
    # Generate Charts if data exists
    if 'rsi' in data:
        create_chart(data['rsi'], "RSI (Momentum)", "chart_rsi.png", 100)
        pdf.image("chart_rsi.png", x=10, w=80)
        os.remove("chart_rsi.png")
    
    if 'pe_ratio' in data:
        # Normalized P/E chart (just visual)
        pe = data['pe_ratio']
        create_chart(pe, "P/E Ratio", "chart_pe.png", 100) # Cap visual at 100
        pdf.image("chart_pe.png", x=110, y=pdf.get_y() - 25, w=80) # Place next to RSI
        os.remove("chart_pe.png")

    pdf.output(output_path)
    print(f"✓ PDF Report generated: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py '<json_data>' [output_path]")
        sys.exit(1)
    
    output_path = "report.pdf"
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
        
    generate_pdf(sys.argv[1], output_path)
