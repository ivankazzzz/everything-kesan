import PyPDF2
import os

def pdf_to_text(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None
    return text

def save_as_markdown(text, output_path, title):
    """Save text as Markdown file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            file.write(text)
        print(f"Successfully converted to {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")

def main():
    # Define file paths
    workspace_path = r"c:\Users\Admin\Documents\EVERYTHING KESAN"
    pdf1_path = os.path.join(workspace_path, "v7n2-007.pdf")
    pdf2_path = os.path.join(workspace_path, "v7n2-024.pdf")
    pdf3_path = os.path.join(workspace_path, "Instrumen_Model_Valid_Isi (1).pdf")
    pdf4_path = os.path.join(workspace_path, "buku_Model_Kesan_23_agustus_2025 (1).pdf")
    md_folder = os.path.join(workspace_path, "MD")
    md_kesan_folder = os.path.join(workspace_path, "MD KESAN")
    
    # Convert first PDF
    print("Converting first PDF...")
    text1 = pdf_to_text(pdf1_path)
    if text1:
        output1_path = os.path.join(md_folder, "aptisi 1.md")
        save_as_markdown(text1, output1_path, "APTISI 1")
    
    # Convert second PDF
    print("Converting second PDF...")
    text2 = pdf_to_text(pdf2_path)
    if text2:
        output2_path = os.path.join(md_folder, "aptisi 2.md")
        save_as_markdown(text2, output2_path, "APTISI 2")
    
    # Convert third PDF
    print("Converting third PDF...")
    text3 = pdf_to_text(pdf3_path)
    if text3:
        output3_path = os.path.join(md_kesan_folder, "Instrumen_Model_Valid_Isi.md")
        save_as_markdown(text3, output3_path, "Instrumen Model Valid Isi")
        
    # Convert fourth PDF
    print("Converting fourth PDF...")
    text4 = pdf_to_text(pdf4_path)
    if text4:
        output4_path = os.path.join(md_folder, "buku_Model_Kesan_23_agustus_2025.md")
        save_as_markdown(text4, output4_path, "Buku Model KESAN 23 Agustus 2025")

if __name__ == "__main__":
    main()