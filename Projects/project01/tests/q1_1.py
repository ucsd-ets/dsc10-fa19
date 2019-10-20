test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> type(tracks.column('duration_min').item(0)) == float #verify the new column is of type float 
          True
          >>> #verify labels in correct order
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
