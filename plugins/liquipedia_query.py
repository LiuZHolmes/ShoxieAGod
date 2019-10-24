import pprint

from liquipediapy import counterstrike
from nonebot import on_command, CommandSession

counterstrike_obj = counterstrike("ShoxieAGod")


@on_command('whois')
async def who_is(session: CommandSession):
    player = session.get('player')
    result = build_pro_player_detail(player)
    await session.send(result)


@who_is.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['player'] = stripped_arg
    return


def build_pro_player_detail(player):
    player_detail = counterstrike_obj.get_player_info(player, True)
    print(player_detail['info'])
    return pprint.pformat(player_detail['info'], indent=2)
