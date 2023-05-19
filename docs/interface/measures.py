"""
Module measures.py
"""
import requests
import pandas as pd


class Measures:
    """

    """

    def __int__(self):
        """
        The constructor

        :return:
        """

        self.endpoint = 'http://environment.data.gov.uk/water-quality'

    @staticmethod
    def __read(url):
        """

        :param url:
        :return:
        """

        response = requests.get(url=url, timeout=10)

        try:
            if response.status_code == 200:
                frame = pd.read_csv(filepath_or_buffer=url)
            else:
                frame = pd.DataFrame()
        except RuntimeError as err:
            raise Exception(err)

        return frame

    def exc(self, ):
        """

        :return:
        """
