import urllib3
import json
from nonebot import on_command, CommandSession
@on_command('5e')
async def _5e(session: CommandSession):
    user_name = session.get('user_name')
    history = await get_recent_history_of_user(user_name)
    result = build_recent_history_result(history)
    await session.send(f'{user_name}的最近战绩是{result}')


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


async def get_recent_history_of_user(user_name: str) -> str:
    http = urllib3.PoolManager()
    r = http.request(
        'GET', f'https://www.5ewin.com/api/data/match_list/{user_name}?yyyy=2019&page=1')
    data = str(r.data, encoding='utf-8')
    dataObj = json.loads(data)
    history = dataObj['data']
    return history


def build_recent_history_result(history):
    result = ''
    for i in history:
        result += '胜' if i['is_win'] == '1' else '负'
        pass
    return result

def build_recent_match_statistic(history, user_name):
    match = history[0]
    return f'玩家：{user_name}\n比赛时间：{match["round_time"]}\n地图：{match["map"]}\n击杀数：{match["kill"]}\nrating：{match["rating"]}'