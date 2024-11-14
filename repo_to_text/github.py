import requests
from urllib.parse import urlparse
from .converter import BaseConverter

class GitHubConverter(BaseConverter):
    """Handles conversion of GitHub repositories."""
    
    def __init__(self, output_file: str, github_token: str = None):
        super().__init__(output_file)
        self.headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        if github_token:
            self.headers['Authorization'] = f'token {github_token}'

    def fetch_content(self, api_url: str, path: str = '') -> dict:
        """Fetch repository content from GitHub API."""
        url = f"{api_url}/{path}" if path else api_url
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def process_content(self, content_list: list, api_url: str) -> None:
        """Process and write repository content."""
        for item in content_list:
            if item['type'] == 'file':
                # Skip binary files
                if not item['name'].endswith(('.md', '.py', '.js', '.java', '.cpp', '.h', '.css', 
                                            '.html', '.txt', '.yml', '.yaml', '.json', '.xml', '.sh')):
                    print(f"Skipping likely binary file: {item['path']}")
                    continue
                    
                response = requests.get(item['download_url'], headers=self.headers)
                try:
                    content = response.text
                    self.write_content(item['path'], content)
                except Exception as e:
                    print(f"Error processing {item['path']}: {str(e)}")
                    
            elif item['type'] == 'dir':
                # Recursively process subdirectories
                subdir_content = self.fetch_content(api_url, item['path'])
                self.process_content(subdir_content, api_url)

    def convert(self, repo_url: str) -> None:
        """Convert GitHub repository to text format."""
        # Parse GitHub URL
        parsed = urlparse(repo_url)
        path_parts = parsed.path.strip('/').split('/')
        if len(path_parts) != 2:
            raise ValueError("Invalid GitHub URL format. Expected: https://github.com/owner/repo")
        
        owner, repo = path_parts
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
        
        # Clear output file if it exists
        self.output_file.write_text('')
        
        # Start processing from root
        content = self.fetch_content(api_url)
        self.process_content(content, api_url)