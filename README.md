# falcon
In-silico prediction of mass spectrometry fragmentation

## Installation
```
conda env create -f envs/falcon.yml
```

## Fragmentation Reactions
There are 7 different types of chemical reactions that occur in mass spectrometry:
1. Ionization
2. Simple Inductive Cleavage
3. Charge Migration
4. Compounded Cleavage
5. Charge Retention
6. Rearrangment
7. Resonance
\
Some of these reactions are outlined in this [review](https://pubs-rsc-org.libaccess.lib.mcmaster.ca/en/content/articlehtml/2016/np/c5np00073d). The reactions are coded with `SMARTS` and can be found in `falcon/data/reactions.csv`.

## Example
```python
from falcon.Fragmenter import compute_fragments

smiles = 'CNC[C@H](O)C1=CC=C(O)C(O)=C1'
output = compute_fragments(smiles,
                           max_rounds=6,
                           cores=1)
```