# tweetscraper
Uses selenium to scrape a users tweets, filters out retweets too.

To store tweets in a sqlite format: `python getTweets.py <username>`
To get the raw data, move all of the .db files into a directory, and run `perl dumpTweets.pl <directory>` which will dump all tweets. You can pipe this into a file by adding ` > <file>` to the end of the previous command.

Dependencies: 
  * python `sqlite3` - for storing the results
  * python `selenium` - for automating the loading of pages
  * `geckodriver` - for driving firefox
  * perl `DBI` - for the perl script which exports the sqlite databases to 
