from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):


    title = markdown2.markdown(util.get_entry(entry))

    if not title:
        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/entry.html", {
        "result": title,
        "title": entry
    })

def search(request):

    search_term = request.GET.get("q", "")
    result = util.get_entry(search_term)

    if not result:
        search_term = ""


    return render(request, "encyclopedia/entry.html", {
        "result": result,
        "title": search_term
    })
