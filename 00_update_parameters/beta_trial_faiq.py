# Title link
raw_url = "https://qa-1.financialadvisoriq.com/eal/httpgetwrap%7Chttps://www.qa-1.financialadvisoriq.com?reg=1&email=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&from=https%3A%2F%2Fwww.qa-1.financialadvisoriq.com%2Fc%2F2166523%2F260323%2Fjpmorgan_fined_million_over_alleged_mishandling%3Freferrer_module%3DemailMorningNewsMarketing%26module_order%3D1%26reg%3D1&isBetaRegistration=1"

# FORMAT:
raw_url = (raw_url
           .replace("https://qa-1.financialadvisoriq.com/eal/httpgetwrap%7C", "")
           .replace("%%=URLencode(emailaddr,1,1)=%%", "qa-user1762265806447@money-media.com")
           .replace("%%=URLencode(FirstName,1,1)=%%", "QA")
           .replace("%%=URLencode(LastName,1,1)=%%", "Test")
           .replace("%%=URLencode(TargetAccount,1,1)=%%", "Test")
           .replace("%%=URLencode(Phone,1,1)=%%", "555-555-5555")
           .replace("%%=URLencode(CampaignName,1,1)=%%", "Test")
           .replace("%%=URLencode(CampaignMemberID,1,1)=%%", "Test")
           .replace("%%=URLencode(Title,1,1)=%%", "Test"))

print(f"Test URL = \n{raw_url}")