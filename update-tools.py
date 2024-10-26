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

def print_info(command, name):
    print_line()
    print(f"Running: {command}")
    print(f"Updating {name}...")
    run_command([name, "--version"])
    run_command(command)
    run_command([name, "--version"])
    print_line()

# Update Bun
print("Updating Bun...")
run_command(["bun", "--version"])
run_command(["bun", "upgrade"])
run_command(["bun", "--version"])

# Update pnpm
print("Updating pnpm...")
run_command(["pnpm", "--version"])
run_command(["pnpm", "self-update"])
run_command(["pnpm", "--version"])

# Update Python and pip
print("Updating pip...")
run_command(["pip", "--version"])
run_command(["pip", "install", "--upgrade", "pip"])
run_command(["pip", "--version"])

# Update Deno
print("Updating Deno...")
run_command(["deno", "--version"])
run_command(["deno", "upgrade"])
run_command(["deno", "--version"])

