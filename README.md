# Speaker-Verification
The Speaker Verification for Password Reset system is designed to allow users to reset their password through voice recognition technology. The system works by capturing a voice sample during the user enrollment process and storing it in a database. When a
user requests a password reset, the system will prompt the user to provide a voice sample to compare against the registered sample. The system uses machine learning algorithms to analyze the voice samples and determine if they match. If the samples match, the user will be able to reset their password. If the samples do not match, the user will not be able to reset their password.

Note: To ensure the accuracy of the system, it is recommended to use a high-quality
microphone and to speak clearly during the registration and password reset processes.

Requirements
1. Asterisk PBX:

2. Operating System:
a. Linux (recommended distributions include CentOS, Ubuntu, Debian)
b. Processor: 1 GHz or faster
c. RAM: 1 GB or more
d. Disk Space: At least 20 GB of free space
e. Network: Ethernet interface

3. Zoiper 5:
a. Operating System: Windows 7 or later, macOS 10.10 or later, Linux (various
distributions).
b. Processor: 1 GHz or faster
c. RAM: 512 MB or more.
d. Network: Broadband internet connection for VoIP calls.
e. Microphone and Speakers/Headset: Required for making/receiving calls.
f. Webcam (for video calls).

4. Octave:
a. Operating System: Windows, macOS, Linux.
b. Processor: 1 GHz or faster.
c. RAM: 2 GB or more.
d. Disk Space: Several GBs for installation and data storage.
e. For advanced use, higher computational resources might be needed.
f. scikit-learn.

5. Python:
a. Versions 3.6 and above.
b. Operating System: Windows, macOS, Linux.
c. Dependencies: NumPy, SciPy.
d. Processor: 1 GHz or faster.
e. RAM: 1 GB or more (more for resource-intensive tasks).
f. Disk Space: Depending on the applications and libraries you install; a few
GBs are usually sufficient.

7.2.1.2 Installation

1. Asterisk PBX:
Install Linux: Choose a supported Linux distribution (e.g., CentOS, Ubuntu) and follow
their installation instructions.
Install Dependencies: Open a terminal and install necessary dependencies using
package manager commands specific to your distribution.
Download Asterisk: Download the Asterisk source code from the official website.67
Compile and Install: Extract the downloaded source code, navigate to the extracted
directory, and run the compilation and installation commands.
Configure Asterisk: Edit configuration files as needed for your setup (e.g., sip.conf,
extensions.conf).
Start Asterisk: Start the Asterisk service using the appropriate command.
Test: Use a softphone or SIP client to test your Asterisk installation.

2. Zoiper 5:
Download Installer: Visit the Zoiper website and download the installer for your operating
system.
Run Installer: Run the downloaded installer and follow the on-screen instructions.
Launch Zoiper: Once installed, launch Zoiper.
Set Up Account: Configure your SIP or VoIP account within Zoiper by providing the
necessary credentials.
Test: Make a test call to ensure Zoiper is working correctly.

3. Octave:
Install Octave: Use your package manager (on Linux) or download the installer (on
Windows/macOS) from the Octave website.
Run Octave: Launch Octave from the terminal or the provided shortcut.
Start Using: Octave's command-line interface will open. You can start running Octave
commands and scripts.

4. scikit-learn:
Python Environment: Ensure you have a working Python environment (Python 3.6 or
above) and pip installed.
Install scikit-learn: Open a terminal and run pip install scikit-learn to install the library and
its dependencies.68

5. Python:
Download Python: Download the Python installer for your operating system from the
official Python website.
Run Installer: Run the downloaded installer and follow the installation prompts.
Verify Installation: Open a terminal and run python --version to verify the installation.
Install Packages: Use pip, the Python package manager, to install additional packages
like scikit-learn. For example, pip install scikit-learn.

Usage of the System
1. Asterisk 16.4.0
2. GNU Octave, version 6.4.0
3. Python3
   
For a Systems operator to use the Speaker Verification for Password Reset System, the
operator would need to install the above-mentioned software correctly, in accordance with
their available systems and infrastructures. The operator can use the scripts provided in
the Appendix to set up the system. When implemented, the code will set up the functions
and processes that make up the speaker verification system.
The operator can then use the system to verify speakers. However, there are
modifications to be made to the scripts such as the locations of directories that will store
the audio files, features, models, etc.
