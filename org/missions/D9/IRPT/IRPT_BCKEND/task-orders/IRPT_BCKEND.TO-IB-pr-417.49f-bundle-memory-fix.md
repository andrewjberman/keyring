# TO IRPT_BCKEND.TO-IB-pr-417 -- the 49F narrow bundle rebuilt as IB-pr-410's members plus IB-pr-414's publish-gate memory fix; memory, replay, packet

<to_id>IRPT_BCKEND.TO-IB-pr-417</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~279</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>117</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 19.1 and ADDENDUM 20 (@c3fd5df57a); IB-pr-414 graded complete (fix peak 3,139,624,960 B, wall 417.2 s) | **Decomp cell:** `IB-pr-417` (decomposition section 110) | **outcome_ref:** FWD-14

---

## WORKER FACE

**Client data rule (CTO ruling @0e8209c33c item 6).** No account id, balance, fee or flow goes in any tracked file. The repo carries counts,
sha256 and reason codes only. Extracted trees, node files and inputs stay OUTSIDE the worktree and are deleted file by file at the end.

**Why.** IB-pr-404 put the FWD-14 publish gate live at 3 firms. The 49financial producer was then SIGKILLed on the 4 GiB box (row D2-S56).
IB-pr-414 (commit `3f2bdda578`) folds the served publication into keyed sets: 49F peak drops from 3.98e9 to 3.14e9 B with gate decisions
unchanged. IB-pr-410's bundle (built `47be54d6...`, packet `deliverables/0.9.0_WK_IRPT_BCKEND~273/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-410.md`)
is HELD. This order builds the bundle that IB-pr-413 will apply instead: 410's members plus 414's fix. A signed fix is needed before
Monday 2026-10-12 13:00Z; otherwise a 49F-only Branch B rolls back. Root: `C:/dev/wk-irpt-bckend-279/`.

**Build:**
1. **Compose** the bundle exactly as ~273 did (`deliverables/0.9.0_WK_IRPT_BCKEND~273/compose_410.py`; read 410's packet and census first).
   - The base is the LIVE 49F bytes, sha256 `3f2e738f83aa415a2b56cf506d54368f9d2f86f7ded8f19202fc373ef6a28901`. Verify the live object hashes to it.
   - `holdings_49f.py` is 410's member unchanged.
   - `holdings_snapshot.py` is 410's member plus the `holdings_snapshot.py` diff of `3f2bdda578`, applied cleanly. If it does not apply,
     stop and file a row.
   - Use python 3.12 and LF bytes, pack twice to byte-identical output, and upload nothing.
   - Write `deliverables/0.9.0_WK_IRPT_BCKEND~279/IB117-2_49f_bundle_census.json` in the same shape as `IB111-1_49f_bundle_census.json`.
2. **Memory.** Run ~276's `deliverables/0.9.0_WK_IRPT_BCKEND~276/mem_harness.py` on the BUILT bundle's members, on real 49F inputs, with
   uploads disabled. Write `IB117-2_49f_bundle_memory.json` `{peak_rss_bytes, wall_time_s, cpu_time_s, table_lookups, harness, inputs_date}`.
3. **Replay** on real 49F inputs (AWS reads only). Write `IB117-2_49f_bundle_replay.json` `{arms:[{name, verdict, negative_control, detail}]}`,
   with verdicts exactly `identical` or `expected-diff`:
   - `fwd14_gate_vs_b410`, **identical**: same gate outcome and conditions as 410's bundle.
   - `smartx_class_parity`, **identical**.
   - At least one negative control: the 404 live bundle's served-node list form, on the same harness, peaks above the fixed bundle.
4. **Packet** `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-417.md`, in 410's form:
   - ONE S3 key and two members, with the served change in counts;
   - the landing path, digest-gated and never a mint;
   - Branch A, and Branch B: copy back the live 404 version, named and re-read at apply;
   - the base and built sha256, and the pair: ~P2's COO half, dell1 `2.0.0_SA_COO~M1`'s COO half for the e56 member (via MSTR), and the
     CTO half;
   - the ADDENDUM 18 red list, showing your members touch none of its targets;
   - that it supersedes 410's packet.

<criterion id="IB117-2-AC1" cell_refs="IB-pr-417"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-2-AC1</invocation><expect>IB117-2-AC1 PASS</expect></criterion>
<criterion id="IB117-2-AC2" cell_refs="IB-pr-417"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-2-AC2</invocation><expect>IB117-2-AC2 PASS</expect></criterion>

<expected_criteria>IB117-2-AC1, IB117-2-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD_ONLY, the memory harness and offline replays; no upload, apply or deploy. AWS reads only.
- **Do not edit `holdings_snapshot.py` or `holdings_49f.py` in the tree.** The members are composed only in the bundle.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W279-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~279" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~279@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~279 <0.9.0_WK_IRPT_BCKEND~279@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~279/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-417.49f-bundle-memory-fix.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 110 (round 117, workstream ~P), cell `IB-pr-417`.
<owned_cells>IB-pr-417</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB117-2-AC1, IB117-2-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~279/IRPT_BCKEND.TO-IB-pr-417.49f-bundle-memory-fix.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the built sha256, peak and wall time, each arm's verdict, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- ONE S3 key (the 49F narrow bundle) built, not uploaded; two members; the apply is IB-pr-413, re-pointed by amendment once the pair signs.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the holdings-snapshot schedule is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p117_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~16:5xZ: AC1 FAIL, AC2 FAIL (no census, memory or packet); ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO ADDENDUM 20).
</preflight>
