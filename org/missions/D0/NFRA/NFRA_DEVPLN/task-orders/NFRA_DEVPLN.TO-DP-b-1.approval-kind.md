# TO NFRA_DEVPLN.TO-DP-b-1 -- round 1 THREAD DP-b-1: the `approval` kind in open-calls (add, close with a decision, approval-status)

<to_id>NFRA_DEVPLN.TO-DP-b-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-b-1` (`decompositions/NFRA_DEVPLN_DECOMP.round1.md`) | **outcome_ref:** FWD-2, FWD-4 |
**depends_on:** none (your slot's next order, `DP-b-5`, edits the same file after this one)

---

## WORKER FACE

### THE CELL

A portal feature waiting for approval is ONE row of kind `approval` on the building box's open-calls list (`org/devices/state/<box>/open_calls.json`, with
its S3 cluster copy that the tool already writes). Andrew closes the row `approved` or `declined`; the merge-forward and the promote read that row. Today
`.tools/open-calls.py` line 88 reads `KINDS = ("fork", "act")` and line ~462 refuses a kind not in it. Row validation is around line 462, `add` around lines
740-790, listing around lines 800-910, the `add` parser around line 1360, and the closing logic is in the same file (read it; `comp-read .tools/open-calls.py --for "close command"`).

### BUILD

1. Add `approval` to `KINDS`. Every existing `fork`/`act` behaviour stays byte-identical; a row without `kind` still reads `fork`.
2. `add --kind approval` takes `--project NFRA_DEVPLN --box <box> --branch cand/<box>/<slug> --purpose "<text>" --pages "<p1,p2>" --class client-facing|opal-internal|test-only
   --how "<how to look at it>"`; `--subject` is optional for this kind (default `approval: <branch>`); the context/recommendation text rules for `fork` do not apply to it
   (purpose and how are its text). The row stores `kind: "approval"` and `approval: {box, branch, purpose, pages[], class, how, head_sha, commits}`; `head_sha` and `commits` are
   written as `null` by THIS order (your next order, `DP-b-5`, computes them), and `--branch` must match `cand/<box>/<slug>` with `<box>` equal to `--box`. A bad class or a bad
   branch name is refused with a message naming the field, rc 2, and nothing is written. The row is written to the box's list as every other row is.
3. `close <id> --ruled-by andrew|cto --ruling-file <path> --decision approved|declined` (the existing close plus `--decision`, required for an `approval` row, refused on any other kind).
   The closure stores `closed: {at, by, ruling, decision, ruled_by}` where `by` is the closing identity string (for `andrew` the string `andrew`; for `cto` the serial in `$OPAL_AGENT_SERIAL`).
4. `python .tools/open-calls.py approval-status --branch <b> [--store-dir <dir>]` prints exactly ONE line:
   `APPROVAL branch=<b> state=<ABSENT|OPEN|APPROVED|DECLINED> valid=<yes|no|-> row=<id|-> by=<who|-> head_sha=<sha|-> commits=<n|-> class=<client-facing|opal-internal|test-only|-> box=<box|-> pages=<p1,p2|->`
   (`-` for an unknown field). The box comes from the branch name. The store is that box's `org/devices/state/<box>/open_calls.json` in the working tree, else
   `git show origin/box/<box>:org/devices/state/<box>/open_calls.json`; `--store-dir <dir>` (a directory holding `<box>/open_calls.json`) overrides both, for tests. The newest row by `opened_at`
   for the branch wins. No row: `state=ABSENT valid=-`, rc 0. A store file that is absent for a box with no list, or unreadable JSON: print `APPROVAL branch=<b> state=UNREADABLE ...` and exit rc 2
   (never print ABSENT for a store you could not read).
   `valid=yes` ONLY when `state=APPROVED` and `by` satisfies the class: client-facing needs `by` equal to `andrew` (case-insensitive) or starting `FAST lease`; opal-internal needs `andrew`, a serial
   containing `_SA_CTO`, or `FAST lease`; test-only accepts any APPROVED. Otherwise `valid=no` (and `-` when the state is not APPROVED).
5. The Rule 24 record for the enum widening, at `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/APPROVAL_KIND_RULE24_RECORD_20261013.md`, with four level-2 headings exactly
   `## MECE`, `## SAME GRAIN`, `## INTENT COHERENCE`, `## STATE COHERENCE`. MECE states the domain (the kinds of an open-calls row: `fork` = a decision with options, `act` = an act only Andrew can
   do, `approval` = a feature waiting for his yes or no) and shows the subtraction against a printed denominator: run one census of `"kind"` values over `org/devices/state/` (use `comp-find` with a
   pathspec, `-i`, and paste its printed denominator line). STATE COHERENCE names what closing does NOT move (a declined feature stays on its branch; closing writes no merge).

### RULES FOR THIS CELL

Your tests never touch the live lists or S3: they run `open-calls.py` against a temporary `--store-dir` / temporary repo and set whatever option or environment the tool already offers to skip the
cluster copy (read how its S3 put is made; if it has no switch, make the test replace the put function and say so in your report). You change no row of the real
`org/devices/state/*/open_calls.json`. No push, no merge, no rebase. No non-ASCII in any file. Python standard library only; `ruff check` clean on the two files you edit or add under `.tools/`.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPb1-AC1" cell_refs="DP-b-1"><invocation>python .tools/tests/test_open_calls_approval.py</invocation><expect>ok=True</expect></criterion>
`DPb1-AC1` -- you write this test. It prints a last line `OPEN-CALLS-APPROVAL-TEST cases=<k>/<n> ok=True` and its cases are: add makes an OPEN row; close approved by andrew on a client-facing row reads
`APPROVED valid=yes`; close approved by a CTO serial on a client-facing row reads `valid=no`; the same on an opal-internal row reads `valid=yes`; close declined reads `DECLINED valid=no`;
a branch with no row reads `ABSENT`; unreadable JSON exits rc 2 and does not print ABSENT; a bad class and a bad branch name are refused with nothing written; a `fork` add and a row without `kind` behave as before.

<criterion id="DPb1-AC2" cell_refs="DP-b-1"><invocation>python .tools/open-calls.py approval-status --branch cand/laptop/none-9</invocation><expect>APPROVAL branch=cand/laptop/none-9 state=ABSENT valid=-</expect></criterion>
`DPb1-AC2` -- the seam against the REAL laptop list (a read; nothing written).

<criterion id="DPb1-AC3" cell_refs="DP-b-1"><invocation>grep -c -E "^## (MECE|SAME GRAIN|INTENT COHERENCE|STATE COHERENCE)$" org/missions/D0/NFRA/NFRA_DEVPLN/ledger/APPROVAL_KIND_RULE24_RECORD_20261013.md</invocation><expect>^4$</expect></criterion>
`DPb1-AC3` -- the record carries all four postulates.
</proof_of_spec>

<expected_criteria>DPb1-AC1,DPb1-AC2,DPb1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-b-1.approval-kind.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPb1-AC1,DPb1-AC2,DPb1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.
Your slot's NEXT order (`DP-b-5`) is a separate file the issuer hands you after this one drains; do not start it early.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md</decomp_doc>
<owned_cells>DP-b-1</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_approval.py
org/missions/D0/NFRA/NFRA_DEVPLN/ledger/APPROVAL_KIND_RULE24_RECORD_20261013.md
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee C-APPROVAL, S01; ratified-text SIGNED by 3.0.0_SA_CVO~L (current). Issuer rulings R3 (class rule in `approval-status`) and R5 (pinned interface) in the decomposition.
