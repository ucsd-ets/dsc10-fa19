test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your table should have these labels in this order. To reorder columns, use the select command.
          >>> comparison_table.labels == ('category', 'J', 'DJ')
          True
          >>> # Your table should have 32060 rows. If you have 32061, make sure you are not including Final Jeopardy!
          >>> comparison_table.num_rows == 32060
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