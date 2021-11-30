import tkinter as tk

class IpAddressConverter:

    def __init__(self, start_app=False):
        # if true then run app
        if (start_app == True):
            self.main_window()

    def main_window(self):
        # create root window with title
        root_window = tk.Tk(className=" IP Address to Binary Converter")

        # mengubah ukuran window saat pertama kali dibuka
        root_window.geometry("700x450")

        # agar ukuran windownya tidak bisa dirubah (fix size)
        root_window.resizable(False, False)

        # to give a caption
        caption = tk.Label(root_window, text='IP Address (separate with . (dot))', font=("Arial", 13)).pack(pady=15)

        # input ip address
        inputIpAddress = tk.Entry(root_window, fg="#000000", bg='lightblue', width='37', font=("Arial", 11))
        inputIpAddress.pack(pady=3)

        # displaying conversion result
        def change_binary_result():
            try:
                if (inputIpAddress.get()):
                    binary_result.config(text=f"Binary: {'.'.join(map(self.decimal_to_binary, inputIpAddress.get().strip('.').split('.')))}")
            except ValueError:
                from tkinter import messagebox
                messagebox.showerror(title="Error", message="Invalid Input")


        # button
        myButton = tk.Button(root_window, text='Convert', command=change_binary_result, font=("Arial", 13), padx='10' ,pady="1.5").pack(pady=5)

        # text initial
        binary_result = tk.Label(root_window, font=("Arial", 12))
        binary_result.pack()

        # start app
        root_window.mainloop()

    def decimal_to_binary(self, decimal):
        # convert string to integer
        decimal = int(decimal)

        # to store binary result
        binary = ''

        # run while 'decimal' >= 1
        while (decimal):
            binary += str(decimal % 2)
            decimal //= 2

        # run while length of binary < 8
        while len(binary) < 8:
            binary += '0'

        # return binary with correct order
        return binary[::-1]


if __name__ == "__main__":
    IpAddressConverter(True)
