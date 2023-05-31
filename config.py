import configparser


class Config:

    global config
    config = configparser.ConfigParser()
    config.read('config.ini')

    @staticmethod
    def get_url():
        base_url = config.get('Credentials', 'base_url')
        return base_url

    @staticmethod
    def get_username():
        username = config.get('Credentials', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Credentials', 'password')
        return password



