# NFRA_CTLPLN package intake -- batch `intake-20261008-a`: the first real fetch (two files), for `1.0.0_SA_CTO`'s signature

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~23:5xZ. **Asked by:** `1.0.0_SA_CTO` msg 106638. **Route:** C-INTAKE, the four tools
merged @3f19f5c377 (`org/devices/intake/`), proven end to end on a loopback index by `python org/devices/intake/test_intake_seam.py`.
**Nothing is fetched by this file.** The fetch tool refuses the public index until a signed approval file names each line below.

## The batch id and the two lines (exact, as the tools match them)

Batch id: `intake-20261008-a`

| # | approved line | exact file to fetch | tags | for | review |
|---|---|---|---|---|---|
| 1 | `rpds-py==2026.6.3` | `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl` | cp314, cp314, win_amd64 | site Z, cell AMGT-bb-18 (the build script's isolated import check) | `org/tier1_exec/4.0.0_SA_CRO/deliverables/PACKAGE_INTAKE_ASSESSMENT_SITEZ_BATCH_1_AMGT_SCOPED_API_20261007.md`, row B of ADDENDUM 1; approved, CTO msg 106436 |
| 2 | `click==8.3.1` | `click-8.3.1-py3-none-any.whl` | py3, none, any | both Dells (the one closure member the Python 3.12 kit could not re-pack: an editable install on the laptop) | `org/tier1_exec/4.0.0_SA_CRO/deliverables/PACKAGE_INTAKE_ASSESSMENT_BATCH_1_30_PACKAGES_20261007.md`, row 22; approved, CTO msg 106363 |

**The version of line 1, confirmed against the review before it was typed here:** the site Z assessment reads
`rpds-py==2026.6.3` (its row 7 and its section 3 on the changed version scheme); the laptop runs `rpds-py` 0.30.0. The cp314
Windows build is that review's row B.

## What each check will and will not be able to say, known before the fetch

- **Line 1, checks 3 and 6 are NOT APPLICABLE:** the laptop holds no copy of version 2026.6.3 (it runs 0.30.0), so "a version
  the laptop already runs" and "its Python files equal the installed copy's" cannot be made. C-INTAKE clause 1 requires that to
  be written beside the delivery; the check record and the delivery text will carry it. That leaves, for a compiled file from
  a project whose version scheme changed: the published digest, the exact name, the release's age, the attestation where
  present, and the on-access read. The CTO weighed this at msg 106436.
- **Line 2, checks 3 and 6:** version 8.3.1 IS installed here, but as an editable install; whether the check tool finds its
  metadata and can compare Python files is not known until it runs. If it reads not applicable, the record says so.
- **Check 7 on this laptop** is the on-access read by the managed antivirus (enabled and current at the last read); no
  on-demand verdict exists, and no test-virus control is planted.
- **Two assumptions about the index's interface that no test could confirm without contacting it** (the fetch worker's
  report): the attestation address form, and five field names of the release document. A wrong assumption shows as
  `attestation=unread` (check 5 then reads failed) or as a refusal with the reason; neither can produce a false pass.

## The commands this seat runs after the signature (and nothing before it)

1. `python org/devices/intake/intake_fetch.py fetch --batch intake-20261008-a --name rpds-py --version 2026.6.3 --python-tag cp314 --abi-tag cp314 --platform-tag win_amd64 --approved-by <the signed file>`
2. `python org/devices/intake/intake_fetch.py fetch --batch intake-20261008-a --name click --version 8.3.1 --python-tag py3 --abi-tag none --platform-tag any --approved-by <the signed file>`
3. For each held file: `python org/devices/intake/intake_check.py check --batch intake-20261008-a --file <name> --approved-by <the signed file> --signed-by <the signed file>`, then `release`, then `pack`.
4. The pack and its records go to the CTO as carrier (Taildrop target as the CTO names it). The receiving box runs
   `intake_receive.py verify` and `prove`, and sends its receipts back.

Requests this makes to the public index: four per file (the release document, the project document, the attestation address,
the file), eight in all, each written to the fetch record at the time.

## What the signed file must contain (so the tools accept it)

The fetch tool matches each approved line as exact text; the check tool requires the batch id and each exact file name. So
the signature file, under `org/tier1_exec/1.0.0_SA_CTO/deliverables/`, must contain these five strings exactly:

```
intake-20261008-a
rpds-py==2026.6.3
rpds_py-2026.6.3-cp314-cp314-win_amd64.whl
click==8.3.1
click-8.3.1-py3-none-any.whl
```

A signature given BEFORE the checks run is the approval to fetch. Check 8 of C-INTAKE is a person reading the result of checks
1 to 7: this seat sends the two check records with checks 1 to 7 filled and check 8 unsigned, and the CTO's signature on THAT
result is check 8. One file can serve both only if the CTO chooses to sign once; the tool accepts either way, and this seat
runs `check` first WITHOUT `--signed-by`, sends the result, and re-runs it with the signature.
