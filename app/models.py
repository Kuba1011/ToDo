from dataclasses import dataclass #import dekoratora, ulatwia tworzenie klas danych

@dataclass      #dzieki temu nie trzeba pisac __init__ i __repo__
class Task:     #klasa opisujaca zadanie
    id: int     #identifikator zadania
    title: str  #tytul zadania
    done: bool = False   #czy zadanie zostalo wykonane. domyslnie False 


    
