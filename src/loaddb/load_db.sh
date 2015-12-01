#!/bin/bash

rm -f load_db.sql
touch load_db.sql

python generate_load_db_sql.py

sqlite3 < load_db.sql