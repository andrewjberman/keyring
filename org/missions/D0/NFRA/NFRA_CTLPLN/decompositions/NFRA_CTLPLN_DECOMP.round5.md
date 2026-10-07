# NFRA_CTLPLN decomposition -- ROUND 5: the checked package route, FWD-15's thread (issuer 2.0.0_SA_COO~C; cut 2026-10-07 ~18:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.17 @301f06300d, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN` at the cut: ratified-text SIGNED,
current). Carrier: ADDENDUM v0.15 ("The thread of this addition (round 5 builds it; every later round enriches): FWD-15 on
`PyYAML==6.0.3` for one dell2 lane, then the other 29 packages of the first batch by the same route") and v0.16; contract
C-INTAKE; CTO msgs 106327, 106363 (26 approved), 106372 ("cut the thread now ... The tool takes a platform tag"), 106424 (the
Dells stay on Python 3.14), 106436 (site Z's Windows file joins), 106445 ("close the list before round 5 fetches").

**Round 4 has drained as builds:** every round-4, KIT and ACCESS order is `complete` with a VALID instance at HEAD. Two issuer
acts of round 4 are still open and are NOT this round's: order `NFRA_CTLPLN.TO-APPLY-8` (dell1's scoped fence join, with
`0.7.0_AE_CloudOps~E`) and the transcripts key apply (the CTO half is owed).

**NOT in this round, said at the cut as the CTO asked (msg 106457):** FWD-20's thread (one real Teams request end to end) has a
dedicated COO on a Dell; it is not this lane's and no cell here serves it. FWD-16 to FWD-19 beyond what the thread itself needs
(the request form, the stop on a box that tries to fetch, the waiting-lane view) and FWD-21 to FWD-25 are later rounds'
enrichment.

## The thread, as hops (FWD-15: one real package taken the whole way for one Dell lane, and the lane's work then runs)

| hop | what happens | exists today | this round |
|---|---|---|---|
| 1 | the list of approved packages is closed under dependencies | no: 73 omitted (row S18) | `CT-e-1` |
| 2 | the laptop fetches the ONE exact file into a holding folder, with a record | no | `CT-e-2` |
| 3 | checks 1 to 7 are made and recorded with what each leaves; the CTO signs (check 8); the file is released | no | `CT-e-3` |
| 4 | the file goes to the Dell over the private network | yes: the CTO's carry, as for the kits | issuer act |
| 5 | the Dell installs it with no index, imports it, sends a receipt | partly: the kit's install check | `CT-e-4` |
| 6 | the Dell lane's own work runs | the lane's | issuer read at the close |

**Rule 24.** Domain: the hops a package crosses between "approved" and "a Dell lane's work runs". Subtraction from the six hops
above: 1, 2, 3 and 5 are cells; 4 and 6 are named as issuer acts with an owner; none is unowned. Same grain: each cell is one
tool with its test. One intent each. State coherence: this round moves no installed package on any box and fetches nothing; the
first real fetch is an issuer act after the drain.

## Cells

| cell | what | serves | carrier | risk | slot |
|---|---|---|---|---|---|
| `CT-e-1` | the dependency closure for the Dells' Python from installed metadata, the derived fetch list, the measured read of how the approved list is regenerated with a proposal, and one label repair in the kit's install check | FWD-15, FWD-16 | C-INTAKE 2, 4; msg 106445 | LOCAL | ~13 |
| `CT-e-2` | the fetch tool: one exact file by name and tags (any platform tag) into the holding folder, closed host set, digest against the index, a record on every path; refuses the public index without a signed approval file | FWD-15, FWD-19 | C-INTAKE 2, 3; msg 106372 | LOCAL | ~14 |
| `CT-e-3` | the check tool: the brief's eight checks in order with what each rules out and leaves, the check record, release only when checked and signed, the delivery text, the pack for the carrier | FWD-15, FWD-17 | C-INTAKE 1 | LOCAL | ~6 |
| `CT-e-4` | the receiving box's tool: verify the pack, install with no index into scratch, import, receipt; refuse anything not checked | FWD-15 | C-INTAKE 5 | LOCAL | ~8 |

## Edges and fan-out

The four cells exchange FILES in a format fixed in this document's seam (repeated verbatim on each order's face): the fetch
record, the check record, the receipt, and the holding and release folders. No cell imports another cell's code, and no cell
writes a file another writes. So there is no build dependency: four chains of one. `fanout: 4 of 4 chains, cap 8`.
The seam is exercised END TO END by the issuer at the drain, not by any worker: one synthetic wheel through the fetch tool
against a loopback index, the check tool, the pack, and the receive tool, on the merged trunk.

## Write set (disjoint)

- `CT-e-1`: `org/devices/intake/intake_closure.py`, its test, `closure_cp314_win_amd64.json`, `batch1_fetch_list.json`;
  `org/devices/kit_python_repack.py` and its test (the label repair). Reads `requirements.txt` and `kit_python_wheels.py`.
- `CT-e-2`: `org/devices/intake/intake_fetch.py`, its test, `README.md`, `records/`.
- `CT-e-3`: `org/devices/intake/intake_check.py`, its test. Reads the brief.
- `CT-e-4`: `org/devices/intake/intake_receive.py`, its test.
Hookups owned by no cell (the issuer's, at the merge): none are needed; the README is `CT-e-2`'s.

## The seam (verbatim on every order)

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

## The issuer's acts after the drain

1. THE SEAM RUN on the merged trunk: a synthetic wheel through all four tools against a loopback index; then the three
   criteria-bearing tests and the repo-wide hygiene once.
2. The closure and the fetch list go to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`: any closure member that needs a fetch and is not
   among the 30 assessed is a new request by C-INTAKE clause 7. The regeneration proposal goes to the CTO to rule.
3. THE FIRST REAL FETCH, `PyYAML==6.0.3` for cp314 win_amd64: an act of this seat ONLY on (a) the CTO's signed batch approval
   file naming it, and (b) the CTO's answer to one question this seat puts at the cut: whether Andrew's recorded word for the
   checked route covers each fetch, or a per-use word is wanted for the first. CLAUDE.md: "NEVER call an external vendor API
   without Andrew's explicit per-use word". The public package index is off Opal's infrastructure; this seat does not decide
   that question for itself.
4. Checks 1 to 7 on the held file; the record to the CTO for check 8; release; the pack to the CTO as carrier; dell2 runs
   `verify` and `prove`, sends the receipts, installs; the dell2 lane's work runs: FWD-15's read, EXERCISED on the real route.

## Verification diet

Each order carries two or three mechanical criteria: the built behaviour and one difference control (the fetcher cannot reach
the public index on a bare call; the checker cannot reach "checked" unsigned; the receiver refuses an unchecked file).
Repo-wide hygiene and the seam run are the issuer's at the drain.
