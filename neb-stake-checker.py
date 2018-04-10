import filecmp
import json
import os
import smtplib
import subprocess

import config

NEB_MOST_RECENT_TRANSACTION_CMD = \
    "%s listtransactions | jq 'map(select(.category==\"generate\")) | sort_by(.time) | last(.[].amount)'" % config.NEB_WALLET_EXEC_PATH


class NeblioStakeChecker:

    def __fetch_most_recent_stake(self):
        return json.loads(subprocess.check_output(NEB_MOST_RECENT_TRANSACTION_CMD, shell=True).strip())

    def __write_most_recent_stake(self, filename, stake_amount):
        f = open(filename, 'w')
        f.write("%s" % stake_amount)
        f.close()

    def __send_email(self, subject, body, ):
        recipient = config.GMAIL_USERNAME

        headers = ["From: %s" % config.GMAIL_USERNAME,
                   "Subject: %s" % subject,
                   "To: %s" % recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)

        session.ehlo()
        session.starttls()
        session.ehlo

        session.login(config.GMAIL_USERNAME, config.GMAIL_PASSWORD)

        session.sendmail(config.GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + body)
        session.quit()

    def check(self):
        last_stake_amount = self.__fetch_most_recent_stake()
        print('Last stake amount: %s' % last_stake_amount)
        self.__write_most_recent_stake(config.NEB_CURRENT_STAKE_FILE, last_stake_amount)

        if not os.path.exists(config.NEB_PREVIOUS_STAKE_FILE):
            print('No previous neblio stake file found - first run?')
            self.__send_email("Neblio Stake Checker",
                              "Hi!\r\n\r\n"
                              "Neblio Stake Checker has been successfully configured!\r\n\r\n"
                              "Once you setup cron you will be emailed next time I detect you have hit a new stake.")

        else:
            if filecmp.cmp(config.NEB_CURRENT_STAKE_FILE, config.NEB_PREVIOUS_STAKE_FILE, False):
                print('No new stake')
            else:
                print('New stake received: %s (NEBL)' % last_stake_amount)
                subject = 'New NEBL stake notification'
                body = "Hi, You just received a new NEBL stake of: %s!" % last_stake_amount

                self.__send_email(subject, body)

        self.__write_most_recent_stake(config.NEB_PREVIOUS_STAKE_FILE, last_stake_amount)


neblio_stake_checker = NeblioStakeChecker()
neblio_stake_checker.check()
