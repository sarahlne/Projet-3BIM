from Bio import Entrez

def search(query): #Method use to launch a research on pubmed
    Entrez.email = 'sarah-lne@outlook.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='30',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def article(ident): #Method to get informations about a given article
	Entrez.email = 'sarah-lne@outlook.com'
	handle = Entrez.esummary(db = 'pubmed', id = ident)
	records = Entrez.read(handle)
	return records

def citation(pmid): #Method to get articles who cite the given article
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
	
def recup_abstract(pmids):  #Method to get the abstract of a given article
	Entrez.email = 'sarah-lne@outlook.com'
	handle = Entrez.efetch(db="pubmed", id=','.join(map(str, pmids)),
	                       rettype="xml", retmode="text")
	records = Entrez.read(handle)
	abstracts = [pubmed_article['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
	             for pubmed_article in records['PubmedArticle']]


	abstract_dict = dict(zip(pmids, abstracts))
	if(abstract_dict == {}):
		return "No abstract"
	else: 
		return abstract_dict

#print(citation(6387394))
#print(search("baby without arms")['IdList'])
#print(citation("810668"))
#print(article(30496090))
#print(search("30496090"))
#print(search("baby without arms"))
#print(article("30496090")[0]['PubDate'])

for i in search("directed evolution")['IdList']:
	if(article(str(i))[0]['PubDate'] < "2016" and article(str(i))[0]['HasAbstract']==1):
		print(i)
		print(article(str(i))[0]['PubDate'])
		print(article(str(i))[0]['Title'])
		print(recup_abstract([i]))
		print(citation(i))

"""def info(query):
	Entrez.email = 'sarah-lne@outlook.com'
	handle = Entrez.einfo(db="pubmed")
	record = Entrez.read(handle)
	return record"""
