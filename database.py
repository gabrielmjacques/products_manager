from configparser import ConfigParser
import mysql.connector

configparser = ConfigParser()
configparser.read('db_config.ini')

def DBConnect():
    try:
        connector = mysql.connector.connect(
            host = configparser.get('database', 'host'),
            user = configparser.get('database', 'user'),
            password = configparser.get('database', 'password'),
            database = configparser.get('database', 'database'),
        )
        
        print('Connected')
        return connector
        
    except Exception as e:
        print('Err: ', e)

