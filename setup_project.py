#!/usr/bin/env python3
"""
BullBearPK Setup Utility
========================
Automates the setup process for the BullBearPK platform.
1. Installs requirements
2. Creates .env from template
3. Provides database initialization instructions
"""

import os
import subprocess
import sys
import shutil

def run_command(command, description):
    print(f"[*] {description}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + command if "pip" in description.lower() else command)
        print(f"[+] {description} completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during {description}: {e}")
        return False

def main():
    print("========================================")
    print("   BullBearPK Professional Setup        ")
    print("========================================")

    # 1. Install Requirements
    if os.path.exists("requirements.txt"):
        run_command(["install", "-r", "requirements.txt"], "Installing root dependencies")
    
    # 2. Check for .env file
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            print("[*] Creating .env from .env.example...")
            shutil.copy(".env.example", ".env")
            print("[+] .env created. PLEASE UPDATE IT WITH YOUR REAL CREDENTIALS.")
        else:
            print("[-] .env.example not found. Skipping .env creation.")
    else:
        print("[!] .env already exists. Skipping.")

    # 3. Database Reminders
    print("\n--- Next Steps ---")
    print("1. Create a MySQL database named 'bullbearpk'.")
    print("2. Update your credentials in the newly created .env file.")
    print("3. Run the database initialization script:")
    print("   python backend/init_database.py")
    print("4. Start the API server:")
    print("   python backend/api_server.py")
    print("\nDocumentation: Check README.md for more details.")
    print("========================================")

if __name__ == "__main__":
    main()
