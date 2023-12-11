from flask import Blueprint, current_app, render_template
from webapp.news.models import News
from webapp.weather import get_weather_by_city
from webapp.news_ks import get_news_ks

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'Новости'
    weather = get_weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    new = get_news_ks()
    all_news = News.query.order_by(News.date.desc()).all()
    return render_template(
        'index.html',
        weather=weather,
        all_news=all_news,
        )
