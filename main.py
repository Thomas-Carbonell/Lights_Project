import sys  # Standard library imports
from UserInterface import App
from SmartPlug import SmartPlug
# Optional: Import third-party libraries (e.g., numpy, requests)
# import numpy as np
# import requests

# Optional: Import local modules (e.g., my_module)
# from my_module import some_function


def main():
    """
    Main function that runs when the script is executed.

    :param args: List of command-line arguments.
    """
    plug = SmartPlug("192.168.1.78","thomaslmcarbonell@outlook.com","ErnieandRoxy2018!")
    Devices = []
    f = open("Devices.txt", "r")
    for x in f:
        x=x.strip("\n")
        x = x.split(",")
        Devices.append(x)
    for i in Devices:
        print(i[1])
    plug.connect()
    app = App(plug)
    app.mainloop()


if __name__ == "__main__":
    # Call the main function and pass command-line arguments (excluding the script name)
    main()
