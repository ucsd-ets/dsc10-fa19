test = {
  'name': 'Question 4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #check column names
          >>> test = ['artist_name', 'tag_list', 'average_plays_per_song']
          >>> labels = list(average_plays.labels)
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