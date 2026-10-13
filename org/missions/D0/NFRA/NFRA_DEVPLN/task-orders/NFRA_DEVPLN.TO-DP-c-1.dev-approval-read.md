# TO NFRA_DEVPLN.TO-DP-c-1 -- round 2 ENRICHMENT DP-c-1: FWD-4's per-commit read of portal DEV (approved with its feature and approver, or UNAPPROVED)

<to_id>NFRA_DEVPLN.TO-DP-c-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-c-1` (`decompositions/NFRA_DEVPLN_DECOMP.round2.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-4: for every commit on portal DEV, anyone can tell which approved feature it belongs to and who approved it; a commit on DEV with no approval behind it is visible as such, never silently mixed in. Since the settlement
commit `63c4f9e35f259ad76071b1099aeb9dddb150409f` (DEV = PROD there), a feature reaches DEV only as a two-parent MERGE commit whose message body ends with two trailers, `Feature: <branch>` and `Approved-By: <who> @<row id>`
(built by `.tools/portal-merge-forward.sh`; read it for the exact form). Build the read. MEASURED at the cut: `origin/DEV` is `a577cba5`, 7 commits ahead of PROD, from three merge commits by a dell2 manager that carry no trailer,
so the real read must show them as UNAPPROVED. Your worktree has the portal repo at `portal/` with `origin/DEV` and `origin/PROD` present (do not fetch).

### BUILD

`python .tools/portal-dev-approval-read.py [--portal portal] [--ref origin/DEV] [--since <sha>]` and `python .tools/portal-dev-approval-read.py --selftest`. Standard library only; every git call is a read, run as `git -C <portal> ...`.

1. `--since` defaults to the settlement commit above (a constant with a comment naming it). If `--since` is not an ancestor of `--ref`, print `DEV-APPROVAL result=REFUSED reason=since-not-ancestor` and exit 3.
2. Walk `git rev-list --first-parent <since>..<ref>`, oldest first. For each commit read the full message body. It is APPROVED only when the body carries both a `Feature: <x>` line and an `Approved-By: <who> @<row>` line; otherwise UNAPPROVED. Print one line per commit:
   `DEV-COMMIT <8-char sha> APPROVED feature=<x> by=<who> row=<id>` or `DEV-COMMIT <8-char sha> UNAPPROVED author=<author name> subject=<first 60 chars>`.
3. The LAST stdout line: `DEV-APPROVAL since=<8-char sha> ref=<ref> first_parent_commits=<t> approved=<a> unapproved=<u>` where `t` equals `git rev-list --first-parent --count <since>..<ref>` and `a + u = t`. Exit 0 whatever `u` is (the read reports, it does not gate).
4. `--selftest` builds a temporary repository with a settlement commit then: a two-parent merge carrying both trailers (APPROVED), a merge with only `Feature:` (UNAPPROVED), a plain commit (UNAPPROVED), and a merge whose body quotes the word `Approved-By` mid-sentence without a trailer line (UNAPPROVED); and a `--since` that is not an ancestor (REFUSED). Last line `DEV-APPROVAL-SELFTEST cases=<k>/<n> ok=True|False`.

### RULES FOR THIS CELL

Read only: no fetch, no push, no write to the portal repo; the only files you write are the two in `<paths>`. No non-ASCII. Ruff clean on the tool and its test.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPc1-AC1" cell_refs="DP-c-1"><invocation>python .tools/portal-dev-approval-read.py --selftest</invocation><expect>ok=True</expect></criterion>
`DPc1-AC1` -- the self-test above, every case passing.

<criterion id="DPc1-AC2" cell_refs="DP-c-1"><invocation>python .tools/portal-dev-approval-read.py --portal portal</invocation><expect>DEV-APPROVAL since=63c4f9e3</expect></criterion>
`DPc1-AC2` -- the live read against the real portal refs; the unapproved dell2 merges appear as UNAPPROVED lines.

<criterion id="DPc1-AC3" cell_refs="DP-c-1"><invocation>bash org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/2.0.0_SA_COO~DV/checks/check_devpln_devread.sh portal</invocation><expect>DEVREAD-COUNTS-MATCH</expect></criterion>
`DPc1-AC3` -- the issuer's independent denominator: the tool's `first_parent_commits` equals `rev-list --first-parent --count` read directly, and `approved + unapproved` equals it (the check script is the issuer's; run it, do not edit it).
</proof_of_spec>

<expected_criteria>DPc1-AC1,DPc1-AC2,DPc1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-c-1.dev-approval-read.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPc1-AC1,DPc1-AC2,DPc1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round2.md</decomp_doc>
<owned_cells>DP-c-1</owned_cells>
</decomp_ref>

<paths>
.tools/portal-dev-approval-read.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-c-1.dev-approval-read.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations and the trailer grammar in portal-merge-forward.sh; BLIND to the filesystem around the cited paths. Finding inlined: a body that quotes Approved-By mid-sentence must not count as a trailer (selftest case).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `ledger/ROUND_ANALYSIS.round1.md` @14a0501ee5 item 5; PRD `prd/NFRA_DEVPLN_PRD.md` v0.3 @14a0501ee5 FWD-4 and C-MERGE-FORWARD; ratified-text SIGNED (current). Portal worktree: this order needs `--portal-ref` at the spawn.
