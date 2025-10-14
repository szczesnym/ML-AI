import random
from TaskSql import TaskSql



if __name__ == '__main__':
    task_sql = TaskSql('local.db')
    task_sql.init_table('all')
    #task_sql.init_table('both')
    columns = ['nazwa', 'start_date', 'end_date']
    values = [f'test {random.randint(1, 20)}', '2025-10-15', '2020-10-16']
    task_sql.insert(table='projects', columns=columns, values=values)
    all_sql = task_sql.fetch_all('projects')
    print(all_sql)
    task_sql.update(table='projects', columns=columns, values=values, record_id=2)
    task_sql.delete(table='projects', record_id=random.randint(1, len(all_sql)))