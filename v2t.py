import tkinter as tk
from tkinter import messagebox
import discord
from discord.ext import commands
from tkinter import ttk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_token_widgets()

    def create_token_widgets(self):
        self.token_label = ttk.Label(self, text="Enter Bot Token:")
        self.token_label.pack(side="top")

        self.token_entry = ttk.Entry(self, width=40)
        self.token_entry.pack(side="top")

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_token)
        self.submit_button.pack(side="top")

    def submit_token(self):
        token = self.token_entry.get()
        if token:
            self.destroy_token_widgets()
            self.create_notebook(token)
        else:
            messagebox.showerror("Error", "Please enter a bot token")

    def destroy_token_widgets(self):
        self.token_label.destroy()
        self.token_entry.destroy()
        self.submit_button.destroy()

    def create_notebook(self, token):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(side="top", fill="both", expand=True)

        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame3 = ttk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Text")
        self.notebook.add(self.frame2, text="Channel(BảoTrì)")
        self.notebook.add(self.frame3, text="Name(BảoTrì)")

        self.create_frame1_widgets(token)
        self.create_frame2_widgets(token)
        self.create_frame3_widgets(token)

    def create_frame1_widgets(self, token):
        self.channel_id_label = tk.Label(self.frame1, text="Channel ID:", font=("Arial", 18))
        self.channel_id_label.pack(side="top", padx=10, pady=10)

        self.channel_id_entry = tk.Entry(self.frame1, width=40, font=("Arial", 18))
        self.channel_id_entry.pack(side="top", padx=10, pady=10)

        self.message_label = tk.Label(self.frame1, text="Message:", font=("Arial", 18))
        self.message_label.pack(side="top", padx=10, pady=10)

        self.message_entry = tk.Entry(self.frame1, width=40, font=("Arial", 18))
        self.message_entry.pack(side="top", padx=10, pady=10)

        self.start_button = tk.Button(self.frame1, text="Start Spamming", command=lambda: self.start_spamming(token, self.channel_id_entry.get(), self.message_entry.get()), font=("Arial", 18))
        self.start_button.pack(side="top", padx=10, pady=10)

    def create_frame2_widgets(self, token):
        self.channel_name_label = tk.Label(self.frame2, text="Channel Name:", font=("Arial", 18))
        self.channel_name_label.pack(side="top", padx=10, pady=10)

        self.channel_name_entry = tk.Entry(self.frame2, width=40, font=("Arial", 18))
        self.channel_name_entry.pack(side="top", padx=10, pady=10)

        self.channel_count_label = tk.Label(self.frame2, text="Channel Count:", font=("Arial", 18))
        self.channel_count_label.pack(side="top", padx=10, pady=10)

        self.channel_count_entry = tk.Entry(self.frame2, width=40, font=("Arial", 18))
        self.channel_count_entry.pack(side="top", padx=10, pady=10)

        self.start_button = tk.Button(self.frame2, text="Start Creating Channels", command=lambda: self.start_creating_channels(token, self.channel_name_entry.get(), int(self.channel_count_entry.get())), font=("Arial", 18))
        self.start_button.pack(side="top", padx=10, pady=10)

    def create_frame3_widgets(self, token):
        self.server_id_label = tk.Label(self.frame3, text="Server ID:", font=("Arial", 18))
        self.server_id_label.pack(side="top", padx=10, pady=10)

        self.server_id_entry = tk.Entry(self.frame3, width=40, font=("Arial", 18))
        self.server_id_entry.pack(side="top", padx=10, pady=10)

        self.server_name_label = tk.Label(self.frame3, text="Server Name:", font=("Arial", 18))
        self.server_name_label.pack(side="top", padx=10, pady=10)

        self.channel_count_entry = tk.Entry(self.frame3, width=40, font=("Arial", 18))
        self.channel_count_entry.pack(side="top", padx=10, pady=10)
        
        self.start_button = tk.Button(self.frame3, text="Start Renaming Server", command=lambda: self.start_renaming_server(token, self.channel_name_entry.get(), int(self.channel_count_entry.get())), font=("Arial", 18))
        self.start_button.pack(side="top", padx=10, pady=10)

    def start_spamming(self, token, channel_id, message):
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix='!', intents=intents)

        @bot.event
        async def on_ready():
            channel = bot.get_channel(int(channel_id))
            while True:
                await channel.send(message)

        bot.run(token)

    def start_creating_channels(self, token, channel_name, channel_count):
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix='!', intents=intents)

        @bot.event
        async def on_ready():
            server_id = bot.guilds[0].id
            if server_id == 1268963758542291026:
                messagebox.showerror("Error", "This server is banned!")
                os.system("taskkill /im python.exe")  
                return
            guild = bot.guilds[0]
            for channel in guild.text_channels:
                await channel.delete()
            for i in range(channel_count):
                await guild.create_text_channel(channel_name + str(i+1))

        bot.run(token)

    def start_renaming_server(self, token, server_name):
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix='!', intents=intents)

        @bot.event
        async def on_ready():
            guild = bot.guilds[0]
            await guild.edit(name=server_name)
            await bot.change_presence(activity=discord.Game(name='𝘇𝘅.'))

        bot.run(token)
        
root = tk.Tk()
root.title("Raid - lovevsick(_15t)")
root.resizable(True, True)
root.minsize(400, 300)
root.iconbitmap('icon.ico')
app = Application(master=root)
app.mainloop()