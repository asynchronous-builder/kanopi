cd backend
pipenv install
cd color_project
pipenv run python manage.py migrate
pipenv run python manage.py runserver &

echo "Start frontend"
cd ../../frontend
npm install
npm start

wait