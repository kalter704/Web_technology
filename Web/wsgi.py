def application(environ, start_response):
         
    output='Hello world<br/>'

    if environ['REQUEST_METHOD'] == 'POST':
        output += 'POST data: ' + (environ['wsgi.input'].read())

    if(environ['REQUEST_METHOD'] == 'GET'): 
        output +=  'GET data: ' + (environ['QUERY_STRING'])

    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output	
    #return "hqweello wsgi.py GET POST"
