import discord
from discord.ext import commands
from discord.ext.commands import Bot

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



@bot.command(aliases=['команды'])
async def cmds(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("я могу принести тебе мячик! просто попроси!\nкоманда - мяч!\n\n🔹доступна только сенату и выше "
                   "стоящим!\nclear *число* - очистит чат (писать "
                   "кол-во сообщений(до 100), учитывая эту команду!)\n🔹доступна только сенату и выше стоящим!\nадмин - напомнит кто тут главный")


@bot.command(aliases=['мяч!'])
async def cmd3(ctx):
    await ctx.send('держи\n⚾️')


@bot.command(aliases=['админ'])
async def cmd4(ctx):
    await ctx.send('Главный тут биос!')
    
    
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['негры'])
async def Niggers(ctx)
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


@bot.command(aliases=['эпики'])
async def EGS(ctx):
    await ctx.send('пидорасы и жиды')


@bot.command(aliases=['связаться'])
async def cmd5(ctx):
    await ctx.send('VK - https://vk.com/jererepe\nDiscord - Phrog makes *qwa* 𓆏#5748')


@bot.event
async def on_ready():
    print('Это же Азамат Айталиев!')


@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f'Сообщение было изменено!\n{before.content} -> {after.content}')


token = os.environ.get('BOT_TOKEN')
bot.run('token')
