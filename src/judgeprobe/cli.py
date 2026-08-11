import argparse,json
from dataclasses import asdict
from pathlib import Path
from .core import Pair,audit,length_preferring_judge

def main():
    p=argparse.ArgumentParser(description='Measure pairwise judge position instability.')
    p.add_argument('pairs');a=p.parse_args(); rows=json.loads(Path(a.pairs).read_text())
    print(json.dumps(asdict(audit(length_preferring_judge,[Pair(**r) for r in rows])),indent=2))
if __name__=='__main__':main()
