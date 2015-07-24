## Synopsis

Miscellaneous scripts written in different contexts.


## List of scripts

1. hide.py

Code Example

	def hide_emails(s):
	return re.sub(regex_email,"<span class=\"\">[email hidden]</span>",s)
	`python`

Language : `python`

This script allows to hide specific emails and phone number by injecting HTML Tags.