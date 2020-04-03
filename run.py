import time, schedule
import slack
from slack_utils import post_comment
from arxiv_utils import crawl
from data.config import TOKEN

old_papers = []
query = {
    'ti': '\"Dialogue Generation\"',
    'cat': 'cs.CL'
}
client = slack.WebClient(token=TOKEN)


def format_query(query):
    return ' AND '.join(['{}:{}'.format(k, v) for k, v in query.items()])

def diff_papers(new_papers):
    global old_papers
    new_paper_ids = {idx for (_, idx, _) in new_papers}
    old_paper_ids = {idx for (_, idx, _) in old_papers}
    diff_paper_ids = new_paper_ids - old_paper_ids
    return ['{}\t{}\t{}'.format(title, idx, date) for (title, idx, date) in new_papers if idx in diff_paper_ids]


def post_new_paper():
    global query, client
    paper_list = crawl(query=format_query(query)) # List(Tuple(title, url, date)) <- crawl()
    new_papers = diff_papers(new_papers=paper_list)
    message = 'New paper is published\n' + '\n'.join(new_papers)
    post_comment(client=client, message=message)


def run():
    post_new_paper()
    schedule.every(1).days.do(post_new_paper)
    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run()