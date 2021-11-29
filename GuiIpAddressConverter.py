import tkinter as tk

class IpAddressConverter:

    def __init__(self, start_app=False):
        # if true then run app
        if (start_app == True):
            self.main_window()

    def main_window(self):
        # create root window with title
        root_window = tk.Tk(className=" Convert IP Address to Binary")

        # mengubah ukuran window saat pertama kali dibuka
        root_window.geometry("500x400")

        # agar ukuran windownya tidak bisa dirubah (fix size)
        root_window.resizable(False, False)

        # to give a caption
        caption = tk.Label(root_window, text='IP Address (pisahkan dengan titik)').pack()

        # input ip address
        inputIpAddress = tk.Entry(root_window)
        inputIpAddress.pack()

        # displaying conversion result
        def change_binary_result():
            binary_result.config(text=f"Binary: {'.'.join(map(self.decimal_to_binary, inputIpAddress.get().split('.')))}")
            binary_result.pack()

        # button
        myButton = tk.Button(root_window, text='Convert', command=change_binary_result).pack()

        # text initial
        binary_result = tk.Label(root_window, text="")
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

# start app
IpAddressConverter(True)