import requests

# Example JIRA API URL:
# http://host:port/context/rest/api-name/api-version/resource-name

# https://jira.atlassian.com/rest/api/latest/issue/JRA-9

HOST = "jira.atlassian"							# <calrec jira server URL>
RESOURCE = "issue"
ISSUE_ID = "JRA-9"

print (HOST + RESOURCE + ISSUE_ID)
