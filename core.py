#########################################
############# Core Commands #############
#########################################

import discord
from discord.ext import commands
from config import embed_color

class Core:
    def __init__(self, bot):
        self.bot = bot

#invite command (-invite)
    @commands.command(pass_context = True)
    async def invite(self, ctx):
        embed = discord.Embed(title = "**Invite Kyoto to your server!**", description = "You want to invite **Kyoto** to your server?\nThen you can use this link to invite him!\n\n[Click here to invite **Kyoto**](https://discordapp.com/oauth2/authorize?client_id=365240645419270145&scope=bot&permissions=527952983)", color = embed_color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/365240645419270145/3f6527890a2b55b1eb864dd0113e0589.png")
        await ctx.author.send(embed = embed)

        embed = discord.Embed(description = "**"+ctx.author.name +" a personal message with the bot invite is on the way!** :heart:", color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

#listservers command (-listservers)
    @commands.command(pass_context = True, aliases=['ls'])
    async def listservers(self, ctx):
        x = '\n'.join([str(server) for server in self.bot.guilds])
        print(x)
        embed = discord.Embed(title = "Servers", description = x, color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

#server command (-server)
    @commands.command(pass_context = True, aliases=['si'])
    async def serverinfo(self, ctx):
        vchannels = ctx.guild.voice_channels
        tchannels = ctx.guild.text_channels
        time = str(ctx.guild.created_at); time = time.split(' '); time= time[0];
        roles = [x.name for x in ctx.guild.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles);    

        embed = discord.Embed(colour = embed_color)
        embed.set_thumbnail(url = ctx.guild.icon_url);
        embed.set_author(name = "Server Information", icon_url = "http://icons.iconarchive.com/icons/graphicloads/100-flat/128/information-icon.png")

        embed.add_field(name="Server Name:", value = str(ctx.guild), inline=True)
        embed.add_field(name="Server ID:", value = str(ctx.guild.id), inline=True)
        embed.add_field(name="Server Owner:", value = str(ctx.guild.owner), inline=True)
        embed.add_field(name="Server Owner ID:", value = ctx.guild.owner.id, inline=True)
        embed.add_field(name="Members:", value = str(ctx.guild.member_count), inline=True)
        embed.add_field(name="Text & Voice Channels:", value = str(len(vchannels)) +" - "+ str(len(tchannels)), inline=True)
        embed.add_field(name="Server Region:", value = '%s'%str(ctx.guild.region), inline=True)
        embed.add_field(name="Server Roles:", value = '%s'%str(role_length), inline=True)
        embed.set_footer(text ='Server Created: %s'%time);

        await ctx.send(embed = embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Core(bot))