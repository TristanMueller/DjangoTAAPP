
class Clearance:
  TA = 4
  INSTRUCTOR = 3
  ADMINISTRATOR = 2
  SUPERVISOR = 1


class User:
  def __init__(self, sUsername, sPassword, iClearance):
    self.username = sUsername
    self.password = sPassword
    self.clearance = iClearance
