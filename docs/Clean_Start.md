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

(3) Regenerate Migration
```python
flask db init
flask db migrate
flask db upgrade

```

(4) Start the Server
```bash
./scripts/build.sh
```

(5) Setting Up API (Go to path from base URL)

```url
   baseURL/setup
```