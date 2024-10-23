import discord
from discord.ext import commands
from datetime import datetime

def setup_avatar(bot):
    @bot.command(name='avatar')
    async def avatar(ctx, user: discord.Member = None):
        # Si no se especifica un usuario, usa el autor del mensaje
        target_user = user or ctx.author

        # Obtener la fecha y hora actual
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear el embed
        embed = discord.Embed(
            title=f"Avatar de {target_user.name}",
            description=f"Aquí está el avatar de {target_user.mention}",
            color=discord.Color.from_rgb(255, 0, 0)  # Rojo
        )

        # Añadir el avatar como imagen principal del embed
        embed.set_image(url=target_user.avatar.url)

        # Añadir un footer con el nombre del usuario que solicitó el comando y la fecha/hora
        embed.set_footer(text=f"Solicitado por {ctx.author.name} | {now}")

        # Enviar el embed como respuesta al mensaje
        await ctx.reply(embed=embed)