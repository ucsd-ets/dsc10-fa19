test = {
  'name': 'Question 1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(most_beats,str)  #verify string
          True
          >>> #make sure they didn't alter the tracks table to answer this question
          >>> test = ['artist_name','track_name','key','popularity','acousticness','danceability','energy','valence','tempo','duration_min']
          >>> labels = list(tracks.labels) 
          >>> np.array([True if i in labels else False for i in test]).all()
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