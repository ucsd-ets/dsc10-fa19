test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>>  #the table should have these columns
          >>> test = ['tempo_name','popularity mean','acousticness mean','danceability mean','energy mean','valence mean','tempo mean','duration_min mean']
          >>> labels = list(track_means.labels)
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