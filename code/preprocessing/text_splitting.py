import pypdfium2
from PIL import Image
import pytesseract
from langchain.text_splitter import RecursiveCharacterTextSplitter

def pdf_to_images(pdf_path):
    '''
    **This function takes a pdf file and returns a list of PIL images**
    Args:
    pdf_path (str) = path to the designated pdf file
    Returns:
    a list of PIL images
    '''
    pdf_document = pypdfium2.PdfDocument(pdf_path)
    images = []
    
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        pil_image = page.render().to_pil()
        images.append(pil_image)
    
    pdf_document.close()
    return images


def images_to_text(images):
    '''
    **This function takes a list of images, convert them into list of texts, then join them into a string string**
    Args:
    images (PIL) = a list of PIL images object
    Returns:
    a single Python string
    '''
    texts = []
    for image in images:
        text = pytesseract.image_to_string(image)
        texts.append(text)
    return "\n".join(texts)


def split_text_recursively(text):
    '''
    **This function takes a string into separated chunks of 1500 characters (including whitespace)**
    Args:
    text (str) = a Python string
    Returns:
    a list of text chunks
    '''
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1600,
        chunk_overlap = 100,  #Overlap to ensure context preservation
        length_function = len
    )
    
    chunks = splitter.split_text(text)
    
    return chunks
