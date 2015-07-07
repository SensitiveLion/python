class Common(object):
  import sys
  import re

  password = sys.argv[1]

  def __init__(self, password):
    self.password = password

  def prep(self):
    password.lstrip()

  def long(self):
    len(password) >= 15
    # want to be true

  def only_alphanumaric(self):
    password.isalnum();
    # want to be false

  def only_alpha(self):
    password.isalpha();
    # want to be false

  def only_lowercase(self):
    password.isdigit();
    # want to be false

  def only_numbers(self):
    password.isnumeric();
    # want to be false

  def only_whitespace(self):
    password.isspace();
    # want to be false

  def only_uppercase(self):
    password.isupper();
    # want to be false

  def special_cases(self):
    specail = ["!", "@", "#", "$", "%", "^", "(", ")", "?", ":", "{", "}", "\\", "]", "[", "'", "/", ",", "-", "`", "+", "~", "_"]
    count = 0
    for character in list(password):
      if character in specail:
        count += 1
    if count >= 1:
      return true
    # want to be true

  def uppercase(self):
    matches = re.sub('[^A-Z]*', '', password)
    len(matches) >= 2;
    # want to be true

  def lowercase(self):
    matches = re.sub('[^a-z]*', '', password)
    len(matches) >= 2;
    # want to be true

  def numbers(self):
    matches = re.sub('[^0-9]*', '', password)
    len(matches) >= 2;
    # want to be true

  if uppercase() == True:
    result = "wow nice!"
  elif uppercase() == False:
    result = "not long enough"
  else:
    result = "damnit"

  print result
