import discord
from discord.ext import commands
import difflib

def setup_command_helper(bot):
    # Lista de comandos disponibles (actualiza esta lista con todos tus comandos)
    available_commands = ['ping', 'avatar', 'kitty', 'verify', 'saludar', 'ayuda']

    @bot.event
    async def on_message(message):
        # Ignorar mensajes del propio bot
        if message.author == bot.user:
            return

        # Procesar el comando normalmente
        await bot.process_commands(message)

        # Verificar si el mensaje comienza con '!' pero no es un comando reconocido
        if message.content.startswith('!'):
            command = message.content.split()[0][1:].lower()  # Obtener el comando sin el '!'
            if command not in available_commands:
                # Encontrar comandos similares
                similar_commands = difflib.get_close_matches(command, available_commands, n=3, cutoff=0.6)
                
                if similar_commands:
                    suggestions = ", ".join([f"`!{cmd}`" for cmd in similar_commands])
                    response = f"El comando `!{command}` no existe. ¿Quizás quisiste decir: {suggestions}?"
                else:
                    response = f"El comando `!{command}` no existe. Usa `!ayuda` para ver la lista de comandos disponibles."
                
                await message.reply(response)
                return

    @bot.command(name='ayuda')
    async def ayuda_command(ctx):
        embed = discord.Embed(
            title="Ayuda de Comandos",
            description="Aquí tienes una lista de los comandos disponibles:",
            color=discord.Color.blue()
        )
        
        for cmd in available_commands:
            embed.add_field(name=f"!{cmd}", value="Descripción del comando", inline=False)
        
        embed.set_footer(text="Usa '!' seguido del nombre del comando para ejecutarlo.")
        await ctx.send(embed=embed)

    # Manejador de errores para comandos
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            # Este error ya está manejado en on_message, así que lo ignoramos aquí
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Error: Falta un argumento requerido. Usa `!ayuda {ctx.command}` para más información.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Error: Argumento inválido. Usa `!ayuda {ctx.command}` para más información.")
        else:
            await ctx.send(f"Ocurrió un error al ejecutar el comando: {str(error)}")