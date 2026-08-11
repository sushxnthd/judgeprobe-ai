import json, sys
from dataclasses import asdict
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from judgeprobe.core import Pair,audit,length_preferring_judge
pairs=[]
for i in range(300):
    a='clear answer' if i%2 else 'clear answer with extra but irrelevant padding'
    b='concise answer'
    pairs.append(Pair(f'prompt {i}',a,b))
result=asdict(audit(length_preferring_judge,pairs))
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2));print(result)
