# First edition of the solution that was later decided that this was an improper way to solve the solution
# Queries were found beforehand

import psycopg2
import os
import datetime
import bleach

threemostpopularview = "create view artauthviews_view as select title, author, count(*) as views from articles, log where log.path like concat('%',articles.slug) group by articles.title, articles.author order by views desc;"

errorview = "create view datepercenterror_view as select date(time), round(100.0 * sum(case log.status when '200 OK' then 0 else 1 end) / count(log.status), 2) as 'Percent Error' from log group by date(time) order by 'Percent Error' desc;"
def createviews(firstview, secondview):
    newslog.execute(firstview)
    newslog.execute(secondview)

def threemostpopular():
    # Should be organized by article title and views
    logconnection = psycopg2.connect("dbname=news")
    newslog = logconnection.cursor()
    newslog.execute(threemostpopularview)
    newslog.execute("select title, views from artauthviews_view limit 3;")
    results = newslog.fetchall()
    print(results)
    logconnection.close()

def mostpopularauthors():
    # Should be organized by author's name and views
    logconnection = psycopg2.connect("dbname=news")
    newslog = logconnection.cursor()
    newslog.execute(threemostpopularview)
    newslog.execute("select authors.name, sum(artauthviews_view.views) as views from artauthviews_view, authors where authors.id = artauthviews_view.author group by authors.name order by views desc")
    results = newslog.fetchall()
    print(results)
    logconnection.close()

def errorsmorethanone():
    # Should be organized by Date and the percent of
    # errors which should be more than 1%
    logconnection = psycopg2.connect("dbname=news")
    newslog = logconnection.cursor()
    newslog.execute(errorview)
    newslog.execute("select * from datepercenterror_view where 'Percent Error' > 1")
    results = newslog.fetchall()
    print(results)
    logconnection.close()

while True:
    selection = input('Which sql query do you want to run? \nThree Most Popular Articles [1]\nThree Most Popular Authors [2]\nDates Where Errors Occured More than 1% [3]\n End Program [4]')
    if selection == '1':
        threemostpopular()
    elif selection == '2':
        mostpopularauthors()
    elif selection == '3':
        errorsmorethanone()
    elif selection == '4':
        break
    else:
        print('Wrong input')
        break
