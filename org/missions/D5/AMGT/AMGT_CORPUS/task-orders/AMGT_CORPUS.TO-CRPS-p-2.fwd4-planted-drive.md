# AMGT_CORPUS task order -- `CRPS-p-2` -- ROUND 14: FWD-4's two limbs, driven -- WILL-ADD and REFUSES-ambiguous on two planted folders, refusing transport, poison positive-controlled

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-p-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud act; the drive runs on a temp library under the refusing transport.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 14. Serves **FWD-4 (the induction request for an unresolved backlog name)**.

## 1. THE CELL -- `CRPS-p-2`

**Where this came from.** FWD-4's fence (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md`): *"for one backlog name the universe carries
UNRESOLVED, a single act produces the induction request: it PRINTS what the induction WILL add before anything is added, REFUSES a
name whose identity is ambiguous, and is driven end to end with a REFUSING TRANSPORT and the poison POSITIVE-CONTROLLED, so the run
COULD NOT have reached the network rather than merely having not"*. The act is `lib/research/corpus/induction_request.py`
`run(argv=None, root=None, stdout=None)`: it reads `backlog.build(root)`, takes the folders the universe carries UNRESOLVED,
gathers `(Ticker: ...)` evidence from each folder's `.docx`/`.pdf` reports (`_TICKER_LINE_RE`), classifies EVIDENCED / AMBIGUOUS /
UNPARSEABLE / NO_EVIDENCE, prints the pick, installs the poison (`install_poison`), and writes `induction_request.json` under the
module-level `DELIVERABLES_DIR`. On the live library the population is one organic name (Hitachi 6501 JP, NO_EVIDENCE); the
WILL-ADD and REFUSES-ambiguous limbs are unobserved.

**RULED -- what you build:** `lib/research/corpus/tests/test_induction_planted_drive.py` (new). It builds a SCRATCH library under pytest's `tmp_path`
with exactly two planted folders -- (a) a name that resolves to nothing in the crosswalk, whose one report carries ONE parseable
`Name (Ticker: <ROOT> <CC>)` line (the WILL-ADD arm), and (b) a name whose reports carry two DIFFERENT `(Ticker: ...)` values (the
ambiguous arm) -- plus whatever the backlog needs to read them as backlog folders. It redirects `DELIVERABLES_DIR` to `tmp_path`
(monkeypatch), calls `induction_request.run(root=<scratch>, stdout=<buffer>)` through its real entry point, and asserts: the
WILL-ADD block for (a) is printed BEFORE anything is added (nothing is added at all: no crosswalk or registrations write, no S3
write); (b) is REFUSED as ambiguous; the transport refuses and the poison positive control raises at each of its sites. After its
asserts it prints ONE line with `print()` (read with `pytest -s`), exactly:
`fwd4 will_add_before_add True ambiguous_refused True vendor_calls 0 s3_writes 0 poison_positive <k> of <k>` where `<k>` is the
number of poison sites the module installs (the live run reads 4 of 4). Do NOT edit `induction_request.py`; a limb it cannot show
is a row and a REFUSAL.

## 3. SURFACES

<paths>
lib/research/corpus/tests/test_induction_planted_drive.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-2.fwd4-planted-drive.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library on the synced drive. Scratch `.scratch/p2/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call. NO S3 write, NO write to the live library, NO crosswalk or registrations write; the drive writes only under tmp_path.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p2_AC1.sh</invocation><expect>(?m)^fwd4 will_add_before_add True ambiguous_refused True vendor_calls 0 s3_writes 0 poison_positive 4 of 4$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p2_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the driven exercise's line; AC2 the drive and the existing induction tests pass; AC3 the bound: nothing outside your grant.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-p-2.fwd4-planted-drive.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line and what each planted folder's report text was.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-13 analysis s.4 item 2 @`f1c482d24f` (msg 26603). Checks dry-run at the base `dbafd14c52`: p2_AC1 FAIL (no drive line); p2_AC2 FAIL (no tests ran); p2_AC3 PASS (paths_outside_grant 0).
Hitachi 6501 JP (Z-S58) stays the organic negative arm; not re-driven.
<risk>LOCAL</risk>
<status>complete</status>
<round>14</round>
<slot>~2</slot>
<fabric>site-z</fabric>
