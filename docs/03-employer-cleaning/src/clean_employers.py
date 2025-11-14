#!/usr/bin/env python3
import pandas as pd
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # project root
def normalize(s):
    s = s.lower()
    s = re.sub(r'&', ' and ', s)
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.replace('univ ', 'university ')
    s = s.replace('u mass', 'university of massachusetts')
    s = s.replace('umass', 'university of massachusetts')
    s = s.replace('mass gen hosp', 'massachusetts general hospital')
    s = s.replace('m g h', 'massachusetts general hospital')
    s = s.replace('mgh', 'massachusetts general hospital')
    s = s.replace('pwc', 'pricewaterhousecoopers')
    s = s.replace('price waterhouse cooper', 'pricewaterhousecoopers')
    s = s.replace('pricewaterhouse coopers', 'pricewaterhousecoopers')
    s = s.replace('j and j', 'johnson and johnson')
    s = s.replace('bos city of boston', 'city of boston')
    return s

canonical_map = {
    'google': 'Google',
    'google inc': 'Google',
    'google llc': 'Google',
    'massachusetts general hospital': 'Massachusetts General Hospital',
    'university of massachusetts lowell': 'University of Massachusetts Lowell',
    'pricewaterhousecoopers': 'PwC (PricewaterhouseCoopers)',
    'johnson and johnson': 'Johnson & Johnson',
    'city of boston': 'City of Boston'
}

df = pd.read_csv(BASE / 'data' / 'raw_employers.csv')
df['norm'] = df['employer_raw'].apply(normalize)

def to_canonical(s):
    for k, v in canonical_map.items():
        if k in s:
            return v
    return s.title()

df['employer_clean'] = df['norm'].apply(to_canonical)
(df[['applicant_id','employer_raw','employer_clean']]
   .to_csv(BASE / 'outputs' / 'employers_clean.csv', index=False))
