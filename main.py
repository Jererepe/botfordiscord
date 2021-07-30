import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot: Bot = commands.Bot(command_prefix='', case_insensitive=True)


@bot.command(aliases=['абоба'])
async def cmd0(ctx):
    await ctx.send('напиши "cmds" и увидишь список команд')


@bot.command(aliases=['+правила'])
async def cmd201(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/846436524206719050/870358786987147306/unknown.png")


@bot.command(aliases=['+команды'])
async def cmds(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(
        '>>>я могу принести тебе мячик! просто попроси!\nкоманда - +мяч!\n\n=====доступна только сенату и выше '
        'стоящим!=====\n`clear *число* - очистит чат` \n(писать '
        'кол-во сообщений(до 100), учитывая эту команду!)\n=====доступна только сенату и выше '
        'стоящим!=====\n+связь - ссылка на стим разраба\n+роли - покажет список ролей\n+правила - покажет правила для '
        'всех участников')


@bot.command(aliases=['+мяч!'])
async def cmd3(ctx):
    await ctx.send('держи\n:baseball:')


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['слава'])
async def cmd4(ctx):
    await ctx.send('нации')


@bot.command(aliases=['негры'])
async def Niggers(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("`I HATE NIGGERS`")


@bot.command(aliases=['+связь'])
async def cmd6(ctx):
    await ctx.send('**Steam - https://cutt.ly/dQiph2e** \n**Discord - Phrog makes *qwa* 𓆏#5748** \n**Telegram - '
                   'https://cutt.ly/1QipobR**')


@bot.command(aliases=['+роли'])
async def cmd5(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(
        "*ниже представлен список ролей* \nПадаван(1)\nДжедай(2)\nСитх(3)\nРыцарь Джедай(4)\nРыцарь Ситх("
        "5)\nАстромеханик(6)\nОхотник "
        "за Головами(7)\nПознавший всю мощь силы(8)\nСамо зло(9)\nВетеран(10)\nПобедивший самого себя(11)\nПавший "
        "джедай(12)\nРазносторонний(13)\nНа грани(14)\n\n\n`Что бы получить информацию о роли, напиши в чат - "
        "+рольn, где n - номер роли из спика`")


@bot.command(aliases=['+роль1'])
async def cmd101(ctx):
    await ctx.send('Для получения роли **Падаван** необходимо победить в бою другого носителя роли **Падаван**, '
                   'или же победить в бою высшее руководство')


@bot.command(aliases=['+роль2'])
async def cmd102(ctx):
    await ctx.send('Для получения роли **Джедай** необходимо получить 50+ уровень на любом джедае в игре и отправить '
                   'скриншот в качестве подтверждения')


@bot.command(aliases=['+роль3'])
async def cmd103(ctx):
    await ctx.send('Для получения роли **Ситх** необходимо получить 50+ уровень на любом ситхе в игре и отправить '
                   'скриншот в качестве подтверждения')


@bot.command(aliases=['+роль4'])
async def cmd104(ctx):
    await ctx.send('Для получения роли **Рыцарь джедай** необходимо получить 100+ уровень на любом джедае в игре и '
                   'отправить скриншот в качестве подтверждения')


@bot.command(aliases=['+роль5'])
async def cmd105(ctx):
    await ctx.send('Для получения роли **Рыцарь ситх** необходимо получить 100+ уровень на любом ситхе в игре и '
                   'отправить скриншот в качестве подтверждения')


@bot.command(aliases=['+роль6'])
async def cmd106(ctx):
    await ctx.send('Для получения роли **Астромеханик** необходимо получить 65+ уровень на BB-8, или BB-9E и выслать '
                   'скриншот в качестве подтверждения')


@bot.command(aliases=['+роль7'])
async def cmd107(ctx):
    await ctx.send('Для получения роли **Охотник за головами** необходимо получить 65+ уровень на одном из следующих '
                   'персонажей:**``\nХан Соло\nЛендо Калрисиан\nБоба Фетт\nБосск``**\nи выслать скриншот в '
                   'качестве подтверждения')


@bot.command(aliases=['+роль8'])
async def cmd108(ctx):
    await ctx.send('Для получения роли **Познавший всю мощь силы** необходимо победить 2х участников с ролью **Ситх** '
                   'и 1о участника с ролью **Рыцарь ситх**')


@bot.command(aliases=['+роль9'])
async def cmd109(ctx):
    await ctx.send('Для получения роли **Само зло** необходимо победить 2х участников с ролью **Джедай** '
                   'и 1о участника с ролью **Рыцарь джедай**')


@bot.command(aliases=['+роль10'])
async def cmd1010(ctx):
    await ctx.send('Для получения роли **Ветеран** необходимо получить 100+ на всех базовых классах, т.е.: **Стрелок, '
                   'Тяжёлый боец, Офицер, Специалист** и отправить скриншот в качестве подтверждения')


@bot.command(aliases=['+роль11'])
async def cmd1011(ctx):
    await ctx.send('Роль **Победивший самого себя** выдаётся, если вам удастся последовательно получить следующие '
                   'роли:\n*``1. - Рыцарь Ситх\n2. - Рыцарь Джедай``*')


@bot.command(aliases=['+роль12'])
async def cmd1012(ctx):
    await ctx.send('Роль **Павший Джедай** выдаётся, если вам удастся последовательно получить следующие '
                   'роли:\n*``1. - Рыцарь Джедай\n2. - Рыцарь Ситх``*')


@bot.command(aliases=['+роль13'])
async def cmd1013(ctx):
    await ctx.send('Роль **Разносторонний** выдаётся, если вы часто играете в иные игры, помимо *Battlefront 2*')


@bot.command(aliases=['+роль14'])
async def cmd1014(ctx):
    await ctx.send('Роль **На грани** выдаётся участникам, имеющим 2|3 предупреждений и снимается только после снятия '
                   '**ВСЕХ** имеющихся предупреждений')


@bot.event
async def on_ready():
    print('Execute order 66')


@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f'Сообщение было изменено!\n`{before.content} -> {after.content}`')



token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
