from liquipediapy import counterstrike
from nonebot import on_command, CommandSession

from utils.assembler import extract_field_by_attribute

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


@on_command('upcoming')
async def upcoming(session: CommandSession):
    team = session.get('team')
    result = get_upcoming_by_team(team)
    await session.send(result)


@upcoming.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['team'] = stripped_arg
    return


def build_pro_player_detail(player):
    player_detail = counterstrike_obj.get_player_info(player, True)
    result = extract_field_by_attribute(player_detail["info"], '姓名', 'name')
    result += extract_field_by_attribute(player_detail["info"], '生日', 'birth_details')
    result += extract_field_by_attribute(player_detail["info"], '国籍', 'nationality')
    result += extract_field_by_attribute(player_detail["info"], '状态', 'status')
    result += extract_field_by_attribute(player_detail["info"], '生涯', 'years_active_player')
    result += extract_field_by_attribute(player_detail["info"], '队伍', 'team')
    result += extract_field_by_attribute(player_detail["info"], '曾用ID', 'alternate_ids', True)
    return result


def get_upcoming_by_team(team):
    games = counterstrike_obj.get_upcoming_and_ongoing_games()
    match = find_upcoming_match_by_team(games, team)
    return build_match(match)


def find_upcoming_match_by_team(games, team):
    return next(filter(lambda x: x['team1'] == team or x['team2'] == team, games))


def build_match(match):
    return f"{match['team1']} VS {match['team2']}\n" \
           f"开始时间：{match['start_time']}\n" \
           f"所属赛事：{match['tournament']}"
