import sys
import subprocess

class pip:
    def runCommand(self, command, package):
        process = subprocess.Popen([sys.executable, '-m', 'pip', command, package], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        exit_code = process.wait()
        class returnableClass:
            pass
        returnable = returnableClass()
        returnable.exitcode = int(exit_code)
        returnable.stdout = stdout
        returnable.stderr = stderr
        return returnable
    def install(self, package):
        returnable = self.runCommand('install', package)
        return returnable
    def uninstall(self, package):
        returnable = self.runCommand('uninstall', package)
        return returnable
