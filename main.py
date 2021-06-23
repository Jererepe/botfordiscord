import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import asyncio
from asyncio import sleep

bot: Bot = commands.Bot(command_prefix='')


@bot.command(aliases=['абоба'])
async def cmd0(ctx):
    await ctx.send('напиши "cmds" или "команды" - и увидишь список команд')


@bot.command(aliases=['хуй'])
async def funcmd1(ctx):
    await ctx.send('Нет хуя')


@bot.command(aliases=['пизда'])
async def funcmd2(ctx):
    await ctx.send('Нет пизды')


@bot.command(aliases=['гачи'])
async def gachi(ctx):
    await ctx.send("https://imgur.com/gallery/8H2M6UO.jpg")


@bot.command(aliases=['команды'])
async def cmds(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("я могу принести тебе мячик! просто попроси!\nкоманда - мяч!\n\n=====доступна только сенату и выше "
                   "стоящим!=====\nclear *число* - очистит чат (писать "
                   "кол-во сообщений(до 100), учитывая эту команду!)\n=====доступна только сенату и выше стоящим!=====\nсвязь - ссылка на стим разраба")


@bot.command(aliases=['мяч!'])
async def cmd3(ctx):
    await ctx.send('держи\n:baseball:')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['негры'])
async def Niggers(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('''I HATE NIGGERS''')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTE')

    await member.add_roles(mute_role)
    await ctx.send(f'У {member.mention}, ограничение чата, потому что он вел себя как чмо')


@bot.command(aliases=['слава'])
async def cmd4(ctx):
    await ctx.send('нации')


@bot.command(aliases=['связь'])
async def cmd5(ctx):
    await ctx.send('Steam - https://cutt.ly/jn4PWOh ')


@bot.event
async def on_ready():
    print('Это же Азамат Айталиев!')


@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f'Сообщение было изменено!\n{before.content} -> {after.content}')
    
    
@bot.command()
@commands.has_permissions(manage_roles=True, ban_members=True, kick_members=True)
async def mute(ctx, user: discord.Member, time: int, reason):
    role = user.guild.get_role(856261502515544144) # айди роли которую будет получать юзер
    await ctx.send(f'{user} получил мут на {time} минут по причине: {reason}')
    await user.add_roles(role)
    await user.move_to(None)
    await asyncio.sleep(time * 60)
    await user.remove_roles(role)    


token = os.environ.get('BOT_TOKEN')
bot.run('token')
