'''
Created on May 4, 2015

@author: prateek.jain
'''
import codecs
import csv
import pickle
from urlparse import urlparse

import tldextract

from dmoz_fileparser import parse_dmoz_xml_file


crawled_file_path = '/Users/prateek.jain/work/python-workspace/webcrawler/dmoz_response.csv'
unknown_file_path = '/Users/prateek.jain/work/python-workspace/webcrawler/not_in_dmoz_website.csv'
dmoz_classified_path = '/Users/prateek.jain/work/python-workspace/webcrawler/dmoz_classification.csv'




crawled_file_object = open(crawled_file_path)
dmoz_classified_file_object = codecs.open(dmoz_classified_path,'w','utf8')
wr = csv.writer(dmoz_classified_file_object, dialect='excel')
unknown_file_object = codecs.open(unknown_file_path,'w','utf8')
wr1 = csv.writer(unknown_file_object, dialect='excel')
#csv_reader_file = codecs.open(crawled_file_object,'r','utf8')
#, encoding='utf-8'


def parse_crawled_file(url_classification_dict):
    with codecs.open(crawled_file_path, 'r') as csvfile:
        dmoz_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in dmoz_file_reader:
            categories = {}
            webpage = row[0]
            webpage = webpage.replace('www.','')
            webpage = webpage.replace('WWW.','')
            webpage = webpage.replace('http://','')
            webpage = webpage.replace('https://','')
            if webpage[-1:]=='/':
                webpage = webpage[:-1]
            
            print webpage
            if webpage in url_classification_dict:
                categories = url_classification_dict[webpage]
                category_list = list(categories)
                row = row+category_list
                row_encoded=[]
                for s in row:
                    print s+','+str(type(s))
                    try:
                        s = unicode(s.strip(codecs.BOM_UTF8), 'utf-8')
                    except UnicodeDecodeError:
                        s = ''
                    #s = s.decode('ascii','ignore').encode('utf8','ignore')
                    row_encoded.append(s)
                #wr1.writerow(row_encoded)
                wr.writerow([unicode(s.strip()).encode("ascii",'ignore') for s in row_encoded])
                #dmoz_classified_file_object.write(row+',"'+str(categories)+'"\n')
            else:
                extracted = tldextract.extract(webpage)
                hostname = "{}.{}".format(extracted.domain, extracted.suffix)
                if hostname in url_classification_dict:
                    categories = url_classification_dict[hostname]
                    category_list = []
                    for category in categories:
                        category_list.append(category.encode('utf8','ignore'))
                    #category_list = list(categories)
                    row = row+category_list
                    row_encoded=[]
                    for s in row:
                        print s+','+str(type(s))
                        try:
                            s = s.encode('utf-8','ignore')
                        except UnicodeDecodeError:
                            s = ''
                    #s = s.decode('ascii','ignore').encode('utf8','ignore')
                        row_encoded.append(s)
                    wr.writerow([unicode(s.strip()).encode("ascii",'ignore') for s in row_encoded])
                else:
                    row_encoded=[]
                    for s in row:
                        row_encoded.append(s.decode("ascii",'ignore'))
                        
                    string_len_check = ''.join(row_encoded)
                    if len(string_len_check.strip())>0:
                        wr1.writerow([unicode(s.strip()).encode("ascii",'ignore') for s in row_encoded])
    dmoz_classified_file_object.flush()
    unknown_file_object.flush()
    dmoz_classified_file_object.close()
    unknown_file_object.close()
    

if __name__ == '__main__':
    #url_classification_dict = parse_dmoz_xml_file()
    url_classification_dict = pickle.load( open( "dmoz_dict.p", "rb" ) )
    parse_crawled_file(url_classification_dict)