from django.shortcuts import render, HttpResponse


def letsencrypt1(request):
    return HttpResponse(
        'ABp6xBPOOdxK4W8OMKiqLntaxZDxxnAoFIYHUNWnPag.XwnczyaCPkwyyhUn0Hyko_vPtjZBq31fIKmZHsCJqu0',
        content_type='text/plain'
    )


def letsencrypt2(request):
    return HttpResponse(
        'QvxfKr8WTh3PGyxDxTec_zSAHhiQchDSWeie23rMgwI.XwnczyaCPkwyyhUn0Hyko_vPtjZBq31fIKmZHsCJqu0',
        content_type='text/plain'
    )

