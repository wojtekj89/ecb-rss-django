
# ecb-rss-django
Simple currency exchange rate API scraping data from ECB RSS feeds. Using celery to create daily task pulling new rates just after they are published - at 15:10 CET. Technology used: Pytho, Django, DRF, Celery with Redis as a broker, PostreSQL and BeutifulSoup.

## Getting started
### Prerequisities
In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage
```
docker-compose build
docker-compose up
```

If you want to run the app again please use `docker-compose down` before you rebuild the container to remove duplicated data.
### After successfull build application will be runnig [here](http://localhost:8000/all)
# Supported API Endpoints

## /all

### GET

List of all currency exchange rates collected by the app. Possible filtering by currency symbol
Examples:
`/all?currency=usd` for all USD exchange rates

## /today

### GET

List of latest currency exchange rates.

# Ideas for next iterations:
* Refactor and think more about DB model - analyze use cases and most common scenarios
* Create unit tests
* CI/CD 
* Handle possible exceptions in views
* Add more sorting and filtering options
* Create better way to read archive data on start
* Prevent from adding duplicates
* Fix bug with no data in /today when latest update was more than 2 days earlier
* Celery retry policy, make sure data is read even if app was down when task was executed
