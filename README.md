# CryptoPY

CryptoPY is a basic script that compares five cryptocurrencies (for now), those are BTC, ETH, XRP, XMR and USDT.
Amongst all the functionalities of the script, there are two key ones, the **alert system** (currently being developed) and **monitoring prices for x seconds**, with the last one you are able to check the prices for the seconds you want to, you can even run the script all day long, so in case the price drops beyond the limit you have stipulated, you get an email.

## Getting Started
You can fork the repository and then clone it to a folder you want. The steps are simple:
- Fork the repository as you can see in this image.
![Forking a repository](https://help.github.com/assets/images/help/repository/fork_button.jpg)
- Once the repository is forked, you can go to your new forked repository and clone it.
![Cloning a repository](https://help.github.com/assets/images/help/repository/clone-repo-clone-url-button.png)
![Clone repository with HTTPS](https://help.github.com/assets/images/help/repository/https-url-clone.png)
- Once you got the link in the https clone tab, all you have to do is go to a terminal, and type git clone *url* in the folder you want the repository to get cloned.
- Once you did this, you got the repository ready to work!

### Prerequisites
This project needs a couple of prerequisites, they are listed below and it is explained how to install them so the script runs well.

- Python 3. You can get it [here.](https://www.python.org/downloads/)
- Termcolor. This prerequisite is used to color the python shell. You can install it by typing one of these commands:
```
pip install termcolor
```
```
pip3 install termcolor
```

### Installing
The installation is fairly simple, all you have to do is execute the python script, typing the following code:
```
python crypto.py
```
```
python3 crypto.py
```
Once you do this, a menu will pop up, asking what do you want to do, there are 4 different options.
- Option 1 (**Check current prices**): This option provides the current prices for the cryptocurrencies listed above.
![Current prices](https://raw.githubusercontent.com/romeuu/cryptopy/doc/docs/1.gif)
- Option 2 (**Setup an alert**): It sets an alert so when the price drops or gets to the price you have indicated in the alert, an email is sent.  
![Alert](https://raw.githubusercontent.com/romeuu/cryptopy/doc/docs/2.gif)
- Option 3 (**Check prices for x seconds**): This option gives you the hability to check the prices for the cryptos for the time you want (in seconds). So you are able to run it autopilot if you wish to, for instance, you can put a day in seconds and it will work. Furthermore, this option will check the variances (increments and decreasements).  
![Check prices for seconds](https://raw.githubusercontent.com/romeuu/cryptopy/doc/docs/3.gif)
- Option 4 (**Simulate trading**): This is a safe environment to test out trading strategies, or just to try to trade in a safe environment before trading with real money.  
![Trading environment](https://raw.githubusercontent.com/romeuu/cryptopy/doc/docs/4.gif)  
As you can see, there are a list of arguments you have to give to the script so it runs well:
    + **Crytpo you are going to trade.**
    + **Price where you want to sell and buy.**
    + **Starting amount of crypto.**
    + **Starting money you have destinated to buy crytpo.**
    + **How much you want to sell each time the script enters in selling mode.**
    + **How much money you want to spend when the script enters in buying mode.**

## License
The license as listed in the [LICENSE.md](./LICENSE.md) is a CC-BY-NC-SA-3.0 license. Here it is what you can do with this project:
- Share the project.
- Modify the project, so you can contribute to it.
What you can't do is:
- List the work as yours, you have to give the author recognition.
- You can't use this project for commercial purposes.
- If you want to share the project you have to do it under the same license. (CC-BY-NC-SA-3.0)

## Contributions
You are free to modify the repository by any means, all you have to do is fork it and then submit a pull request. I will review it and merge it if it's neccesary.
Feel free to submit anything! Thank you!

## Author
This project has been developed by **Sergio Romeu**, a web dev from Spain.

## Acknowledgments
- Thanks to nomics for providing me access to the API.