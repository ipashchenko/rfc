import urllib2
import posixpath


# http://stackoverflow.com/questions/7894384/python-get-url-path-sections
# by Iwan Aucamp
def parse_path(path_string, normalize=True):
    result = []
    if normalize:
        tmp = posixpath.normpath(path_string)
    else:
        tmp = path_string
    while tmp != "/":
        (tmp, item) = posixpath.split(tmp)
        result.insert(0, item)
    return result


def parse_url_path(url, normalize=True):
    url_parsed = urllib2.urlparse.urlparse(url)
    path_parsed = parse_path(urllib2.unquote(url_parsed.path),
                             normalize=normalize)
    return path_parsed
