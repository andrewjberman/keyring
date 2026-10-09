# AMGT_RESAPP task order -- `AMGT-dd-3` -- THE WALK ON PORTAL DEV: FWD-1 ON AMD AND FWD-7, WHERE DSGN_AMGTV1 ROUND 53 DRAWS THEM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-dd-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~317</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account through its own skill's mechanism; no other write.
comp-adversary: RUN by the issuer at the cut -- round 79's walk (portal 38cc0ecf) read AMD's segment place as a reason while the API served a 6-row table, and /freshness drew 0 of 10 served Seeking Alpha sentences. DSGN_AMGTV1 round 53 draws both; its real run read AMD's table as 6 rows on portal DEV 84e13d0f (ROUND53_CLOSE @14ff884fd7). origin/DEV reads 8d2a08a9 at the cut, one commit on 84e13d0f.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** the GO names it (branch `wk-AMGT_RESAPP-317`) and the portal ref, with the main tree's packages linked. Work and commit only there. Start every shell call with `cd` into that path. **Run no `bun install`, `bun add`, `bun update`, `npm` or `npx` in this worktree:** its packages are linked from the base checkout. If `bun run dev:live` fails for a missing package, file a BLOCKING row and stop.

## 1. THE ACT -- `AMGT-dd-3` (round 80, decomposition s.88)

**The walker account is one identity across boxes.** On this box run it with `py -3.12` (the default Python lacks
`bcrypt`). If `py -3.12 .claude/skills/ui-walk/ui_walker_account.py status` reads armed by anyone else when you start or
between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole first. Serve the dev build on
`http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role admin. Round 79's
driver is at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~314/instrument/`; copy it into your own
`instrument/` and extend it there.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~317/WALK_ROUND80.md`. Its first line is
`PORTAL_REF: <the portal commit you served>`. Per act: the DONE WHEN quoted from the PRD
(`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`, with its version and line), what you saw, and the captures
(COPIED into `.../0.9.0_WK_AMGT_RESAPP~317/captures/`) with a positive control. Head each act with a markdown heading
carrying its token: `FWD-1`, `FWD-7`. An act you could not walk is still headed, with its reason. Record what you saw; give
no verdict.

- **FWD-1 on AMD US** (`AMD_US_Equity`). The model numbers, the business description, and what is drawn where the
  segment breakdown is. The server sends `segment_table` (six lines of revenue by business line, the first column fiscal
  year 2025, USD millions). Record what the page draws: the table's lines and first values, or a reason (quote it). From
  the signed-in dev build's own API client record beside it: `segment_table.status`, the count of `rows`, the first row's
  name and first value, `periods[0].label`, `currency`, `units`.
- **FWD-7.** Open /freshness on a first visit. Read the Seeking Alpha cell on TEN rows and record each exactly: BA, BABA
  and COST, then seven more of your choosing including at least two without a date. For the same ten read
  `seeking_alpha.state` and `seeking_alpha.sentence` from the API client and record them beside what the page draws.
  Record how many rows are flagged stale and which, and the first-paint time of a first and a second visit.
- Then disarm.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-R1-W317-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. No plant by you.
3. No `bun install`, `bun add`, `bun update`, `npm` or `npx` in this worktree. Nothing is fetched from the internet.
4. The dev server runs only on port 5174. Stop it when you finish and confirm 0 listeners on that port as the last line of
   your report.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~317/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-dd-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd3.py"; echo "exit=$?"</invocation><expect>6 or more captures and a walk record heading FWD-1 and FWD-7 and naming its PORTAL_REF; R80 DD3 WALK RECORD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-dd-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; py -3.12 .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads armed=no armedBy=none; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-dd-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~317 <0.9.0_WK_AMGT_RESAPP~317@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~317/AMGT_RESAPP.TO-AMGT-dd-3.the-walk-of-fwd-1-and-fwd-7-on-dev.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the capture count;
- for FWD-1 and FWD-7: what the page draws against what the server sends;
- any row;
- as the LAST line: that the dev server is stopped and the count of listeners on port 5174.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~Z round-79 analysis R3, enrichment item 3: a read, not a build; graded by a walk on DEV at or after
84e13d0f. AC3 is the CVO's L9 read (3.0.0_SA_CVO, dell1). The signed-in walk on dell1 needed the walker's `ssm:GetParameter` on
`/opal/ui-walker/password` for the Dell group: APPLIED before the cut (laptop NFRA_CTLPLN.TO-APPLY-22 Step H, MSTR~DELL1 msg 1384,
CTO~DELL1 msg 1386; read-only, no Delete). DSGN_AMGTV1's owed walk (2.0.0_SA_COO~D1) uses the same walker identity; the order's
armed-by-another rule is the lease (CTO~Z round-79 R4). Check dry-run at the base: AC1 base: FAIL as
expected (0 captures, no record; exit=1); green arm (6 captures, both heads, PORTAL_REF) YES; a FWD-18 heading does not satisfy
FWD-1 (NO). AC2 base: the account reads `armed=no armedBy=none` (py -3.12, 01:3xZ).

<status>pending</status>
<round>80</round>
<slot>0.9.0_WK_AMGT_RESAPP~317</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @a68418f40a (walk bb5273f8dd, proof 668c7475e3 VALID rc=0). Re-run on the shared tree: R80 DD3 WALK RECORD: YES (17 captures, both heads, PORTAL_REF 8d2a08a92b5e); AC2 armed=no armedBy=none. On portal 8d2a08a9: FWD-1 AMD draws the 6-row Revenue by segment table (Data Center 16,635, Fiscal year 2025) equal to the served segment_table, while the lower 'Business segments -- from the filing' panel still reads its no-analysis sentence; FWD-7 draws the served Seeking Alpha sentence on 10 of 10 rows, 1 of 95 flagged stale (Lenovo 992 HK). AC3 is the CVO's L9 read. Rows D1-W317-S1 (walker DeleteParameter denied on disarm), S2 (walk script's bare python lacks bcrypt), S3 (R1 id form refused).</status>
