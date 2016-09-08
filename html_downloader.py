import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        print 'download begin'
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        print 'download success'
        return response.read()
