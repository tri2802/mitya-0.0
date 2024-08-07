from generate_prompt import *
from text_splitting import *
import time

def create_data(csv_path, pdf_path):
  '''
  **This function takes a pdf file, then generates prompts from the LLM corresponding to parts of the text, and saves it into the CSV**
  Args:
  csv_path (str) = path to CSV file storing data
  pdf_path (str) = path to pdf file to get data
  '''
  try:
    # Convert PDF to images
    images = pdf_to_images(pdf_path)
        
    # Extract text from images
    text = images_to_text(images)
        
    # Split text into chunks
    chunks = split_text_recursively(text)
        
    # Process each chunk and generate Q&A
    for chunk in chunks:
      question, answer = generate_prompts_api(chunk)
            
      # Append Q&A to CSV
      append_to_csv(question, answer, csv_path)
            
    print("Data processing complete.")

  except Exception as e:
    print(f"An error occurred: {e}")

# Call this to use the tesseract as path on the local machine
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Call the function
pdf_p = "path_to_pdf.pdf"
csv_p = "path_to_csv.csv"

create_data(csv_path = csv_p, pdf_path = pdf_p)
