import discord

def setup_new_members(bot):
    @bot.event
    async def on_member_join(member):
        role = member.guild.get_role(1297889374930735205)
        if role:
            try:
                await member.add_roles(role)
                print(f"Rol asignado a {member.name}")
            except discord.HTTPException:
                print(f"No se pudo asignar el rol a {member.name}")
        else:
            print("El rol especificado no existe en el servidor")