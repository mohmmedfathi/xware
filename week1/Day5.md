# Day 5
# Install Postgresql
* >>>sudo apt update

* >>> sudo apt install postgresql postgresql-contrib

* >>>sudo systemctl start postgresql.service

* >>>service posgresql status

* >>>sudo -u postgres psql

* >>>sudo systemctl restart postgresql

# Install pgAdmin
* >>> sudo -u postgres psql

* >>> sudo apt-get update

* >>> sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

* >>> sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update

* >>> sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

* >>> sudo apt istall pgadmin4
