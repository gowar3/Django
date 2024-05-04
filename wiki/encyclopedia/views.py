from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    title = util.get_entry(entry)

    if title is None:
        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/entry.html", {
        "result": title,
        "title": entry
    })

def search(request):

    if request:
        search_term = request.GET.get("q", "")
        result = util.get_entry(search_term)
    else:
        search_term = None


    return render(request, "encyclopedia/entry.html", {
        "result": result,
        "title": search_term
    })
