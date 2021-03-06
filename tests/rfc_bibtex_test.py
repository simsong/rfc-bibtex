import unittest

from rfc_bibtex.rfc_bibtex import RFCBibtex
from rfc_bibtex.exceptions import BadRFCNumberException

class TestRFCMethods(unittest.TestCase):
    def test_re(self):
        self.assertTrue(RFCBibtex.LATEX_CITATION_RE.search(r"\citation{RFC32}"))
        self.assertTrue(RFCBibtex.LATEX_CITATION_RE.search(r"\citation{draft-tls-nothing}"))
        self.assertFalse(RFCBibtex.LATEX_CITATION_RE.search(r"\citation{nothing}"))

    def test_rfc_keyfunction(self):
        self.assertEqual(RFCBibtex._rfc_key_function("RFC32"), "RFC00032")
        self.assertEqual(RFCBibtex._rfc_key_function("draft-nothing"), "draft-nothing")
        try:
            self.assertEqual(RFCBibtex._rfc_key_function("RFC32a"), "RFC32a")
        except BadRFCNumberException:
            pass
        

if __name__=="__main__":
    unittest.main()
