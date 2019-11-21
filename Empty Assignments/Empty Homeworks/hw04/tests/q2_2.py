test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(owners_pets, Table)
          True
          >>> set(owners_pets.labels) == {'Age','Gender','Kind','Name','OwnerID','OwnerName','PetID','State','StateFull','Surname','ZipCode'}
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
