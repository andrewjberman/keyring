# TO IRPT_ANLREQ.TO-AR-y-388.armed-row-evidence-audit-b -- a READ-ONLY audit of 21 armed surprise rows that name 2.0.0_SA_COO~Y2 as disarm owner: for each row, whether its hazard still stands at the current tree and the records, with the evidence that decides it; no row is dispositioned by the worker and nothing is edited outside its own deliverables

<to_id>IRPT_ANLREQ.TO-AR-y-388</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~288</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ49</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of the tree and of committed records; no write outside the worker's deliverables folder and the channel)
**Decomp cell:** `AR-y-388` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the L10 gate: every ARMED row dispositioned) | **depends_on:** none (base: current branch HEAD)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~288`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-288` (branch `wk-IRPT_ANLREQ-288`), provisioned by the issuer from the current branch (sparse; it holds `.tools/`, `lib/` and `org/missions/D9/IRPT/IRPT_ANLREQ`). Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~288 <0.9.0_WK_IRPT_ANLREQ~288@opal.agent>" -F <msgfile> -- <paths>`. Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md`; this cell appends nothing to it unless it files a row (id `IRPT_ANLREQ-D2-W288-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, APPEND only, 0 deletions). Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add. No live call, no AWS call, no push. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.
- Read the tree ONLY with `git show HEAD:<path>` or `git grep ... HEAD -- <pathspec>` (the worktree is sparse, so a missing file on disk proves nothing). A verdict that rests on a file read from the sparse disk is invalid.

### THE CELL (`AR-y-388`, inlined)

*Context. Before the L10 slug can go to the CTO, every ARMED surprise row must be dispositioned (CLAUDE.md rule 27). 21 of the project's armed rows name `2.0.0_SA_COO~Y2` as the disarm owner; the issuer dismisses a row only on evidence that its hazard no longer stands. This cell collects that evidence; it dispositions nothing. The rows (id, full text) come from `python .tools/comp-surprise.py --project IRPT_ANLREQ --json` (keys `items` and `armed`; read `one_line`, `spec_asserts`, `world_is`, `disarm_owner`, `surfaced_at`; an id can appear twice, once as the investigation row and once as a REMEDIATION entry: read the investigation row).*

**The rows:** IRPT_ANLREQ-D2-W128-S3 IRPT_ANLREQ-D2-W129-S1 IRPT_ANLREQ-D2-S100 IRPT_ANLREQ-D2-W133-S1 IRPT_ANLREQ-D2-W133-S4 IRPT_ANLREQ-D2-W136-S2 IRPT_ANLREQ-D2-W141-S1 IRPT_ANLREQ-D2-W141-S2 IRPT_ANLREQ-D2-W145-S1 IRPT_ANLREQ-D2-W145-S5 IRPT_ANLREQ-D2-W145-S6 IRPT_ANLREQ-D2-W145-S8 IRPT_ANLREQ-D2-W144-S1 IRPT_ANLREQ-D2-W146-S4 IRPT_ANLREQ-D2-W147-S2 IRPT_ANLREQ-D2-W148-S1 IRPT_ANLREQ-D2-S118 IRPT_ANLREQ-D2-W150-S2 IRPT_ANLREQ-D2-W150-S3 IRPT_ANLREQ-D2-W155-S2 IRPT_ANLREQ-D2-W166-S1

1. **For each row, decide ONE verdict** and write it to `r47/AUDIT_b.json` in your deliverables folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~288/`), a list with one object per row: `id`, `verdict` (one of `CLOSED`, `STANDS`, `NEEDS-LIVE-READ`), `hazard` (one line, your words), `evidence` (a list; each item is `{"kind": "code"|"record"|"commit", "ref": "<path:line at HEAD>" | "<committed record path>" | "<sha>", "says": "<what the cited bytes show, <= 200 chars>"}`), `deployed` (`yes`|`no`|`n/a`|`unread`: whether a DEPLOYED artifact is involved and whether a committed apply or ledger record shows a release built after the remedy carries it), and `reason` (<= 400 chars).
2. **The evidence rule (binding).** `CLOSED` needs (a) the remedy visible in the tree at HEAD (`code` evidence with the `path:line` and the bytes), AND (b) when the hazard is in a deployed artifact (a Lambda, the resident host, the portal on PROD or DEV), a `record` showing a deploy of a release whose build is later than the remedy commit (an apply or deploy-ledger file under `org/tier2_senior/` or `org/critical_paths/change_management/` with status CLOSED, or an IB2/AQ2 after-read). Without (b) on a deployed hazard the verdict is `NEEDS-LIVE-READ` and `reason` names the read. A row whose hazard is a process or a closed round's artifact with no live consumer may be `CLOSED` on the tree and the order records alone: say so in `reason`. `STANDS` needs the line that shows the hazard is still present. Never infer from the row's own text; the row is the claim, not the evidence. A row you cannot read to a verdict is `NEEDS-LIVE-READ` with `reason` naming what stopped you.
3. **Write `r47/audit_check.py`** (python, stdlib only): it loads `r47/AUDIT_b.json` and prints `AUDIT-OK <n> rows <c> CLOSED <s> STANDS <l> NEEDS-LIVE-READ` only when (i) the ids are exactly the 21 listed above, each once, (ii) every verdict is in the enum, (iii) every `CLOSED` row carries at least one `code` evidence item and, when `deployed` is not `n/a`, at least one `record` item, (iv) every `ref` resolves: a `path:line` item's path exists at HEAD (`git cat-file -e HEAD:<path>`) and has at least that many lines, a `record` path exists on disk or at HEAD, a `commit` sha resolves (`git cat-file -e <sha>^{commit}`); otherwise `AUDIT-BAD <why>` and exit 1.
4. **Control.** `audit_check.py` must have a mode `--selftest` that writes a temporary copy of the audit in which one `CLOSED` row's only `code` ref points at a path that does not exist, runs the checks on it and prints `CONTROL-FIRES` only when that copy is rejected (and removes the copy).
5. **In your report:** the counts per verdict and, for every `CLOSED`, the one line that decided it.

### ACCEPTANCE

<criterion id="AR388-AC1" cell_refs="AR-y-388"><invocation>python C:/dev/wk-irpt-anlreq-288/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~288/r47/audit_check.py</invocation><expect>^AUDIT-OK </expect></criterion>
`AR388-AC1`: the completeness, enum, evidence-shape and ref-resolution check of step 3.

<criterion id="AR388-AC2" cell_refs="AR-y-388"><invocation>python C:/dev/wk-irpt-anlreq-288/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~288/r47/audit_check.py --selftest</invocation><expect>CONTROL-FIRES</expect></criterion>
`AR388-AC2`: the control of step 4 (a CLOSED row with a dead reference is rejected).

<criterion id="AR388-AC3J" cell_refs="AR-y-388" judgment="true"/>
`AR388-AC3J` (judgment, graded at L9, never by you): each verdict follows the evidence rule; no `CLOSED` rests on the row's own text or on a file read from the sparse disk; every `NEEDS-LIVE-READ` names the read; nothing outside the deliverables folder was edited; and the record says plainly what it did not read.

<expected_criteria>AR388-AC1 AR388-AC2 AR388-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~288/` and this order's file (status flip only). Read everything else with `git show HEAD:` / `git grep ... HEAD`. No push, no live call, no row dispositioned.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-388</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~288/IRPT_ANLREQ.TO-AR-y-388.armed-row-evidence-audit-b.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-388`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR388-AC1,AR388-AC2,AR388-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of the tree and committed records; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the issuer's own five dismissals (D2-S168 to D2-S172) and the traps they met against the cell; the lens: a CLOSED verdict resting on a source line while the deployed artifact predates it, a file read from the sparse disk that is simply absent there, a row read from its own text, a REMEDIATION entry mistaken for the investigation row, a dead evidence reference passing the check. The cell requires the remedy at HEAD, a later deploy record for a deployed hazard, refs that resolve, and a control that fires. NOT seen (blind): any live state; denominator: 21 rows, 2 mechanical checks, 1 control.
</preflight>

---

## RECORD FACE

- Cut by the issuer while window 5 and the Retry wait on other seats; the output feeds the issuer's per-row dismissal rows (the issuer re-reads the cited bytes of every `CLOSED` before it writes one). Workstream `ZZ49` of round 43. Base: the audit files and the checker are absent, so `AR388-AC1` and `AC2` FAIL as expected.
- The nine GRADUATED rows (S26, W52-S24, W52-S29, W52-S31, W52-S33, W52-S35, W52-S36, W61-S2, W64-S6) are disarmed by the CVO at L8 through the REMEDIATION entries; their audit lines give the CVO the evidence.
