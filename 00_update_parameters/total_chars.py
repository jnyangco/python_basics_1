
# headline
headline = "QA Test Most Popular Article 1"

# abstract
# expected last word = "testing..."
abstract = "The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testing ellipses."

# # expected last word = "last..."
# abstract = "The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testings ellipses."

full_title_abstract = headline + " " + abstract # total 290 chars
print(f">>> full_title_abstract = {full_title_abstract}")
print(f">>> full_title total chars = {len(full_title_abstract)}")

if len(full_title_abstract) <= 290:
    print(f">>> full_title_abstract = {full_title_abstract}")
else:
    # Truncate at the last full word before 290 characters
    truncated = full_title_abstract[:290]
    if full_title_abstract[290] != ' ':
        truncated = truncated.rsplit(' ', 1)[0]
    expected_display = truncated.strip() + "..."
    print(f">>> expected_abstract = {expected_display}")

