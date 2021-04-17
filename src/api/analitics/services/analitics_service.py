import datetime
from rest_framework.response import Response

from posts.models import PostLike, PostDislike


class AnaliticsService:
    def get_analitics(self, date_from, date_to):
        res = []
        for day in range((date_to - date_from).days + 1):
            date = date_from + datetime.timedelta(days=day)
            min_datetime = self._get_min_datetime(date)
            max_datetime = self._get_max_datetime(date)
            res.append({
                date.strftime('%Y-%d-%m'): {
                    'likes': PostLike.objects.filter(date__range=(min_datetime, max_datetime)).count(),
                    'dislikes': PostDislike.objects.filter(date__range=(min_datetime, max_datetime)).count()
                }
            })
        return Response(res)

    def _get_min_datetime(self, date):
        return datetime.datetime.combine(date, datetime.datetime.min.time())

    def _get_max_datetime(self, date):
        return datetime.datetime.combine(date, datetime.datetime.max.time())
