import urllib.request
import urllib.error

urls = ['http://127.0.0.1:5000/', 'http://127.0.0.1:5000/ping', 'http://127.0.0.1:5000/data.json']
for u in urls:
    print('---', u)
    try:
        with urllib.request.urlopen(u, timeout=5) as r:
            b = r.read()
            print('status:', r.getcode())
            print('len:', len(b))
            print(b.decode('utf-8', errors='replace')[:1000])
    except Exception as e:
        print('ERROR', e)
