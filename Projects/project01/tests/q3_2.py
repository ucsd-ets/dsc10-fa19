test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #make sure column names are correct and no extra columns have been added
          >>> test = ['artist', 'country', 'artist_listeners', 'artist_plays', 'tag_list']
          >>> labels = list(relax_artists.labels)
          >>> np.array([True if i in labels else False for i in test]).all()
          True
          >>> 'relax' in relax_artists.column('tag_list').item(1) #make sure the tag list contains relax
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