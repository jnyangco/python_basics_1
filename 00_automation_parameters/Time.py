from datetime import datetime
import pytz

# Create a naive or timezone-aware datetime (assuming UTC for example)
# start_time = datetime.utcnow().replace(tzinfo=pytz.utc)
start_time = datetime.now()


# Define timezones
hk_tz = pytz.timezone('Asia/Hong_Kong')
eu_tz = pytz.timezone('Europe/Berlin')

# Convert to each timezone
start_time_hk = start_time.astimezone(hk_tz)
start_time_eu = start_time.astimezone(eu_tz)

# Print the converted times
print("Start time (UTC):", start_time)
print("Start time (Hong Kong):", start_time_hk)
print("Start time (Europe/Berlin):", start_time_eu)
