# upgrade altair
!pip install altair==4.2
# importing packages, opening files, creating dataframe
import pandas as pd
import altair as alt
import xml.etree.ElementTree as ET

file = open("spotify.xml")
spotify_xml = file.read()
file.close()


spotify = ET.fromstring(spotify_xml)
spotify

# create lists
name = []
popularity = []
followers = []
genres = []
idlist = []
images = []

# go through all item elements in the tree
for item in spotify.findall('.//items'):
  # extract information and titles
  name.append( item.find('.//name').text )
  popularity.append( item.find('.//popularity').text )
  followers.append( item.find('.//followers/total').text )
  genres.append( item.find('.//genres').text )
  idlist.append( item.find('.//id').text )
  images.append( item.find('.//images').text )

# create dataframe
spotify_df = pd.DataFrame(
    {'name': name,
     'popularity': popularity,
     'followers' : followers,
     'genres' : genres,
     'idlist' : idlist,
     'images' : images
    })

# check
spotify_df
