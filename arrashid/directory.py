
import os

def search_file(name='config', priority_order=['.json', '.xml', '.yaml', '.txt'], directory='.'):
    """
    Select a file with the specified name and any of the specified extensions from the specified directory
    based on priority order for extensions.

    :param name: Optional. The base name of the file (default is 'config').
    :param priority_order: Optional. List of file extensions in priority order (default is ['.json', '.xml', '.yaml', '.txt']).
    :param directory: Optional. The directory to search for the file (default is the current directory).
    :return: The selected file name or None if no matching file is found.
    """
    files = os.listdir(directory)
    
    # Initialize a variable to store the selected file
    selected_file = None

    # Iterate through the priority order
    for ext in priority_order:
        full_name = f"{name}{ext}"
        if full_name in files:
            selected_file = full_name
            break  # Found a file with this extension, break the loop

    return selected_file
