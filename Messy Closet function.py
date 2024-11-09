def read_closet_file(file_name):
    # Read items from the text file
    with open(file_name, 'r') as file:
        items = file.read().split()
    return items

def sort_closet(items):
    # Sort items alphabetically
    return sorted(items)

def count_item(items, item_to_search):
    # Count occurrences of a specific item
    return items.count(item_to_search)

# Main program
file_name = 'closet.txt'
try:
    # Read and sort the closet items
    items = read_closet_file(file_name)
    sorted_items = sort_closet(items)
    
    print("Closet items sorted alphabetically:")
    print(" ".join(sorted_items))
    
    # Search for a specific item
    item_to_search = input("Enter the item letter to search for (e.g., 'T' for T-shirts): ").strip()
    item_count = count_item(items, item_to_search)
    
    print(f"Found {item_count} '{item_to_search}' in the closet.")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found. Please make sure the file exists in the directory.")
