# TO NFRA_CTLPLN.TO-CT-z-1 -- round 10 CT-z-1: thread-trace can read the thread of ONE order, so a round that mixes boxes is not read as one box's (E1)

<to_id>NFRA_CTLPLN.TO-CT-z-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~73</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-z-1` (`decompositions/NFRA_CTLPLN_DECOMP.round10.md`) | **outcome_ref:** FWD-1, FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-1 (PRD v0.25, re-based): one real round is planned on the laptop, worked and pushed by a Dell to its box branch, merged by the integrator into `CLOUD`, and graded on the laptop; each hop's start and end are read from git by `.tools/thread-trace.py`. MEASURED on round 9 of this project: the round holds a laptop worker order (`TO-CT-y-1`, worker `0.9.0_WK_NFRA_CTLPLN~72`) and a dell1 seat order (`TO-CT-y-2`, seat `0.7.0_AE_CloudOps~CT1`). The tool, with no way to name an order, printed `HOP 2 WORK ... by=0.9.0_WK_NFRA_CTLPLN~72 where=origin/box/laptop` and `pushed_by_working_box=True`, so the dell1 hop (commit 1a677233f3 by `0.7.0_AE_CloudOps~CT1`, integrated by `0.0.0_AB_MSTR`) is not what it read. You add the filter.

### BUILD

In `.tools/thread-trace.py` (read the module docstring at the top, `find_orders` at about line 212, the HOP 2 block at about line 272 and `main` at about line 497):
1. A repeatable argument `--order <id>`: only the task orders whose id (`<to_id>`, or the file stem after `NFRA_CTLPLN.` such as `TO-CT-y-2`) matches one given value are used for the hops. An `--order` that matches no order of the round makes the tool print the same zero-hops line it prints for a round with no orders and exit non-zero (never a silent full-round trace). With no `--order` the behaviour is EXACTLY as today (the existing four selftest cases pass unchanged).
2. The five hops for the chosen orders: HOP 1 the issuance commit(s) of those orders (not the other orders' issuance), HOP 2 the first and last commit by those orders' `<issued_to>` serial that touch those orders' `<paths>`, order file and proof instance, and the rest as today, driven from HOP 2's last commit.
3. The LAST line gains the filter: `THREAD project=<CODE> round=<n> orders=<ids or ALL> hops=<k>/5 ...` (keep every existing field and its order; add `orders=` after `round=`). Update the docstring.
4. Selftest: add FOUR cases to the temporary-repository fixture: (a) two orders in one round issued to different serials on different box branches; `--order` for the first reads the first's hops only (HOP 2 names the first's serial and branch); (b) the same for the second; (c) no `--order` reads the whole round as before (the same line a pre-change run printed, plus `orders=ALL`); (d) an unknown `--order` reads 0 of 5 and exits non-zero. LAST selftest line `THREAD-TRACE-SELFTEST cases=8/8 ok=True`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. The tool READS git; it writes nothing, fetches only with `--fetch`, pushes nothing. Tests run in temporary directories and temporary git repositories. No aws, no terraform, nothing on the agent bus. Standard library only; ruff clean; ASCII only; no box name or path under a user's home typed. The law files CLAUDE.md and org/XXX.md are LOCKED. Do NOT commit the `portal` gitlink. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W73-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTz1-AC1" cell_refs="CT-z-1"><invocation>python .tools/thread-trace.py --selftest</invocation><expect>THREAD-TRACE-SELFTEST cases=8/8 ok=True</expect></criterion>
`CTz1-AC1` -- the old four and the new four pass.

<criterion id="CTz1-AC2" cell_refs="CT-z-1"><invocation>python .tools/thread-trace.py --project NFRA_CTLPLN --round 9 --order TO-CT-y-2</invocation><expect>orders=TO-CT-y-2</expect></criterion>
`CTz1-AC2` -- a real read of round 9 for the dell1 order alone; its last line carries `orders=TO-CT-y-2`, and HOP 2 names `0.7.0_AE_CloudOps~CT1` (report the whole output). The grade hop may read ABSENT; the exit code is not graded.
</proof_of_spec>

<expected_criteria>CTz1-AC1,CTz1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation (no `timeout` prefix). Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~73/NFRA_CTLPLN.TO-CT-z-1.thread-trace-order-filter.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTz1-AC1,CTz1-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID (if the flip is refused as outside your grant, leave it `pending` and say so; the issuer flips). Report the whole output of AC2.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round10.md</decomp_doc>
<owned_cells>CT-z-1</owned_cells>
</decomp_ref>

<paths>
.tools/thread-trace.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a filter that silently falls back to the whole round when nothing matches (case d: zero hops, non-zero exit); a tool that now reads one order but prints no sign of it (the `orders=` field); a change that alters the unfiltered read (case c and the four old cases); BLIND: a dell1 order whose commits were authored by a different serial than its `<issued_to>`.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round9.md section 3 (E1); the round-9 read of this project (ROUND7_STAGED_INPUTS R10-1).
