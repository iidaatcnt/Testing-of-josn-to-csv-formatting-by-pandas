import unittest

import formater_001

class GetpqTest(unittest.TestCase):

    @unittest.skip('skip!')
    def test_get_header(self):
        getqb =  formater_001.Getqb('input/sample.json')
        self.assertEqual(getqb.get_header(),'Age,College,Exp,Hash,Player,Pos,WT')

    def test_write_to_csv(self):
        getqb =  formater_001.Getqb('input/sample.json')
        self.assertEqual(getqb.write_to_csv(),'input/sample.json')

if __name__ == '__main__':
    unittest.main()