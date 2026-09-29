speed-test-cli is a terminal tool that records your internet speed test results, including download and upload metrics, into an SQLite database and provides insights into ISP latency. To use this tool, simply run `python speed_test_cli.py --db <database_file>` where <database_file> is the name of the SQLite database file you wish to use. The tool will automatically create the database and table if they do not exist.

### Installation

```sh
pip install speedtest-cli sqlite3
```

### Usage

```sh
python speed_test_cli.py --db speed_test.db
```

This will perform a speed test, record the results, and print the download and upload speeds to the terminal.