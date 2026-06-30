# expected last word = "testing..."
headline = "QA Test Most Popular Article 1"
abstract = "The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testing ellipses."

# Sample FF
# headline = "The ‘LinkedIn Run Club’: Industry Execs Adopt Influencer Tactics to Humanize Firms"
# abstract = "A growing number of industry leaders are taking inspiration from financial influencers, blending videos they film themselves – sometimes dressed in Lycra – with market commentary and industry insights, in an effort to relate to institutional and wealth clients online. "

# LASP
# The Loophole That Helped Blow Open a $2.16B Hole at Insolvent Insurer
# An accounting move to count a certain reinsurance agreement as an asset has quietly helped life insurers boost their reported capital. But a move by Connecticut regulators suggests it may pose broader risks to the industry.


# headline = "The ‘LinkedIn Run Club’: Industry Execs Adopt Influencer Tactics to Humanize Firms"
# abstract = (
#     "A growing number of industry leaders are taking inspiration from financial influencers, "
#     "blending videos they film themselves – sometimes dressed in Lycra – with market commentary "
#     "and industry insights, in an effort to relate to institutional and wealth clients online. "
# )


full_combined = headline + "abstract
max_length = 290

if len(full_combined) <= max_length:
    expected_abstract = abstract.strip()
else:
    truncated = full_combined[:max_length]

    if not truncated.endswith(" "):
        truncated = truncated.rsplit(" ", 1)[0]

    truncated_with_ellipsis = truncated.strip() + "..."

    prefix = headline + " "
    if truncated_with_ellipsis.startswith(prefix):
        expected_abstract = truncated_with_ellipsis[len(prefix):]
    else:
        expected_abstract = ""

print(f"expected_abstract: {expected_abstract}")
