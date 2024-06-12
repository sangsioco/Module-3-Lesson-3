def check_for_duplicate_artists(artist_names):
    """
    This function takes a list of artist names and checks for duplicates.
    
    Parameters:
    artist_names (list): A list of artist names.
    
    Returns:
    bool: True if duplicates are found, False otherwise.
    """
    return len(artist_names) != len(set(artist_names))

# List of artist names
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

# Check for duplicates
duplicates_found = check_for_duplicate_artists(artist_names)

# Create a set of unique artists
unique_artists = set()

# Loop through each artist in the list and add them to the set
for artist in artist_names:
    unique_artists.add(artist)

# Print the unique lineup
print(unique_artists)

# Check if duplicates were found and print the result
if duplicates_found:
    print("Duplicate artists found: True")
else:
    print("Duplicate artists found: False")
