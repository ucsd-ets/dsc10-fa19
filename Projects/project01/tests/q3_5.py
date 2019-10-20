test = {
  'name': 'Question 3_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #check column names
          >>> test = ['artist','country','artist_listeners','artist_plays','tag_list','num_countries']
          >>> labels = list(with_num_countries.labels)
          >>> np.array([True if i in labels else False for i in test]).all()
          True
          >>> isinstance(with_num_countries.column('num_countries').item(0),int) or isinstance(with_num_countries.column('num_countries').item(0),np.integer)#check type
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