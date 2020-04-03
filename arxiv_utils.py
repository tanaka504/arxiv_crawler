import arxiv

def crawl(query):
    paper_list = arxiv.query(
        query=query,
        sort_by='submittedDate',
        sort_order='descending',
        max_results=10
    )
    return [(paper['title'], paper['arxiv_url'], paper['published']) for paper in paper_list]