.separator ,
.nullvalue NULL
.mode csv CS106A_Fall2013_allData
drop table if exists CS106A_Fall2013_allData;
create table CS106A_Fall2013_allData(
	Platform TEXT, 
	Course TEXT, 
	anon_screen_name TEXT, 
	Date DATE, 
	Time TIME, 
	[SessionLength(sec)] INTEGER, 
	NumEventsInSession INTEGER
);
.import ./data/Engineering_CS106A_Fall2013/engagement_Engineering_CS106A_Fall2013_allData.csv CS106A_Fall2013_allData
delete from CS106A_Fall2013_allData limit 1;
.mode csv CS106A_Fall2013_summary
drop table if exists CS106A_Fall2013_summary;
create table CS106A_Fall2013_summary(
	Platform TEXT, 
	Course TEXT, 
	TotalStudentSessions TEXT, 
	[TotalEffortAllStudents(secs)] INTEGER, 
	MedPerWeekOneToTwenty INTEGER, 
	MedPerWeekTwentyoneToSixty INTEGER, 
	MedPerWeekGreaterSixty INTEGER
);
.import ./data/Engineering_CS106A_Fall2013/engagement_Engineering_CS106A_Fall2013_summary.csv CS106A_Fall2013_summary
delete from CS106A_Fall2013_summary limit 1;
.mode csv CS106A_Fall2013_weeklyEffort
drop table if exists CS106A_Fall2013_weeklyEffort;
create table CS106A_Fall2013_weeklyEffort(
	Platform TEXT, 
	Course TEXT, 
	anon_screen_name TEXT, 
	Week INTEGER, 
	[Effort (sec)] INTEGER
);
.import ./data/Engineering_CS106A_Fall2013/engagement_Engineering_CS106A_Fall2013_weeklyEffort.csv CS106A_Fall2013_weeklyEffort
delete from CS106A_Fall2013_weeklyEffort limit 1;
.mode csv CS106A_Fall2013_ActivityGrade
drop table if exists CS106A_Fall2013_ActivityGrade;
create table CS106A_Fall2013_ActivityGrade(
	activity_grade_id INTEGER, 
	student_id INTEGER, 
	course_display_name TEXT, 
	grade FLOAT, 
	max_grade FLOAT, 
	percent_grade FLOAT, 
	parts_correctness TEXT, 
	answers TEXT, 
	num_attempts INTEGER, 
	first_submit DATETIME, 
	last_submit DATETIME, 
	module_type TEXT, 
	anon_screen_name TEXT, 
	resource_display_name TEXT, 
	module_id TEXT, 
	name TEXT, 
	screen_name TEXT
);
.import ./data/Engineering_CS106A_Fall2013/Engineering_CS106A_Fall2013_ActivityGrade.csv CS106A_Fall2013_ActivityGrade
delete from CS106A_Fall2013_ActivityGrade limit 1;
.mode csv CS106A_Fall2013_EventXtract
drop table if exists CS106A_Fall2013_EventXtract;
create table CS106A_Fall2013_EventXtract(
	anon_screen_name TEXT, 
	event_type TEXT, 
	ip_country TEXT, 
	time DATETIME, 
	quarter TEXT, 
	course_display_name TEXT, 
	resource_display_name TEXT, 
	success TEXT, 
	video_code TEXT, 
	video_current_time FLOAT, 
	video_speed TEXT, 
	video_old_time FLOAT, 
	video_new_time FLOAT, 
	video_seek_type TEXT, 
	video_new_speed FLOAT, 
	video_old_speed FLOAT, 
	goto_from FLOAT, 
	goto_dest FLOAT
);
.import ./data/Engineering_CS106A_Fall2013/Engineering_CS106A_Fall2013_EventXtract.csv CS106A_Fall2013_EventXtract
delete from CS106A_Fall2013_EventXtract limit 1;
.mode csv CS106A_Fall2013_VideoInteraction
drop table if exists CS106A_Fall2013_VideoInteraction;
create table CS106A_Fall2013_VideoInteraction(
	event_type TEXT, 
	resource_display_name TEXT, 
	video_current_time FLOAT, 
	video_speed FLOAT, 
	video_new_speed FLOAT, 
	video_old_speed FLOAT, 
	video_new_time FLOAT, 
	video_old_time FLOAT, 
	video_seek_type TEXT, 
	video_code TEXT, 
	time DATETIME, 
	course_display_name TEXT, 
	quarter TEXT, 
	anon_screen_name TEXT, 
	video_id TEXT, 
	name TEXT, 
	screen_name TEXT
);
.import ./data/Engineering_CS106A_Fall2013/Engineering_CS106A_Fall2013_VideoInteraction.csv CS106A_Fall2013_VideoInteraction
delete from CS106A_Fall2013_VideoInteraction limit 1;
.save data.db
select * from CS106A_Fall2013_allData limit 1;
select * from CS106A_Fall2013_summary limit 1;
select * from CS106A_Fall2013_weeklyEffort limit 1;
select * from CS106A_Fall2013_ActivityGrade limit 1;
select * from CS106A_Fall2013_EventXtract limit 1;
select * from CS106A_Fall2013_VideoInteraction limit 1;
.schema