from django.http import JsonResponse
from .requests_methods import ZKTeco

def logs(request, id_user, sdate=None, edate=None):
	zkteco = ZKTeco()
	if sdate and edate:
		return zkteco.logs(id_user, sdate, edate)
	return JsonResponse(zkteco.logs(id_user))

def users(request, first=None, last=None):
	zkteco = ZKTeco()
	return JsonResponse(zkteco.users(first, last))

def user(request):
	return JsonResponse({})