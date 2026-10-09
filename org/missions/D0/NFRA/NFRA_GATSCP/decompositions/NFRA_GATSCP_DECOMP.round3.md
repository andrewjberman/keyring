# NFRA_GATSCP decomposition -- ROUND 3, the remediation rows of the round-2 analysis (issuer 2.0.0_SA_COO~N1; cut 2026-10-09)

**Status: CUT for one issuance.** FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round2.md` @0ef2dc8325 with ADDENDUM 1 (1.0.0_SA_CTO~DELL1): FWD-1..FWD-7 REALIZED; section 3, five
items (R2-R6); R7 (D1-S12) landed by 4.0.0_SA_CRO~A @6f91f8fafb; FWD-5 graded on MSTR~DELL1's driven pass (msg 2481). Plus row
D1-S5's fix, which CTO msg 2258 cut "at the next issuance after round 2's cut" and the analysis's list omits. PRD v0.2.

## Measured at the base (box/dell1 642c914b19, 2026-10-09 ~13:4xZ; read-only agent at 2baefcde83 plus the issuer's dry runs)

1. **The POINTER limb is in the ROW gate, not to-pipeline-gate.** Rows D1-S4/S11 and R2 name `to-pipeline-gate.py`; the census that
   counts a seat-home POINTER as an open order is `.tools/surprise-row-gate.py` `_open_tos_census` (:1282-1327), reached from
   `_route_precondition_violations` (:1826). It enumerates `*/task_orders/<CODE>.*.md` and tree orders; a file with no `<status>`
   reads `<no status tag>`, is not terminal, and counts. The overrides used were SURPRISE-ROW-OVERRIDE lines. The cell is placed on
   the file that holds the limb (an issuer re-point inside the decomposition; R2's outcome unchanged). to-decomp-ref-lint's seating
   census skips the POINTER already (no `<issued_to>` tag).
2. **CRLF.** `to-pipeline-gate.py` reads blobs as bytes and decodes without normalising (`_staged_blob` :2988; `_head_blob` :2979,
   which shadows a text-mode twin at :2156); `PLACEHOLDERS_TAG_RE` (:183), `STATUS_ELEMENT_RE` (:1301), `ROUND_ELEMENT_RE` (:2039),
   `WORKSTREAM_ELEMENT_RE` (:2046), `DIRECT_ACT_ELEMENT_RE` (:2064) end `[ \t]*$` under re.M and cannot match before `\r`. Dry run:
   a CRLF-only edit of a pending order refuses (rc 1) where the LF edit passes (rc 0).
3. **round-close-check** matches the whole status text against `STATUS_WORDS` (:270-277) and counts `done` as `status ==
   "complete"` (:435); TO-BF-aa-1's `<status>complete -- landed by ...</status>` reads as no status, so LGIC_BLANKFIX round 12 reads
   complete=0, judgment=0 although the order is complete with a `judgment="true"` criterion. Round 13 reads orders=3 judgment=1;
   DSGN_AMGTV1 round 65 orders=1 judgment=1. Terminal sets disagree across tools; the spine defines terminal by proof, not a word.
4. **Crossbox custody.** DEVICES_CROSSBOX (`.owned-paths.yaml:822-827`) admits 0.0.0_AB_MSTR, 1.0.0_SA_CTO, 2.0.0_SA_COO~C. The
   validator (`owned-paths-validate.py` `check_agent` :289) has no per-record permit; the worker `<paths>` grant covers only
   `0.9.0_WK_*` serials. `crossbox-call.py` `ack` writes ack.at/ack.by on the receiving box and commits nothing.
   `merge-resolve-known.py` knows three classes (channel, generated index, APPEND_ONLY); a crossbox JSON is "not a known
   multi-writer class". `crossbox-call.py merge --id --ref` already folds fields and refuses a field both sides hold differently.
5. **safe-merge --continue** commits at :850 and then runs `_verify_merge_tree HEAD` (:867), which on conflicted parents only WARNs
   on a partial drop (:304-307); nothing compares the committed paths with the merge's staged set (`$STATE`). Self-test: 28
   structural arms, none on committed vs staged; `.tools/exercise-safe-merge-continue.sh` exists.
6. **The seven gates** (D1-S7): `.tools/commit_gate_runner.py`, `.tools/to-pipeline-gate.py`, `.tools/to-decomp-ref-lint.py`,
   `.tools/git-hooks/owned-paths-check.sh`, `.tools/git-hooks/mstr-ledger-check.sh`, `.tools/git-hooks/pipescript-suite-check.sh`,
   `rcg/bin/manifest_check.py`. Logs: `org/to-pipeline-override-audit.log` (`TS | author | path | reason`),
   `org/git-author-override-audit.log` (PASS/BLOCK/OVERRIDE/SURPRISE-ROW-OVERRIDE/FORCE-BYPASS/MERGE-REFUSED lines),
   `org/tier0/audit/ledger-hook-audit.log`; `org/pipescript-suite-gate-audit.log` only in `org/audit/archive/**`; no rcg log.

## Rule 24 record

**The cell set.** Domain: the analysis's five items plus the CTO-cut remediation D1-S5. Subtraction:

| item | cell |
|---|---|
| R2 POINTER (D1-S11, D1-S4) | `GS-f-1` (surprise-row-gate.py) |
| R4 CRLF (D1-S6) | `GS-f-2` (to-pipeline-gate.py) |
| R3 round-close-check (D1-S9) | `GS-f-3` |
| R5 crossbox custody + resolver (D1-S10, Z-S1) | `GS-f-4` |
| R6 seven-gate census (D1-S7) | `GS-f-5` (read-only) |
| D1-S5 --continue partial (msg 2258) | `GS-f-6` |

Six items, six cells. R7 is landed and FWD-5 graded; neither is cut. Same grain: one tool and its test per cell. State: every cell
`NOT_EVALUATED` at the cut.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule is created or changed by any cell.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- no IAM; GS-f-4 changes a repository lane permit, not a cloud grant.
- `comp-adversary`: RUN, in the cut's own arms: GS-f-1 keeps a real open order counted; GS-f-2 keeps a real CRLF defect refused;
  GS-f-4 refuses another lane's record and a same-field clash; GS-f-6's test carries a planted-partial arm. BLIND: GS-f-5 is a
  census, its conclusions are the CTO's.

## The cells

| cell | what | rows | placement | risk | status |
|---|---|---|---|---|---|
| `GS-f-1` | the row gate's open-order census never counts a file carrying `# pipeline-override: this file is a POINTER` (or headed `# POINTER (not an order)`) as an order; a real open order still counts | D1-S11, D1-S4 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-f-2` | to-pipeline-gate normalises CRLF to LF on every blob read (staged, HEAD), so an order that differs only in line endings grades the same | D1-S6 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-f-3` | round-close-check reads an order's status by its leading word against the shared terminal set, so `complete -- landed by ...` is complete and its judgment criteria count | D1-S9 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-f-4` | a crossbox record's receiving lane may commit its own record (the validator reads the staged record's `to_serial`), never another's; the integrate resolver folds a crossbox record written on both ends by field and refuses a same-field clash | D1-S10, Z-S1 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-f-5` | a read-only census of the seven gates: what each reads against the act's write set, and its false refusals and audited overrides in the last seven days, from the logs | D1-S7 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-f-6` | `safe-merge.sh --continue` exits non-zero, naming the missing paths, unless the merge commit carries every path the conflicted merge staged | D1-S5 | dell1 | LOCAL | NOT_EVALUATED |

## Interfaces fixed at the cut

- `owned-paths-validate.py --check-path <agent> <path>`: prints `PERMIT` or `REFUSE <reason>`, exit 0 / 1; reads a crossbox record
  from the index git resolves.
- `merge-resolve-known.py`: a fourth class, `org/devices/crossbox/XB-*.json`, printed `RESOLVED <path> <blob> crossbox-fold`.
- `safe-merge.sh --continue`: on a partial commit, exit non-zero with `safe-merge: REFUSED -- the merge commit lacks N staged
  path(s): ...`.

## Dependency edges

None. M = 6 chains.

## Write sets (disjoint)

- **GS-f-1:** `.tools/surprise-row-gate.py`. **GS-f-2:** `.tools/to-pipeline-gate.py`. **GS-f-3:** `.tools/round-close-check.py`.
- **GS-f-4:** `.tools/owned-paths-validate.py`, `.tools/merge-resolve-known.py`.
- **GS-f-5:** its deliverables folder only. **GS-f-6:** `.tools/safe-merge.sh`, `.tools/tests/test_safe_merge_continue.py`.
- Each: the project's `surprise-channel/investigations/INVESTIGATION_v1.md` (append-only; the merge unions it).

## The checks (dry-run at the base box/dell1 642c914b19)

`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/`.

| check | cell | base |
|---|---|---|
| `r3_pointer.py` | GS-f-1 AC1 | FAIL as expected (the POINTER is in the open list; the real open order arm PASS) |
| `r3_crlf.py` | GS-f-2 AC1 | FAIL as expected (CRLF-only edit rc 1 where LF rc 0; the defect arm PASS) |
| `r3_close_terminal.py` | GS-f-3 AC1 | FAIL as expected (LGIC r12 complete=0 judgment=0; r13 and DSGN r65 controls PASS) |
| `r3_xbox_custody.py lane` | GS-f-4 AC1 | FAIL as expected (no --check-path) |
| `r3_xbox_custody.py resolver` | GS-f-4 AC2 | FAIL as expected (not a known multi-writer class; the clash arm PASS) |
| `r3_census.py` | GS-f-5 AC1 | FAIL as expected (no report) |
| `.tools/tests/test_safe_merge_continue.py` (built by the cell) | GS-f-6 AC1 | FAIL as expected (absent) |
| `r1_fastlane.py` | GS-f-6 AC2 | PASS as expected (a control: the self-test stays green) |

## The close

Round 3's analysis is the close read (ADDENDUM 1). The issuer's real run at the close: a NEW remediation row commit beside the live
POINTER files (GS-f-1, no override), and one drain that ends through `--continue` (GS-f-6), recorded in the trace.
