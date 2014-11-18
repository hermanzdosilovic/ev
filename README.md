ev
==

Smart tool for task testing in Competitive Programming.

Tutorial - How to use it?
-------------------------
_ev_ is a smart script can do a lot for you. To give you idea of how it works I prepared a short tutorial for you. I really recommend you to go thru this tutorial.

###Get the tutorial

1. You need to install _ev_. Follow [install instructions](https://github.com/hermanzdosilovic/ev#how-to-install-and-get-updates).
2. In your _ev_ project folder open `tutorial` folder.
3. Open `start.txt` file and follow instructions.

How to install and get updates
------------------------------

Basic idea of instalation is being able to run _ev_ in every directory from your terminal.
So basicly you need to copy or link `ev` script in some directory that is in your `$PATH` environmental variable, for example `/usr/local/bin/`.

###Install

Choose any directory in which you will keep this project. In that directory execute these commands: 
	
	$ git clone git@github.com:hermanzdosilovic/ev.git
	$ cd ev
	$ sudo chmod +x ev
	$ sudo ln -s $(pwd)/ev /usr/local/bin/ev

###Get updates
	
In _ev_ project directory execute this command:
	
	$ git pull origin master
		

How to run
----------
You always run _ev_ the same way.
	
	$ ev
	
And that is the beauty of it. Enjoy :)

Testing _ev_ on your machine
----------------------------
If you want to be 100% sure that _ev_ works on your machine you can run tests for it. Follow these instructions to test _ev_:

1. You need to install _ev_. Follow [install instructions](https://github.com/hermanzdosilovic/ev#how-to-install-and-get-updates).
2. In your _ev_ project open `test` folder in terminal.
3. Start script `start.sh`:
	
		$ sudo chmod +x start.sh
		$ ./start.sh

If all tests passed you should see folowing output:
	
	- run-file -
	PASSED
	 - wa-leave -
	PASSED
	- space in py or rb name -
	PASSED
	- space in c name -
	PASSED

If some of the tests failed, please contact me so we can make _ev_ better. :)
 

Contributing
------------
1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

License
-------
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
