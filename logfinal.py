#!/usr/bin/env python3

# FINAL SOLUTION FOR THE LOG ANALYSIS Udacity Project

# Import of Pyscopg2 module
# Declaration of DB_NAME which
# is the news database provided
import psycopg2
DB_NAME = "news"

# The view created to be able to get the title, and author and views
view1 = """create view autharticle_view as select title, author,count(*)
        as views from articles,log where
        log.path like concat('%',articles.slug) group by articles.title,
        articles.author order by views desc;"""

# The view created to be able to get the date and the percent error
view2 = """create view error_view as select date(time),
        round(100.0*sum(case log.status when '200 OK'
        then 0 else 1 end)/count(log.status),2) as "Percent Error"
        from log group by date(time)
        order by "Percent Error" desc;"""

# Query for the three most popular articles by article name and views
query1 = "select title, views from autharticle_view limit 3;"

# Query for the three most popular authors by name and views
query2 = """select authors.name, sum(autharticle_view.views) as views from
         autharticle_view,authors where authors.id = autharticle_view.author
         group by authors.name order by views desc;"""

# Query for everytime on a single day when there are a greater than
# 1% that there is an error that day
query3 = "select * from error_view where \"Percent Error\" > 1;"

# Declaring Each query to be a dict variable type so that I can
# efficiently store the titles and results of the queries

# Query1
query1_result = dict()
query1_result['title'] = "\nThe 3 most popular articles of all time:\n"
# Query2
query2_result = dict()
query2_result['title'] = """\nThe most popular article authors of
all time:\n"""
# Query3
query3_result = dict()
query3_result['title'] = """\nDays with more than 1% of request that
lead to an error:\n"""


# function to get the query results with the input of query
def get_query_results(query):
    """This function takes an input of query which is
    a string variable with the sql command to run
    and return the results of the command"""
    db = psycopg2.connect(database=DB_NAME)
    log = db.cursor()
    log.execute(view1)
    log.execute(view2)
    log.execute(query)
    results = log.fetchall()
    db.close()
    return results


def print_query_results(query_result):
    """Since the formatting of the first two queries are
    the same format, this is how both of those queries will
    be displayed and outputted

    query_result will be the results from the function get_query_results
    """
    print (query_result['title'])
    for result in query_result['results']:
        print (str(result[0]) + ' --- ' + str(result[1]) + ' views')


def print_error_results(query_result):
    """Since the formatting of the first two queries are
    the same format, this is how the error query will be
    displayed and outputted

    query_result will be the results from the function get_query_results
    """
    print (query_result['title'])
    for result in query_result['results']:
        print (str(result[0]) + ' --- ' + str(result[1]) + ' %')


# Calls the function get_query_results and stores it within
# results in each respective variable
query1_result['results'] = get_query_results(query1)
query2_result['results'] = get_query_results(query2)
query3_result['results'] = get_query_results(query3)

# Calls the functions which will print the titles and results
print_query_results(query1_result)
print_query_results(query2_result)
print_error_results(query3_result)
