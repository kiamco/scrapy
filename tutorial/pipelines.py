# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class JobPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        
    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS jobs""")
        self.cursor.execute("""create table jobs_tb(
                  job_id text,
                  job_title text,
                  company text,
                  location text,
                  salary text,
                  rating text,
                  job_desc text,
                  date_posted text,
                  link text
                  )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.cursor.execute("""insert into jobs_tb values (?, ?, ?, ?, ?, ?, ?, ?, ?)""",(
            item['job_id'][0],
            item['job_title'][0],
            item['company'][0],
            item['location'][0],
            item['salary'][0],
            item['rating'][0],
            item['job_desc'][0],
            item['date_posted'][0],
            item['link'][0]
        ))
        self.conn.commit()
