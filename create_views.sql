create view popular_articles as
    select title, count(*) as views
    from log join articles
    on log.path = concat('/article/',articles.slug)
    group by title, status
    order by status, views desc
    limit 3;

create view popular_articles_fast as
    SELECT title, views
    FROM articles
    JOIN
        (SELECT path, count(*) AS views
         FROM log
         GROUP BY log.path) AS log
    ON log.path = concat('/article/', articles.slug)
    ORDER BY views DESC
    LIMIT 3;

create view popular_authors as
    select authors.name, count(*) as views
    from articles,authors,log
    where articles.author = authors.id and log.path = concat('/article/',articles.slug)
    group by authors.name, status
    order by status, views desc;

create view popular_authors_fast as
    select authors.name, sum(views) as view
    from articles,authors,(SELECT path, count(*) AS views
                            FROM log
                            GROUP BY log.path) AS log
    where articles.author = authors.id and log.path = concat('/article/',articles.slug)
    GROUP BY authors.name
    order by view desc;

create view all_error as
    select cast(time as date) as day, count(*) as error
    from(select * from log where status like '404%') as tab
    group by day
    order by day;

create view all_request as
    select cast(time as date) as day, count(*) as request
    from log
    group by day
    order by day;

create view avg_error as
    select all_error.day,request,error,round(100.0*error/request,2) as perc_error
    from all_request,all_error
    where all_request.day = all_error.day;

create view most_errors as
    select to_char(day,'FMMonth DD, YYYY') as day, perc_error
    from avg_error
    where perc_error > 1.00
    order by perc_error;