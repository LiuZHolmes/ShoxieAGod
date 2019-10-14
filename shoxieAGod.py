from os import path
import nonebot
import config

if __name__ == '__main__':
    nonebot.init()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )
    nonebot.run(host='127.0.0.1', port=8080)