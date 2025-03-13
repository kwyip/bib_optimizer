import sys
import re
import bibtexparser
from bibtexparser.bwriter import BibTexWriter

def bib_cleaner(filename, input_bib, output_bib):
    with open(filename, 'r', encoding='utf-8') as file:
        filecontent = file.read()

    with open(input_bib, 'r', encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)

    allowed_keys = []
    all_keys = []
    temp_citations = set()
    
    for e in re.findall(r'\\cite[tp]?\{([^}]+)\}', filecontent):
        for c in e.split(','):  
            c = c.strip()
            if c not in temp_citations:
                all_keys.append(c)
                temp_citations.add(c)

    for k in all_keys:
        allowed_keys.append(k)



    entry_dict = {entry.get('ID'): entry for entry in bib_database.entries}


    filtered_entries = [entry_dict[key] for key in allowed_keys if key in entry_dict]

    writer = BibTexWriter()
    writer.indent = '    '  
    writer.order_entries_by = None  

    new_bib_database = bibtexparser.bibdatabase.BibDatabase()
    new_bib_database.entries = filtered_entries

    with open(output_bib, 'w', encoding='utf-8') as bibfile:
        bibfile.write(writer.write(new_bib_database))


if __name__=='__main__':
    if len(sys.argv[1:]) != 3:
        raise Exception("Sorry, please input three files: your tex filename, bib filename, and the desired new bib filename")
    tex = sys.argv[1:][0]
    old_bib = sys.argv[1:][1]
    new_bib = sys.argv[1:][2]

    bib_cleaner(tex, old_bib, new_bib)