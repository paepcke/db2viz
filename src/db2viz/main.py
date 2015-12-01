import sys
import sqlite3
import collections
from attr_data_types import *
from graph import *

# returns tuple of (query, db_file to run query on)
def get_query():
	# parse command line args?
	#db_file = sys.argv[1]
	#query = sys.argv[2]

	"""
	db_file = 'test.db' 
	query = 'SELECT day, avg(precipitation)' + \
			'FROM precipitation ' + \
			'GROUP BY day ' + \
			'DISPLAY AS HISTOGRAM '

	query = 'SELECT day, count(precipitation) ' + \
			'FROM precipitation ' + \
			'GROUP BY day ' + \
			'DISPLAY * '
	"""

	db_file = 'data.db'
	
	queries = ['select week, avg([Effort (sec)]) as avg_time from CS106A_Fall2013_weeklyEffort group by week display * as barchart', 
	           'select week, count(distinct anon_screen_name) as num_users from CS106A_Fall2013_weeklyEffort group by week display * as barchart', 
	           'select count(*) as num_weeks from CS106A_Fall2013_weeklyEffort group by anon_screen_name display * as histogram',
	           'select week, sum([Effort (sec)]) as time from CS106A_Fall2013_weeklyEffort group by week display * as barchart']
	query = queries[3]
	
	queries = ["select video_current_time from CS106A_Fall2013_VideoInteraction where event_type = 'pause_video' display * as histogram",
	           "select distinct video_code from CS106A_Fall2013_VideoInteraction",
	           "select video_new_time from CS106A_Fall2013_VideoInteraction where event_type = 'seek_video' display * as histogram"]
	query = queries[0]
	

	return (query.lower(), db_file)


# parses query into select query and display clause (returned as tuple)
# if no display clause, display_query is empty
def parse_query(query):
	display_token = ' display '
	index = query.find(display_token)
	display_query = ''
	if index != -1:
		select_query = query[0 : index]
		display_query = query[index + len(display_token):]
	return (select_query, display_query)
	

def get_output(select_query, db_file):
	# create connection
	connection = sqlite3.connect(db_file)
	connection.row_factory = sqlite3.Row # return as dicts
	cursor = connection.cursor()
	
	# execute query
	cursor.execute(select_query)
	output = cursor.fetchall()
	attr_names = [x[0]for x in cursor.description]
	return (attr_names, output)


def parse_display_query(display_query, attr_names):
	tokens = display_query.split()
	if 'as' in tokens:
		# user specified visualization type
	    index = tokens.index('as')
	    display_attrs = tokens[0 : index]
	    display_type = tokens[index + 1]
	else: 
		# user did not specify visualization type
	    display_attrs = tokens
	    display_type = None
	if display_attrs == ['*']:
	    display_attrs = attr_names
	return (display_attrs, display_type)

def get_metadata(output):
	numRows = len(output)
	outputInfo = 'retrieved ' + str(numRows) + ' rows'
	if numRows == 0: 
	    print outputInfo 
	    sys.exit(0) #exit if no rows retrieved
	numCols = len(output[0])
	outputInfo += ' of ' + str(numCols) + '-tuples'
	return (numRows, numCols, outputInfo)

#MAIN: 
# query -> data query + display query
# data query + db file -> output

query, db_file = get_query()
select_query, display_query = parse_query(query)

attr_names, output = get_output(select_query, db_file)
# display_query != ''
display_attrs, display_type = parse_display_query(display_query, attr_names)
# display_type is not None
num_display_cols = len(display_attrs)

numRows, numCols, output_info = get_metadata(output)
attrDataTypes = getAttrDataTypes(output, numCols)
attrTypes = getAttrTypes(output, numCols)

create_chart(output, attr_names, display_attrs, display_type)


