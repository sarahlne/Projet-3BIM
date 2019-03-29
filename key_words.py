from Bio import Entrez

#Entrez.email = 'your_email@provider.com'

pmids = [26278534]
handle = Entrez.efetch(db="pubmed", id=','.join(map(str, pmids)),
                       rettype="xml", retmode="text")
records = Entrez.read(handle)
key = [pubmed_article['MedlineCitation']['KeywordList'][0]
             for pubmed_article in records['PubmedArticle']]
print(key)
for i in range(len(key[0])):
    print(key[0][i])


#abstract_dict = dict(zip(pmids, abstracts))

#print(abstract_dict)