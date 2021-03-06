""" SQL Injection Checker """

from massweb.vuln_checks.match import match_strings
from massweb.vuln_checks.check import Check

class SQLICheck(Check):
    """ SQL Injection Checker: Checks for evidence of successful SQL injection in result from fuzzers."""
    #FIXME: Add breif description of the attack

    def __init__(self):
        """ Initialize the object and normalize the strings used to check for
            vulnerability in the response """
        vuln_strings_raw = ["you have an error in your sql syntax",
            "supplied argument is not a valid mysql",
            "[microsoft][odbc microsoft acess driver]",
            "[microsoft][odbc sql server driver]",
            "microsoft ole db provider for odbc drivers",
            "java.sql.sqlexception: syntax error or access violation",
            "postgresql query failed: error: parser:",
            "db2 sql error:",
            "dynamic sql error",
            "sybase message:",
            "ora-01756: quoted string not properly terminated",
            "ora-00933: sql command not properly ended",
            "pls-00306: wrong number or types",
            "incorrect syntax near",
            "unclosed quotation mark before",
            "syntax error containing the varchar value",
            "ora-01722: invalid number",
            "ora-01858: a non-numeric character was found where a numeric was expected",
            "ora-00920: invalid relational operator",
            "ora-00920: missing right parenthesis"]
        self.vuln_strings = [x.lower() for x in vuln_strings_raw]

    def check(self, content):
        """ Check the string returned by the fuzzer (content) against the list
            of strings indicating vulnerability. """
        content = content.lower()
        return match_strings(content, self.vuln_strings)
