class User:
  username = ""
  password = ""
  clearance = -1

  def __init__(self, sUsername, sPassword, iClearance):
    self.username = sUsername
    self.password = sPassword
    self.clearance = iClearance
