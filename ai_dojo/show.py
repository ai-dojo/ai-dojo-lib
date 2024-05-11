from IPython.display import display, Markdown, HTML
import requests
import html



def command(cmd):
    """
    Display a terminal command with an HTML layout, including a "Copy" button with a clipboard symbol.
    
    This function produces a stylized HTML representation of a terminal command.
    It features a light gray background, rounded corners, and a "Copy" button that
    allows users to copy the command to their clipboard using a clipboard symbol as the button label.
    
    Parameters:
        cmd (str): The terminal command to be displayed.
    
    Returns:
        IPython.core.display.HTML: HTML object for IPython display.
    
    Example:
        command("git pull")
    """
    # Escape the command to safely display special HTML characters
    escaped_cmd = html.escape(cmd)
    
    # HTML content with styling for the terminal command display and copy functionality
    html_content = f"""
    <div style='margin:10px 0; padding:10px; background-color:#f0f0f0; border:1px solid #ccc; border-radius: 5px; display: flex; align-items: center;'>
        <tt style='flex-grow: 1;'>{escaped_cmd}</tt>
        <button onclick='navigator.clipboard.writeText("{escaped_cmd}")' style='padding: 5px 10px; margin-left: 10px; cursor: pointer; border: none; background-color: #ccc; color: #333; border-radius: 5px;'>📋</button>
    </div>
    """
    return HTML(html_content)

def text(text: str, limit: int = 1000):
    """Display text in an output cell formatted with Markdown, limited to a specified number of characters.

    Args:
    text (str): The text to be displayed.
    limit (int): The maximum number of characters to be displayed. Default is 1000.
    """
    # Limit the text to the specified number of characters
    limited_text = text[:limit]
    # Display the text as Markdown
    display(Markdown(limited_text))


def github_repo(repo_url, github_token=None):
    """
    Display a preview of a GitHub repository in a Jupyter Notebook.

    This function fetches repository information from GitHub API and displays
    an HTML formatted preview including the repository's name, organization/user,
    star count, license, and a short description ("About" section). If an error occurs
    during the API request, or if the request times out after 5 seconds, it displays
    a fallback message with the repository URL.

    Parameters:
        repo_url (str): The URL of the GitHub repository.
        github_token (str, optional): A GitHub access token for authentication.
            Default is None, which means no authentication is used.

    Returns:
        None: This function directly renders HTML content in a Jupyter Notebook
        environment and does not return any value.

    Example usage:
        display_github_repo_preview("https://github.com/jupyter/notebook")
        display_github_repo_preview("https://github.com/jupyter/notebook", "your_github_token")
    """

    # Extract the user and repo name from the URL
    parts = repo_url.split("/")
    user, repo = parts[-2], parts[-1]
    
    # Prepare the API URL
    api_url = f"https://api.github.com/repos/{user}/{repo}"
    
    # Headers for authentication (if token provided)
    headers = {'Authorization': f'token {github_token}'} if github_token else {}
    
    try:    
        # Fetch repository data from GitHub API with a timeout
        response = requests.get(api_url, headers=headers, timeout=5)  # 5 seconds timeout
        
        if response.status_code == 200:
            repo_data = response.json()
            # Prepare elements from the response
            repo_name = repo_data.get('name', 'Repository Name')
            stars = repo_data.get('stargazers_count', 0)
            license_info = repo_data.get('license', {}).get('name', 'No license')
            avatar_url = repo_data.get('owner', {}).get('avatar_url', 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
            organization = repo_data.get('owner', {}).get('login', 'No organization')
            description = repo_data.get('description', 'No description provided.')
            
            # Construct HTML content
            html_content = f"""
            <div style="border:1px solid #e1e4e8; padding: 20px; border-radius: 6px; font-family: Arial, sans-serif; box-shadow: 0 2px 3px rgba(0,0,0,0.1); display: flex; align-items: center;">
                <img src="{avatar_url}" alt="Repo Icon" style="width: 50px; vertical-align: middle; border-radius: 50%; margin-right: 10px;">
                <div style="flex-grow: 1;">
                    <span style="font-size: 20px;"><a href="{repo_url}" target="_blank">{repo_name}</a></span>
                    <p style="margin: 5px 0;"><strong>Organization/User:</strong> {organization}</p>
                    <p style="margin: 5px 0;"><em>{description}</em></p>
                </div>
                <div style="margin-left: auto; text-align: right;">
                    <p style="margin: 0; font-size: 16px;">★ {stars}</p>
                    <p style="margin: 0; font-size: 16px;"><strong>License:</strong> {license_info}</p>
                </div>
            </div>
            """
            display(HTML(html_content))
        else:
            raise Exception("Failed to fetch data from GitHub API")
    except Exception as e:
        # Fallback display when any error occurs
        html_content = f"""
        <div style="border:1px solid #e1e4e8; padding: 20px; border-radius: 6px; font-family: Arial, sans-serif; box-shadow: 0 2px 3px rgba(0,0,0,0.1); text-align: center;">
            <p style="font-size: 18px;">Unable to fetch repository details due to an error: {str(e)}</p>
            <p style="font-size: 16px; font-weight: bold;"><a href="{repo_url}" target="_blank">{repo_url}</a></p>
        </div>
        """
        display(HTML(html_content))

