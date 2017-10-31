# Log Analysis Project

This project basically takes a given database and does certain sql Queries
in order to successfully arrange the data for addressed ways to have it
arranged

## Directions

## Requirements
- python3
- Vagrant

## Virtual Machine And DATABASE
1. Install Vagrant
2. Clone the Fullstack-Nanodegree-VM
3. Download the newsdata.sql file from Udacity
4. Place this file within the Fullstack-Nanodegree-VM
5. Open terminal/command prompt and redirect to the Fullstack-Nanodegree-VM
6. Run 'vagrant up' (whenever your computer restarts you have to run this)
7. Run 'vagrant ssh' to open the VM
8. Redirect to where the newsdata.sql file is in the VM
9. Run 'psql -d news -f newsdata.sql'
10. To connect to this database run 'psql -d news'

## News Views
### Due to the README file, whenever 'all' is put in these sql queries, it means the asterisk
1. Connect to the news database
2. Create the first view by running
'create view autharticle_view as select title, author,count(all)
        as views from articles,log where
        log.path like concat('%',articles.slug) group by articles.title,
        articles.author order by views desc;'
3. Create the second view by running
'create view error_view as select date(time),
        round(100.0*sum(case log.status when '200 OK'
        then 0 else 1 end)/count(log.status),2) as "Percent Error"
        from log group by date(time)
        order by "Percent Error" desc;'

## RUNNING THE Program
To execute the code follow these Directions
1. Download this code and save it in the VM directory (Note: You only need to download logfinal.py)
2. Once you are open within the VM and redirected into the same directory as the python program run
'python3 logfinal.py'
3. You will get a text result with the correct results! :)
4. If you prefer to read the results in a text file you can open, results.txt





## NOTE INFORMATION BELOW IS IRRELEVANT BUT IF YOU WISH TO UNDERSTAND THE DATABASE YOU MAY READ THIS

## Tables in 'news' Database

### articles
author - int (3)
- Foreign key for authors'
title - text (Bad things gone, say good people)
slug - text (bad-things-gone)
lead - text (All bad things have gone away, according to a poll of good people, Thursday.)
body - text (Bad things are a thing of the bad......)
time - timestamp with time zone (2016-08-15 18:55:10.814316+00)
id - integer (23)
- 23 - 30 are all articles

### authors
name - text (Ursula La Multa)
- Ursula La Multa (1)
- Rudolf von Treppenwitz (2)
- Anonymous Contributor (3)
- Markoff Chaney (4)
bio - text (Ursula La Multa is an expert...)
id - integer (1)

### log
path - text (/)
ip - inet (198.51.100.195)
method - text (GET)
- 'GET' is the only value for method
status - text (200 OK)
- only values for this are ('200 OK' and '404 NOT FOUND')
time - timestamp with time zone (2016-07-01 7:00:00+00)
id - int (1678923)
