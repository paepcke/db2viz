"""
loads data from .csv files into .db
csv file names are formatted: (engagement_)department_className(_classInfo)_tableName.csv
						- ex: Engineering_CS101_Summer2014_ActivityGrade.csv
"""

import os
import sys
import glob
import csv
import sqlite3

#data_path = sys.argv[1]

predefined_schemas = {'allData' : '\n\tPlatform TEXT, ' + \
								  '\n\tCourse TEXT, ' + \
								  '\n\tanon_screen_name TEXT, ' + \
								  '\n\tDate DATE, ' + \
								  '\n\tTime TIME, ' + \
								  '\n\t[SessionLength(sec)] INTEGER, ' + \
								  '\n\tNumEventsInSession INTEGER',

					  'summary' : '\n\tPlatform TEXT, ' + \
								  '\n\tCourse TEXT, ' + \
								  '\n\tTotalStudentSessions TEXT, ' + \
								  '\n\t[TotalEffortAllStudents(secs)] INTEGER, ' + \
								  '\n\tMedPerWeekOneToTwenty INTEGER, ' + \
								  '\n\tMedPerWeekTwentyoneToSixty INTEGER, ' + \
								  '\n\tMedPerWeekGreaterSixty INTEGER',

					  'weeklyEffort' : '\n\tPlatform TEXT, ' + \
									   '\n\tCourse TEXT, ' + \
									   '\n\tanon_screen_name TEXT, ' + \
									   '\n\tWeek INTEGER, ' + \
									   '\n\t[Effort (sec)] INTEGER',

					  'ActivityGrade' : '\n\tactivity_grade_id INTEGER, ' + \
  										'\n\tstudent_id INTEGER, ' + \
  										'\n\tcourse_display_name TEXT, ' + \
  										'\n\tgrade FLOAT, ' + \
  										'\n\tmax_grade FLOAT, ' + \
  										'\n\tpercent_grade FLOAT, ' + \
  										'\n\tparts_correctness TEXT, ' + \
  										'\n\tanswers TEXT, ' + \
  										'\n\tnum_attempts INTEGER, ' + \
  										'\n\tfirst_submit DATETIME, ' + \
  										'\n\tlast_submit DATETIME, ' + \
  										'\n\tmodule_type TEXT, ' + \
  										'\n\tanon_screen_name TEXT, ' + \
  										'\n\tresource_display_name TEXT, ' + \
  										'\n\tmodule_id TEXT, ' + \
  										'\n\tname TEXT, ' + \
  										'\n\tscreen_name TEXT',
					 
					  'EventXtract' : '\n\tanon_screen_name TEXT, ' + \
									  '\n\tevent_type TEXT, ' + \
									  '\n\tip_country TEXT, ' + \
									  '\n\ttime DATETIME, ' + \
									  '\n\tquarter TEXT, ' + \
									  '\n\tcourse_display_name TEXT, ' + \
									  '\n\tresource_display_name TEXT, ' + \
									  '\n\tsuccess TEXT, ' + \
									  '\n\tvideo_code TEXT, ' + \
									  '\n\tvideo_current_time FLOAT, ' + \
									  '\n\tvideo_speed TEXT, ' + \
									  '\n\tvideo_old_time FLOAT, ' + \
									  '\n\tvideo_new_time FLOAT, ' + \
									  '\n\tvideo_seek_type TEXT, ' + \
									  '\n\tvideo_new_speed FLOAT, ' + \
									  '\n\tvideo_old_speed FLOAT, ' + \
									  '\n\tgoto_from FLOAT, ' + \
									  '\n\tgoto_dest FLOAT',

					  'VideoInteraction' : '\n\tevent_type TEXT, ' + \
										   '\n\tresource_display_name TEXT, ' + \
										   '\n\tvideo_current_time FLOAT, ' + \
										   '\n\tvideo_speed FLOAT, ' + \
										   '\n\tvideo_new_speed FLOAT, ' + \
										   '\n\tvideo_old_speed FLOAT, ' + \
										   '\n\tvideo_new_time FLOAT, ' + \
										   '\n\tvideo_old_time FLOAT, ' + \
										   '\n\tvideo_seek_type TEXT, ' + \
										   '\n\tvideo_code TEXT, ' + \
										   '\n\ttime DATETIME, ' + \
										   '\n\tcourse_display_name TEXT, ' + \
										   '\n\tquarter TEXT, ' + \
										   '\n\tanon_screen_name TEXT, ' + \
										   '\n\tvideo_id TEXT, ' + \
										   '\n\tname TEXT, ' + \
										   '\n\tscreen_name TEXT'
}


sql_filename = 'load_db.sql'
sql_file = open(sql_filename, 'a')
sql_file.write('.separator ,\n')
sql_file.write('.nullvalue NULL\n'),

def getClassTableName(fileName):
	# given csv fileName formatted as above, returns [className, (classInfo,) tableName]
	tokens = fileName.split('_')
	tableName = tokens[len(tokens) - 1]
	if tokens[0] == 'engagement':
		return tokens[2:]
	return tokens[1:]

for csvfile in glob.glob('./data/Engineering_CS106A_Fall2013/*.csv'):
	fileName = os.path.splitext(os.path.basename(csvfile))[0]
	tableInfo = getClassTableName(fileName)
	tableNameSuffix = tableInfo[len(tableInfo) - 1]
	tableName = '_'.join(tableInfo)

	sql_file.write('.mode csv ' + tableName + '\n')
	sql_file.write('drop table if exists ' + tableName + ';\n')
	sql_file.write('create table ' + tableName + '(' + predefined_schemas[tableNameSuffix] + '\n);\n')
	sql_file.write('.import ' + csvfile + ' ' + tableName + '\n')
	sql_file.write('delete from ' + tableName + ' limit 1;\n')

sql_file.write('.save data.db\n')

# sanity check
sql_file.write('select * from CS106A_Fall2013_allData limit 1;\n')
sql_file.write('select * from CS106A_Fall2013_summary limit 1;\n')
sql_file.write('select * from CS106A_Fall2013_weeklyEffort limit 1;\n')
sql_file.write('select * from CS106A_Fall2013_ActivityGrade limit 1;\n')
sql_file.write('select * from CS106A_Fall2013_EventXtract limit 1;\n')
sql_file.write('select * from CS106A_Fall2013_VideoInteraction limit 1;\n')
sql_file.write('.schema')
