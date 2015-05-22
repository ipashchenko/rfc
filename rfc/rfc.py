import urllib2
import BeautifulSoup


if __name__ == '__main__':
    rfc_url = "http://astrogeo.org/vlbi/solutions/rfc_2015b/rfc_2015b_cat.html"
    request = urllib2.Request(rfc_url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup.BeautifulSoup(response)

    for a in soup.findAll('a'):
        if '_S_' in a['href'] and 'vis.fits' in a['href']:
            print a['href']
