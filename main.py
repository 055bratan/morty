import os
import requests

os.system("clear")

def get_url(id):
    url=f'https://rickandmortyapi.com/api/character/{id}'
    responce=requests.get(url=url)
    data=responce.json()
    return data



def get_location(id):
    character=get_url(id)
    for i in character.keys():
        if i=='location':
            name_location=character['location']['name']
            url_location=character['location']['url']
            if url_location not in "":
              location_responce=requests.get(url_location)
              data=location_responce.json()
              info=f"""Наязвание локации: {name_location}
              Тип локации: {data['type']}
              Измерение локации:{data['dimension']}
              Дата создания:{data['created']}
             """
            else:info=f""" 
            Наязвание локации: {name_location}
            Тип локации: Unkown
            Измерение локации:Unkown
            Дата создания:Unknown
            """
            return info

    return data


def get_characters(id):
    if id <= 826:
        character=get_url(id)
        info=f"""
        Id personaja: {character['id']}
        Imya personaja:{character['name']}
        Pol personaja:{character['gender']}
        Rasa:{character['species']}
        Zhiznennoe polozhenie:{character['status']}
        Lichnost:{character['type']}
        Data sozdaniya:{character['created']}
        {get_location(id)}
        """
        return info
    else:
        return "Net takogo id"
    
id_characters=int(input("Enter id characters "))
print(get_characters(id_characters))


# try:
#      a=int(input("Vvedite cifru"))
# except ValueError:
#        print("Valuerror Tut nado cifru")
# else:
#       print("Its okay")
# finally:
#       print("123c 123")

# try:
#     with open('image/n.jpg','rb') as f:
#         f.read()
# except FileNotFoundError:
#     os.mkdir('image')
#     os.system('touch image/a.txt')
#     with open ('image/a.txt','r') as f:
#         f.read()
# else:
#     print("its okay")

# def my_function(name,age=10):
#     try:

