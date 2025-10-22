import fire
import json
import logging
import resource
from falcon.Fragmenter import compute_fragments


logging.getLogger().disabled = True


def main(smiles, depth, memory_limit):
    _, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (memory_limit, hard))
    output = compute_fragments(smiles, max_rounds=depth, cores=1)
    return json.dumps({k: v.to_dict(orient="records") for k, v in output.items()})


if __name__ == "__main__":
    fire.Fire(main)
