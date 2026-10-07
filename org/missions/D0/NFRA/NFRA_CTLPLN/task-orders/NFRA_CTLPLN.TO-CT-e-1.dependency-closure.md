# TO NFRA_CTLPLN.TO-CT-e-1 -- round 5 CT-e-1: the approved list closed under dependencies, and how a reviewed addition survives a regeneration

<to_id>NFRA_CTLPLN.TO-CT-e-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~13</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-e-1` (`decompositions/NFRA_CTLPLN_DECOMP.round5.md`) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** none (the record contract below is the seam; no cell waits on another's code)

---

## WORKER FACE

### THE CELL

`CT-e-1`, C-INTAKE clauses 2 and 4. The checked route fetches ONE file by exact name with no dependency resolution, so the list
of approved packages must be CLOSED under dependencies before anything is fetched. Today it is not: the root `requirements.txt`
(67 lines, generated, do-not-hand-edit header) omits 73 packages its own lines require (row `NFRA_CTLPLN-S18`), and on a Dell the
kit's install showed three imports failing for exactly that reason: `pandas_market_calendars` needs `exchange_calendars`, `yfinance`
needs `frozendict`, `s3fs` needs `aiobotocore` (row `NFRA_CTLPLN-S21`). CTO msg 106445: "close the list before round 5 fetches."
And clause 4: "Round 5's first cell decides, by measurement, how a reviewed addition and a regeneration stop overwriting each
other; until it lands, no line is added by hand."
Target environment: Python 3.14 on 64-bit Windows (both Dells). This machine runs Python 3.12 and holds an installed copy of
every listed package, whose `METADATA` carries its `Requires-Dist` lines.

### THE SEAM

THE RECORD CONTRACT (fixed here so the four cells share FILES and never wait on each other's code).
All records are JSON, UTF-8, ASCII-only, one file per event, under `org/devices/intake/records/<batch>/`:
- FETCH record `<file name>.fetch.json`, written by the fetch tool AT THE TIME OF THE FETCH, also when the fetch fails:
  `schema` ("intake-fetch/1"), `batch`, `requested` {`name`, `version`, `python_tag`, `abi_tag`, `platform_tag`, `file_name`},
  `index_base`, `requests` (a list, one entry per HTTP request made: `url`, `method`, `status`, `bytes`, `at` UTC),
  `published` {`sha256`, `size`, `upload_time`, `yanked`, `requires_python`} (as the index states them for that exact file name),
  `project` {`release_count`, `first_release_at`, `this_release_at`}, `attestation` ("present" | "absent" | "unread", with the
  URL asked), `held_path` (relative to the holding root, never absolute), `held_sha256`, `held_bytes`, `outcome`
  ("held" | "refused" | "failed") with `reason`, `fetched_by` (the serial), `at`.
- CHECK record `<file name>.check.json`, written by the check tool: `schema` ("intake-check/1"), `batch`, `file_name`,
  `held_sha256`, `checks` (a list of exactly eight, in the brief's order, each `n`, `name`, `verdict`
  ("passed" | "failed" | "not_applicable" | "unsigned"), `evidence`, `rules_out`, `leaves` -- the last two the brief's own
  words for that check), `verdict` ("checked" only when checks 1 to 7 are each passed or not_applicable WITH a reason and
  check 8 reads "passed" with a signer and a file path; otherwise "not_checked"), `checked_by`, `at`.
- RECEIPT record `<file name>.receipt.<device>.json`, written on the receiving box: `schema` ("intake-receipt/1"), `device`,
  `python`, `file_name`, `received_sha256`, `check_record_sha256`, `install` {`command`, `rc`}, `imports` (per top-level module:
  `module`, `rc`, `first_error_line`), `outcome` ("installed_imported" | "installed_import_failed" | "refused" | "install_failed")
  with `reason`, `at`.
The HOLDING ROOT is outside every git tree: `<drive>/opal-intake/` (derive the drive prefix: `/cygdrive/c` if it exists, else
`/c`; on Windows Python resolve it from the workspace root's drive), with `holding/<batch>/` for fetched files and
`release/<batch>/` for files whose check record reads "checked". A file moves from holding to release ONLY by the check tool.

### BUILD

1. `org/devices/intake/intake_closure.py`:
   - `closure --target cp314-win_amd64`: starting from the 67 lines of the root `requirements.txt`, follow `Requires-Dist` through
     the INSTALLED copies on this machine (markers evaluated for the TARGET: python_version 3.14, sys_platform win32,
     platform_machine AMD64; extras followed only where a requirement line or a parent asks for the extra), to a fixed point.
     Reuse `org/devices/kit_python_wheels.py` for parsing, marker evaluation and tag logic (import it; do not copy it).
     For every member print and save: name, the version installed here, whether it is a LINE of `requirements.txt` or a
     dependency (and of which parents), its fit class for the target as that tool defines it (pure, fits already, compiled for
     3.12 only, no metadata), and whether the installed version satisfies every specifier that reaches it. A dependency with NO
     installed copy here is `UNKNOWN-NOT-INSTALLED` (counted, named, never guessed: its own dependencies are unread).
     Saves `org/devices/intake/closure_cp314_win_amd64.json`. LAST line
     `INTAKE-CLOSURE target=cp314-win_amd64 lines=<n> closure=<c> dependencies_added=<d> pure=<p> fits=<f> needs_fetch=<x> unknown_not_installed=<u> specifier_conflicts=<k> fixed_point=<True|False> ok=<True|False>`
     (`ok=True` when the fixed point was reached and every member has exactly one class; `unknown_not_installed` and
     `specifier_conflicts` are findings, reported, not hidden).
   - `--from-file <json>` re-prints the last line (the criterion's bounded form).
   - `explain <name>`: the chain of parents that brings a package in.
2. THE FETCH LIST, derived, in your deliverables folder as `INTAKE_BATCH_1_FETCH_LIST.md` and as
   `org/devices/intake/batch1_fetch_list.json`: every closure member whose class is "compiled for 3.12 only" for the target, with
   the exact wheel FILE NAME it would need (`{name}-{version}-cp314-cp314-win_amd64.whl`, name normalised as the wheel
   specification states; say plainly that whether that file exists on the index is UNREAD: nothing was asked), marked APPROVED
   or NOT-YET-APPROVED against the CTO's decision of 26 names
   (`org/tier1_exec/4.0.0_SA_CRO/deliverables/PACKAGE_INTAKE_ASSESSMENT_BATCH_1_30_PACKAGES_20261007.md` holds the 30 assessed;
   CTO msg 106363: 26 approved; pyarrow, pyiceberg, hdbscan and kuzu not approved at their pins). A closure member that needs a
   fetch and is not among the 30 assessed is a NEW request: list it separately; it is not approved by this cell.
3. Clause 4, BY MEASUREMENT: find how `requirements.txt` is generated (its header names the generator or the record; search the
   repository for the script and read it). Run the generator in a mode that writes to a SCRATCH path only (never over the real
   file) and report: does a regeneration reproduce the committed file byte for byte today; and what happens to a line added by
   hand (add one to a scratch copy, regenerate into scratch, compare). Then write `PROPOSAL_APPROVED_LIST_AND_REGENERATION.md` in
   your deliverables folder: the mechanism you recommend so that a reviewed addition (C-INTAKE clause 7: assessed by
   `4.0.0_SA_CRO`, decided by `1.0.0_SA_CTO`) and a regeneration do not overwrite each other (for example a second, reviewed
   input file the generator merges, with the closure as a generated lock beside it), with the measured evidence, in standard
   technical English. YOU DO NOT EDIT `requirements.txt` OR ITS GENERATOR: the proposal is for the CTO to rule.
4. One repair in `org/devices/kit_python_repack.py` (row `NFRA_CTLPLN-S21`): in `install-check`, an import that fails with
   `ModuleNotFoundError` naming a module that is NOT one of the package's own top-level modules is `import_missing_dep` (with the
   module named), not `failed`; a package whose OWN module is missing stays `failed`. Add the two cases to
   `org/devices/test_kit_python_repack.py` (its last line then reads `cases=12/12`).

### RULES FOR THIS CELL

**No request leaves this machine from anything YOU run.** No `pip install`, `pip download`, `pip index`, no `curl`, `wget`,
`npm`, `bun`. Every HTTP request your code makes in a test goes to a listener you start on 127.0.0.1. You never run your tool
against the public index: the first real fetch is the issuer's act, after the drain, on the CTO's signature.
No non-ASCII in any file you write. Standard library only unless the order names a package. Bake no absolute path and no user name.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CT5e1-AC1" cell_refs="CT-e-1"><invocation>python org/devices/intake/intake_closure.py closure --from-file org/devices/intake/closure_cp314_win_amd64.json</invocation><expect>INTAKE-CLOSURE target=cp314-win_amd64 lines=67</expect></criterion>
`CT5e1-AC1` -- the closure was computed and saved; the same line must read `fixed_point=True ok=True`.

<criterion id="CT5e1-AC2" cell_refs="CT-e-1"><invocation>python org/devices/intake/test_intake_closure.py</invocation><expect>INTAKE-CLOSURE-TEST cases=</expect></criterion>
`CT5e1-AC2` -- on synthetic installed distributions in a temporary directory: a two-level chain closes; a marker that excludes the target is not followed; an extra is followed only when asked; a missing copy is UNKNOWN-NOT-INSTALLED; a cycle terminates; a specifier conflict is counted. The line must read `ok=True` with every case passing.

<criterion id="CT5e1-AC3" cell_refs="CT-e-1"><invocation>python org/devices/test_kit_python_repack.py</invocation><expect>PY-REPACK-TEST cases=12/12 ok=True</expect></criterion>
`CT5e1-AC3` -- the label repair, with the ten earlier cases still passing.
</proof_of_spec>

<expected_criteria>CT5e1-AC1,CT5e1-AC2,CT5e1-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/NFRA_CTLPLN.TO-CT-e-1.dependency-closure.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CT5e1-AC1,CT5e1-AC2,CT5e1-AC3`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round5.md</decomp_doc>
<owned_cells>CT-e-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_closure.py
org/devices/intake/test_intake_closure.py
org/devices/intake/closure_cp314_win_amd64.json
org/devices/intake/batch1_fetch_list.json
org/devices/kit_python_repack.py
org/devices/test_kit_python_repack.py
org/devices/kit_python_wheels.py
requirements.txt
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a closure that looks complete because a missing copy was skipped (UNKNOWN-NOT-INSTALLED is a counted class); markers evaluated for the laptop's 3.12 where the Dell runs 3.14 (target evaluation, tested); an index consulted to resolve (no request leaves the machine; installed metadata only); requirements.txt overwritten by a regeneration run (scratch output only; the file is in the grant to be READ); BLIND: dependencies of packages not installed here, and whether any needed cp314 file exists on the index.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.17 @301f06300d (ADMITTED), ADDENDUM v0.15 and v0.16, contract C-INTAKE; brief
`docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md` @adc8997f1b Part V.1; CTO msgs 106327, 106363, 106372,
106424, 106436, 106445.
