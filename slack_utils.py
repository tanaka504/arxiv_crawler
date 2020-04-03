import os
import slack
from data.config import TOKEN


def post_comment(client, message):
    response = client.chat_postMessage(
        channel='#arxiv-crawl',
        text=message
    )
    assert response['ok']


if __name__ == "__main__":
    client = slack.WebClient(token=TOKEN)
    post_comment(client=client, message='Hello World')