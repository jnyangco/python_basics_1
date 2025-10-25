# Title link
raw_url = "https://www.qa-1.lifeannuityspecialist.com/eal/httpgetwrap%7Chttps://www.qa-1.lifeannuityspecialist.com/c/4969844/695214/matter_offer_word_well_reduce_discover_surface_media?referrer_module=emailMorningNewsMarketing&module_order=0&refemail=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&isInsuranceAgent=1"

# FORMAT:
raw_url = (raw_url
           .replace("https://www.qa-1.lifeannuityspecialist.com/eal/httpgetwrap%7C", "")
           .replace("%%=URLencode(emailaddr,1,1)=%%", "lasp-user-001@money-media.com")
           .replace("%%=URLencode(FirstName,1,1)=%%", "QA")
           .replace("%%=URLencode(LastName,1,1)=%%", "Test")
           .replace("%%=URLencode(TargetAccount,1,1)=%%", "Test")
           .replace("%%=URLencode(Phone,1,1)=%%", "555-555-5555")
           .replace("%%=URLencode(CampaignName,1,1)=%%", "Test")
           .replace("%%=URLencode(CampaignMemberID,1,1)=%%", "Test")
           .replace("%%=URLencode(Title,1,1)=%%", "Test"))

print(f"Test URL = \n{raw_url}")