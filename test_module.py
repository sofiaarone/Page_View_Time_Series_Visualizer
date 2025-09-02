# unit tests to make sure our visualizations return a valid matplotlib figure
import unittest
import time_series_visualizer as tsv
import matplotlib as mpl

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_line_plot(self):
        fig = tsv.draw_line_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)

    def test_bar_plot(self):
        fig = tsv.draw_bar_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)

    def test_box_plot(self):
        fig = tsv.draw_box_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)

if __name__ == "__main__":
    unittest.main()