from django.shortcuts import render
import markdown2
from django.urls import reverse
from django.http import HttpResponseRedirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entry(request, entry):

    page = util.get_entry(entry)

    if page:

        title = markdown2.markdown(page)

    else:

        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/entry.html", {
        "result": title,
        "title": entry
    })



def search(request):

    search_term = request.GET.get("q", "")

    entries = util.list_entries()

    for entry in entries:

        if search_term in entry:

            result = util.get_entry(entry)

        else:

            return render(request, "encyclopedia/error.html")


    return render(request, "encyclopedia/entry.html", {
        "result": markdown2.markdown(result),
        "title": search_term
    })



def new(request):


    if request.method == "POST":

        title = request.POST["title"]

        util.save_entry(request.POST["title"], request.POST["content"])

        return HttpResponseRedirect(reverse("entry", args= [title]))


    return render(request, "encyclopedia/new.html")



def edit(request, title):

    content = util.get_entry(title)

    if request.method == "POST":

        util.save_entry(request.POST["title"], request.POST["content"])

        return HttpResponseRedirect(reverse("entry", args= [title]))

    return render(request, "encyclopedia/edit.html", {
        "content": content,
        "title": title
    })



def rndm(request):

    list = util.list_entries()

    x = random.randint(0, len(list) - 1)

    return HttpResponseRedirect(reverse("entry", args= [list[x]]))





