from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    title = util.get_entry(entry)

    return render(request, "encyclopedia/search.html", {
        "result": title
    })

def search(request):

    search_term = request.GET.get("q", "")
    result = util.get_entry(search_term)


    return render(request, "encyclopedia/search.html", {
        "result": result
    })
