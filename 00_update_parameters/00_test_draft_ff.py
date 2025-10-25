# Title link
raw_url = "https://www.qa-1.fundfire.com/eal/httpgetwrap%7Chttps://www.qa-1.fundfire.com/download/agreement/1943084/4972234?referring_issue_id=693764&referrer_module=partnerContentEmail&refemail=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&showContentUrls=1"

# FORMAT:
raw_url = (raw_url
           .replace("https://www.qa-1.fundfire.com/eal/httpgetwrap%7C", "")
           .replace("%%=URLencode(emailaddr,1,1)=%%", "ff-user005@money-media.com")
           .replace("%%=URLencode(FirstName,1,1)=%%", "QA")
           .replace("%%=URLencode(LastName,1,1)=%%", "Test")
           .replace("%%=URLencode(TargetAccount,1,1)=%%", "Test")
           .replace("%%=URLencode(Phone,1,1)=%%", "555-555-5555")
           .replace("%%=URLencode(CampaignName,1,1)=%%", "Test")
           .replace("%%=URLencode(CampaignMemberID,1,1)=%%", "Test")
           .replace("%%=URLencode(Title,1,1)=%%", "Test"))

print(f"Test URL = \n{raw_url}")