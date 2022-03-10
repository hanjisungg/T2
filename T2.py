#T2

#ex 182  --> A FAIRE

def stats_csv(fichier):
    import fichier
    f = open("table.fichier", "r")
    table = list(csv.DictRead(f))
    f.close
    
    print("nombre de ligne =", len(table))
    
    

#ex 184
    
def valide(e):
    ref = e["ref"]
    designation = e["designation"]
    prix = float(e["prix"])
    qte = int(e["qte"])
    return {"ref": ref, "designation": designation, "prix": prix, "qte": qte}
    
def ex184(nom_fichier):
    import csv
    f = open(nom_fichier, "r")
    table = list(csv.DictReader(f))
    f.close
    
    table_valide = [valide(e) for e in table]
    
    return table_valide
    
    
    
    
