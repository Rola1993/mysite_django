# mysite_django
Django, Python, PostgreSQL, Twilio, Stripe, Ngnix, Gunicorn, DigitalOcean <br />
see deployed website on http://www.mygoodcanteen.com <br />
developing on http://167.99.161.247:8000/<br />
<br />
This project's github profile mistakenly shows another contributor because of a configuration problem. All the code is produced by La Luo.<br />
<br />

Note:<br />
To enable remote access to PostgreSQL server: <br />
nano /etc/postgresql/9.5/main/postgresql.conf<br />
change #listen_addresses = 'localhost'<br />
to listen_addresses = '*'.  (Don't forget to remove #)<br />
nano /etc/postgresql/9.5/main/pg_hba.conf<br />
add host all all all md5 #all ip to the end of that file<br />
sudo service postgresql restart <br />
check: netstat -an | grep 5432 <br />



