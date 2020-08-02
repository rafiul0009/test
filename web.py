from darksky.api import DarkSky
from darksky.types import languages, units, weather

API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'


# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 23.8103
longitude = 90.4125
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False,
    lang=languages.ENGLISH,
    values_units=units.AUTO,
    exclude=[weather.MINUTELY, weather.ALERTS]
)

tz = forecast.timezone
tm = forecast.currently.temperature
sm = forecast.currently.summary


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    t = "Home"
    zone = tz
    temp = tm
    summ = sm
    return render_template("index.html", title=t, timezone=zone, temperature=temp, summary=sm)


@app.route("/about")
def about():
    t = "About"
    return render_template("about.html", title=t)


@app.route("/contact")
def contact():
    t = "Contact"
    return render_template("contact.html", title=t)