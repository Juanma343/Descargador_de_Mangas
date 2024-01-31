import descargar
import listaCap
import pickle

def DescargarMangas():
    with open('listaMangas.json', 'rb') as archivo:
        mangas = pickle.load(archivo)
    return mangas

def CargarMangas(listaMangas):
    with open('listaMangas.json', 'wb') as archivo:
        pickle.dump(listaMangas, archivo)

if __name__ == "__main__":
    mangas = DescargarMangas()
    print(mangas)