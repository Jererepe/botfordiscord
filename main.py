import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot: Bot = commands.Bot(command_prefix='')


@bot.command(aliases=('абоба',))
async def cmd0(ctx):
    await ctx.send('напиши "cmds" и увидишь список команд')


@bot.command(aliases=['хуй'])
async def funcmd1(ctx):
    await ctx.send('Нет хуя')


@bot.command(aliases=['пизда'])
async def funcmd2(ctx):
    await ctx.send('Нет пизды')


@bot.command(aliases=['команды'])
async def cmds(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("я могу принести тебе мячик! просто попроси!\nкоманда - мяч!\n\n=====доступна только сенату и выше "
                   "стоящим!=====\nclear *число* - очистит чат \n(писать "
                   "кол-во сообщений(до 100), учитывая эту команду!)\n=====доступна только сенату и выше "
                   "стоящим!=====\nсвязь - ссылка на стим разраба") 

@bot.command(aliases=['мяч!'])
async def cmd3(ctx):
    await ctx.send('держи\n:baseball:')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['слава'])
async def cmd4(ctx):
    await ctx.send('нации')

@bot.command(aliases=['роли'])
async def cmd5(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("*ниже представлен список ролей* \nПадаван\nДжедай\nСитх\nРыцарь Джедай\nРыцарь Ситх\nАстромеханик\nОхотник "
        "за Головами\nПознавший всю мощь силы\nСамо зло\nВетеран\nПобедивший самого себя\nПавший "
        "джедай\nРазносторонний\nНа грани\n\n\nЧто бы получить информация о роли, написать в чат - Роль инфо ["
        "название роли]")  
    
@bot.command(aliases=['негры'])
async def Niggers(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("'I HATE NIGGERS'")

    
@bot.command(aliases=['связь'])
async def cmd5(ctx):
    await ctx.send('Steam - https://cutt.ly/jn4PWOh \nDiscord - Phrog makes *qwa* 𓆏#5748')
    

@bot.command(aliases=['Эпики'])
async def EGS(ctx):
    await ctx.send('пидорасы и жиды')
    
    
@bot.event
async def on_ready():
    print('Это же Азамат Айталиев!')


@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f'Сообщение было изменено!\n`{before.content} -> {after.content}`')


@bot.event
async def on_member_join(ctx, member):
    """это же Азамат Айталиев!."""
    await ctx.send(f'Добро пожаловать {member}! Напиши "команды" чтобы узнать мои команды.')


token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
