import os
from flask import Flask, request
import shlex
import subprocess
def validate_command(cmd):
    safe_commands = ['ls', 'cd']
    splitted_cmd = cmd.split()
    if not splitted_cmd or splitted_cmd[0] not in safe_commands:
        return None
    main_cmd = splitted_cmd.pop(0)
    validated_index = int(safe_commands.index(main_cmd))
    allowed_command = [safe_commands[validated_index]]
    if len(splitted_cmd) >= 1:
        allowed_command = allowed_command + splitted_cmd
    return allowed_command
def validate_command(cmd):
    splitted_cmd = cmd.split()
    if not splitted_cmd or splitted_cmd[0] not in SAFE_COMMANDS:
        raise ValueError('Command not allowed')

SAFE_COMMANDS = {'ls', 'cd'}

app = Flask(__name__)

@app.route('/run')
def run_command():
    # Vulnerable: Directly using URL parameter in a system command
    command = request.args.get('command')
    validate_command(command)
    command = shlex.split(command)
    validated_command = validate_command(command)
    subprocess.run(validated_command, check=True, shell=False)
    return "Command executed"

if __name__ == "__main__":
    app.run()



