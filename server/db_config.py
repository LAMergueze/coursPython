from flaskext.mysql import MySQL


def loadconfig(app):
    mysql = MySQL()

    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'ubuqfhczfbbhxi5b'
    app.config['MYSQL_DATABASE_PASSWORD'] = '4O1WXfSVmZeqOXBud8cT'
    app.config['MYSQL_DATABASE_DB'] = 'bw0ylhu3oiklg07o2ruu'
    app.config['MYSQL_DATABASE_HOST'] = 'bw0ylhu3oiklg07o2ruu-mysql.services.clever-cloud.com:3306'