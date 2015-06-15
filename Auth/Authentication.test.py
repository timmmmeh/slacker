import uittest
import Authentication

class TestAuth(unittest.TestCase):

    def setUp(self):

        self.sessions = Authentication.AuthService()
        self.sessions.add_session("Daniel")



    def test_add_session(self):
        pass

    def test_remove_session(self):
        pass

    def test_validator(self):
        pass

    def test_check_user_db(self):
        pass

    def test_POST(self):
        pass

if __name__ == '__main__':
    unittest.main()