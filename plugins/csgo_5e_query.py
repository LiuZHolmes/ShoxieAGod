import redis
from nonebot import on_command, CommandSession

from utils.assembler import response_data_to_dict
from utils.requester import send_request


@on_command('history')
async def history(session: CommandSession):
    user_name = session.get('user_name')
    recent_history = await get_recent_history_of_user(user_name)
    result = build_recent_history_result(recent_history)
    await session.send(f'{user_name}的最近历史战绩是{result}')


@history.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['user_name'] = stripped_arg
    return


@on_command('recent')
async def recent(session: CommandSession):
    user_name = session.get('user_name')
    recent_history = await get_recent_history_of_user(user_name)
    result = build_recent_match_statistic(recent_history, user_name)
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
    else:
        r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
        print(r.get(session.ctx['user_id']))
        session.state['user_name'] = r.get(session.ctx['user_id'])
    return


@on_command('compare')
async def compare(session: CommandSession):
    first_user_name = session.get('first_user_name')
    second_user_name = session.get('second_user_name')
    first_detail = await get_player_detail(first_user_name)
    second_detail = await get_player_detail(second_user_name)
    result = build_compare_detail(first_detail, second_detail, first_user_name, second_user_name)
    await session.send(result)


@compare.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip().split()
    if stripped_arg:
        session.state['first_user_name'] = stripped_arg[0]
        session.state['second_user_name'] = stripped_arg[1]
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
    return f'玩家：{user_name}\n' \
           f'比赛时间：{match["round_time"]}\n' \
           f'地图：{match["map"]}\n' \
           f'击杀数：{match["kill"]}\n' \
           f'rating：{match["rating"]}'


def build_player_detail(detail, user_name):
    return f'玩家：{user_name}\n' \
           f'天梯分：{detail["elo"]}\n' \
           f'爆头率：{detail["per_headshot"]}\n' \
           f'击杀数：{detail["kill"]}\n' \
           f'MVP数：{detail["mvp_total"]}'


def build_compare_detail(first_detail, second_detail, first_user_name, second_user_name):
    return f'玩家：{first_user_name} VS {second_user_name}\n' \
           f'天梯分：{first_detail["elo"]} VS {second_detail["elo"]} ({round(float(first_detail["elo"]) - float(second_detail["elo"]), 2)})\n' \
           f'爆头率：{first_detail["per_headshot"]} VS {second_detail["per_headshot"]} ({round(float(first_detail["per_headshot"]) - float(second_detail["per_headshot"]), 2)})\n' \
           f'击杀数：{first_detail["kill"]} VS {second_detail["kill"]} ({int(first_detail["kill"]) - int(second_detail["kill"])})\n' \
           f'MVP数：{first_detail["mvp_total"]} VS {second_detail["mvp_total"]} ({int(first_detail["mvp_total"]) - int(second_detail["mvp_total"])})'
