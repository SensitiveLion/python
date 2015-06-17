  def prep
    password.lstrip()

  def long
    len(password); >= 30
    # want to be true

  def special_cases
    specail = [" "]
    count = 0
    for x in list(password):
      if x in specail:
        count += 1
        print count
    if count >= 1:
      return true
    # want to be true
