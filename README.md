# Scraping 2018 NBA Scores

<h3>By Daniel Lee</h3>
<h3>January 4, 2019</h3>

## Description

This is a web scraper that extracts 2018 NBA scores from <a href='http://www.espn.com'>espn.com</a>.

<h2>Data Scraping Implementation</h2>
	<ul>
		<li>The data is obtained through scraping the <a href="http://www.espn.com">espn.com</a> website using the following:
			<ul>
				<li>Python (v. 3.6.7)
				<li>Scrapy (v. 1.5.1)
				<li>Splash (v. 0.7.2)
			</ul>
		<li>The data is stored in a MongoDB database. 
		<li>The web scraping app is deployed on Heroku. 
	</ul>
<h2>REST API Implementation</h2>
	<ul>
		<li>You can access the scraped data using <a href='https://nba-scores-api.herokuapp.com/'>2018 NBA Scores API</a>.
		<li>You can access the code for the API <a href='https://github.com/danielhanbitlee/nba_scores_api_flask_pymongo'>here</a>.
		<li>The REST API is implemented using the following:
		<ul>
			<li>Python (v. 3.6.7)
			<li>Flask (v. 1.0.2)
		</ul>
		<li>This API is connected to a MongoDB database to access the data
		<li>The API is deployed on Heroku.
		<li>There's also an /auth route and a /register route for authentication and logging in. This requires Postman to use. For simplicity's sake, I removed the authentication requirements for the routes /team, /city, /date, /team_list, and /city_list.
	</ul>

