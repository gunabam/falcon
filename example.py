from falcon.Fragmenter import compute_fragments

smiles = "CNC[C@H](O)C1=CC=C(O)C(O)=C1"
output = compute_fragments(smiles, max_rounds=6, cores=1)
print(output)
