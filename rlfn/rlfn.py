import requests

class Publication:

    def __init__(self, pmcid):
        self.pmcid = pmcid
        self.title = self.lookup_title()

    def lookup_title(self):
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id={}&retmode=json".format(self.pmcid)
        resp = requests.get(url)
        resp.raise_for_status()
        json_dict = resp.json()