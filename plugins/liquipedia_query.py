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
    return f'姓名：{player_detail["info"]["name"]}\n' \
           f'生日：{player_detail["info"]["birth_details"]}\n' \
           f'国籍：{player_detail["info"]["nationality"]}\n' \
           f'状态：{player_detail["info"]["status"]}\n' \
           f'生涯：{player_detail["info"]["years_active_player"]}\n' \
           f'队伍：{player_detail["info"]["team"]}\n' \
           f'曾用ID：{player_detail["info"]["alternate_ids"]}\n'
