__author__ = 'Richie Foreman <richie.foreman@gmail.com>'

import sys
import telnetlib
import settings
from MailTest import MailTest

def test_google_to_google():
    print "Sending a test message from Google User (%s) to Google User (%s)" % (settings.GOOGLE_USER_1,
                                                                                settings.GOOGLE_USER_2)

    telnet = MailTest.get_instance()
    ret = telnet.send_test_message(to_email=settings.GOOGLE_USER_2,
                                   from_email=settings.GOOGLE_USER_1)

    telnet.close()
    return ret

def test_eagerlegacyuser_to_registeredlegacy():
    print "Sending a test message from Eager to be a Googler Registered Legacy User (%s (in Google)) to Registered Legacy User (%s)" % (settings.REGISTERED_LEGACY_USER_1,
                                                                                                                                        settings.REGISTERED_LEGACY_USER_2)
    telnet = MailTest.get_instance()
    ret = telnet.send_test_message(to_email=settings.REGISTERED_LEGACY_USER_2,
                                   from_email=settings.REGISTERED_LEGACY_USER_1)
    telnet.close()
    return ret

def test_eagerlegacyuser_to_unregisteredlegacy():
    print "Sending a test message from Eager to be a Googler Registered Legacy User (%s (in Google)) to UnRegistered Legacy User (%s)" % (settings.REGISTERED_LEGACY_USER_1, settings.UNREGISTERED_LEGACY_USER)

    telnet = MailTest.get_instance()
    ret = telnet.send_test_message(to_email=settings.UNREGISTERED_LEGACY_USER,
                                   from_email=settings.REGISTERED_LEGACY_USER_1)
    telnet.close()
    return ret

def test_eagerlegacyuser_to_google():
    print "Sending a test message from Eager to be a Googler Registered Legacy User (%s (in Google)) to Google User (%s)" % (settings.REGISTERED_LEGACY_USER_1, settings.GOOGLE_USER_1)

    telnet = MailTest.get_instance()
    ret = telnet.send_test_message(to_email=settings.GOOGLE_USER_1,
                                   from_email=settings.REGISTERED_LEGACY_USER_1)
    telnet.close()
    return ret


def test_google_to_registeredlegacy():

    print "Sending a test message from Google User (%s) to Registered Legacy User (%s)" % (settings.GOOGLE_USER_1,
                                                                                           settings.REGISTERED_LEGACY_USER_1)
    telnet = MailTest.get_instance()
    ret = telnet.send_test_message(to_email=settings.REGISTERED_LEGACY_USER_1,
                                   from_email=settings.GOOGLE_USER_1)
    telnet.close()
    return ret


def test_google_to_unregisteredlegacy():
    print "Sending a test message from Google User (%s) to UnRegistered Legacy User (%s)" % (settings.GOOGLE_USER_1,
                                                                                             settings.UNREGISTERED_LEGACY_USER)

    telnet = MailTest.get_instance()
    ret = telnet.send_test_message(to_email=settings.UNREGISTERED_LEGACY_USER,
                                   from_email=settings.GOOGLE_USER_1)

    telnet.close()
    return ret

def main():

    print "Google Mail Routing Test Suite!"
    raw_input("Press any key to continue...")
    tests = [test_google_to_google,
             test_google_to_registeredlegacy,
             test_google_to_unregisteredlegacy,
             test_eagerlegacyuser_to_google,
             test_eagerlegacyuser_to_registeredlegacy,
             test_eagerlegacyuser_to_unregisteredlegacy]

    for test in tests:
        try:
            if test():
                print "Test OK!"
            else:
                print "Test Failed!"
        except Exception, e:
            print e
            print "TEST BLEW UP"
        raw_input("Press any key to continue...")

    print "fin!"

if __name__ == "__main__":
    main()