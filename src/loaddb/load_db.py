"""
loads data from .csv files into .db
csv file names are formatted: (engagement_)department_className(_classInfo)_tableName
						- ex: Engineering_CS101_Summer2014_ActivityGrade.csv
"""

import os
import sys
import glob
import csv
import sqlite3


connection = sqlite3.connect('data.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def getClassTableName(fileName):
	# given csv fileName formatted as above, returns [className, (classInfo,) tableName]
	tokens = fileName.split('_')
	tableName = tokens[len(tokens) - 1]
	if tokens[0] == 'engagement':
		return tokens[2:]
	return tokens[1:]

def pruneColumnName(columnName):
	# given original column name, prunes to avoid confusion in sql
	# replaces parentheses and quotations with spaces, then prunes extra spaces
	x = columnName.translate(None, '()"\'')
	x = ' '.join(x.split())
	return x

def pruneTableName(tableName):
	# given intended table name, prunes to avoid confusion in sql
	# removes hyphens (so far only used for CS-144 --> CS144)
	return tableName.replace('-', '').strip()

for csvfile in glob.glob('./data/*/*.csv'):
	fileName = os.path.splitext(os.path.basename(csvfile))[0]
	tableName = '_'.join(getClassTableName(fileName))
	tableName = pruneTableName(tableName)
	print tableName

	with open(csvfile, "rb") as f:
		reader = csv.reader(f)

		header = True
		for row in reader:
			if header:
				header = False

				drop_sql = 'DROP TABLE IF EXISTS ' + tableName + ';'
				cursor.execute(drop_sql)
				column_names = [pruneColumnName(name) for name in row]
				attribute_names = ','.join(column_names)
				create_sql = 'CREATE TABLE ' + tableName + '(' + attribute_names + ');'
				cursor.execute(create_sql)
				# TODO: create index for student id's?
				numCols = len(row)

			elif len(row) == numCols:
				# TODO: rows with NULL values are never stored - how to tell which columns are null
				attribute_names = ','.join(['?'] * numCols)
				insert_sql = 'INSERT INTO ' + tableName + ' VALUES (' + (attribute_names) + ');'
				cursor.execute(insert_sql, row)

	connection.commit()

"""
cursor.execute('SELECT * FROM CS106A_Fall2013_weeklyEffort;')
output = cursor.fetchall()
print output
"""
