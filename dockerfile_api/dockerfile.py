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

class WorkdirCommand(Command):
  def __init__(self, workdir):
    super(WorkdirCommand, self).__init__("WORKDIR")
    self.workdir = workdir

class EnvCommand(Command):
  def __init__(self, env_var, val):
    super(EnvCommand, self).__init__("ENV")
    self.env_var = env_var
    self.val = val

class CopyCommand(Command):
  def __init__(self, source, destination):
    super(CopyCommand, self).__init__("COPY")
    self.source = source
    self.destination = destination

class EntrypointCommand(Command):
  def __init__(self, entrypoint):
    super(EntrypointCommand, self).__init__("ENTRYPOINT")
    self.entrypoint = entrypoint

def command_from(image):
  return FromCommand(image)

def command_run(command):
  return RunCommand(command)

def command_user(user):
  return UserCommand(user)

def command_workdir(workdir):
  return WorkdirCommand(workdir)

def command_env(env_var, val):
  return EnvCommand(env_var, val)

def command_copy(source, destination):
  return CopyCommand(source, destination)

def command_entrypoint(entrypoint):
  return EntrypointCommand(entrypoint)

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
  elif command.command == "WORKDIR":
    file.write(f"{command.workdir}")
  elif command.command == "ENV":
    file.write(f"{command.env_var} {command.val}")
  elif command.command == "COPY":
    file.write(f"{command.source} {command.destination}")
  elif command.command == "ENTRYPOINT":
    file.write(command.entrypoint)
  else:
    pass
    
  file.write("\n")
