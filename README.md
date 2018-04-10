
# Neblio Stake Checker for Google Mail

This project allows you to know get notified via Email (Google Mail) when your [Neblio](https://nebl.io) Wallet installed on a Raspberry Pi 
has earned a new stake.

<table width="60%" align="center" padding=0 margin=0>
    <tr>
        <td style="padding:0">
            <img src="https://github.com/mouserd/neblio-stake-checker-gmail/blob/master/assets/neblio-stake-checker-example-nofication.png" 
                title="Neblio Stake Checker" alt="Neblio Stake Checker" width="520" />
        </td>
    </tr>
</table>


## Pre-requisites

### Raspberry Pi
This project uses Python, so you will need to ensure that this is available on your Raspberry Pi.  This was 
tested on a Raspberry Pi Zero W running Raspbian Stretch which came pre-installed with Python 2.7.

In addition to Python, we also need a utility called [jq](https://stedolan.github.io/jq/) which is command-line tool for parsing and querying json:

```
sudo apt-get install jq
```


## Installation 

### Basic Setup

Once you have satisfied all of the [pre-requisites](#pre-requisites), simply copy both the `neb-stake-checker.py` and `config.py` scripts
to your `pi` users home directory (`/home/pi`).  Edit the `config.py` python script with the following:

1. Replace the value corresponding to `GMAIL_USERNAME` with your real gmail username/email address
2. Replace the value corresponding to `GMAIL_PASSWORD` with your real gmail password. *Note:* If your gmail account uses 2-Factor Authentication
    then see [Using with Google 2-Factor Authentication](#using-with-google-2-factor-authentication)

To test that your Neblio Stake Checker is working, start the main python script by running the Python script from your Raspberry Pi 
terminal/ssh session:

```
python /home/pi/neb-stake-checker.py
```

The first time this runs, if everything is setup correctly, you should receive a 
email to demonstrate that it has been configured correctly:

<table width="60%" align="center" padding=0 margin=0>
    <tr>
        <td style="padding:0">
            <img src="https://github.com/mouserd/neblio-stake-checker-gmail/blob/master/assets/neblio-stake-checker-setup-success.png" 
                title="Neblio Stake Checker" alt="Neblio Stake Checker" width="520" />
        </td>
    </tr>
</table>

### Using with Google 2-Factor Authentication

If your google account uses 2-Factor Authentication (2FA) then there is some additional steps required to ensure that the python script is
a trusted application.  To setup the trusted application you need to:

1. Log-in into Gmail with your account
2. Navigate to https://security.google.com/settings/security/apppasswords
3. In 'select app' choose 'custom', give it an arbitrary name and press generate, this will provide you with a unique 16 characters token
4. Replace the `GMAIL_PASSWORD` in the `config.py` with this 16 character token

### Automatic Scheduling

Once the Basic Setup is complete you can setup your Raspberry Pi to run automatically on a regular interval.  To do this we use a tool 
pre-installed on all Raspberry Pi's called cron and I have mine setup to check for new neblio stakes every 10 minutes.  
To setup cron run the following command in your Raspberry Pi terminal/ssh session:

```crontab -e```

In the resulting file, add the following to the bottom, making sure to leave a blank line at the end:
```
*/10 * * * * /usr/bin/python /home/pi/neb-stake-checker.py >> /var/log/neb-stake-checker.log 2>&1
```

Save and exit your cron (Ctrl+X if using nano).

Now all you need to do is sit back and wait to be notified of your next stake! :rocket:

## Donate / Tip :dollar:

:thumbsup: I hope you've found the **Neblio Stake Checker** useful!  If you'd like to donate or tip me to assist with the cost of building and maintaining 
this project then it would be much appreciated.

Neblio Address: ﻿`NbmG8tDpXVvjjac4UAmtsuitFAHf9YHcD3`

Ethereum Address: `0x6E644b360f314a50A8684a9E6676E13CbB702d1d` 

