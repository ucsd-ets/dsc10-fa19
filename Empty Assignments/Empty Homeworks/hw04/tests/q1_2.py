test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(evaluations) == 100
          True
          >>> isinstance(evaluations, np.ndarray)
          True
          >>> set(np.unique(evaluations)) == {'Excellent', 'Good', 'Fair', 'Poor', 'Bad'}
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
