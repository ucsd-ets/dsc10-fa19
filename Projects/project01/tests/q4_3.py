test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> #check column names
          >>> test = ['tag', 'score']
          >>> labels = list(scores.labels)
          >>> np.array([True if i in labels else False for i in test]).all()
          True
          >>> (scores.column(1)>=1).all() and (scores.column(1)<=5).all() #each tag's score should be between 1 and 5
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