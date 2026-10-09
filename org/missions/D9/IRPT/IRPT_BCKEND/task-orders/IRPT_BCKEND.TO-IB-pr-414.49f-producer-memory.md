# TO IRPT_BCKEND.TO-IB-pr-414 -- the 49financial holdings producer's peak memory: measure pre-404 / 404 / 410 on one harness, and fix the FWD-14 gate's memory so the producer runs under 85% of 4 GiB with its decisions unchanged

<to_id>IRPT_BCKEND.TO-IB-pr-414</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~276</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>115</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 19.1 (msg 3478, @d09687479d), on row D2-S56 | **Decomp cell:** `IB-pr-414` (decomposition section 108) | **outcome_ref:** FWD-14

---

## WORKER FACE

**The finding (row D2-S56, `0.7.0_AE_CloudOps~IB2`).** On IB-pr-404's first fire:
- inflection and cottonwood PUBLISHED;
- the **49financial producer was SIGKILLed** (rc 137, 5m09s) on the shared t3.medium (4 GiB, `i-02448edb624a7a7cf`), before printing
  OK or REFUSED. Its three earlier fires, before the FWD-14 gate, all succeeded.

49F is the largest firm, at about 155k nodes. The CTO's frame: measure the peak, then fix the code. A bigger instance is NOT the fix.
Root: `C:/dev/wk-irpt-bckend-276/`.

**1. Measure on ONE harness**, for the 49financial producer run of `holdings_snapshot.py`'s `run_firm`. Use real 49F inputs (business date
of the last fire, 2026-10-08), upload disabled, AWS reads only, and scratch outside the worktree. Record peak RSS for four trees:
- `pre404`: the 49F bundle before IB-pr-404, version `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur`;
- `b404`: the live 49F bundle, built `3f2e738f...`;
- `b410`: IB-pr-410's built bundle, `47be54d6...`, in `0.9.0_WK_IRPT_BCKEND~273/`;
- `fix`: your fix.
Use psutil or the OS peak-working-set counter, sampled across the whole run. State the method. Read ~265/~266/~269/~273's replay scripts
under `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/` for how to drive `run_firm` offline.

**2. Find where b404 spends memory beyond pre404.** The FWD-14 publish gate (`9af6811b61`, `ce6e2a218e`) compares the candidate against the
prior publication. Then **fix the GATE's memory** in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`. Change ONLY the
publish-gate code those two commits added; never dell1's e56 / CUSIP code (`01e843ce2e`). Examples of acceptable fixes:
- compare streaming or keyed summaries instead of two full node lists;
- free the candidate's intermediate frames before the comparison.
The gate's decisions must not change.

**3. Write** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~276/IB115-1_memory_census.json`:
`{harness, method, upload:false, business_date, limit_bytes: 3650722201, trees:{pre404:{peak_rss_bytes}, b404:{...}, b410:{...}, fix:{...}}}`.
The limit is `int(0.85 * 4 GiB)`. The fix must be UNDER it on this harness. If the harness machine's peaks are not comparable to the
t3.medium's, say so in `method` and give the ratio you measured, e.g. b404 here against the box's kill.

**4. Gate-decision replay:** run the fix tree and the b404 tree at the 3 firms on real inputs. Write `IB115-1_gate_decision_replay.json`
`{arms:[...]}` with:
- `fix_vs_b404_gate_decision_<firm>`, identical in outcome and conditions, for 49financial, inflection and cottonwood;
- at least one negative control, e.g. the QA worse candidate still REFUSES on the fix.

**5. Tests:** keep every `publish_gate` test green. Add one named `publish_gate_memory...` that guards the change; for example, the gate
never materialises both full node lists at once.

<criterion id="IB115-1-AC1" cell_refs="IB-pr-414"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r115/p115_cells.py" . IB115-1-AC1</invocation><expect>IB115-1-AC1 PASS</expect></criterion>
<criterion id="IB115-1-AC2" cell_refs="IB-pr-414"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r115/p115_cells.py" . IB115-1-AC2</invocation><expect>IB115-1-AC2 PASS</expect></criterion>
<criterion id="IB115-1-AC3" cell_refs="IB-pr-414"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r115/p115_cells.py" . IB115-1-AC3</invocation><expect>IB115-1-AC3 PASS</expect></criterion>

<expected_criteria>IB115-1-AC1, IB115-1-AC2, IB115-1-AC3</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~15:0xZ, issuer 2.0.0_SA_COO~P2, on CTO ADDENDUM 20 item 1 (@c3fd5df57a))

The 9x e56 fallback cost (row W269-S2) joins this harness. For EACH of the four trees, the memory census also records:
- `wall_time_s`: the producer's run, same harness;
- `table_lookups`: the count of security-table lookups, CUSIP-key fallbacks included.
The CTO grades the SIGKILL fix and the e56 cost together. IB-pr-410/413 stays HELD until both read under the line on `b410` rebuilt with
your fix: peak RSS under 85% of 4 GiB, and wall time no worse than `pre404` x 2. If the e56 cost cannot be brought under that line inside
the gate code you may touch, say so in a row; the e56 code itself is dell1's. `p115_cells.py` IB115-1-AC1 is amended to read both fields.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests and offline measurement; no upload, apply or deploy. AWS reads only.
- **Deadline:** the CTO's: if no fix is signed by Monday 2026-10-12 13:00Z, 404's Branch B runs on the 49F key. Report as soon as the
  three criteria pass.
- **Client data:** inputs and node files stay OUTSIDE the worktree and are deleted at the end (file-by-file, never a recursive delete);
  the census holds numbers only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W276-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~276" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~276@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~276 <0.9.0_WK_IRPT_BCKEND~276@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~276/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-414.49f-producer-memory.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 108 (round 115, workstream ~P), cell `IB-pr-414`.
<owned_cells>IB-pr-414</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB115-1-AC1, IB115-1-AC2, IB115-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~276/IRPT_BCKEND.TO-IB-pr-414.49f-producer-memory.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the four peaks and the limit, where the memory went, the fix, the replay verdicts, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- holdings_snapshot.py's FWD-14 publish-gate code only (never the e56/CUSIP code); tests; offline measurement; no release in this cell (the fixed member rides a new narrow 49F bundle and pair).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p115_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~14:4xZ: AC1 FAIL (no census), AC2 PASS (control: publish_gate 18, suite 391 with the live-state S71 guard excused by name), AC3 FAIL (no replay); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (FWD-14 gate code is ~P's: 9af6811b61, ce6e2a218e; CTO ADDENDUM 19.1).
</preflight>
