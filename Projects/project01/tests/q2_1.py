test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #check column names
          >>> test = ['artist_name','track_name','key','popularity','acousticness','danceability','energy','valence','tempo','duration_min','tempo_name']
          >>> labels = list(tracks.labels)
          >>> np.array([True if i in labels else False for i in test]).all()
          True
          >>> #make sure there are no spelling or capitalization errors
          >>> tracks.where('tempo_name', are.not_contained_in(["Lento", "Adagio", "Adante", "Moderato", "Allegro", "Vivace", "Presto"])).num_rows
          0
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