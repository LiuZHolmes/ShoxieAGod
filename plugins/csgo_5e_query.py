from nonebot import on_command, CommandSession

from utils.assembler import response_data_to_dict
from utils.requester import send_request


@on_command('5e')
async def _5e(session: CommandSession):
    user_name = session.get('user_name')
    history = await get_recent_history_of_user(user_name)
    result = build_recent_history_result(history)
    await session.send(f'{user_name}的最近战绩是{result}')


@_5e.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['user_name'] = stripped_arg
    return


@on_command('recent')
async def recent(session: CommandSession):
    user_name = session.get('user_name')
    history = await get_recent_history_of_user(user_name)
    result = build_recent_match_statistic(history, user_name)
    await session.send(result)


@recent.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['user_name'] = stripped_arg
    return


@on_command('player')
async def player(session: CommandSession):
    user_name = session.get('user_name')
    detail = await get_player_detail(user_name)
    result = build_player_detail(detail, user_name)
    await session.send(result)


@player.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['user_name'] = stripped_arg
    return


async def get_recent_history_of_user(user_name: str) -> str:
    response = send_request('GET', f'https://www.5ewin.com/api/data/match_list/{user_name}?yyyy=2019&page=1')
    history = response_data_to_dict(response)
    return history


async def get_player_detail(user_name: str) -> str:
    response = send_request('GET', f'https://www.5ewin.com/api/data/player/{user_name}')
    detail = response_data_to_dict(response)
    return detail


def build_recent_history_result(history):
    result = ''
    for i in history:
        result += '胜' if i['is_win'] == '1' else '负'
        pass
    return result


def build_recent_match_statistic(history, user_name):
    match = history[0]
    return f'玩家：{user_name}\n比赛时间：{match["round_time"]}\n地图：{match["map"]}\n击杀数：{match["kill"]}\nrating：{match["rating"]}'


def build_player_detail(detail, user_name):
    return f'玩家：{user_name}\n天梯分：{detail["elo"]}\n爆头率：{detail["per_headshot"]}\n击杀数：{detail["kill"]}\nMVP数：{detail["mvp_total"]}'
