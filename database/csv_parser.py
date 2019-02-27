import pandas as pd
from database.mongo_basic import MongoConnect


class CsvReader:

    def reader(self, filename):
        df = pd.read_csv(filename)
        # columns = list(df.columns)
        # maplist = ['Tdate', 'Products', 'Prices', 'Payment_Source', 'Name', 'City',
        # 'State', 'Con', 'Account_Created_Date', 'Last_Login_Time', 'Latitude', 'Longitude']
        df.rename(columns={'Transaction_date': 'Tdate', 'Account_Created': 'Account_Created_Date'}, inplace=True)
        records = df.to_dict(orient='records')
        mongo = MongoConnect()
        mongo.insert_many_in_database('test', records)


if __name__ == '__main__':
    reader = CsvReader()
    reader.reader("D:\sample.csv")