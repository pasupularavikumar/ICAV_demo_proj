git clone https://github.com/pasupularavikumar/ICAV_demo_proj.git
open the folder ICAV_demo_proj
pip install virtualenv
"create virtualenv" =>  virtualenv demoenv     "here demoenv is environment name
'windows' => cd demoenv/scripts/activate     'linux/ubuntu' source demoenv/bin/activate
change the directory to ICAV_demo_proj/demoproj
pip install -r requiremnts.txt 
python manage.py makemigrrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
open the browser and paste the given url 
and login and check the website
