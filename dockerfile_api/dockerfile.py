class Command:
  def __init__(self, command):
    self.command = command

class FromCommand(Command):
  def __init__(self, image):
    super(FromCommand, self).__init__("FROM")
    self.image = image

class RunCommand(Command):
  def __init__(self, run_command):
    super(RunCommand, self).__init__("RUN")
    self.run_command = " \\\n".join(run_command.split("\n"))

class UserCommand(Command):
  def __init__(self, user):
    super(UserCommand, self).__init__("USER")
    self.user = user

def command_from(image):
  return FromCommand(image)

def command_run(command):
  return RunCommand(command)

def command_user(user):
  return UserCommand(user)

def write(filename, dockerfile):
  with open(filename, "w") as file:
    for command in dockerfile:
      write_command(command, file)

def write_command(command, file):
  file.write(f"{command.command} ")
  if command.command == "FROM":
    file.write(f"{command.image}")
  elif command.command == "RUN":
    file.write(f"{command.run_command}")
  elif command.command == "USER":
    file.write(f"{command.user}")
  else:
    pass
    
  file.write("\n")
