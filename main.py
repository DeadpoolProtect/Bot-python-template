import discord
from discord.ext import commands
import random

client = commands.Bot(
  command_prefix='+', # Le préfix pour les commandes est "+"
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(), #intents j'ai mis all pour pas vous soyer embeter 
  help_command=None
)

@client.command()
async def say(ctx, *, message):
    """Le bot répete le meme message que vous ecriver."""
    await ctx.message.delete()  # supprimer la commande originale du message
    await ctx.send(message)

@client.command()
async def ping(ctx):
    """Donne le ping du bot."""
    latency = round(client.latency * 1000) # Obtenir la latence en millisecondes
    
    embed = discord.Embed(title="Pong!", description=f"{latency}ms", color=0x00ff00)
    
    await ctx.send(embed=embed)

@client.command()
async def gay(ctx):
    """Retourne un pourcentage de "gay" aléatoire."""
    if ctx.author.id == 585844703296225311:
        pourcentage = random.randint(80, 100)
    else:
        pourcentage = random.randint(0, 100)
    
    await ctx.message.delete()
    if pourcentage > 90:
        embed = discord.Embed(title="🌈 Taux de gay", description=f"{ctx.author.mention} Vous êtes {pourcentage}% gay. Ah oe faudrait peut-être revoir ton orientation sexuelle !", color=0xFF0000)
    else:
        embed = discord.Embed(title="🌈 Taux de gay", description=f"{ctx.author.mention} Vous êtes {pourcentage}% gay", color=0xFFC300)
    
    await ctx.send(embed=embed)

import discord


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Liste des commandes',
        description='Voici la liste des commandes disponibles:',
        color=discord.Color.blue()
    )

    # Ajouter des champs pour chaque commande
    embed.add_field(name='+ping', value='Vérifie si le bot est en ligne')
    embed.add_field(name='+say [message]', value='Fait dire au bot un message')
    embed.add_field(name='+gay', value='Retourne un pourcentage de "gay" aléatoire.')
    embed.add_field(name='+userinfo [nom_utilisateur]', value='Affiche les informations d\'un utilisateur')

    await ctx.send(embed=embed)

@client.command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    roles = [role.name for role in member.roles[1:]]
    joined_at = member.joined_at.strftime("%d/%m/%Y à %H:%M:%S")
    created_at = member.created_at.strftime("%d/%m/%Y à %H:%M:%S")
    embed = discord.Embed(title=f"Information utilisateur - {member}", color=0x00ff00)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Pseudo:", value=member.display_name, inline=False)
    embed.add_field(name="Compte créé le:", value=created_at, inline=False)
    embed.add_field(name="A rejoint le serveur le:", value=joined_at, inline=False)
    embed.add_field(name=f"Rôles ({len(roles)})", value=", ".join(roles), inline=False)
    await ctx.send(embed=embed)



client.run("MTAzNzA2NjMyMDY5MDI5MDcxMA.GJ4c2F.cC9H0X6FnJzI94VAjBjKUB-P0t5EqzfH8qqmIw")
