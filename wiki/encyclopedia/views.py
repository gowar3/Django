from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    result = util.get_entry(request)

## Check why it does not return the result if found

    return render(request, "encyclopedia/search.html", {
        "result": result
    })
