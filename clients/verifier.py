import discord
from discord.ext import commands
import random
import string
from PIL import Image, ImageDraw, ImageFont
import io
import asyncio

# Función para generar el captcha
def generate_captcha():
    # Generar una cadena aleatoria de 6 caracteres
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    # Crear una imagen
    image = Image.new('RGB', (200, 100), color = (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)
    
    # Dibujar el texto
    draw.text((20,20), captcha_text, font=font, fill=(0,0,0))
    
    # Añadir ruido
    for _ in range(1000):
        draw.point((random.randint(0, 200), random.randint(0, 100)), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    # Convertir la imagen a bytes
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    
    return captcha_text, buffer
def setup_verifier(bot):
    @bot.event
    async def on_message(message):
        if message.content.lower() == '!verify':
            # Verificar si el mensaje está en el canal correcto
            if message.channel.id != 1297889375824117923:
                await message.delete()
                try:
                    await message.author.send("Por favor, usa el comando !verify en el canal de verificación designado.")
                except discord.Forbidden:
                    # Si no podemos enviar DM, enviamos un mensaje efímero en el canal
                    await message.channel.send(f"{message.author.mention}, por favor usa el comando !verify en el canal de verificación designado.", delete_after=10)
                return

            # Borrar el mensaje del usuario
            await message.delete()
            
            # Generar y enviar el captcha
            captcha_text, captcha_image = generate_captcha()
            
            try:
                await message.author.send("Por favor, resuelve este captcha. Tienes 3 intentos.")
                await message.author.send(file=discord.File(captcha_image, 'captcha.png'))
                
                for attempt in range(3):
                    try:
                        response = await bot.wait_for('message', check=lambda m: m.author == message.author and m.guild is None, timeout=60.0)
                    except asyncio.TimeoutError:
                        await message.author.send("Tiempo agotado. Por favor, intenta de nuevo con !verify en el canal de verificación.")
                        return
                    
                    if response.content.upper() == captcha_text:
                        # Captcha correcto
                        guild = message.guild
                        member = guild.get_member(message.author.id)
                        
                        role_to_remove = guild.get_role(1297889374930735205)
                        role_to_add = guild.get_role(1297889374930735207)
                        
                        if role_to_remove in member.roles:
                            await member.remove_roles(role_to_remove)
                        await member.add_roles(role_to_add)
                        
                        await message.author.send("¡Verificación exitosa! Se te ha otorgado el rol verificado.")
                        return
                    else:
                        if attempt < 2:
                            await message.author.send(f"Incorrecto. Te quedan {2-attempt} intentos.")
                        else:
                            await message.author.send("Has agotado tus intentos. Por favor, intenta de nuevo con !verify en el canal de verificación.")
                            return
            except discord.Forbidden:
                await message.channel.send(f"{message.author.mention}, no puedo enviarte mensajes directos. Por favor, habilita los mensajes directos de los miembros del servidor e intenta de nuevo.", delete_after=10)
        
        await bot.process_commands(message)