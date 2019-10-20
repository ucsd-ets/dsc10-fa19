test = {
  'name': 'Question 5_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> #check column names, possibly in a different order
          >>> set(joined_by_song_artist.labels) == set(['Song; Artist','artist_name','track_name','key','popularity','acousticness','danceability','energy','valence','tempo','duration_min','tempo_name','Song','Artist','Weeks On Chart','Peak Rank'])
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