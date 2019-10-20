test = {
  'name': 'Question 5_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(joined_by_song, Table) #table called joined_by_song 
          True
          >>> joined_by_song.labels == ('track_name', 'artist_name','key','popularity','acousticness','danceability','energy','valence','tempo','duration_min','tempo_name','Artist','Weeks On Chart','Peak Rank') #check column labels, possibly in a different order
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}