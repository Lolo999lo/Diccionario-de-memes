meme_dict = {
            "CRINGE" : "Algo excepcionalmente raro o embarazoso",
            "LOL" : "Una respuesta común a algo gracioso",
            "BRO" : "Así se le dice a un amigo",
            "CREEPY" : "Algo aterrador o siniestro"
            "HATER" : "Alguien odioso o que da puro hate (malas opiniones)"
            }
            
word = input("Escribe una palabra que no entiendas o no conoscas (Que sea en mayuscula por favor)")

if word in meme_dict.keys():
    print(meme_dict[word])
else: 
    print("En el momento no tenemos esa palabra, lo sentimos")
