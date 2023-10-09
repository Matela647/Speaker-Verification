#!/usr/bin/env python3
import os
import subprocess
import sys  # Import sys module to access command line arguments

# Set the login name and current working directory
working_directory = "/home/setenane/Desktop/SV_for_Password_Reset/Code_Snippets/mfcc"

# Change the current working directory
os.chdir(working_directory)

# Get the callerID argument passed from the dialplan
if len(sys.argv) < 2:
    print("Error: Missing callerID argument.")
    sys.exit(1)

callerID = str(sys.argv[1])  # Convert the argument to a string

# Execute the enrollment.m script in Octave using the callerID
octave_command = f"octave --eval \"addpath('{working_directory}'); verification('{callerID}'); exit;\""

try:
    # Capture the output and error messages
    result = subprocess.run(octave_command, shell=True, capture_output=True, text=True)
    # Get the verification result from Octave's output
    verification_result = result.stdout.strip()

    # Print the verification result for Asterisk to capture
    print(verification_result)


except subprocess.CalledProcessError as e:
    print(f"Error executing Octave command: {e}")

