# -*- coding: UTF-8 -*-

import ads.sandbox


def authors(paper):
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
    return unicode('''
    {}
    {}
    {}, {}, {}, {}
    ''').format(paper.title[0], authors(paper), paper.year, paper.pub, paper.issue, paper.page[0])


relevant_fields = ['aff', 'citation_count', 'title', 'author', 'year', 'issue']
ciera_affiliations = ['*northwestern*', '*CIERA*',
                      '*Center for Interdisciplinary Exploration and Research in Astrophysics*']
relevant_months = '2016-09-00 TO 2017-08-00'
sort_type = 'citation_count+desc'

q = ads.SearchQuery(aff=ciera_affiliations, fl=relevant_fields, pubdate=relevant_months, sort=sort_type)

papers = [paper for paper in q]

for paper in papers:
    print ciera_format(paper)
