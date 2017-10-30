
import psycopg2
import os
import datetime
import bleach

def threemostpopular():
    logconnection = psycopg2.connect("dbname=news)

    logconnection.close()
