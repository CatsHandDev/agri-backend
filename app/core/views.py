from django.http import JsonResponse  # type: ignore


def api_root(request):
    """
    APIのルートにアクセスした際に表示するシンプルなビュー
    """
    return JsonResponse({"status": "ok", "message": "Welcome to the Agri-Support API!"})
