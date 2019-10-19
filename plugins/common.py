from nonebot import on_command, CommandSession, on_request, RequestSession


@on_command('changelog')
async def changelog(session: CommandSession):
    with open('plugins/resource/changelog.txt', 'r', encoding='utf-8') as f:
        try:
            str = f.read()
        except:
            f.close()
    await session.send(str)


@on_request('group')
async def _(session: RequestSession):
    await session.approve()
    return
