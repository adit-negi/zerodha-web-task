# zerodha-web-task
Initial task for zerodha backend engineer

## Set up instructions
<li>Install python and pip</li>
<li>git clone</li>
<li>cd into repo</li>
<li>pip install -r requirements.txt </li>
<li>run - python manage.py runserver/migrate to start up</li>
<li>change redis location to your local port</li>
<li>python manage.py crontab add to start the cron process</li>

## Implemented features
<li>Data is fetched from bhavcopy website https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx</li>
<li>Zip file is extracted and stored in REDIS, with the name as key.(Name chosen because it was unique for over 10k records and thus it was reasonable to believe it is always unique)</li>
<li>API end points built
   <br>
   <ul>1. Fetch all data</ul>
   <ul>2. Fetch name specific provided slug</ul>
</li>
<li>Daily task scheduler/cron built which adds new data every day at 6pm IST</li>
<li>Search through data in redis</li>
<li>Due to limitations of free tier I have set redis to timeout at every 7 days</li>
<li>Added celery queues if tasks get data intensive in future we can run them asynchronously</li>

## Shortcomings
<li>Frontend needs a lot of improvement(vue experience.....)</li>
<li>Should add pagination to data from the backend itself(didn't because with the timeout the size isn't going to be that big of an issue)</li>

## ToDo
<li>Add export to csv option</li>
