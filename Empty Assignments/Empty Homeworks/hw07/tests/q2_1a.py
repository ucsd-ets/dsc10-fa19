test = {
  'name': 'Question 2_1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(course_means, Table)
          True
          >>> set(course_means.labels) == {'course', 'Study Hrs/wk mean', 'grades mean'}
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
