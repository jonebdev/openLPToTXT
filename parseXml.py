import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join

def parseXml(fileName, xmlFile):
  file = open(fileName, 'w')
  tree = ET.parse(xmlFile)
  root = tree.getroot()
  
  for child in root[1]:
    if (child[0].text != None):
      lines = child[0].text.split(' newline ')
      for line in lines: 
        file.write(line)
        file.write('\n')
    file.write('\n')
  
  file.close()



mypath = 'songs/'
songs = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for song in songs:
  songName = song.split('.xml')
  fileName = 'output/' + songName[0] + '.txt'
  xmlFileName = 'songs/' + song
  parseXml(fileName, xmlFileName)