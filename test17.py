import PyPDF2 # solo se ejecuta cin la maquina virtual, se debe instalar pip install PyPDF2 

with open("ejemplo.pdf", "rb") as f:
    pdf_reader = PyPDF2.PdfReader(f)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text =page.extract_text()
        print(text)
        print("--"*20)

        # en la maquina virtual escribir: pip freeze > requeriments.txt para que se gener el archivo que necesita el usuario para instalar
        #en la maquina virtual escribir: pip install -r requirements.txt y se instala todos los packages 
        
