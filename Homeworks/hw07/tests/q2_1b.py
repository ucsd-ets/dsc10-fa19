test = {
  'name': 'Question 2_1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(writing_fixed, Table)
          True
          >>> set(writing_fixed.labels) == {'course', 'Study Hrs/wk', 'grades'}
          True
          >>> isinstance(course_means_fixed, Table)
          True
          >>> set(course_means_fixed.labels) == {'course', 'Study Hrs/wk mean', 'grades mean'}
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
