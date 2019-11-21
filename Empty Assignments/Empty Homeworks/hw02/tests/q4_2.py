test = {
  'name': 'Question 4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Wrong Format
          >>> isinstance(bad_apps, int) or isinstance(bad_apps, np.integer)
          True
          >>> isinstance(good_apps, int) or isinstance(good_apps, np.integer)
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
