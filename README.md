# judgeprobe-ai

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF)](.github/workflows/ci.yml) [![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)](pyproject.toml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[**Live demo →**](https://sushxnthd.github.io/judgeprobe-ai/) · [Architecture](docs/architecture.md) · [Benchmarks](benchmarks/results.json)


A small audit harness for pairwise AI judges. It counterbalances every comparison (`A/B` and `B/A`) and reports how often the judge changes its canonical preference when presentation order changes.

```bash
pip install -e .
judgeprobe examples/pairs.json
```

## Core metric

`position_flip_rate` is the fraction of pairs where swapping response order changes the judge's underlying choice after mapping labels back to the original candidates.

That catches a common evaluation failure mode without needing a reference answer.

## Bring your own judge

```python
from judgeprobe.core import Pair, audit
result = audit(my_judge, [Pair(prompt, answer_a, answer_b)])
```

A judge is just a callable returning `A`, `B` or `TIE`, so API-backed and local judges can use the same audit logic.

## Benchmark

The checked-in benchmark uses an intentionally simplistic length-preferring judge with a deterministic first-position tie break. This gives a known bias signal for regression testing.

## Roadmap

- confidence intervals and McNemar tests
- verbosity/confidence-style perturbations
- judge agreement matrices
- async batched evaluator adapters

MIT licensed.

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for the data flow and design boundaries.
