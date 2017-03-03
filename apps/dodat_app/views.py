from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re, random

# multiple_replace from web.
def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

# Create your views here.
def index(request):
    return render(request, "dodat_app/index.html")

def search(request):
    if request.method == "POST":
        if len(request.POST['question']) == 0:
            messages.info(request, "You have to ask a question!")
            return redirect("/")
        else:
            dict = {
                "+" : "%2B",
                " " : "+",
                "!" : "%21",
                '"' : "%22",
                "#" : "%23",
                "$" : "%24",
                "%" : "%25",
                "&" : "%26",
                "'" : "%27",
                "(" : "%28",
                ")" : "%29",
                "*" : "%2A",
                "-" : "%2D",
                "." : "%2E",
                "/" : "%2F",
                ":" : "%3A",
                ";" : "%3B",
                "<" : "%3C",
                "=" : "%3D",
                ">" : "%3E",
                "?" : "%3F",
                "@" : "%40",
                "[" : "%5B",
                '\\' : "%5C",
                "]" : "%5D",
                "^" : "%5E",
                "_" : "%5F",
                "`" : "%60",
                "{" : "%7B",
                "|" : "%7C",
                "}" : "%7D",
                "~" : "%7E",
            }
            clueless = ""
            if(request.POST['search_button'] == "I'm feeling clueless"):
                clueless = "iie=1&"
            search_engine_choices = ['', 's=b&', 's=y&', 's=a&', 's=k&', 's=d&']
            search_string = multiple_replace(dict, request.POST['question'])

        return redirect("http://lmgtfy.com/?"+clueless+random.choice(search_engine_choices)+"q="+search_string+"")
    messages.info(request, "Please use the search box to search for something.")
    return redirect("/")
