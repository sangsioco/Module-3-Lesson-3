def compare_routes(our_routes, competitor_routes):
    # 1. Destinations that both airlines fly to
    common_destinations = our_routes & competitor_routes
    
    # 2. Destinations unique to your airline
    unique_to_our_airline = our_routes - competitor_routes
    
    # 3. Check if there are any destinations that neither airline shares
    all_known_destinations = our_routes | competitor_routes
    
    # Assuming a hypothetical set of all possible destinations for the sake of this example
    all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SYD", "NRT"}
    
    # Destinations that neither airline shares
    neither_airline_destinations = all_possible_destinations - all_known_destinations
    
    # Output the results
    print("Common destinations:", common_destinations)
    print("Destinations unique to our airline:", unique_to_our_airline)
    print("Destinations that neither airline shares:", neither_airline_destinations)
    
 # Routes destination
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

while True:
    print("\n1. Compare flight routes")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        compare_routes(our_routes, competitor_routes)
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again")
