test = {
  'name': 'Question 1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #verify correct columns
          >>> test = ['artist_name', 'proportion_top_songs']
          >>> labels = list(popular_table.labels) 
          >>> np.array([True if i in labels else False for i in test]).all()
          True
          >>> (popular_table.column('proportion_top_songs')>0).all() #make sure they only include artists with songs above 90 popularity
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