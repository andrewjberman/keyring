# Package intake assessment: the dell2 Python 3.12 kit for IRPT_DASHBD E2(1)

**Author:** `4.0.0_SA_CRO~D2`, 2026-10-07 ~21:3xZ.
**For:** `1.0.0_SA_CTO~DELL2`, who decides.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 1093, on `2.0.0_SA_COO~D2` msg 1088: "write the package intake, matching the served layer's versions".
**Route:** `org/devices/intake/README.md`, hops 1-2 (request and assessment). The CTO signs the batch file (hop 3); the laptop fetches and checks (hops 4-5).

## 1. Recommendation

**YES** for all four lines below, at exactly these versions, for `win_amd64` / CPython 3.12 on dell2.

| # | Line | Kind | Rec |
|---|---|---|---|
| 1 | `python-3.12.10-amd64.exe` | interpreter (red tier) | YES. Already admitted by Andrew (msg 1005/1010), on two conditions: a valid Authenticode signature from the Python Software Foundation, and a sha256 equal to python.org's. Andrew runs it elevated. Install it side by side; dell2's Python 3.14.7 stays. |
| 2 | `pandas==2.2.3` | compiled wheel | YES |
| 3 | `numpy==1.26.4` | compiled wheel | YES |
| 4 | `pyarrow==14.0.2` | compiled wheel | YES |

**Plus four pure-Python dependencies** that pandas 2.2.3 requires. These are one build for every Python, so the laptop can re-pack them from its own install with no internet fetch. Any one the laptop lacks is a line for this batch.

| # | Line | Needed by | Note |
|---|---|---|---|
| 5 | `python-dateutil==2.9.0.post0` | pandas (`>=2.8.2`) | the estate pins this version (`requirements.txt`:59) |
| 6 | `pytz==2025.2` | pandas (`>=2020.1`) | the estate pins this version (`requirements.txt`:63) |
| 7 | `tzdata==2026.5` | pandas (`>=2022.7`) | not pinned in `requirements.txt`; this is the version dell2 already runs |
| 8 | `six==1.17.0` | python-dateutil | not pinned; this is the version dell2 already runs |

Nothing was downloaded. No package file was fetched, opened or installed.

## 2. What was measured

**Source.** The public index's record for each exact release (`https://pypi.org/pypi/<name>/<version>/json`), read 2026-10-07 ~21:2xZ. The reader was the summarising web tool, which the batch-1 assessment section 2 flagged as unreliable on long pages.
- pandas: the page is 113,835 characters; the tool read the first 100,000. The `cp312-cp312-win_amd64` file was found inside that range.
- numpy and pyarrow: read whole.

| Line | `cp312-cp312-win_amd64` file | Uploaded | Age (days) | Size (bytes) | sha256 (reader-reported) | Yanked | requires_python |
|---|---|---|---|---|---|---|---|
| pandas 2.2.3 | `pandas-2.2.3-cp312-cp312-win_amd64.whl` | 2024-09-20 | 747 | 11,504,248 | `59ef3764d0fe818125a5097d2ae867ca3fa64df032331b7e0917cf5d7bf66b13` | no | `>=3.9` |
| numpy 1.26.4 | `numpy-1.26.4-cp312-cp312-win_amd64.whl` | 2024-02-05 | 975 | 15,517,754 | `08beddf13648eb95f8d867350f6a018a4be2e5ad54c8d8caed89ebca558b2818` | no | `>=3.9` |
| pyarrow 14.0.2 | `pyarrow-14.0.2-cp312-cp312-win_amd64.whl` | 2023-12-18 | 1,024 | 25,043,754 | `e4b123ad0f6add92de898214d404e488167b87b5dd86e9a434126bc2b7a5578d` | no | `>=3.8` |

**The digests are copied from a summarising reader. Treat them as a cross-check only.** The real control is `intake_check.py` on the laptop, which reads the index by exact file name (C-INTAKE clause 1, check 2). A mismatch between that check and this table means re-read; it does not mean the file is bad.

**Declared dependencies.** Read from `requires_dist`, entries with no extras only.
- pandas 2.2.3 needs: `numpy>=1.26.0` (on Python 3.12), `python-dateutil>=2.8.2`, `pytz>=2020.1`, `tzdata>=2022.7`.
- pyarrow 14.0.2 needs: `numpy>=1.16.6`.
- The set is consistent: numpy 1.26.4 satisfies both, and there are no other compiled dependencies.

**dell2 today (measured with `python -m pip list`).**
- Python 3.14.7 is the only interpreter (`py -0`).
- pandas 3.0.6, numpy 2.5.3, pyarrow 25.0.1.
- python-dateutil 2.9.0.post0, pytz 2025.2, six 1.17.0, tzdata 2026.5.

**Legitimacy.**
- These are the three standard data libraries the estate already runs, under their own names.
- The releases are 2 to 3 years old and not withdrawn.
- This is NOT an audit of maintainers or code.

**Stability.**
- These are old, final patch releases of their lines; numpy 1.26.4 is the last 1.x.
- The three are pinned together in the repo: `infra/aws/lambda/layers/find-insure-parse-deps/requirements.txt` lists exactly `pyarrow==14.0.2`, `pandas==2.2.3`, `numpy==1.26.4`.

## 3. "Matching the served layer": what is and is not established

- **[held]** The served IRPT layer runs pandas 2.2.3. Sources: `2.0.0_SA_COO~D2` msg 1088, and `IRPT_DASHBD .../0.9.0_WK_IRPT_DASHBD~22/PANDAS_ONCE_E3.md`:28.
- **[measured]** One repo file pins this exact trio: the `find-insure-parse-deps` layer requirements above.
- **[not measured]** I did not trace the IRPT dashboard Lambda to its attached layer ARN, or read that layer's installed versions. `shared-infra/layers.tf` defines `pandas-pyarrow-requests-layer`, but its pandas, numpy and pyarrow versions are not in the file. If the served layer's numpy or pyarrow differ from 1.26.4 or 14.0.2, the E2(1) test still runs on the right pandas, but this kit would not match the layer. The laptop relay of E2(1), which runs "on the served layer's pandas 2.2.3" (msg 1093 (1)), is where this gets confirmed.

## 4. Scope and effect

- **Scope.** This kit is for dell2 only, in a separate Python 3.12 environment for the IRPT_DASHBD test. It moves no pin in `requirements.txt` and changes nothing on the laptop or site Z.
- **Effect on dell2.** A second interpreter sits beside 3.14. Seats must call it explicitly, as `py -3.12` or a 3.12 venv. A bare `python` stays 3.14 with pandas 3.0.6. That is the point: E2 tests the None-hardening on both pandas majors.
- **Unmeasured.** Whether anything else on dell2 assumes `python` resolves to 3.12 after the install (PATH order). Unticking "Add to PATH" in the installer, or leaving the `py` launcher default on 3.14, avoids the question.

-- 4.0.0_SA_CRO~D2
