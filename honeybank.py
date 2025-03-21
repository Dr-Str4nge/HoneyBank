import os
import random
import csv
import argparse
from faker import Faker
from docx import Document
import pandas as pd
from fpdf import FPDF

def create_fake_docx(file_path, customer_name, account_number, fake):
    """Generate a fake banking document in .docx format."""
    doc = Document()
    doc.add_heading("Confidential Banking Document", level=1)
    doc.add_paragraph(f"Customer Name: {customer_name}")
    doc.add_paragraph(f"Account Number: {account_number}")
    doc.add_paragraph(f"Balance: ${fake.random_int(min=1000, max=500000)}")
    doc.add_paragraph(f"Date: {fake.date_this_year()}")
    doc.save(file_path)

def create_fake_xlsx(file_path, customer_name, account_number, fake):
    """Generate a fake banking transaction record in .xlsx format."""
    data = {
        "Transaction ID": [fake.uuid4() for _ in range(10)],
        "Date": [fake.date_this_year() for _ in range(10)],
        "Amount ($)": [round(random.uniform(100, 5000), 2) for _ in range(10)],
        "Description": [fake.sentence() for _ in range(10)]
    }
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

def create_fake_csv(file_path, customer_name, account_number, fake):
    """Generate a fake banking customer data file in .csv format."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Customer Name", "Account Number", "Balance", "Last Transaction Date"])
        for _ in range(10):
            writer.writerow([customer_name, account_number, 
                             fake.random_int(min=1000, max=500000), 
                             fake.date_this_year()])

def create_fake_pdf(file_path, customer_name, account_number, fake):
    """Generate a fake bank account statement in .pdf format."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='', size=12)
    pdf.cell(200, 10, txt="Bank Account Statement", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Customer: {customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Account Number: {account_number}", ln=True)
    pdf.cell(200, 10, txt=f"Balance: ${fake.random_int(min=1000, max=500000)}", ln=True)
    pdf.output(file_path)

def generate_fake_files(base_path, num_folders, min_files, max_files, file_types):
    """Generate fake customer folders with banking-related documents."""
    fake = Faker()
    file_names = [
        "Account_Statement", "Wire_Transfer", "Loan_Agreement", "Customer_Profile",
        "Fraud_Investigation_Report", "Internal_Audit", "Financial_Report",
        "Tax_Return", "Mortgage_Application", "Investment_Portfolio"
    ]
    
    for i in range(num_folders):
        customer_name = fake.name()
        account_number = str(fake.random_number(digits=8, fix_len=True))
        folder_name = f"{customer_name.replace(' ', '_')}-{account_number}"
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        num_files = random.randint(min_files, max_files)  # Generate a random number of files per folder
        for _ in range(num_files):
            file_ext = random.choice(file_types)
            file_name = f"{random.choice(file_names)}_{fake.random_number(digits=4)}.{file_ext}"
            file_path = os.path.join(folder_path, file_name)
            
            if file_ext == "docx":
                create_fake_docx(file_path, customer_name, account_number, fake)
            elif file_ext == "xlsx":
                create_fake_xlsx(file_path, customer_name, account_number, fake)
            elif file_ext == "csv":
                create_fake_csv(file_path, customer_name, account_number, fake)
            elif file_ext == "pdf":
                create_fake_pdf(file_path, customer_name, account_number, fake)
    
    print(f"Generated {num_folders} fake customer folders with fake banking data.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake customer banking files for honey shares.")
    parser.add_argument("--base_path", type=str, default="./honey_shares", help="Base directory for generated files")
    parser.add_argument("--num_folders", type=int, default=10, help="Number of customer folders to create")
    parser.add_argument("--min_files", type=int, default=4, help="Minimum number of files per folder")
    parser.add_argument("--max_files", type=int, default=10, help="Maximum number of files per folder")
    parser.add_argument("--file_types", nargs="+", default=["docx", "xlsx", "csv", "pdf"], help="List of file types to generate")
    
    args = parser.parse_args()
    os.makedirs(args.base_path, exist_ok=True)
    generate_fake_files(args.base_path, args.num_folders, args.min_files, args.max_files, args.file_types)
