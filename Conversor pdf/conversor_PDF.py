from pdf2image import convert_from_path
from PIL import Image
from pdf2docx import Converter


def conv_pdf_png():
    # Caminho do PDF
    pdf_path = 'seu_arquivo.pdf'

    # Converte o PDF em imagens
    images = convert_from_path(pdf_path)

    # Salva cada página como PNG
    for i, image in enumerate(images):
        image.save(f'pagina_{i + 1}.png', 'PNG')# se for  .jpg, 'JPEG'

    print("PDF convertido em imagens PNG.")

def conv_png_pdf():
    
    # Caminho da imagem
    image_path = 'sua_imagem.png'

    # Abre a imagem
    image = Image.open(image_path)

    # Salva a imagem como PDF
    image.save('saida.pdf', 'PDF')

    print("Imagem convertida em PDF.")  

def conv_pdf_word():
        
    # Caminho do PDF
    pdf_path = 'seu_arquivo.pdf'  # Substitua pelo seu arquivo PDF

    # Converte o PDF em Word
    cv = Converter(pdf_path)
    cv.convert('saida.docx', start=0, end=None)
    cv.close()

    print("PDF convertido em documento Word.")      
