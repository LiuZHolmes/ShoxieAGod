import asyncio
import unittest
from unittest.mock import mock_open, patch, MagicMock

from nonebot import CommandSession

from plugins import common


class TestCommon(unittest.TestCase):
    @patch("plugins.common.open", mock_open(read_data="mock"))
    def test(self):
        async def async_magic():
            pass

        MagicMock.__await__ = lambda x: async_magic().__await__()
        CommandSession.send = MagicMock()
        asyncio.run(common.changelog(CommandSession))
        CommandSession.send.assert_called_with('mock')
        pass


if __name__ == '__main__':
    unittest.main()
