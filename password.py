class Common(object):
  import sys
  import re

  password = sys.argv[1]

  def __init__(self, password):
    self.password = password

  def prep(self):
    self.password.lstrip()

  def long(self):
    len(self.password) >= 15
    # want to be true

  def only_alphanumaric(self):
    self.password.isalnum();
    # want to be false

  def only_alpha(self):
    self.password.isalpha();
    # want to be false

  def only_lowercase(self):
    self.password.isdigit();
    # want to be false

  def only_numbers(self):
    self.password.isnumeric();
    # want to be false

  def only_whitespace(self):
    self.password.isspace();
    # want to be false

  def only_uppercase(self):
    self.password.isupper();
    # want to be false

  def special_cases(self):
    specail = ["!", "@", "#", "$", "%", "^", "(", ")", "?", ":", "{", "}", "\\", "]", "[", "'", "/", ",", "-", "`", "+", "~", "_"]
    count = 0
    for character in list(self.password):
      if character in specail:
        count += 1
    if count >= 1:
      return true
    # want to be true

  def uppercase(self):
    matches = re.sub('[^A-Z]*', '', self.password)
    len(matches) >= 2;
    return matches
    # want to be true

  def lowercase(self):
    matches = re.sub('[^a-z]*', '', self.password)
    len(matches) >= 2;
    # want to be true

  def numbers(self):
    matches = re.sub('[^0-9]*', '', self.password)
    len(matches) >= 2;
    # want to be true

if Common.uppercase():
  result = "wow nice!"
elif not(Common.uppercase()):
  result = "not long enough"
else:
  result = "damnit"

print result
