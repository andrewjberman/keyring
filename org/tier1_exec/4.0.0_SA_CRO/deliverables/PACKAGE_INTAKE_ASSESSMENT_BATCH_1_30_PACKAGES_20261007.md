# Package intake assessment, batch 1: the 30 packages that need a fetch for Python 3.14 on the Dells

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07 ~15:5xZ. **For:** `1.0.0_SA_CTO`, who decides (NFRA_CTLPLN
PRD v0.16, contract C-INTAKE clause 7; Andrew-direct 2026-10-07 ~15:1xZ: "CRO ... assess legitimacy/stability, then
deliver their recommendation to the CTO and CTO runs the requirements addition").
**The batch:** `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/PYTHON_WHEELS_NEEDING_A_FETCH_FOR_CP314.md`
@bd489b912b: 18 lines of `requirements.txt` plus 12 compiled dependencies that are not lines.

## 1. Recommendation

- **YES for 26 of 30**, at the pinned version. Each is an established project, the pinned release is not withdrawn, the
  laptop already runs that exact version, and the index publishes a build for Python 3.14 on 64-bit Windows.
- **NO for 4 of 30 at the pinned version: `pyarrow==18.1.0`, `pyiceberg==0.9.1`, `hdbscan==0.8.41`, `kuzu==0.11.3`.**
  The index publishes no Python 3.14 Windows build of those versions, so there is nothing to fetch. Each needs a
  different version or stays a laptop-only package. A different version is a new request, because it changes what the
  laptop itself runs.
- **`pyarrow` is the one that matters.** 474 tracked files import it, and pandas' file reading, `awswrangler`,
  `pyiceberg` and `s3fs` lean on it. Until it is settled, a Dell can install pandas and still fail on the first
  parquet read.

Nothing was downloaded. No package file was fetched, opened or installed.

## 2. What was measured, and how far to trust it

- **Source:** the public package index's own record for each exact release (`https://pypi.org/pypi/<name>/<version>/json`),
  read 2026-10-07 15:4xZ to 15:5xZ, one read per package, 34 reads in all.
- **Reader:** a web-reading tool that summarises the page. It is not a parser. **It was wrong four times**: on four
  long pages it reported "no Python 3.14 Windows build" because it read only the first part of the page (pandas,
  matplotlib, fonttools, regex). Each was re-read from where the first read stopped, and the build is there. The four
  NO answers that stand (pyarrow, pyiceberg, hdbscan, kuzu) are on pages the tool read whole. The fetch step's own
  check (C-INTAKE clause 1, check 2) reads the index by exact file name and is the real control; this file is the
  recommendation, not that check.
- **Legitimacy** here means: the name is the one the laptop already has installed (taken from installed metadata, not
  typed); the project is one this seat recognises as long-standing and widely used; the release is not withdrawn. It
  is NOT an audit of who maintains each project or of the code.
- **Stability** here means: the laptop already runs this exact version, and the release has been public for the time
  shown. The youngest release in the batch is 81 days old.
- **Not read:** file hashes (the summarising reader is not fit to copy them; the fetch check reads them); build
  attestations; maintainer accounts; licences; what each package itself depends on under Python 3.14.

## 3. The 30, one line each

`3.14 build` = a file named `...-cp314-cp314-win_amd64.whl` exists for the pinned version. Dates are the upload date of
that file (or of the release, where no such file exists). Age is counted to 2026-10-07.

### 3a. Lines of `requirements.txt` (18)

| # | Package and pin | Project | 3.14 build | Published | Age (days) | Rec |
|---|---|---|---|---|---|---|
| 1 | `catboost==1.2.10` | Yandex's gradient-boosting library | yes | 2026-02-18 | 231 | YES |
| 2 | `lxml==6.0.2` | the standard XML library | yes | 2025-09-22 | 380 | YES |
| 3 | `matplotlib==3.11.1` | the standard plotting library | yes | 2026-07-18 | 81 | YES |
| 4 | `pandas==2.3.3` | the standard data-frame library | yes | 2025-09-29 | 373 | YES |
| 5 | `pyarrow==18.1.0` | Apache Arrow | **NO** (builds stop at 3.13) | 2024-11-26 | 680 | **NO at this pin** |
| 6 | `PyYAML==6.0.3` | the standard YAML library | yes | 2025-09-25 | 377 | YES |
| 7 | `websockets==16.0` | the standard websockets library | yes (a pure build also exists) | 2026-01-10 | 270 | YES |
| 8 | `duckdb==1.5.0` | DuckDB | yes | 2026-03-09 | 212 | YES |
| 9 | `hdbscan==0.8.41` | clustering library (scikit-learn-contrib) | **NO** (builds stop at 3.13) | 2025-12-12 | 299 | **NO at this pin** |
| 10 | `kuzu==0.11.3` | Kuzu graph database | **NO** (builds stop at 3.13) | 2025-10-10 | 362 | **NO at this pin**; see note |
| 11 | `numpy==2.4.2` | NumPy | yes | 2026-01-31 | 249 | YES |
| 12 | `pyiceberg==0.9.1` | Apache Iceberg's Python client | **NO** (builds stop at 3.12) | 2025-04-30 | 525 | **NO at this pin** |
| 13 | `pywin32==311` | the Windows API bindings | yes | 2025-07-14 | 450 | YES |
| 14 | `scikit-learn==1.8.0` | scikit-learn | yes | 2025-12-10 | 301 | YES |
| 15 | `pillow==12.1.1` | the standard imaging library | yes | 2026-02-11 | 238 | YES |
| 16 | `rpds-py==0.30.0` | data structures behind `jsonschema` | yes | 2025-11-30 | 311 | YES |
| 17 | `scipy==1.17.1` | SciPy | yes | 2026-02-23 | 226 | YES |
| 18 | `torch==2.10.0` | PyTorch | yes | 2026-01-21 | 259 | YES |

### 3b. Compiled dependencies that are not lines (12)

| # | Package and version | Needed by | 3.14 build | Published | Age (days) | Rec |
|---|---|---|---|---|---|---|
| 19 | `aiohttp==3.14.1` | s3fs | yes | 2026-06-07 | 122 | YES |
| 20 | `cffi==2.0.0` | cryptography, curl-cffi | yes | 2025-09-08 | 394 | YES |
| 21 | `charset-normalizer==3.4.4` | requests, pdfminer-six | yes | 2025-10-14 | 358 | YES |
| 22 | `click==8.3.1` | uvicorn, pyiceberg | not needed: it is pure Python, one build fits every version | 2025-11-15 | 326 | YES |
| 23 | `contourpy==1.3.3` | matplotlib | yes | 2025-07-26 | 438 | YES |
| 24 | `coverage==7.13.5` | pytest-cov | yes | 2026-03-17 | 204 | YES |
| 25 | `fonttools==4.63.0` | matplotlib | yes (a pure build also exists) | 2026-05-14 | 146 | YES |
| 26 | `greenlet==3.3.2` | playwright | yes | 2026-02-20 | 229 | YES |
| 27 | `jiter==0.13.0` | anthropic, openai | yes | 2026-02-02 | 247 | YES |
| 28 | `kiwisolver==1.5.0` | matplotlib | yes | 2026-03-09 | 212 | YES |
| 29 | `mmh3==5.2.1` | pyiceberg | yes | 2026-03-05 | 216 | YES |
| 30 | `regex==2026.2.28` | transformers | yes | 2026-02-28 | 221 | YES |

Count: 26 YES, 4 NO; 26 + 4 = 30. None of the 30 releases is marked withdrawn on the index.

## 4. Notes on particular lines

- **`click` (22).** It was on the fetch list only because the laptop's copy is a development install that cannot be
  re-packed. The index's own file for 8.3.1 is pure Python.
- **`mmh3` (29) is needed only by `pyiceberg`**, which is a NO. If `pyiceberg` is not carried to the Dells, `mmh3`
  need not be fetched.
- **`kuzu` (10).** This seat recalls the Kuzu project being archived by its makers in late 2025. That is a
  recollection, NOT read today. If true, no later version will ever carry a Python 3.14 build, and the one file that
  imports it should stay on the laptop or move off it. Worth one read before anyone spends time on it.
- **`pyarrow` (5).** A later Arrow release with Python 3.14 builds exists as far as this seat recalls; which one, and
  whether pandas 2.3.3, `awswrangler==3.11.0` and `pyiceberg==0.9.1` accept it, was NOT measured. That is the content
  of the version-change request.
- **`torch` (18)** is very large and one file imports it through `sentence-transformers`. A YES on legitimacy; whether
  the Dells need it at all is a scope question for the CTO, not a safety one.

## 5. What the CTO's decision should also weigh

1. **The four NOs need an owner.** REC: `pyarrow` gets a version-change request now (it gates the data stack);
   `pyiceberg`, `hdbscan` and `kuzu` stay laptop-only until a lane on a Dell actually needs one.
2. **A YES here is a YES to fetch and check, not a YES to trust.** The eight checks of C-INTAKE clause 1 still run on
   each file. Check 6 (the Python files equal the laptop's copy of the same version) is the strongest one for this
   batch, because all 26 are versions the laptop already runs.
3. **None of the 30 is a new package name**, so call F (run a new name somewhere with no sign-in first) does not
   arise in this batch.
4. **The batch is not closed under dependencies.** 73 dependencies are not lines of the list (the wheels file's own
   table). The 12 compiled ones are in 3b; the 59 pure and 2 fit-any-version ones go in the kit offline. Whether any of
   the 26 pulls in something further under Python 3.14 was not measured.

## 6. Reproduce

For each package: open `https://pypi.org/pypi/<name>/<version>/json` and look in its `urls` list for a file name
ending `-cp314-cp314-win_amd64.whl` (not `cp314t`), and read `yanked` and that file's `upload_time_iso_8601`.
