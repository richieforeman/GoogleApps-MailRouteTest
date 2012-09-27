__author__ = 'Richie Foreman <richie.foreman@gmail.com>'

import telnetlib
import settings

class MailTest(telnetlib.Telnet):

    @staticmethod
    def get_instance():
        telnet = MailTest(host=settings.HOST,
                          port=settings.PORT)
        print "\t<< %s " % telnet.read_some().strip()
        return telnet

    def write_line(self, l, read=True):
        print "\t>> %s" % l
        self.write("%s\r\n" % l)
        if read:
            r = self.read_some().strip()
            print "\t<< %s" % r
            return r

    def send_test_message(self, to_email, from_email, body="Test Message"):
        self.write_line("HELO")
        self.write_line("MAIL FROM: <%s>" % from_email)
        self.write_line("RCPT TO: <%s>" % to_email)
        self.write_line("DATA")
        self.write_line(body, read=False)
        if "OK" in self.write_line("."):
            return True
        else:
            raise Exception
