"""
This file, when run, pulls papers from ADS that are affiliated with Northwestern or CIERA, and then outputs them in a
usable format intended for the annual report, sorted by citation count. It is important that this list then be filtered
manually to select the most meaningful papers to include, weighing such factors as CIERA's contributions to the effort
and the importance of a work in the field.
"""

import ads



def authors(paper):
    """
    Formats the author list in CIERA's specified format.

    :param paper: a paper object to return the printable author list of
    :return: the formatted list of authors for the paper
    """
    authors = paper.author
    if len(authors) == 1:
        return unicode('{}').format(authors[0])
    elif len(authors) == 2:
        return unicode('{} and {}').format(authors[0], authors[1])
    elif len(authors) == 3:
        return unicode('{}, {}, and {}').format(authors[0], authors[1], authors[2])
    else:
        return unicode('{} et al.').format(authors[0])


def ciera_format(paper):
    """
    Format the paper in CIERA's preferred format for the annual report.

    :param paper: a paper object to return a printable version of
    :return: the printable version of that paper
    """
    if paper.page is not None:
        page = paper.page[0]
    else:
        page = None
    return unicode('''
{}
{}
{}, {}, {}, {}
''').format(paper.title[0], authors(paper), paper.year, paper.pub, paper.issue, page) \
        .replace("None, ", "").replace(", None", "")


relevant_fields = ['aff', 'citation_count', 'title', 'author', 'year', 'issue', 'pub', 'page']
ciera_affiliations = ['*northwestern*', '*CIERA*',
                      '*Center for Interdisciplinary Exploration and Research in Astrophysics*']
relevant_months = '2016-09-00 TO 2017-08-00'
sort_type = 'citation_count+desc'

q = ads.SearchQuery(aff=ciera_affiliations, fl=relevant_fields, pubdate=relevant_months, sort=sort_type, rows=300)

papers = [paper for paper in q]

print len(papers)

with open('ciera-papers.txt', 'w') as outfile:
    for paper in papers:
        print ciera_format(paper)
        outfile.write(ciera_format(paper).encode('utf-8'))
