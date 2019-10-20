test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #make sure column names are correct
          >>> test = ['artist', 'country', 'artist_listeners', 'artist_plays', 'tag_list']
          >>> labels = list(artists.labels)
          >>> np.array([True if i in labels else False for i in test]).all()
          True
          >>> isinstance(artists.column('tag_list').item(0),list) #each entry of tag_list should be a list
          True
          >>> artists.column('tag_list').item(0)[2][0]!=" " #make sure your tags don't start with a space
          True
          >>> artists.column('tag_list').item(6)[0].islower() #make sure tags are lowercase
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