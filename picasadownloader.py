import urllib
import xml.etree.ElementTree as ET
import os, sys

username = ''

albumListFeed = urllib.urlopen('http://picasaweb.google.com/data/feed/api/user/'+username+'?kind=album')
albumListFile = albumListFeed.read()
albumList = ET.fromstring(albumListFile)
galleryDirectory = 'gallery/'
os.mkdir( galleryDirectory, 0755 );
  
for child in albumList.iter('{http://www.w3.org/2005/Atom}entry'): 
	albumFeedUrl = child.find('{http://www.w3.org/2005/Atom}link').get('href')
	albumFeed = urllib.urlopen(albumFeedUrl)
	albumFile = albumFeed.read() 
	albumName = galleryDirectory+(child.find('{http://schemas.google.com/photos/2007}name').text)
	os.mkdir( albumName, 0755 );

	album = ET.fromstring(albumFile)
	i = 1
	for photo in album.iter('{http://www.w3.org/2005/Atom}entry'):
		photoUrl = photo.find('{http://www.w3.org/2005/Atom}content').get('src') 
		photoUrl = photoUrl[::-1].replace("/","/0s/",1)[::-1]
		urllib.urlretrieve(photoUrl, albumName+'/'+str(i)+'.jpg')
		i = i + 1
