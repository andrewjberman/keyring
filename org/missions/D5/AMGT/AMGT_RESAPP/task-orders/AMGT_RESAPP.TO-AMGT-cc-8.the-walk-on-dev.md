# AMGT_RESAPP task order -- `AMGT-cc-8` -- THE WALK ON DEV AFTER THE ROUND-79 REDEPLOY: FWD-18 ON ASML NA, FWD-1 ON AMD, FWD-7, AND THE FIVE STORED SECTIONS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~314</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- round 78's walk (portal d1b21c97, function +s6R0/rc) did not walk FWD-18 on ASML NA; read AMD's segment place as a reason and the Seeking Alpha column as 2026-09-11 three times and Not collected twice on five rows; the served thesis for ASML NA carries a driver series of three share counts with the chart refused in plain words (round79/reads/FWD18_ASML_SERVED_READ.md).
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** the GO names it (an idle worktree is re-used so no new checkout is made; branch `wk-AMGT_RESAPP-314`), with the portal ref the GO names and the main tree's packages linked. Work and commit only there. Start every shell call with `cd` into the path the GO names: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout. **Run no `bun install`, `bun add`, `bun update`, `npm` or `npx` in this worktree:** its packages are linked from the base checkout. If `bun run dev:live` fails for a missing package, file a BLOCKING row and stop.

## 1. THE ACT -- `AMGT-cc-8` (round 79, decomposition s.87)

**The issuer holds the walker slot.** If `python .claude/skills/ui-walk/ui_walker_account.py status` reads armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole first. Serve the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role admin. Round 78's driver is at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~303/instrument/`; copy it into your own `instrument/` and extend it there.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~314/WALK_ROUND79.md`: per act, the DONE WHEN quoted from the PRD (with its version and line), what you saw, and the captures (COPIED into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~314/captures/`) with a positive control. Record what you saw; give no verdict. Head each act with its token so a reader can find it: FWD-18, FWD-1, FWD-7, SECTIONS. An act you could not walk is still headed, with its reason.

For every act below, where the page draws nothing for a field this round serves, do TWO things: record that the page does not draw it, and read the same field for the same name from the signed-in dev build's own API client, recording it beside the screen. The server serving a value the page does not yet draw is a finding for the page's owner, not a failure of your walk.

- **FWD-18 on ASML NA** (`ASML_NA_Equity`), the Thesis tab. Find the place where a driver chart would be. Record exactly what is drawn there: a chart, or a sentence in its place (quote it). Then find a figure in the thesis text that can be pressed, press ONE, and record what opens: which passage, from which filing, with which heading and paragraph. Capture before and after the press. Then do the same on BA (`BA_US_Equity`), which draws a chart: press ONE point of the chart, count how many times the passage is rendered (once is the repair of an earlier round), and read the y-axis tick labels.
- **FWD-1 on AMD US** (`AMD_US_Equity`). The model numbers, the business description, and what is drawn where a segment breakdown would be. This round the server sends a segment table for AMD: six lines of revenue by business line, the first column named fiscal year 2025, in USD millions. Record whether the page draws it; if it draws a reason instead, quote the reason and record the served table from the API client (the key is `segment_table`: its `status`, the count of `rows`, the first row's name and first value, `periods[0].label`, `currency`, `units`).
- **FWD-7.** Open /freshness on a first visit. Read the Seeking Alpha cell on TEN rows and record each exactly: take BA, BABA and COST, then seven more of your choosing including at least two that read without a date. This round the server sends one of three states per company (a last-read date; checked and nothing new held; no collection record yet), each with a sentence. Record what the page draws for each of the ten, and for the same ten read `seeking_alpha.state` and `seeking_alpha.sentence` from the API client. Record how many rows are flagged stale on the page and which. First-paint time of the first and of a second visit.
- **SECTIONS.** This round the server sends five stored sections of the team's notes on `/thesis` (company description, why we own, positives, negatives, special items) under the key `dossier_sections`. On ASML NA and on NU (`NU_US_Equity`): record whether the page draws any of the five, where, and with what heading; and from the API client record, for each of the five, its `status` and the first 80 characters of its `text` or its `reason`.
- Then disarm.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W314-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. No plant by you: a planted read is the issuer's act, named in the GO.
3. No `bun install`, `bun add`, `bun update`, `npm` or `npx` in this worktree. Nothing is fetched from the internet.
4. The dev server runs only on port 5174. Stop it when you finish and confirm 0 listeners on that port as the last line of your report.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~314/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc8.py"; echo "exit=$?"</invocation><expect>8 or more captures and a walk record naming every act; R79 CC8 WALK RECORD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-8" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~314 <0.9.0_WK_AMGT_RESAPP~314@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~314/AMGT_RESAPP.TO-AMGT-cc-8.the-walk-on-dev.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts;
- for FWD-18: what is drawn in the chart's place on ASML NA, and what the one press opened;
- for FWD-1, FWD-7 and SECTIONS: what the page draws against what the server sends;
- any row;
- as the LAST line: that the dev server is stopped and the count of listeners on port 5174.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-78 analysis @1a67e26433, enrichment item 4 (FWD-18 on ASML NA) and R1 (FWD-1, FWD-7 served this round). Staged until cc-7's redeploy closes and its snapshot event has re-written the /freshness snapshot. The GO names the worktree, the portal ref, and whether DSGN_AMGTV1's rows SAUX-41 and SAUX-42 (the Seeking Alpha states and the five sections drawn) are on that ref. AC3 is the CVO's L9 read. FWD-7 is graded only after DSGN's cell draws the served sentence (CTO msg 31672, term three). Checks dry-run at the base: cc-8 AC1 base FAIL as expected (0 captures, no record); AC2 as round 78's bb-19 (the account reads disarmed).

<status>staged</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~314</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending -- GO 2026-10-08T21:3xZ by the issuer after cc-7 closed (@42700562a4, graded @7cf4305781; snapshot ar7KPWgP rewritten 18:08Z by the new code ltXvElw). Worktree C:/tmp/r79-308 re-used (drained, clean), branch wk-AMGT_RESAPP-314 at the shared HEAD; portal ref 38cc0ecf (origin DEV), packages linked; DSGN_AMGTV1 SAUX-41 and SAUX-42 are NOT on that ref (0 seeking_alpha / dossier_sections hits in portal src), so FWD-7 and SECTIONS read the API beside the page; walker account disarmed, armedBy none; port 5174 0 listeners; no plant</status>
<status>pending -- RE-GO 2026-10-08T21:51:49Z by the issuer: the first GO came back BLOCKED @d03508571e/b44271afcc (rows Z-W314-S1 walker and S2 port, both contention with an AMGT_CORPUS walk); port 5174 released by 1.0.0_SA_CTO~Z (msg 32036), issuer read 0 listeners and the walker disarmed (armedBy none); same worker ~314, same worktree C:/tmp/r79-308, portal 38cc0ecf</status>
