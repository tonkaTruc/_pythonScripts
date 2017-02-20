from jira import JIRA
import getpass

#jira = JIRA('http://calrec-jira:9090')

usrName = raw_input("Please enter your JIRA username: ")
usrPw = getpass.getpass(prompt="Please enter your JIRA password: ")

authed_jira = JIRA('http://calrec-jira:9090', basic_auth=(usrName,usrPw ))								# Needs to use OAUTH for better security

issueID = raw_input("Please enter the issue ID. Include CAL prefix: ")												# Enter issue ID
issue = authed_jira.issue(issueID)		

print("")
print ("Summary: " + issue.fields.summary)           																			# Pull the "description" body for the specified issue out of the API 																					
print("")
print ("Description: " + issue.fields.description) 
print("")          																								# Pull the "description" body for the specified issue out of the API 
print ("\nIssue project: " + issue.fields.project.key)             																# 'CAL'
print ("Issue type: " + issue.fields.issuetype.name)         																# 'Bug'
print ("Reported by: " + issue.fields.reporter.displayName + "\n")   	 												# Reporter name


