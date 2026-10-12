# TO NFRA_CTLPLN.TO-CT-aa-1 -- round 2 HYGIENE (round 11 of the project) CT-aa-1: thread-trace reads the round's orders from git, so a checkout that lacks an order file CLOUD holds does not drop it silently (W73-S2)

<to_id>NFRA_CTLPLN.TO-CT-aa-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~74</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>HYGIENE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aa-1` (`decompositions/NFRA_CTLPLN_DECOMP.round11.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/thread-trace.py` reads one round's five hops from git. The hops come from git, but the round's ORDER SET comes from a glob of the reading checkout's working tree: `find_orders` (about line 231) calls `glob.glob` over `org/missions/D*/*/<CODE>/task-orders/*.md` and over `org/tier2_senior/*/task_orders/<CODE>.*.md`. An order file that `origin/CLOUD` holds but the reading checkout lacks is dropped, and the trace prints no sign of it (surprise row `NFRA_CTLPLN-W73-S2`, filed by the worker of the previous order). You make the order set come from git and print its denominator.

### BUILD

In `.tools/thread-trace.py` (read the module docstring at the top, `find_orders`, `trace` and `main`; the class `Repo` and the function `git` already run git for the hops):
1. `find_orders` reads the order files from git, not from the files on disk: for each ref in this order, `HEAD` then `origin/CLOUD` (a ref that does not resolve is skipped; if NEITHER resolves, the tool prints an `ERROR:` line and exits non-zero, never a silent zero-order read), list the files with `git ls-tree -r --name-only <ref>` matching the two path patterns above, and read each with `git show <ref>:<path>` as bytes decoded with `encoding='utf-8', errors='replace'`. A path present on both refs is read from `HEAD` (the reading checkout's committed state); a path on only one ref is read from that ref. The tag rules, the round filter, the status rule (the last line-anchored `<status>` tag; superseded, cancelled, withdrawn and retired orders are not part of the thread) and every returned field stay exactly as today. An uncommitted file in the working tree is NOT read (the read is from git).
2. The LAST line gains the denominator: `THREAD project=<CODE> round=<n> orders=<ids or ALL> orders_found=<k> hops=<j>/5 ...` (keep every existing field and its order; `orders_found=<k>` goes right after `orders=`). `<k>` is the number of orders of the round that are part of the thread, counted BEFORE the `--order` filter is applied. An `--order` that matches nothing still prints `orders=NONE`, now with the `orders_found` of the round, and exits non-zero as today.
3. Update the module docstring: the order set is read from `HEAD` and `origin/CLOUD`, not the working tree; state it as a DELIBERATE CHANGE.
4. Selftest: add TWO cases to the temporary-repository fixture: (a) an order file committed only on a fake `origin/CLOUD` ref (the checkout's `HEAD` lacks it) IS found: `orders_found` counts it and `--order` by its slug-less id reads its hops; (b) an order file present only as an UNCOMMITTED working-tree file is NOT found: `orders_found` does not count it. The existing ten cases pass unchanged except for the new `orders_found=<k>` field (update only what the field changes in their expected text). LAST selftest line `THREAD-TRACE-SELFTEST cases=12/12 ok=True`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. The tool READS git; it writes nothing, fetches only with `--fetch`, pushes nothing. Tests run in temporary directories and temporary git repositories. No aws, no terraform, nothing on the agent bus. Standard library only; ruff clean; ASCII only; no box name or path under a user's home typed. The law files CLAUDE.md and org/XXX.md are LOCKED. Do NOT commit the `portal` gitlink. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W74-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaa1-AC1" cell_refs="CT-aa-1"><invocation>python .tools/thread-trace.py --selftest</invocation><expect>THREAD-TRACE-SELFTEST cases=12/12 ok=True</expect></criterion>
`CTaa1-AC1` -- the old ten and the new two pass.

<criterion id="CTaa1-AC2" cell_refs="CT-aa-1"><invocation>python .tools/thread-trace.py --project NFRA_CTLPLN --round 9 --order TO-CT-y-2</invocation><expect>orders_found=2</expect></criterion>
`CTaa1-AC2` -- a real read of round 9 for the dell1 order alone from git; its last line carries `orders=TO-CT-y-2 orders_found=2` (the round holds two orders, `TO-CT-y-1` and `TO-CT-y-2`), and HOP 2 still names `0.7.0_AE_CloudOps~CT1` (report the whole output). The grade hop may read ABSENT; the exit code is not graded.
</proof_of_spec>

<expected_criteria>CTaa1-AC1,CTaa1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation (no `timeout` prefix). Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~74/NFRA_CTLPLN.TO-CT-aa-1.thread-trace-orders-from-git.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaa1-AC1,CTaa1-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID (if the flip is refused as outside your grant, leave it `pending` and say so; the issuer flips). Report the whole output of AC2.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round11.md</decomp_doc>
<owned_cells>CT-aa-1</owned_cells>
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
comp-adversary: RUN -- a read that falls back to the working tree when git has no answer (neither ref resolves: an ERROR line and a non-zero exit, never a zero); an order held only by CLOUD and dropped (case a); an uncommitted file counted as part of the round (case b); a change that alters the filtered read of round 9 (AC2 and the old ten cases); BLIND: a ref that resolves but is shallow, or an order file renamed between HEAD and CLOUD (read as two orders).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round10.md section 3 (W73-S2); surprise row NFRA_CTLPLN-W73-S2 and its disposition row NFRA_CTLPLN-S9114.
