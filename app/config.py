class Config:
    DEBUG = False
    SECRET_KEY = "charles123"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


app_configuration = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
