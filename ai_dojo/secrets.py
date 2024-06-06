import os

def get_secret(file_name, secrets_dir="../../secrets"):
    """
    Reads the first line from a specified file in a given directory and returns it as a secret.
    
    Args:
    file_name (str): Name of the file containing the secret.
    secrets_tir (str): Directory where the secret file is stored. Default is "../../secrets".
    
    Returns:
    str: The secret stored in the first line of the file, or None if an error occurs.
    """
    # Construct the full path to the file
    file_path = os.path.join(secrets_dir, file_name)
    
    try:
        with open(file_path, 'r') as file:
            secret = file.readline().strip()  # Read the first line and strip newline characters
        return secret
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

