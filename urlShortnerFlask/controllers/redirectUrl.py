from flask import Flask, Response, request, jsonify
from controllers.slugGenerator import generate_code


def create_short_url(long_url):
    slug = generate_code()     # create new slug for our short url 
    
    # giving the url to android and ios untill we change it later 
    android_primary = long_url
    android_fallback = long_url
    ios_primary = long_url
    ios_fallback = long_url
    
    # web entry 
    web = long_url
    
    # now we can zip all of this into json request to be posted in our db 
    payload = {
        "slug" : slug,
        "android": {
        "fallback": android_fallback,
        "primary": android_primary
    },
    "ios": {
        "fallback": ios_fallback,
        "primary": ios_primary
    },
    "web": web
    }
    return payload
    
