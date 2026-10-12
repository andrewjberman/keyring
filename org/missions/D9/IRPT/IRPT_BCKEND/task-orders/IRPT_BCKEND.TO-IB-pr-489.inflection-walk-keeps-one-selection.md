# TO IRPT_BCKEND.TO-IB-pr-489 -- one Inflection walk keeps ONE selection reference outside the repo and leaves the walker disarmed

<to_id>IRPT_BCKEND.TO-IB-pr-489</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~341</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>169</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ROUND-169 ANALYSIS section 3 item 2 (msg 6660) | **Decomp cell:** `IB-pr-489` (decomposition section 161) | **outcome_ref:** FWD-3

---

## WORKER FACE

**AMENDMENT 1 (issuer, 2026-10-12T23:5xZ, ruling on your row W341-S4, which was right):** the Firm control's option for this firm reads `Inflection Wealth Management`, not `Inflection`; every `--firm` use below carries that exact label, and the record's `firm_label` is that string. Your inherited walk record and proof from the first attempt are replaced by this run.

**AMENDMENT 2 (issuer, 2026-10-12T00:0xZ; your second run, row W341-S5, was right):** the Firm option is selected but the EMPTY client search lists no client (the page shows the search box and no list; `directory/resolve` answered 200 three times). Your grant already covers `.claude/skills/ui-walk/`: extend `--first-client` in `walk.mjs` so that, when the empty search lists no client, it types ONE letter into the search box in turn (`a`, `e`, `i`, `o`, `n`, `r`, `s`, `t`), waits for the list the way `firstListedClient` waits, and walks the first listed client of the first letter that lists one (clear the box between letters the way the `--client` step clears it). If no letter lists a client, STOP as your refusal clause says, and add to your row: the number of options the open search showed after each letter, and any empty-state sentence the page prints (words only; no client name). A client name still reaches no file outside `tmp/ui-walk/` and no terminal line. Re-run `node --check .claude/skills/ui-walk/walk.mjs` and the three `IB169-1` criteria (`p169_cells.py . IB169-1-AC1`, `AC2`, `AC3`) after the edit and say so in the report; then run the walk.

**Cell `IB-pr-489` (inlined):** the deployed `irpt-performance-adapter` computes a performance answer only for Inflection (orion); no selection reference for an Inflection client exists. Walk ONE Inflection client's Performance tab with the walker as extended by `IB-pr-488` (your own earlier commit on this worktree: `--firm` and `--first-client`), and keep the selection reference the page itself creates. **Start only if `IB169-1-AC1`..`AC3` all passed in your report for `IB-pr-488`; otherwise STOP and report.**

**Steps:**
1. Read `C:\dev\ajb_workspace\.claude\skills\ui-walk\SKILL.md` (the safety model and the invocation block) in your worktree's copy. The walk is read-only, signs in as the dormant UI walker service account on the LOCAL dev build, and never leaves `localhost`.
2. The local dev build on port 5174 must answer: `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/`. If it does not, start it in the background from the main tree: `cd /c/dev/ajb_workspace/portal && bun run dev:live --port 5174` (resolve `bun` through the profile; port 5174 only), wait until the curl reads 200 (bounded at 3 minutes), and record the process id you started. You stop that process, and only that one, at the end.
3. From YOUR worktree root run the walk (it arms the account, walks, and disarms; allow it up to 10 minutes, run it in the background and poll its log): `node .claude/skills/ui-walk/walk.mjs --base http://localhost:5174 --route /investor-reporting --firm "Inflection Wealth Management" --first-client --performance-state --max-minutes 12`. The walk writes `tmp/ui-walk/<stamp>/` in your worktree (gitignored). **Client data stays local: never print a client name, never commit or message a screenshot or the findings.**
4. From the walk's network log in that folder (method, status and path only), read the PERFORMANCE request path and take the one `sel_` + 64 hex reference in it. Write that single reference as ONE line to `C:\Users\Test\AppData\Local\Temp\claude\C--dev-ajb-workspace\f0005e69-69e0-455c-b522-7be87d97fcdc\scratchpad\inflection_sel_ref.txt` (a path outside any git tree; do not copy it anywhere else; never put it in the record, the report or a commit).
5. Confirm the walker is dormant: `python .claude/skills/ui-walk/ui_walker_account.py status` must read `status=disabled armed=no`. If it reads active (the walk died), run `disarm <armedBy from status>` at once and say so in the report.
6. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~341/IB169-2_walk_record.json` with EXACTLY these keys: `firm_label` (the string `Inflection Wealth Management`, the label the Firm control shows), `performance_tab_reached` (true if the Performance tab loaded an answer), `performance_request_paths` (the number of performance request paths in the net log), `walker_disarmed` (true), `walk_stamp` (the folder's stamp `YYYYMMDDTHHMMSSZ`), `reference_file_written` (true). Nothing else: no client name, no account, no figure.

**Criteria (run each under `timeout 120`, record the output and exit code verbatim):**

<criterion id="IB169-2-AC1" cell_refs="IB-pr-489"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-2-AC1</invocation><expect>IB169-2-AC1 PASS</expect></criterion>
<criterion id="IB169-2-AC2" cell_refs="IB-pr-489"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-2-AC2</invocation><expect>IB169-2-AC2 PASS</expect></criterion>
<criterion id="IB169-2-AC3" cell_refs="IB-pr-489"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-2-AC3</invocation><expect>IB169-2-AC3 PASS</expect></criterion>

<expected_criteria>IB169-2-AC1, IB169-2-AC2, IB169-2-AC3</expected_criteria>

What the checks grade: AC1 the scratch file holds exactly one `sel_` + 64 hex line; AC2 the walker account reads dormant (disabled, armed=no); AC3 the walk record carries exactly the six whitelisted keys with the stated values (`firm_label` begins with `Inflection`).

## BOUNDS

- **Grant:** the `paths` block and nothing else. The walker's own guard stays on: GET/HEAD/OPTIONS and the listed POSTs only. No other AWS call than the walker's own arming and disarming; no write to any selection store by hand; no mint of any identity; no PROD site.
- **Refusal clause:** STOP, disarm if armed, file a row, and report on any of: `FIRM_OPTION_ABSENT` (say which labels the control showed, labels only), no client listed under the Inflection firm, the Performance tab not reached, a `HELD by` lease line from the walker (someone else is walking: wait up to 10 minutes, then STOP), or a performance request path with no `sel_` reference. Never invent a reference.
- **Row ids** are `IRPT_BCKEND-D2-W341-S<k>` (the next free `k`).
- **Commit** on your worktree branch per your definition; the record only; ASCII only. Report once, under 150 words, with no client name.

<paths>
.claude/skills/ui-walk/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~341/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-489.inflection-walk-keeps-one-selection.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 161 (round 169, workstream ~P), cell `IB-pr-489`.
<owned_cells>IB-pr-489</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB169-2-AC1, IB169-2-AC2, IB169-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~341/IRPT_BCKEND.TO-IB-pr-489.inflection-walk-keeps-one-selection.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the walk arms the dormant UI walker service account (`USER#usr_opal_ui_walker` in `opal-users-v2`, plus SSM `/opal/ui-walker/password`) for the length of the walk and disarms it; it reads served data through the local dev build; the page creates the selection record as a person's click does (the walker's guard admits the `.../selections` POST). No other resource. The skill's safety model is the CRO's (`ANDREW_DIRECT_20260926_220xZ_UI_WALKER_SERVICE_ACCOUNT`).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the walker uses the laptop-profile credentials its skill names.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p169_cells.py dry-run at base on dell2 2026-10-12 ~23:2xZ: IB169-2 AC1 FAIL (no reference file), AC2 PASS (a bound: the walker account reads `status=disabled armed=no` now), AC3 FAIL (no record). Risk of this order: a walk that dies leaves the account armed (disarm instruction in step 5); the issuer reads `status` at the drain.
lane: the <paths> block IS the grant; worker slot ~341 of IRPT_BCKEND, second order of its queue. Class SERVED.
</preflight>
