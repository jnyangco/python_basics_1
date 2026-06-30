# Title link
raw_url = "https://qa-1.financialadvisoriq.com/eal/httpgetwrap%7Chttps://www.qa-1.financialadvisoriq.com?reg=1&email=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&from=https%3A%2F%2Fwww.qa-1.financialadvisoriq.com%2Fc%2F4869134%2F639144%2Fsecretary_prodded_defend_fiduciary_rule%3Freferrer_module%3DemailMorningNewsMarketing%26module_order%3D0%26reg%3D1&isBetaRegistration=1"

# FORMAT:
raw_url = (raw_url
           .replace("https://qa-1.financialadvisoriq.com/eal/httpgetwrap%7C", "")
           .replace("%%=URLencode(emailaddr,1,1)=%%", "faiq-user001@money-media.com")
           .replace("%%=URLencode(FirstName,1,1)=%%", "fn1")
           .replace("%%=URLencode(LastName,1,1)=%%", "lname2")
           .replace("%%=URLencode(Title,1,1)=%%", "jt")
           .replace("%%=URLencode(TargetAccount,1,1)=%%", "cmpe") # cmp
           .replace("%%=URLencode(Phone,1,1)=%%", "222") # phone
           .replace("%%=URLencode(CampaignName,1,1)=%%", "ccode") # campcode
           .replace("%%=URLencode(CampaignMemberID,1,1)=%%", "sid2") # salesforceid
           )
print(f"Test URL = \n{raw_url}")