import asyncio
import unittest
from unittest.mock import MagicMock

import urllib3

from plugins import _5e_query


class Test_5e(unittest.TestCase):
    def test_get_recent_history_of_user(self):
        with open('resource/recent_history.json', 'r', encoding='utf-8') as f:
            try:
                str = f.read()
            except:
                f.close()
        response = bytes(str, encoding='utf-8')
        r = urllib3.HTTPResponse(body=response)
        urllib3.PoolManager.request = MagicMock(return_value=r)
        result = asyncio.run(_5e_query.get_recent_history_of_user('test'))
        self.assertEqual(result[0]['rating'], "23.39")


if __name__ == '__main__':
    unittest.main()
