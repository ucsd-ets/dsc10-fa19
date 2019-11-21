test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(ungroup_table) # your answer should be a function called `ungroup_table`
          True
          >>> isinstance(np.std(ungroup_table(salaries)), float)
          True
          >>> isinstance(np.mean(ungroup_table(salaries)), float)
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
