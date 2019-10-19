from nonebot import on_command, CommandSession


@on_command('changelog')
async def changelog(session: CommandSession):
    with open('resource/changelog', 'r', encoding='utf-8') as f:
        try:
            str = f.read()
        except:
            f.close()
    await session.send(str)
