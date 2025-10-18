import csv
import datetime

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, String, Column, Integer, Float, DateTime, ForeignKeyConstraint, insert, select

engine = create_engine('sqlite:///clean.db')
metadata = MetaData()

stations = Table('stations', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('station', String),
            Column('latitude', Float),
            Column('longitude', Float),
            Column('elevation', Float),
            Column('name', String),
            Column('country', String),
            Column('state', String)
                 )

measures = Table('measures', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('station', String, nullable=False),
                  Column('date', DateTime),
                  Column('precip', Float),
                  Column('tobs', Integer),
                 ForeignKeyConstraint(['station'], ['stations.station']),
                 )

metadata.create_all(engine)

def load_stations(filename: str) -> None:
    """Reads station's data from CSV file to table 'stations'."""
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # pomiń nagłówek
        data: List[Dict] = []
        for row in reader:
            try:
                data.append({
                    'station': row[0],
                    'latitude': float(row[1]) if row[1] else None,
                    'longitude': float(row[2]) if row[2] else None,
                    'elevation': float(row[3]) if row[3] else None,
                    'name': row[4],
                    'country': row[5],
                    'state': row[6]
                })
            except (IndexError, ValueError) as e:
                print(f"Loading error in  {row}: {e}")

        if data:
            with engine.begin() as conn:
                conn.execute(insert(stations), data)
            print(f"Inserted {len(data)} records to table 'stations'.")


def load_measures(filename: str) -> None:
    """Loads data from CVS file to tables 'measures'."""
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        data: List[Dict] = []
        for row in reader:
            try:
                data.append({
                    'station': row[0],
                    'date': datetime.datetime.strptime(row[1], '%Y-%m-%d'),
                    'precip': float(row[2]) if row[2] else None,
                    'tobs': int(row[3]) if row[3] else None
                })
            except (IndexError, ValueError) as e:
                print(f"Loading error in row {row}: {e}")

        if data:
            with engine.begin() as conn:
                conn.execute(insert(measures), data)
            print(f"Inserted {len(data)} records to table 'stations'.")




if __name__ == '__main__':
    #load_stations('data/clean_stations.csv')
    #load_measures('data/clean_measure.csv')

    """
     The Engine.execute() method is considered legacy as of the 1.x series of SQLAlchemy and will be removed in 2.0.
      All statement execution in SQLAlchemy 2.0 is performed by the Connection.execute() method of Connection, or in the ORM by the Session.execute() method of Session.
      (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    """

    with engine.connect() as conn:
        print("\nPierwsze 5 rekordów (SQL):")
        result = conn.execute(sqlalchemy.text("SELECT * FROM stations LIMIT 5"))
        for row in result:
            print(row)

        print("\nPierwsze 5 rekordów (SQLAlchemy Core):")
        result = conn.execute(select(stations).limit(5))
        for row in result:
            print(row)