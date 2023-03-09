# simple-weather-telegram-bot
<b>This bot allows users to get current weather and weekly forecast for user's locations based on city input.</b>


<b>1.Create a new Telegram bot with [Bot Father](https://web.telegram.org/k/#@BotFather)</b>

Copy and paste the API token into [config.py](weather_bot/config.py)

<code>BOT_API_TOKEN = 'Paste your API token here'</code>

<b>2. Create an account on [WeatherApi](https://www.weatherapi.com/)</b>
	(hint: you can use [temporary mail](https://temp-mail.org/))

Copy and paste the API token into [config.py](weather_bot/config.py)

<code>WEATHER_API = 'Paste your API key here'</code>

<b>3. Get the latest Python version</b>

<b>4. Create a virtual environment.</b>

Not necessary, but highly recommended.

<b>5.Install requirements</b>

<code>pip install -r requirements.txt</code>

<b>6.Run [bot.py](weather_bot/bot.py)</b>

<code>python .\weather_bot\bot.py</code>