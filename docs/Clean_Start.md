(1) Delete Migration
```bash
rm -rf ./migrations
```

(2) Run following SQL
```sql
DEOP DATABASE koup; # if exists
CREATE DATABASE koup;
CREATE USER robot WITH ENCRYPTED PASSWORD 'rootpwd';
GRANT ALL PRIVILEGES ON DATABASE koup TO robot;

```

(3) Start the Server
```bash
make prod
```

(4) Setting Up API (Go to path from base URL)

```url
baseURL/setup
```