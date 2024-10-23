import discord
from discord.ext import commands
from datetime import datetime

def setup_ping(bot):
    @bot.command(name='ping')
    async def ping(ctx):
        # Calcular la latencia
        latency = round(bot.latency * 1000)  # Convertir a milisegundos

        # Obtener la fecha y hora actual
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear el embed
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latencia: **{latency}ms**",
            color=discord.Color.from_rgb(255, 0, 0)  # Rojo
        )

        # Añadir un campo adicional con un color negro
        embed.add_field(
            name="Estado",
            value="```ansi\n\u001b[0;30mOnline\u001b[0m```",
            inline=False
        )

        # Añadir una imagen al thumbnail
        embed.set_thumbnail(url="https://imgs.search.brave.com/hWZJyxEQ69R7vuZw7BaO5YdLW-flkRcscI5_o_JKNbc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9nY2Ru/LmVtb2wuY2wvbWl0/b3MteS1lbmlnbWFz/L2ZpbGVzLzIwMTYv/MDcvZXN2YXN0aWNh/LnBuZw")

        # Añadir un footer con el nombre del usuario y la fecha/hora
        embed.set_footer(text=f"Solicitado por {ctx.author.name} | {now}")

        # Enviar el embed
        await ctx.send(embed=embed)