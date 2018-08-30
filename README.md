#Install

If you don't have brew 
  To install Homebrew
  
  `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  
  The script will explain what changes it will make and prompt you before the installation begins. Once you’ve installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. You can do this by adding the following line at the bottom of your ~/.profile file

  export PATH=/usr/local/bin:/usr/local/sbin:$PATH
  
  
To install python

`brew install python`

To install selenium

`pip install selenium`

To install chorme driver

`brew cask install chromedriver`

Now you can run amazon task project

`python3 AmazonTest.py`
