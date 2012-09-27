__author__ = 'Richie Foreman <richie.foreman@gmail.com>'

from MailTest import MailTest

def main():
    more = "y"
    while True:
        to_email = raw_input("To: ")
        from_email = raw_input("From: ")
        telnet = MailTest.get_instance()
        ret = telnet.send_test_message(to_email=to_email,
                                       from_email=from_email)
        if ret:
            print "TEST OK"
        else:
            print "TEST FAILED"
        telnet.close()

        more = raw_input("\nRun Another (y/n)?: ").strip()
        if more == "n":
            break

if __name__ == "__main__":
    main()

