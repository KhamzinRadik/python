# -*- coding: cp1251 -*-
violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
m_time=float(0)

while True: 
  number_of_songs=int(input('input number_of_songs: '))
  if number_of_songs<=len(violator_songs):
      break
for i_song in range (number_of_songs):
 

  while True:
      name_of_the_songs=input('enter the name of the song :')
      if name_of_the_songs in violator_songs :
        m_time=m_time+(violator_songs[name_of_the_songs])
        break
      else:
          print ('There is no such song in the list')


print('there is no such song in the list of Total playing time of the songs:',m_time)


