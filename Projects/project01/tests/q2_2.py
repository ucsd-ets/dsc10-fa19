test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(most_common_combination,np.ndarray) #make sure it's an array
          True
          >>> most_common_combination.size == 2 #make sure length is 2
          True
          >>> #make sure they have correct order
          >>> most_common_combination.item(0) in ["Lento", "Adagio", "Adante", "Moderato", "Allegro", "Vivace", "Presto"] 
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