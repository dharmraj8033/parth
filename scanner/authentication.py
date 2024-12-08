import httpx

class Authentication:
    def __init__(self, login_url, credentials):
        self.login_url = login_url
        self.credentials = credentials
        self.session = httpx.Client()

    def login(self):
        try:
            response = self.session.post(self.login_url, data=self.credentials)
            if response.status_code == 200:
                print("Authentication successful!")
                return True
            else:
                print(f"Login failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def get_authenticated_session(self):
        return self.session
