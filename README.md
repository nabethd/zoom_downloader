# zoom_downloader

how to get the request URL, Cookie and all the other HEADERS:

step 1:   
open the URL of the recording in a new window, make sure to open with Google Chrome 

step 2:
click f12 or right click and then inspect (on mac its command+shift+I)
and go to the Network tab and then choose sub-tab media (next to img and font)

step 3:
click play on the video and skip the video a few minutes,
you should see under the Name tab a file name GMT_blah_blah_blah
click on it and its should open the headers section.

step 4:
under General you can see the 'Request URL', copy it to STEP 1 in the zoom_downloader.py

step 5:
under Request Headers you can find all of the other necessary headers.
copy the 'Cookie' to step 2 in the zoom_downloader.py,
copy 'User-Agent' to step 3 in the zoom_downloader.py,
and make sure that all other headers are the same (it may vary from computer to computer).
**(you don't need to add the missing headers, update only the one in zoom_downloader.py)

step 6:
change the location and name in step 4 in the zoom_downloader.py.

RUN and wait a few sec :)

you will get an error at the end because there is a problem getting the last bit of the video,
dont worry the video is fine. you can watch it
I will try to patch and fix it in the future. 

important note:
**the cookie change every couple of days so make sure to update it if necessary.
**all headers except the 'cookie' and 'request url' will stay the same. no need to change it again
**don't forget to change the name file every time
