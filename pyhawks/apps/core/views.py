from django.shortcuts import render, HttpResponse


def letsencrypt1(request):
    return HttpResponse(
        'q6hRTs6iOXlgVgI94gUxh1qTLMuhf7SMm7Zo59Lwwzg.XwnczyaCPkwyyhUn0Hyko_vPtjZBq31fIKmZHsCJqu0',
        content_type='text/plain'
    )


def letsencrypt2(request):
    return HttpResponse(
        '1qMP4xHZjjjQuwiU8Bjz0-bnsdmsv7VSHPmG8r3ij04.XwnczyaCPkwyyhUn0Hyko_vPtjZBq31fIKmZHsCJqu0',
        content_type='text/plain'
    )

