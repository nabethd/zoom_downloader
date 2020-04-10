import requests


##########           STEP 1          ####################
#put your URL here
request_url = '    '

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Accept-Language': 'en-US,en;q=0.9,he;q=0.8',
    'Connection': 'keep-alive',

##########           STEP 2          ####################
    #put the new Cookie here
    'Cookie': '    ',

    'Host': 'ssrweb.zoom.us',
    'Range': 'bytes=0-50',
    'Referer': 'https://zoom.us/',
    'Sec-Fetch-Dest': 'video',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',

##########           STEP 3          ####################
    #change the 'User-Agent' to match your computer
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
 }

r = requests.get(request_url, headers=headers)
size = int(r.headers['Content-Range'].rpartition('/')[-1])                      ## get the size of the video from the headers

##########           STEP 4          ####################
# change the destination location to the place you want the file on your computer
# and make sure to change the file name.
# don't change the mp4 format

with open('c:/users/dnabeth/Desktop/recording/Introduction_to_code-motion_refactoring_lecture3.mp4', 'wb') as f:
    start = 0
    chunk_size = 100000000
    received = 0
    while received < size:
        # get content and write to file
        headers['Range'] = f'bytes={start}-{min(size, start + chunk_size - 1)}'
        r = requests.get(request_url, headers=headers)
        f.write(r.content)
        print(f"Received: {r.headers['content-range']}")
        start += chunk_size
print()
