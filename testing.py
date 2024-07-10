import unittest
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
from Gempa import load_data, create_map, get_options

class TestMainFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    
        # Load sample data or set up any necessary resources
        cls.csv_file = "gempagempigisel.csv"
        cls.df = load_data(cls.csv_file)
    
    def test_load_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertEqual(set(self.df.columns), {"tanggal", "waktu", "latitude", "longitude", "kedalaman", "magnitudo", "daerah"})
    
    def test_create_map(self):
        m = create_map()
        self.assertIsInstance(m, leafmap.Map)
    
    def test_get_options(self):
        options = get_options(self.df)
        expected_options = np.append(self.df['daerah'].unique(), ['Tampilkan Semua'])
        np.testing.assert_array_equal(options, expected_options)

if __name__ == "__main__":
    unittest.main()
