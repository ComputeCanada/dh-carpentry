# Twitter Scraper Install in CC Cloud

The tool we will be installing is called **twarc** and is maintained on GitHub at [https://github.com/edsu/twarc](https://github.com/edsu/twarc).  If you would like additional help then There are instructions there to supplement the twarc configuration that is shared here.

## Part 1: Setting up the VM

1. Launch an instance from the OpenStack dashboard, Horizon, with the following specs from the instance panel, details tab:

	* Availability Zone: nova (just leave this as the default)
	* Instance Name: Make up something that you can remember
	* Flavor: p2-1.5gb
	* Instance Count: 1
	* Instance Boot Source: Boot from image (creates a new volume)
	* Image Name: Ubuntu_14.04...
	* Device Size (GB): 10
	* Device Name: vda

2. From the Access & Security tab setup a key pair.
3. From the Networking tab make sure at least one internal network is associated.
4. Associate a floating IP using the dropdown menu on the instance panel.
5. Change the name of the attached volume to something meaningful from the Volumes panel.
6. Set the security group rules to allow ssh in the Access & Security panel. 
7. Log in via ssh and do the appropriate updates to the OS from the VM command line:

	```
	$ ssh -i <<path to your private key here>> ubuntu@<<Your IP Address here>>
	$ sudo apt-get update
	$ sudo apt-get -y upgrade
	$ sudo reboot
	```

## Part 2: Install twarc
twarc is the tool that will be used to collect tweets from the Twitter API.

1. Log back in to the VM (the reboot done after the update would have closed the connection) and Install pip (The Python package installer) from the VM command line: 
	
	```
	$ ssh -i <<path to your private key here>> ubuntu@<<Your IP Address here>>
	$ sudo apt-get install python-pip
	```

2. Install twarc:

	```
	$ sudo pip install twarc
	```

3. Register the app with Twitter: [http://apps.twitter.com](http://apps.twitter.com)
4. When the app is registered go to the "Keys and Access Tokens" tab and generate an access token.  Once this is done note the following:
	* Consumer Key (e.g. 6q3avm7iWk9YqGKzWAYWuDJIq)
	* Consumer Secret (e.g. hHReWGbOfnYazHlOkJeInR13k1adqRumHaInnVth0on7qJ31LN)
	* Access Token (e.g. 567223483-Ew5zX3w4N3t9Cv6YFx1rfgIk4Wkj1r9PzwYPeWKk)
	* Access Secret (e.g. LtOtuTNsjQrIlwqLibBRaC0z6WSgkd0Kw0WKD3Mr4mCFH)
5. Under the "Permissions" tab set the access to "Read only".
6. Return to your terminal and run ```twarc.py```.  On the first run the tool will ask for the keys and secrets generated in step 8.  Copying and pasting these directly from the twitter page is the best way to pass these.

	>NOTE: Doing step 6 will produce an error.  The tool is complaining because it doesn't have enough information to actually run a scrape.  This is fine because all we care about it is having the tool generate a ```.twarc``` file in the home directory and save the keys to that file in the correct format.

	```
	$ twarc.py
	```

7. Test the service: 

	```
	$ twarc.py --search ponies
	```
	Which will return something like:
	
	```
	{"contributors": null, "truncated": false, "text": "@AndreaLibman Perhaps see if @buildabear still has some ponies left?", "is_quote_status": false, "in_reply_to_status_id": 669565796805246976, "id": 669611796609765376, "favorite_count": 0, "source": "<a href=\"https://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android Tablets</a>", "retweeted": false, "coordinates": null, "entities": {"symbols": [], "user_mentions": [{"id": 392460743, "indices": [0, 13], "id_str": "392460743", "screen_name": "AndreaLibman", "name": "Andrea Libman"}, {"id": 14997308, "indices": [29, 40], "id_str": "14997308", "screen_name": "buildabear", "name": "Build-A-BearWorkshop"}], "hashtags": [], "urls": []}, "in_reply_to_screen_name": "AndreaLibman", "in_reply_to_user_id": 392460743, "retweet_count": 0, "id_str": "669611796609765376", "favorited": false, "user": {"follow_request_sent": false, "has_extended_profile": false, "profile_use_background_image": true, "default_profile_image": false, "id": 4020151696, "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", "verified": false, "profile_text_color": "333333", "profile_image_url_https": "https://pbs.twimg.com/profile_images/657332685623435265/uuBKjqeY_normal.jpg", "profile_sidebar_fill_color": "DDEEF6", "entities": {"description": {"urls": []}}, "followers_count": 277, "profile_sidebar_border_color": "C0DEED", "id_str": "4020151696", "profile_background_color": "C0DEED", "listed_count": 4, "is_translation_enabled": false, "utc_offset": null, "statuses_count": 719, "description": "I live in Elkhart, IN, with my brother. I draw fan art, and aspire to be a professional comic artist.", "friends_count": 892, "location": "", "profile_link_color": "0084B4", "profile_image_url": "http://pbs.twimg.com/profile_images/657332685623435265/uuBKjqeY_normal.jpg", "following": false, "geo_enabled": false, "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "screen_name": "crowew1978", "lang": "en", "profile_background_tile": false, "favourites_count": 55, "name": "William Crowe", "notifications": false, "url": null, "created_at": "Thu Oct 22 22:59:54 +0000 2015", "contributors_enabled": false, "time_zone": null, "protected": false, "default_profile": true, "is_translator": false}, "geo": null, "in_reply_to_user_id_str": "392460743", "lang": "en", "created_at": "Wed Nov 25 20:21:07 +0000 2015", "in_reply_to_status_id_str": "669565796805246976", "place": null, "metadata": {"iso_language_code": "en", "result_type": "recent"}} <<ETCETERA>>
	```

	>What matters here is seeing a stream of information come back from Twitter.  Rather than watch it all run the download process can be interrupted without consequence by holding the Control key and pressing "C".

## Part 3: Running twarc as a service
This will set the system to run twarc at regular intervals, stripping duplicate entries, and storing the output chronologically.  We will install a package of scripts from GitHub called ArchiveTools to help with this process. ArchiveTools requires Python 3, which is installed by default in Ubuntu 14.  If you are using another OS you may need to install Python 3 separately.

1. Create a new directory and move into it:

	```
	$ mkdir DH_Scrape
	$ cd DH_Scrape
	```

2. Create a directory to hold the tweets: 

	```
	$ mkdir tweets
	```

3. Create a directory to hold the specific collection of tweets:

	```
	$ mkdir tweets/DH2016
	```

4. Install Git and get ArchiveTools: 

	```
	$ sudo apt-get git
	$ git clone https://github.com/recrm/ArchiveTools
	```
`
5. Copy `json-extractor.py` from the `ArchiveTools` folder into the `tweets` folder:

	```
	$ cp ArchiveTools/json-extractor.py tweets/
	```

6. Create a script named **DH_Scrape.sh** with the following content:

	```
	#! /usr/bin/bash

	#Note: sometimes twarc changes the names of the commands or their
	#locations. If you get an error that says the command isn't found
	#then read their github page to find the file name.  Once you know
	#the file name you can then use 'which file_name_you_found' to get 	#the location.  Change the bin value here to match this.
	bin=/usr/local/bin/twarc-archive.py

	output=/home/ubuntu/DH_scrape/tweets

	$bin \#DH2016 $output/DH2016

	myFilename="tweets/DH2016/"`date +%Y%m%d%H%M%S`"-DH2016"

	python3 tweets/json-extractor.py -path tweets/DH2016 -compress -output 	$myFilename -id id_str text id created_at id_str
	```
7. Test this script and do any necessary corrections due to errors that arise.  From the directory the script is in run:

	```
	$ bash DH_Scrape.sh
	```


8. Create a cron job to run this script twice a week.
	* Open the cron editor (If this is the first time you have run the tool it will ask you which editor to use. If you are unsure then `nano` is a generally friendly option): 
		
		```
		$ crontab -e
		```
	* Add the following lines to the bottom of the editor:
  
	```
	#This line will set the DH Twitter scraper to run at midnight every Sunday and Wednesday
	0 0 * * 0,3 bash /home/ubuntu/DH_scrape/DH_Scrape.sh
	```
9. Transfer the tweet data from your cloud machine to your home machine in whatever directory you are currently working in:

	```
	$ exit
	
	logout
	Connection to 206.167.180.229 closed.
	
	$ scp -r -i <<path to your private key here>> ubuntu@<<Your IP Address here>>:~/DH_Scrape/tweets/DH2016 . 
	
	archive.log                                   100% 4788     4.7KB/s   00:00    
	tweets-0001.json                              100%  396KB 396.4KB/s   00:00    
	20160308163459-DH2016.json                    100%  396KB 396.4KB/s   00:01 
	```
