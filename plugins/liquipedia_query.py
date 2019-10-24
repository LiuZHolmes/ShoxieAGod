from liquipediapy import counterstrike
from nonebot import on_command, CommandSession

counterstrike_obj = counterstrike("ShoxieAGod")


@on_command('whois')
async def who_is(session: CommandSession):
    user_name = session.get('player')
    player_details = counterstrike_obj.get_player_info(user_name, True)
    print(player_details)
    await session.send('done')


@who_is.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['player'] = stripped_arg
    return
