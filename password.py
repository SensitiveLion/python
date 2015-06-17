class CommonTests:
  import re
  def __init__(self, password):
    self.password = password

  def prep
    password.lstrip()

  def long
    len(password); >= 15
    # want to be true

  def only_alphanumaric
    password.isalnum();
    # want to be false

  def only_alpha
    password.isalpha();
    # want to be false

  def only_lowercase
    password.isdigit();
    # want to be false

  def only_numbers
    password.isnumeric();
    # want to be false

  def only_whitespace
    password.isspace();
    # want to be false

  def only_uppercase
    password.isupper();
    # want to be false

  def special_cases
    specail = ["!", "@", "#", "$", "%", "^", "(", ")", "?", ":", "{", "}", "\\", "]", "[", "'", "/", ",", "-", "`", "+", "~", "_"]
    count = 0
    for character in list(password):
      if character in specail:
        count += 1
    if count >= 1:
      return true
    # want to be true

  def uppercase
    matches = re.sub('[^A-Z]*', '', password)
    len(matches) >= 2;
    # want to be true

  def lowercase
    matches = re.sub('[^a-z]*', '', password)
    len(matches) >= 2;
    # want to be true
    `
  def numbers
    matches = re.sub('[^0-9]*', '', password)
    len(matches) >= 2;
    # want to be true
