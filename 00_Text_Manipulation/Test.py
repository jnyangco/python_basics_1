# expected last word = "testing..."
# headline = "QA Test Most Popular Article 1"
# abstract = "The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testing ellipses."
# "QA Test Most Popular Article 1 The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testing ellipses."
# "QA Test Most Popular Article 1 The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testing..."

# Sample FF - expected last word = "in an..."
# headline = "The ‘LinkedIn Run Club’: Industry Execs Adopt Influencer Tactics to Humanize Firms"
# abstract = "A growing number of industry leaders are taking inspiration from financial influencers, blending videos they film themselves – sometimes dressed in Lycra – with market commentary and industry insights, in an effort to relate to institutional and wealth clients online. "
# "The ‘LinkedIn Run Club’: Industry Execs Adopt Influencer Tactics to Humanize Firms A growing number of industry leaders are taking inspiration from financial influencers, blending videos they film themselves – sometimes dressed in Lycra – with market commentary and industry insights, in an effort to relate to institutional and wealth clients online. "
# "The ‘LinkedIn Run Club’: Industry Execs Adopt Influencer Tactics to Humanize Firms A growing number of industry leaders are taking inspiration from financial influencers, blending videos they film themselves – sometimes dressed in Lycra – with market commentary and industry insights, in an..."


# LASP -> "risks to the..."
# headline = "The Loophole That Helped Blow Open a $2.16B Hole at Insolvent Insurer"
# abstract = "An accounting move to count a certain reinsurance agreement as an asset has quietly helped life insurers boost their reported capital. But a move by Connecticut regulators suggests it may pose broader risks to the industry."
# "The Loophole That Helped Blow Open a $2.16B Hole at Insolvent Insurer An accounting move to count a certain reinsurance agreement as an asset has quietly helped life insurers boost their reported capital. But a move by Connecticut regulators suggests it may pose broader risks to the industry."
# "The Loophole That Helped Blow Open a $2.16B Hole at Insolvent Insurer An accounting move to count a certain reinsurance agreement as an asset has quietly helped life insurers boost their reported capital. But a move by Connecticut regulators suggests it may pose broader risks to the..."




def truncate_to_290_chars(headline, abstract):
    # Combine headline and abstract
    full_combine = headline + " " + abstract

    # If the combined text is already 290 characters or less, return as is
    if len(full_combine) <= 290:
        return full_combine

    # Calculate available space for abstract (290 - headline length - 1 space)
    available_space = 290 - len(headline) - 1

    # If there's no space for abstract, just return headline
    if available_space <= 0:
        return headline

    # Split abstract into words
    abstract_words = abstract.split()

    # Build truncated abstract word by word
    truncated_abstract = ""
    for word in abstract_words:
        # Check if adding this word would exceed available space
        test_length = len(truncated_abstract + word) if not truncated_abstract else len(truncated_abstract + " " + word)
        if test_length <= available_space:
            if truncated_abstract:
                truncated_abstract += " " + word
            else:
                truncated_abstract = word
        else:
            break

    # Combine and add ellipsis (ellipsis doesn't count toward 290 chars)
    result = headline + " " + truncated_abstract + "..."

    return result


# Test with your sample data
headline = "QA Test Most Popular Article 1"
abstract = "The spaceship's system hummed steadily as the astronauts monitored their instruments, each moment is bringing them closer to re-entry to the point at which their training, experiment, calculations, and trust in the engineering team would face the last testing ellipses."

headline = "The ‘LinkedIn Run Club’: Industry Execs Adopt Influencer Tactics to Humanize Firms"
abstract = "A growing number of industry leaders are taking inspiration from financial influencers, blending videos they film themselves – sometimes dressed in Lycra – with market commentary and industry insights, in an effort to relate to institutional and wealth clients online. "

headline = "The Loophole That Helped Blow Open a $2.16B Hole at Insolvent Insurer"
abstract = "An accounting move to count a certain reinsurance agreement as an asset has quietly helped life insurers boost their reported capital. But a move by Connecticut regulators suggests it may pose broader risks to the industry."

result = truncate_to_290_chars(headline, abstract)
print(f"Result: {result}")
print(f"Length without '...': {len(result) - 3}")
print(f"Total length with '...': {len(result)}")