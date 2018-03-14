import os

from restfulpy_boilerplate import restfulpy_boilerplate

restfulpy_boilerplate.configure()
restfulpy_boilerplate.initialize_models()


verbs = [
    'GET',
    'HEAD',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS',
    'METADATA',
    'LOGIN'
]

http_headers = [
    'X-Pagination-Count',
    'X-Pagination-Take',
    'X-Pagination-Skip',
    'X-Identity',
    'X-New-JWT-Token',
    'ETag',
    'X-Reason'
]


def cross_origin_helper_app(environ, start_response):

    def better_start_response(status, headers):
        headers.append(('Access-Control-Allow-Origin', os.environ.get('TRUSTED_HOSTS', '*')))
        headers.append(('Access-Control-Allow-Headers', 'Content-Type, Authorization'))
        headers.append(('Access-Control-Allow-Credentials', 'true'))
        headers.append(('Access-Control-Allow-Methods', ', '.join(verbs)))
        headers.append(('Access-Control-Expose-Headers', ', '.join(http_headers)))
        start_response(status, headers)

    return restfulpy_boilerplate(environ, better_start_response)


app = cross_origin_helper_app
