import pandas as pd
from database.db_connection import get_connection

def upload(csv_path="data/queries.csv"):
    df = pd.read_csv(csv_path)
    df.columns = [c.strip() for c in df.columns]
    df['query_created_time'] = pd.to_datetime(df['query_created_time'], errors='coerce')
    df['query_closed_time'] = pd.to_datetime(df.get('query_closed_time'), errors='coerce')

    conn = get_connection()
    cursor = conn.cursor()

    insert_sql = """
    INSERT INTO queries (mail_id, mobile_number, query_heading, query_description, status, query_created_time, query_closed_time)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_sql, (
            row.get('mail_id'),
            row.get('mobile_number'),
            row.get('query_heading'),
            row.get('query_description'),
            row.get('status') if pd.notna(row.get('status')) else 'Open',
            row.get('query_created_time').to_pydatetime() if pd.notna(row.get('query_created_time')) else None,
            row.get('query_closed_time').to_pydatetime() if pd.notna(row.get('query_closed_time')) else None
        ))
    conn.commit()
    cursor.close()
    conn.close()
    print('Upload completed')

if __name__ == '__main__':
    upload()
