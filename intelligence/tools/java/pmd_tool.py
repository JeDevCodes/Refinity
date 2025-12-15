import subprocess

class PMDTool:
    def __init__(self, pmd_path: str):
        self.pmd_path = pmd_path

    def run_pmd(self, code: str):
        # Save code to a temporary file
        with open("temp.java", "w") as file:
            file.write(code)

        # Run PMD using subprocess
        result = subprocess.run(
            ['java', '-cp', self.pmd_path, 'net.sourceforge.pmd.cli.Main', 'temp.java', 'xml'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Parse the result (XML or text format)
        return result.stdout.decode()  # PMD output
