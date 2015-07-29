import xml.etree.ElementTree as ET

__author__ = 'aldola'

tags = []

#Llegeix el fitxer i generea un Etree
def get_data_tree(fname):
    myfile = open(fname,'r') #Obrim el fitxer
    data = myfile.read()     #Convertim el fitxer a un string
    etree = ET.fromstring(data) #Obtenim un etree
    return etree

#Rep la llista de tots els tags de un xml i els fica a la variable global tags
def get_tags(etree):
    iterator = etree.iter()     #Convertim el etree en un iterador
    for element in iterator:        #Recorrem el iterador
        if element.tag not in tags: #Obtenim nomes els tags no trobats encara
            tags.append(element.tag)#Afegim els tags a la variable global

#Retorna totes les dades que etiguin encapsulades en el tag
def get_tag_data(etree,tag):
    data = []
    for element in etree.findall(tags[1]):#Mes info a info 1
        data.append(element.find(tag).text) #Afegim les dades en una llista
    return data #Retorna una llista amb totes les dades trobades


if __name__ == "__main__":
    etree = get_data_tree("plants.xml")
    get_tags(etree)
    print get_tag_data(etree,"BOTANICAL")
    
    
    
'''
INFO
-----------------------------------------------------------------------------------------
1:En el cas de que el xml estigo encapsulat en aquesta estructura.

<DATA>
    <TIPE>
        <INFO1>text</INFO1>
        <INFO2>text</INFO1>
        <INFO3>text</INFO1>
    </TIPE>
</DATA>

Agafa el grup tipe per poder accedir a les seus tags, en case de que estigo en un altre
nivell, s'haura de canviar.
'''
