import tkinter
import customtkinter
from SmartPlug import SmartPlug
#newPlug = addPlug("IP","account", "Password")
#connect(newPlug)



# System Settings

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="Energy Usage")
        self.label.pack(padx=20, pady=20)
        self.title("Energy Usage")
        usage = customtkinter.CTkLabel(self, text=f"{usage} wh")
        usage.pack()


class App(customtkinter.CTk):
    def __init__(self, plug):
        super().__init__()
        self.plug = plug
        self.geometry("400x150")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        # App Frame
        self.geometry("1080x540")
        self.title("Light Interface")
        # Adding UI elements
        title = customtkinter.CTkLabel(self, text="Turn Light On and Off")
        title.pack(padx=10, pady=10)


        # Adding Light Button
        Light = customtkinter.CTkButton(self, text="Switch", command=self.toggle_light)
        Light.pack(padx=10, pady=10)

        # Adding option to get Energy Usage from the Plug
        self.energyUsage = customtkinter.CTkButton(self, text="Energy Consumption", command=self.open_toplevel)
        self.energyUsage.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def toggle_light(self):
        """
        Toggle the light on and off using the SmartPlug object.
        """
        print("toggled")
        self.plug.toggle()

    # Code to open "Top level" window
    def open_toplevel(self):
        usage = self.plug.getEnergyUsage()
        if usage is None:
            usage = "None"
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

