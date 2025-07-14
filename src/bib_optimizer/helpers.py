import bibtexparser
import re
from bibtexparser.bwriter import BibTexWriter

def _augment_func(filecontent, all_keys, temp_citations):
    for e in re.findall(r'\\cite[tp]?\{([^}]+)\}', filecontent):
        for c in e.split(','):  
            c = c.strip()
            if c not in temp_citations:
                all_keys.append(c)
                temp_citations.add(c)
                
    return all_keys, temp_citations
                
def bib_opt(filename, input_bib, output_bib):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    filtered_lines = [line for line in lines if not line.lstrip().startswith('%')]
    filecontent = ''.join(filtered_lines)
    
    with open(input_bib, 'r', encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)

    allowed_keys = []
    all_keys = []
    temp_citations = set()
    
    split_pattern = r'(.*?)(\\(?:input|include)[^\n]*\n)(.*?)((?=\\(?:input|include))|\Z)'
    matches = re.findall(split_pattern, filecontent, flags=re.DOTALL)
    split_results = [(before, after.strip()) for before, input_line, after, _ in matches]
    
    input_pattern_extended = r'\\(?:input|include)\s*(?:{([^}]+)}|([^\s\n]+))'
    matches = re.findall(input_pattern_extended, filecontent)
    input_files_extended = [m[0] if m[0] else m[1] for m in matches]    

    if not split_results:
        all_keys, temp_citations = _augment_func(filecontent, all_keys, temp_citations)
    else:
        for split_result, input_file_extended in zip(split_results, input_files_extended):
            all_keys, temp_citations = _augment_func(split_result[0], all_keys, temp_citations)
            
            if ".tex" not in input_file_extended:
                input_file_extended += ".tex"
            
            try:
                with open(input_file_extended, 'r', encoding='utf-8') as file:
                    _lines = file.readlines()

                _filtered_lines = [line for line in _lines if not line.lstrip().startswith('%')]
                _filecontent = ''.join(_filtered_lines)     

                all_keys, temp_citations = _augment_func(_filecontent, all_keys, temp_citations)
            except Exception as e:
                print(f'{e}, skipped.')

            all_keys, temp_citations = _augment_func(split_result[1], all_keys, temp_citations)

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

    print(f'successfully created {output_bib}')