from django.shortcuts import render
import markdown2
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
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

        return render(request, "encyclopedia/entry.html", {
        "result": title,
        "title": entry
        })

    else:

        return render(request, "encyclopedia/error.html", {
            "error": "Entry not found"
        })





def search(request):


    search_term = request.GET.get("q", "").lower()

    entries = util.list_entries()

    list= []

    for word in entries:

        if search_term == word.lower():

            result = util.get_entry(word)

            return render(request, "encyclopedia/entry.html", {
            "result": markdown2.markdown(result),
            "title": word
        })

        elif search_term in word.lower():


            list.append(word)

    if list:


        return render(request, "encyclopedia/search.html", {
            "entries": list
        })




    return render(request, "encyclopedia/error.html", {
        "error": "Page not Found"
    })






def new(request):

    entries = util.list_entries()


    if request.method == "POST":

        title = request.POST["title"]

        if title in entries:

            return render(request, "encyclopedia/error.html", {
                "error": "Entry already exist"
            })


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





