import click
import sqlite3
from speedtest import Speedtest

@click.command()
@click.option('--db', default='speed_test.db', help='Database file name')
def speed_test(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY, download REAL, upload REAL, timestamp TEXT)''')
    conn.commit()
    st = Speedtest()
    download_speed = st.download() / 1024 / 1024
    upload_speed = st.upload() / 1024 / 1024
    c.execute('INSERT INTO results (download, upload, timestamp) VALUES (?, ?, strftime("%Y-%m-%d %H:%M:%S", "now"))', (download_speed, upload_speed))
    conn.commit()
    print(f'Download: {download_speed:.2f} Mbps
Upload: {upload_speed:.2f} Mbps')
def main():
    speed_test()
if __name__ == '__main__':
    main()
