import subprocess
import platform

def run_command(command):
    try:
        # Use shell=True on Windows for compatibility
        result = subprocess.run(
            command, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            shell=(platform.system() == "Windows")
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(command)}:\n{e.stderr}")

def print_line():
    print("--------------------------------------------------")

def do_work(command, name):
    print_line()
    print(f"Running: {command}")
    print(f"Updating {name}...")
    print("Before update: ")
    run_command([name, "--version"])
    print("updating...")
    run_command(command)
    print("After update: ")
    run_command([name, "--version"])
    print_line()

# Update Bun
do_work(["bun", "--version"], "Bun")

# Update pnpm
do_work(["pnpm", "--version"], "pnpm")

# Update pip
do_work(["pip", "--version"], "pip")

# Update Deno
do_work(["deno", "--version"], "Deno")

