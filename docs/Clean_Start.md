(1) Delete Migration
```bash
rm -rf ./migrations  # If exists
```


(2) Run following SQL
```sql
DROP DATABASE koup;  /* if exists */
CREATE DATABASE koup;
CREATE USER robot WITH ENCRYPTED PASSWORD 'rootpwd';
GRANT ALL PRIVILEGES ON DATABASE koup TO robot;
```


(3) Set .env Variable to `Init`
```txt
BUILD_TYPE = Init
```


(4) Start the Server
```bash
./scripts/build.sh
```


(5) Set .env Variable to `Update`
```txt
BUILD_TYPE = Update
```


(6) Setting Up API (Go to path from base URL)

```url
baseURL/setup
```
