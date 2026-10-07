# Package intake assessment, site Z batch 1: seven wheels for the `opal-amgt-scoped-api` Lambda build

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07 ~16:3xZ. **For:** `1.0.0_SA_CTO`, who decides (NFRA_CTLPLN
contract C-INTAKE clause 7). **Asked by:** `1.0.0_SA_CTO` msg 106393.
**The list:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/SITEZ_C_INTAKE_WHEEL_LISTS_FOR_CTO_20261007_1615Z.md`, section A
(AMGT_RESAPP cell bb-18, from `2.0.0_SA_COO~Z`). The pins are line 126, 132 and 133 of
`infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`, read on the laptop.

## 1. Recommendation

- **YES for all seven**, at the pinned versions.
- **Five of the seven need no fetch at all.** They are pure Python, one build fits every platform, and the laptop has
  each one installed at exactly the pinned version. The kit can re-pack them from the laptop's disk and send them.
- **Two need a fetch through the checked route:** `pyarrow==16.1.0` and `rpds-py==2026.6.3`, each as a Linux build for
  Python 3.11. The laptop holds neither version (it runs `pyarrow` 18.1.0 and `rpds-py` 0.30.0, both for Windows).
- **`rpds-py==2026.6.3` carries one flag** (section 3): the version number changed scheme. A YES, with one cheap read
  recommended before the fetch.

Nothing was downloaded.

## 2. The seven, one line each

| # | Package and pin | Build asked for | On the laptop at this version? | On the index | Published | Rec |
|---|---|---|---|---|---|---|
| 1 | `jsonschema==4.26.0` | pure Python | yes, pure | not read; not needed | -- | YES, re-pack offline |
| 2 | `attrs==26.1.0` | pure Python | yes, pure | not read; not needed | -- | YES, re-pack offline |
| 3 | `jsonschema-specifications==2025.9.1` | pure Python | yes, pure | not read; not needed | -- | YES, re-pack offline |
| 4 | `referencing==0.37.0` | pure Python | yes, pure | not read; not needed | -- | YES, re-pack offline |
| 5 | `typing_extensions==4.16.0` | pure Python | yes, pure | not read; not needed | -- | YES, re-pack offline |
| 6 | `pyarrow==16.1.0` | Python 3.11, Linux x86-64 (`manylinux2014`) | no (laptop: 18.1.0, Windows) | the file exists; release not withdrawn | 2024-05-14 (876 days) | YES, fetch |
| 7 | `rpds-py==2026.6.3` | Python 3.11, Linux x86-64 (`manylinux2014`) | no (laptop: 0.30.0, Windows) | the file exists; release not withdrawn | 2026-06-30 (99 days) | YES, fetch; see section 3 |

Measured: rows 1 to 5 from the laptop's installed metadata (version and build tag of each). Rows 6 and 7 from the
public index's record for the exact release, one read each, through the same summarising reader as batch 1, with the
same limits (`PACKAGE_INTAKE_ASSESSMENT_BATCH_1_30_PACKAGES_20261007.md` section 2). Both pages were read far enough to
show the named file; hashes were not read.

## 3. Notes

- **`pyarrow==16.1.0` is deliberately not the boxes' version.** The build script says so: "16.1.0 only, 17+ NOT
  admitted", named on two signed halves. So the Lambda and the boxes run different `pyarrow` versions on purpose, and
  today's decision to keep the boxes on 18.1.0 does not touch this pin. Legitimacy: Apache Arrow, a release more than
  two years old.
- **`rpds-py==2026.6.3`: the version scheme changed.** The laptop runs 0.30.0; the index's project record gives the
  latest as 2026.9.1. So the project moved from numbers like 0.30 to date-style numbers. The name is the same and the
  release is on the same project page. This seat did not read the project's own notes on the change. The cheap read
  that settles it: whether the DEPLOYED `opal-amgt-scoped-api` already carries `rpds-py` 2026.6.3 (the pin is in the
  committed script, so a prior build very likely fetched it). If it does, this is a version already running in
  production, not a new one.
- **Checks 3 and 6 of C-INTAKE cannot apply to rows 6 and 7.** Both compare the fetched file with the laptop's own
  copy of the same version, and the laptop has neither version. Checks 1, 2, 4, 5, 7 and 8 still run. The
  recommendation is YES with that stated, not YES as if all eight ran.
- **Not in the seven:** section B of the list, a Windows build of `rpds-py` 2026.6.3 for Python 3.14, used only by the
  script's local import check on site Z. Not assessed here because it was not asked. The list names the alternative: a
  script edit that skips that check, which is the CTO's call. If site Z takes Python 3.12 as the Dells do, the tag it
  needs changes with it.
- **What the list itself says is unmeasured:** the exact file names on the index, the hashes, and the separate
  `opal-amgt-print-deps` layer build.

## 4. Reproduce

Rows 1 to 5: `python -c "import importlib.metadata as m; d=m.distribution('<name>'); print(d.version, d.read_text('WHEEL'))"`
on the laptop. Rows 6 and 7: open `https://pypi.org/pypi/<name>/<version>/json` and find the file name ending
`-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`.
