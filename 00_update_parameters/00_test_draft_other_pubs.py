# Title link
raw_url = "http://qa-1.ignitesasia.com/eal/httpgetwrap%7Chttps://www.qa-1.ignitesasia.com/c/2153243/261003/firms_press_ahead_with_asia_expansions_despite_tough?referrer_module=emailMorningNewsMarketing&module_order=0&refemail=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&isBetaOptin=1"

# FORMAT:
raw_url = (raw_url
           .replace("https://qa-1.ignitesasia.com/eal/httpgetwrap%7C", "")
           .replace("%%=URLencode(emailaddr,1,1)=%%", "ia-user021@money-media.com")
           .replace("%%=URLencode(FirstName,1,1)=%%", "QA")
           .replace("%%=URLencode(LastName,1,1)=%%", "Test")
           .replace("%%=URLencode(TargetAccount,1,1)=%%", "Test")
           .replace("%%=URLencode(Phone,1,1)=%%", "555-555-5555")
           .replace("%%=URLencode(CampaignName,1,1)=%%", "Test")
           .replace("%%=URLencode(CampaignMemberID,1,1)=%%", "Test")
           .replace("%%=URLencode(Title,1,1)=%%", "Test"))

print(f"Test URL = \n{raw_url}")