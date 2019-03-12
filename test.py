from Bio import Entrez

def search(query):
    Entrez.email = 'sarah-lne@outlook.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='30',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def article(ident):
	Entrez.email = 'sarah-lne@outlook.com'
	handle = Entrez.esummary(db = 'pubmed', id = ident)
	records = Entrez.read(handle)
	return records

def citation(pmid):
	Entrez.email = 'sarah-lne@outlook.com'
	handle = Entrez.elink(dbfrom="pubmed", db="pmc",
						LinkName="pubmed_pmc_refs", id=pmid)
	result = Entrez.read(handle)
	longueur = len(result[0]["LinkSetDb"])
	if longueur == 0:
		return -1
	else: 
		pubmed_ids = [link["Id"] for link in result[0]["LinkSetDb"][0]["Link"]]
		return pubmed_ids 

#print(citation(6387394))
print(search("baby without arms")['IdList'])
#print(citation("810668"))
#print(article(30496090))
#print(search("30496090"))
"""print(search("baby without arms"))
print(article("30496090")[0]['PubDate'])"""

"""for i in search("baby without arms")['IdList']:
	if(article(str(i))[0]['PubDate'] < "2016"):
		print(article(str(i))[0]['PubDate'])
		print(citation(i))"""

"""def info(query):
	Entrez.email = 'sarah-lne@outlook.com'
	handle = Entrez.einfo(db="pubmed")
	record = Entrez.read(handle)
	return record"""