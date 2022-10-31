from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\Users\\lenovo\\Desktop\\SeleniumPython\\BDDBehavePOM\\ConfigurationData\\config.ini")
    return config.get(section, Key)