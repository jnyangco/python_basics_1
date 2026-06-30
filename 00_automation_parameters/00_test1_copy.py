# Title link
# raw_url = "https://commercial.qa-1.pandcspecialist.com/eal/httpgetwrap%7Chttps://commercial.qa-1.pandcspecialist.com/c/4377744/568254/these_commercial_insurers_strengthened_loss_ratios_most?referrer_module=emailMorningNewsMarketing&module_order=1&refemail=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&isBetaTrial=1"
# raw_url = "https://qa-1.fundfire.com/eal/httpgetwrap%7Chttps://www.qa-1.fundfire.com/c/5014814/723984/forward_than_thousand_director_turn_somebody_none_relationship_your?referrer_module=emailMorningNewsMarketing&module_order=0&refemail=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&isBetaTrial=1"

# FF
raw_url = "https://qa-1.fundfire.com/eal/httpgetwrap%7Chttps://www.qa-1.fundfire.com/c/5014814/723984/forward_than_thousand_director_turn_somebody_none_relationship_your?referrer_module=emailMorningNewsMarketing&module_order=0&refemail=%%=URLencode(emailaddr,1,1)=%%&fn=%%=URLencode(FirstName,1,1)=%%&ln=%%=URLencode(LastName,1,1)=%%&cmp=%%=URLencode(TargetAccount,1,1)=%%&ph=%%=URLencode(Phone,1,1)=%%&campcode=%%=URLencode(CampaignName,1,1)=%%&salesforce_id=%%=URLencode(CampaignMemberID,1,1)=%%&jobtitle=%%=URLencode(Title,1,1)=%%&isBetaTrial=1";

# FORMAT:
raw_url = (raw_url
           .replace("https://qa-1.fundfire.com/eal/httpgetwrap%7C", "")
           .replace("%%=URLencode(emailaddr,1,1)=%%", "ff-user-10002@money-media.com")
           .replace("%%=URLencode(FirstName,1,1)=%%", "QA")
           .replace("%%=URLencode(LastName,1,1)=%%", "Test")
           .replace("%%=URLencode(TargetAccount,1,1)=%%", "Test")
           .replace("%%=URLencode(Phone,1,1)=%%", "555-555-5555")
           .replace("%%=URLencode(CampaignName,1,1)=%%", "Test")
           .replace("%%=URLencode(CampaignMemberID,1,1)=%%", "Test")
           .replace("%%=URLencode(Title,1,1)=%%", "Test"))

print(f"Test URL = \n{raw_url}")