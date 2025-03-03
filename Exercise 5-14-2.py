"""Use integer division and the modulus operator to compute the number of days since January 1, 1970 and the
current time of day in hours, minutes, and seconds."""

import time

# Get the current time in seconds since the Unix epoch  (January 1, 1970, 00:00:00 UTC)
current_seconds = int(time.time())

# Number of seconds in a day (24 hours * 60 minutes * 60 seconds)
seconds_in_day = 24 * 60 * 60

# Compute the number of days since January 1, 1970
epoch_time = current_seconds // seconds_in_day

# Compute the remaining seconds after full days have passed
remaining_seconds = current_seconds % seconds_in_day

# Compute the current time of day (hours, minutes, seconds)
hours = remaining_seconds // 3600  # 3600 seconds in an hour
remaining_seconds %= 3600

minutes = remaining_seconds // 60  # 60 seconds in a minute
seconds = remaining_seconds % 60 # Finds remaining seconds left over from minutes

# Output the results
print(f"Days since January 1, 1970: {epoch_time:,}")
print(f"Current time of day: {hours:02}:{minutes:02}:{seconds:02}")