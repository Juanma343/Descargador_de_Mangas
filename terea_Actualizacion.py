import os
import mangas

def main():
    mangas_ = mangas.DescargarMangas()
    for i in mangas_["Nuevo"]:
        print(f"Descargando: {i["nombre"]}")
        if not os.path.exists(i["path"] + "\\" + i["nombre"]):
            os.mkdir(i["path"] + "\\" + i["nombre"])
        lista = i["funcionlis"](i["direccion"])
        for j in lista:
            print(f"    Descargando: {j[0]}")
            i["funcionDesc"](j[1],j[0], os.path.join(i["path"], i["nombre"]))
        if not i["funcionFin"](i["direccion"]):
            aux = i
            aux["ultimoCap"] = lista[0][0]
            mangas_["Actualizacion"].append(aux)
        else:
            mangas_["Nuevo"].remove(i)
            
    for i in mangas_["Actualizacion"]:
        print(f"Descargando: {i["nombre"]}")
        if not os.path.exists(i["path"] + "\\" + i["nombre"]):
            os.mkdir(i["path"] + "\\" + i["nombre"])
        lista = i["funcionlis"](i["direccion"])
        for j in lista:
            if j[0] == i["ultimoCap"]:
                break
            print(f"    Descargando: {j[0]}")
            i["funcionDesc"](j[1],j[0], i["path"])
        if i["funcionFin"](i["direccion"]):
            mangas_["Actualizacion"].remove(i)
    mangas.CargarMangas(mangas_)
        

if __name__ == "__main__":
    main()