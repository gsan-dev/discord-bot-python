import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Importar comandos
from clients.new_members import setup_new_members
from clients.verifier import setup_verifier
from clients.helpingmachine import setup_command_helper

from commands.ping import setup_ping
from commands.avatar import setup_avatar
from commands.kitty import setup_kitty


# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar el bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ha conectado a Discord!')

setup_command_helper(bot)

# Configurar la funcionalidad de nuevos miembros
setup_new_members(bot)

# Configurar el verificador
setup_verifier(bot)

setup_ping(bot)

setup_avatar(bot)

setup_kitty(bot)

# Ejecutar el bot
bot.run(TOKEN)