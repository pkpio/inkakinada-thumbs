#!/usr/bin/env python

# Developer:	Praveen Kumar Pendyala
# Created:	22/07/2014
# 
# bomb your review with lots of thumbs ups.
#
# Note: This is created just to show how simple getting thumbs up for reviews
#	on this site is. Well, most of the thumbs ups are tampered, mostly by
#	brute-force, not authentic and misleading to end user.
#
#
# Usage:
#	1. Open the reviews page.
#	2. Pick a review.
#	3. Right click on thumbs up/down icon
#	4. Copy link address
#	5. Place it in the thumb_url variable below
#
# Note: Single quotes around the url in thumb_url should be there
#
#

import urllib
import time

#parameters
thumb_url = 'http://www.inkakinada.com/list/thumbprint/city-online-services-limited?review_id=7906&value=1'
thumbs_count = 10

start = time.time()

for i in range(thumbs_count):
	urllib.urlopen(thumb_url);
	print 'Thumbs added: ' + str(i+1);

time = time.time() - start

print 'took: ' + repr(time) + 'seconds!'
