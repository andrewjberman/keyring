# Package intake assessment: `pyarrow`, the version change

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07 ~15:5xZ. **For:** `1.0.0_SA_CTO`, who decides.
**Asked by:** `1.0.0_SA_CTO` msg 106362: "assesses the lowest version that has that build, and states what moving the
pin does to the laptop and site Z, which must run the same version."

## 1. Answer

- **The lowest `pyarrow` with a Python 3.14 64-bit Windows build is 22.0.0** (published 2025-10-24, 348 days old, not
  withdrawn). Version 21.0.0 has none. The latest release is 25.0.1.
- **Moving the pin from 18.1.0 to 22.0.0 breaks two declared requirements on every box that follows it**, and jumps four
  major versions under 474 importing files with no test run behind it.
- **Recommendation: do not move the pin for this.** Put Python 3.12 on the Dells instead (section 4). That removes the
  cause, and with it most of the first batch.
- If the pin must move: YES on legitimacy for `pyarrow==22.0.0` (Apache Arrow; same project the estate already runs),
  and NO on stability until the two conflicts below are settled and the laptop's suites have run on it.

## 2. What was measured

| Fact | Source | Result |
|---|---|---|
| 21.0.0 has a `cp314-cp314-win_amd64` file | the index's record for 21.0.0, read whole (51 files) | no; builds stop at Python 3.13 |
| 22.0.0 has one | the index's record for 22.0.0 | yes, `pyarrow-22.0.0-cp314-cp314-win_amd64.whl`, uploaded 2025-10-24; needs Python 3.10 or later; not withdrawn |
| the latest version | the index's project record | 25.0.1 |
| which installed packages declare a `pyarrow` requirement | the laptop's installed metadata, all distributions | 19 declarations; 2 carry an upper bound |
| how the estate pins it | `requirements.txt`; the 28 Lambda requirements files | root list `pyarrow==18.1.0` (474 files import it); 0 Lambda requirements files name pyarrow |

Not measured: whether a release between 21.0.0 and 22.0.0 exists (the index's full release list is too long for the
reader; Arrow does not normally publish one); what site Z has installed; any behaviour of 22.0.0. Nothing was
downloaded. The same reader limits as the batch file apply
(`PACKAGE_INTAKE_ASSESSMENT_BATCH_1_30_PACKAGES_20261007.md` section 2).

## 3. What moving the pin to 22.0.0 does to the laptop and site Z

**Two declared conflicts (measured on the laptop's installed metadata):**

| Package | Its declared range | Effect at 22.0.0 | Reach |
|---|---|---|---|
| `awswrangler==3.11.0` | `pyarrow >=8.0.0,<19.0.0` (and `>=18.0.0,<19.0.0` on Python 3.13 or later) | outside the range; `pip check` fails; it also needs its own version change | 1 file imports it (a Lambda source) |
| `pyiceberg==0.9.1` | `pyarrow >=17.0.0,<20.0.0` for its arrow, pandas and duckdb extras | outside the range | 15 files import it; it is already laptop-only by today's decision, and the laptop would then run it outside its range |

No conflict declared: `pandas==2.3.3` (needs 10.0.1 or later), `duckdb`, `fsspec`, `narwhals`, `scikit-learn`.

**Unmeasured, and the larger risk:**
- Four major versions (19, 20, 21, 22) of changes under 474 files that import `pyarrow` and 953 that import pandas.
  No suite has run on 22.0.0. Running one means installing it on the laptop or site Z, which is itself a fetch.
- **Files written on a box are read in AWS.** The Lambdas do not take `pyarrow` from the root list: none of the 28
  Lambda requirements files names it, and Lambda layers named `pandas-pyarrow-layer` exist, whose `pyarrow` version
  was not read. A box writing parquet with 22.0.0 that a Lambda reads with an older copy is a format question
  nobody has tested. This is the served-data risk, not a developer-convenience one.
- Site Z runs the Bloomberg-bound pipelines. Its installed set was not read.

So the cost of the move is three version changes (`pyarrow`, then `awswrangler`, then a look at `pyiceberg`), one test
campaign on two boxes, and one cross-version read test against the Lambda layers.

## 4. The alternative that removes the cause

The whole first batch exists because the Dells run Python 3.14 and the laptop and its pins are Python 3.12.

- With Python 3.12 on the Dells, the kit's own rule applies: `org/devices/kit_python_pack.py` rebuilds a compiled
  package from the laptop's installed files "when the target's Python minor version and platform tag equal this
  machine's". All 18 listed packages and the 12 compiled dependencies are on the laptop as Python 3.12 builds.
- Effect: the 30-package fetch falls to zero or near it; the four NOs (`pyarrow`, `pyiceberg`, `hdbscan`, `kuzu`)
  disappear, because each has a 3.12 build that the laptop already runs; no pin moves; every box runs the same
  versions on the same Python.
- Cost: one program, the Python 3.12 installer, reaches each Dell. That is a red-tier item: it goes from the laptop
  over the tailnet, checked first, never from the internet onto a Dell. Whether the laptop still holds the 3.12
  installer file was not checked. A side-by-side install leaves the Dell's 3.14 in place.
- Not measured: whether anything on the Dells needs 3.14 specifically; why they were set up on 3.14.

This is a design choice for `1.0.0_SA_CTO` and, for the installer, Andrew's tier word applies. It is put here because
the version-change request, taken alone, would hide it.

## 5. Recommendation

1. Decide section 4 first. If the Dells take Python 3.12, withdraw the `pyarrow` version change, and re-cut the first
   batch against 3.12 (most of it becomes an offline re-pack).
2. If the Dells stay on 3.14: `pyarrow==22.0.0` is the version to request, together with an `awswrangler` change, and
   it is not approved for any box until the laptop's suites and one Lambda read of a file written by 22.0.0 have
   passed.
