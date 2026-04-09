# Pipeline Modules

Deterministic tools that run before LLM workers. Zero API calls.

## Perceive

| Module | What it does |
|--------|-------------|
| `perceive.filesystem_scanner` | Scans directory tree. Extracts path, extension, size, line count, first line per file. |
| `perceive.corpus_aggregator` | Corpus-level statistics from scanner output. Extension distribution, directory concentration, group counts, size histogram, structural depth. Zero file reads -- metadata only. Informs pipeline selection and complexity tier. |
| `perceive.corpus_indexer` | Builds a tantivy inverted index over file contents. First call: ~1s for 500 files. Subsequent queries: <5ms. Persists at `{dir}/.corpus_index/`. Use `CorpusIndex(dir).search("query")` for instant ranked keyword search across any corpus. Also provides `read_chunk(path, start, length)`, `count_pattern(pattern, dir)`, `extract_pattern(pattern, path)`. |
| `perceive.vector_index` | Builds a dense vector index over file chunks using sentence-transformers. Persists at `{dir}/.vector_index/`. First call: ~30s for 500 files (embedding). Subsequent queries: <10ms. Use `VectorIndex(dir).search("semantic query")` for conceptual proximity search. Pure numpy cosine similarity -- no external vector DB. Graceful degradation if sentence-transformers not installed. |

## Interpret

| Module | What it does |
|--------|-------------|
| `interpret.content_fingerprinter` | Classifies files into 5 groups by extension: DOCUMENT (.md, .txt, .html, .pdf), DATA (.json, .yaml, .csv, .xml), CODE (.py, .js, .go, .sh), CONFIG (.env, .ini, .dockerfile), ASSET (.png, .zip, .exe). Also handles special filenames (Dockerfile, Makefile, README, etc). |
| `interpret.ast_extractor` | Parses Python (function signatures, class hierarchies, imports), JSON/YAML (schema shape), Markdown (heading hierarchy). |
| `interpret.crossref_graph` | Builds citation graph from internal references. Outputs authority ranking, orphan list, blast radius. |

## Act

| Module | What it does |
|--------|-------------|
| `act.key_generator` | Generates OOK keys from classification + spine template. Handles collisions. |
| `act.registry_writer` | Writes inventory JSON, registry JSON, summary MD from keyed objects. |

## Adapt

| Module | What it does |
|--------|-------------|
| `adapt.structural_validator` | 8 checks: paths exist, codes valid, spine matches, count matches, keys unique, format compliant. |
| `adapt.differential_regression` | Diffs current output against last baseline. Flags additions, removals, mutations, regressions. |
| `adapt.coverage_auditor` | Set difference: source files vs registry entries. Finds gaps both ways. |

## Pipeline Composition

See `registry.json` for work-type pipelines. D-mode modules run
inline. LLM workers dispatch for judgment (classification, code writing).
