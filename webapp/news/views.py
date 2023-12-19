from flask import Blueprint, abort, current_app, render_template
from webapp.news.models import News
from webapp.weather import get_weather_by_city
from webapp.news_ks import get_news_ks

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'Новости'
    weather = get_weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    get_news_ks()
    all_news = News.query.order_by(News.date.desc()).all()
    return render_template(
        'index.html',
        weather=weather,
        all_news=all_news,
        title=title
        )


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)
    return render_template(
        'single_news.html',
        title=my_news.title,
        text=my_news.text,
    )
