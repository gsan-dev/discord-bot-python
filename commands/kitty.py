import discord
from discord.ext import commands
from datetime import datetime

def setup_kitty(bot):
    @bot.command(name='kitty')
    async def kitty(ctx):
        # Obtener la fecha y hora actual
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear el embed
        embed = discord.Embed(
            title="🐱 Hello Kitty",
            description="Hello Kitty es un personaje icónico creado por la compañía japonesa Sanrio.",
            color=discord.Color.from_rgb(255, 0, 0)  # Rojo
        )

        # Añadir campos con información sobre Hello Kitty
        embed.add_field(name="Creación", value="Diseñada por Yuko Shimizu, lanzada en 1974.", inline=False)
        embed.add_field(name="Características", value="Gata bobtail blanca con un lazo rosa en la oreja izquierda.", inline=False)
        embed.add_field(name="Cumpleaños", value="1 de noviembre de 1974", inline=False)
        embed.add_field(name="Lugar de Nacimiento", value="Londres, Inglaterra", inline=False)
        embed.add_field(name="Comida Favorita", value="Tarta de manzana hecha por su madre.", inline=False)
        embed.add_field(name="Palabra Favorita", value="Amistad", inline=False)

        # Añadir un footer con el nombre del usuario que solicitó el comando y la fecha/hora
        embed.set_footer(text=f"Solicitado por {ctx.author.name} | {now}")

        # Enviar el embed como respuesta al mensaje
        await ctx.reply(embed=embed)