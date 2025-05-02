def presenteer(dictionary,totaal):
    uitvoer = []
    dict_list = [f"{k} : {v} euro" for k,v in dictionary.items()]
    uitvoer.extend(dict_list)
    uitvoer.append("="*26)
    uitvoer.append(f"Totaal : {totaal} euro")
    for item in uitvoer:
        print(item)
    
    #for k,v in dictionary.items():
     #   print(f"{k} : {v}")
    
