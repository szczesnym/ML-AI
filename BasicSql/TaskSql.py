import sqlite3
from typing import Literal
from sqlite3 import Error
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
_TABLES = ['projects', 'tasks', 'all']


class TaskSql:
    def __init__(self, db_string: str) -> None:
        if db_string != '':
            self.db_string = db_string
        else:
            logging.error('db_string is empty')
            exit(-1)

    def fetch_all(self, table: str) -> list:
        sql = f'SELECT * FROM {table}'
        return self.query(sql)


    def query(self, sql: str) -> list:
        with sqlite3.connect(self.db_string) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
            except Error as e:
                print(e)
                exit(-1)
            return cursor.fetchall()


    def insert(self,table:str, columns: list, values: list) -> int:
        if len(columns) != len(values):
            logging.error('columns and values must have same length')
            return -1
        with sqlite3.connect(self.db_string) as conn:
            sql = f'INSERT INTO {table}({",".join(columns)}) VALUES (\'{"','".join(values)}\')'
            cursor = conn.cursor()
            try:
                rows = cursor.execute(sql)
            except Error as e:
                logging.error(f'Insert ERROR {e}')
                return -1
            conn.commit()
        return 1


    def update(self, table:str , columns: list, values: list, record_id: int) -> int:
        if len(columns) != len(values):
            logging.error('columns and values must have same length')
            return -1
        with sqlite3.connect(self.db_string) as conn:
            core =' ,'.join(f'{column}=\'{value}\'' for column,value in zip(columns,values))
            sql = f'UPDATE {table} SET {core} WHERE id={record_id}'
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
            except Error as e:
                logging.error(f'Update ERROR {e}')
                return -1
            return 1


    def delete(self, table: str, record_id: int) -> int:
        with sqlite3.connect(self.db_string) as conn:
            sql = f'DELETE FROM {table} WHERE id={record_id}'
            cursor = conn.cursor()
            try:
                    cursor.execute(sql)
                    conn.commit()
            except Error as e:
                logging.error(f'Delete ERROR {e}')
                return -1
        return 1


    def init_table(self, table: str ) -> int:
        if table not in _TABLES:
            logging.error(f'Table {table} not in list of available tables {_TABLES}')
            return -1
        if table == 'projects' or table == 'all':
            sql_projects = """
            CREATE TABLE IF NOT EXISTS projects (
                id integer PRIMARY KEY AUTOINCREMENT,
                nazwa text NOT NULL,
                start_date text,
                end_date text);
            """
            self.query(sql_projects)
        if table == 'tasks' or table == 'all':
            sql_tasks = """
                CREATE TABLE IF NOT EXISTS tasks (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    project_id integer NOT NULL,
                    nazwa VARCHAR(250) NOT NULL,
                    opis TEXT,
                    status VARCHAR(15) NOT NULL,
                    start_date text NOT NULL,
                    end_date text NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects (id));
            """
            self.query(sql_tasks)
        return 1
