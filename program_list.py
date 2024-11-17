import os
import subprocess


def _process_output(data):
    lines = data.splitlines()

    # Find where 'DisplayName' is and remove the header and dashed lines
    start_index = next((i for i, line in enumerate(lines) if line.strip() == 'DisplayName'), None)

    # If header is found, remove the first two lines (header + dashed line)
    if start_index is not None:
        lines = lines[start_index + 2:]

    # Remove any lines that are empty or just spaces
    lines = [line.strip() for line in lines if line.strip()]

    # Print the final list of program names
    return lines


class GetProgramList:
    def __init__(self, script='Control_Panel_Get_Soft_List.ps1'):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.script = os.path.join(script_dir, script)

    def get_program_list(self):
        """
        Returns a formatted list of all programs installed on PC. Necessary powershell script is located in
        Control_Panel_Get_Soft_List.ps1 file.
        """

        output = subprocess.run(['powershell.exe', '-ExecutionPolicy', 'RemoteSigned', '-File', self.script],
                                stdout=subprocess.PIPE)
        output = output.stdout.decode().strip()
        output = _process_output(output)
        return output
