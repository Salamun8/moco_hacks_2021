import os

try:
    # imports all necessary packages & modules
    import subprocess
    from subprocess import CalledProcessError
    import sys

# except case to handle import failure
except Exception as e:
    print("Some of the required libraries are missing! {}".format(e))



# Libraries to install:
# wget, bs4, requests, schedule, PyDrive
packages_to_install = ["wget", "bs4", "requests", "schedule", "PyDrive"]

# initializes array to track names of failed package installations
failed_package_installations = []

# installs all prerequisite packages
def install(packages_to_install):
    # creates loop to install each package
    for i in range(len(packages_to_install)):
        package = packages_to_install[i]

        # tries to pip install each package
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print("Installation of " + str(package) + " was successful!")
        
        # except case to report and account for installation failure
        except CalledProcessError:
            failed_package_installations.append(package)
            print("Installation of " + str(package) + " was unsuccessful!")
    
    # check for successful installation quantity
    successful_installations = len(packages_to_install) - len(failed_package_installations)

    # alerts user that all necessary packages have been installed successfully
    if(successful_installations == len(packages_to_install)):
        print("Installations of all prerequisites successful!")
    
    # alerts user that some of the necessary packages have not been installed successfully, and specifies which ones failed
    else:
        print("Installation of " + str(failed_package_installations) + " package(s) failed!")

# runs installation function
install(packages_to_install)