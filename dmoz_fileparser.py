'''
Created on Apr 28, 2015

@author: prateek.jain
'''

ns = {'dmoz_rdf': 'http://dmoz.org/rdf/'}

file_to_write = ''
dmoz_content_file = ''


import xml.etree.ElementTree as ET




def get_classification_list(external_page):
    empty_set = set()
    for topic in external_page.findall('dmoz_rdf:topic', ns):
        topic_text = topic.text
        if topic_text not in empty_set:
            empty_set.add(topic_text)
    
    return empty_set





def parse_dmoz_xml_file():
    tree = ET.parse(dmoz_content_file)
    root = tree.getroot()
    url_classification_dict = {}
    for external_page in root.findall('dmoz_rdf:ExternalPage', ns):
        page_link = external_page.attrib
        url_string = page_link.get('about')
    
        new_topic_set = get_classification_list(external_page)
    
        if url_string in url_classification_dict:
            classification_set = url_classification_dict[url_string]
            classification_set = classification_set.union(new_topic_set)
        else:
            classification_set = new_topic_set
        url_classification_dict[url_string] = classification_set
    #if len(url_classification_dict) == 100:
    write_to_csv_file(url_classification_dict)
            #break


def write_to_csv_file(dmoz_dictionary):
    dmoz_csv_file_object = open(file_to_write,'w')
    for webpage in dmoz_dictionary:
        write_string = '"'+webpage+'",'
        classification_set = dmoz_dictionary[webpage]
        for topic in classification_set:
            write_string = write_string+'"'+topic+'",'
        write_string = write_string[:-1]+'\n'
        print write_string
        dmoz_csv_file_object.write(write_string.encode('utf8','ignore'))
    dmoz_csv_file_object.flush()
    dmoz_csv_file_object.close()
    
    
if __name__=='__main__':
    parse_dmoz_xml_file()