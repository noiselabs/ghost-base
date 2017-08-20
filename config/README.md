# Config

Place here your Ghost and Docker configuration files. You can start with the example files provided in the `.dist` folder.

```
cp .dist/* ./
```

The values for the MySQL root password and user and password for the Ghost MySQL database are missing. Please edit the `.json` and `.env`. files and provide those details.

`config.<env>.json`:
```
"database": {
    "client": "mysql",
    "connection": {
      "host": "db",
      "database": "ghost_prod",
      "user": "",
      "password": ""
    }
  },
  ```

`<env>.env`:
```
MYSQL_DATABASE=ghost_prod
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_ROOT_PASSWORD=
```