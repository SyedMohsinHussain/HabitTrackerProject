
def format_completed_dates(completed_dates):
    """
    Truncate the completed dates list to the latest 3 dates and add '...' if there are more than 3 dates.
    """
    # Reverse the list to get the latest dates, then truncate to the first 3
    if len(completed_dates) > 3:
        return ", ".join(completed_dates[-3:]) + " ..."
    return ", ".join(completed_dates)