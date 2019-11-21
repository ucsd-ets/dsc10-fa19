test = {
  'name': '2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> one_resample.column("serial number").item(0) == 108
          True
          >>> one_resample.column("serial number").item(16) == 78
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
