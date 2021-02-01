import time
import logging
import threading
import requests
import json
import os
from dataclasses import dataclass
from typing import List, Optional


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="[%(asctime)s] [%(levelname)s] {%(filename)s:%(lineno)d} {%(process)d:%(threadName)s} - %(message)s")

total = 0
URL = 'https://api.pushshift.io/reddit/comment/search'
COMMENTS_FILE = '../comments.json'


def custom_default(self, o):
    if isinstance(o, Comment):
        return o.as_dict()


setattr(json.JSONEncoder, 'default', custom_default)


@dataclass
class Comment:
    id: str
    body: str
    created_utc: int

    def as_dict(self):
        return dict(
            id=self.id,
            body=self.body,
            created_utc=self.created_utc
        )


class RedditCommentsDownloader(threading.Thread):

    def __init__(self, query: dict, file_lock : threading.RLock, limit: int = 10000, user_nickname: str = None):
        super().__init__()
        self.query = query

        self._limit = limit
        self.file_lock = file_lock
        self._comments = []
        self._min_comment_created_utc = int(time.time() * 1000)
        self._continue_requesting = True

        if user_nickname:
            self.query['author'] = user_nickname

    def run(self):
        while len(self._comments) < self._limit and self._continue_requesting:
            self.query['size'] = self._min_comment_created_utc
            response: requests.Response = requests.get(URL, params=self.query)
            if not response.ok:
                logger.error(f'Not ok: {response.status_code} - current size: {len(self._comments)}')
                time.sleep(2)
                continue

            self._process_response(response)
        else:
            logger.info(f'Comments limit reached: {len(self._comments)}')
            self._save()

    def _process_response(self, response):
        response_data_json = response.json().get('data')
        if not response_data_json:
            self._continue_requesting = False
            return

        for comment in response_data_json:
            self._comments.append(
                Comment(
                    id=comment.get('id'),
                    body=comment.get('body'),
                    created_utc=comment.get('created_utc')
                )
             )

        self._min_comment_created_utc = self._get_min_comment_created_utc()

    def _get_min_comment_created_utc(self):
        return min(comment.created_utc for comment in self._comments)

    def _get_file_comments(self) -> List[Comment]:
        data = []
        if not os.path.exists(COMMENTS_FILE):
            return data

        with open(COMMENTS_FILE) as f:
            comments = json.loads(f.read())
            for comment in comments:
                data.append(
                    Comment(
                        id=comment.get('id'),
                        body=comment.get('body'),
                        created_utc=comment.get('created_utc')
                    )
                )

        return data

    def _save(self):
        self.file_lock.acquire()
        try:
            file_comments = self._get_file_comments()
            self._comments += file_comments
            self._comments.sort(key=lambda comment: comment.created_utc)

            with open(COMMENTS_FILE, 'w') as f:
                f.write(json.dumps(self._comments))
        finally:
            self.file_lock.release()


params = dict(
    size=500,
    fields=['created_utc', 'id', 'body']
)

threads = []

file_lock = threading.RLock()

for name in ['stalenin69', 'Science205014', 'Eli-Mordrake', 'petrichoring', 'bignewsforyou']:
    comments_downloader = RedditCommentsDownloader(params, file_lock, user_nickname=name)
    comments_downloader.start()
    threads.append(comments_downloader)


for thread in threads:
    thread.join()

data = []
with open(COMMENTS_FILE) as f:
    comments = json.loads(f.read())
    for comment in comments:
        data.append(
            Comment(
                id=comment.get('id'),
                body=comment.get('body'),
                created_utc=comment.get('created_utc')
            )
        )

logger.info(data)
