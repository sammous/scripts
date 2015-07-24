import re

#Regex for an email address scheme
regex_email = re.compile("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")

#Regex for phone numbers, supported schemes are between 7 to 10 digits and :
"""

000 000 0000
000.000.0000

(000)000-0000
(000)000 0000
(000)000.0000
(000) 000-0000
(000) 000 0000
(000) 000.0000

000-0000
000 0000
000.0000

0000000
0000000000
(000)0000000

"""
regex_phone = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")



def hide_emails(s):
	return re.sub(regex_email,"<span class=\"\">[email hidden]</span>",s)
	 
def hide_phones(s):
	return re.sub(regex_phone,"<span class=\"\">[phone hidden]</span>",s)






