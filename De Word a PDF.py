import aspose.words as PW #<- libreria  ' pip install aspose-words '
adorno,titulo = "","De dpf a word"
print(adorno.center(50,"*"))
print(titulo.center(50).upper())
print(adorno.center(50, "*"))

NombreDePDF = input("Ingrese el nombre del archivo PDF: ")
NombreWord = input("Ingrese el nombre para el documento WORD: ")
def Conver():
    print("Espere unos minutos por favor 😅")
    try:
        #Cargar el archivo PDF
        documento = PW.Document(f"{NombreDePDF}.pdf") #<- Ojo el pdf a combertir tiene que estar ubicado en donde se encuentra el archivo del programa 
    
        #Guardar el archivo como word
        documento.save(f"{NombreWord}.docx") #<- El archivo pdf combertido a word se almacenara en donde se encuentra el archivo del programa
    except:
        print("Algo Salio Mal 😓")
    else:
        print("\nArchivo de word creado 😄")

Conver()