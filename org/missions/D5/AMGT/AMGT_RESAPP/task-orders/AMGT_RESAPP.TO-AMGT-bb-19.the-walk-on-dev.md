# AMGT_RESAPP task order -- `AMGT-bb-19` -- THE WALK ON DEV AFTER THE ROUND-78 REDEPLOY: FWD-16, FWD-12, FWD-7, FWD-1, THE COVERAGE MARKER AND THE OFFICER ORDER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~303</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- round 77's walk (portal 8ddfe409, function MkM9Kf37) read FWD-16 with no press of a news item recorded, the thesis and the overlay stating a company's inputs in two places that disagree, 17 of 93 officer lists with the chief executive not first, and a company outside coverage reading "No articles collected this month" beside an article dated in the month.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** the GO names it (`C:/tmp/r78-303`, branch `wk-AMGT_RESAPP-303`, cut from the issuer's tree after the round-78 redeploy, with the portal ref the GO names and `--node-modules link`). Work and commit only there. Start every shell call with `cd /c/tmp/r78-303`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout. **Run no `bun install` in this worktree:** its packages are linked from the base checkout. If `bun run dev:live` fails for a missing package, file a BLOCKING row and stop.

## 1. THE ACT -- `AMGT-bb-19` (round 78, decomposition s.86)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z`. If `python .claude/skills/ui-walk/ui_walker_account.py status` reads
armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole
first. Serve the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role
admin. Round 77's one-pass driver is at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~286/instrument/`; copy it into your own
`instrument/` and extend it there.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~303/WALK_ROUND78.md`: per act, the DONE WHEN quoted from the PRD (with its version and line), what you saw,
and the captures (COPIED into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~303/captures/`) with a positive control. Record what you saw; give no verdict. Head each act
with its token so a reader can find it: FWD-16, FWD-12, FWD-7, FWD-1, COVERAGE, OFFICERS. An act you could not walk is still headed,
with its reason.

- **FWD-16, with ONE PRESS.** On BA, read the top band: the company line and the newest news day inside 30 days with its date. Then
  PRESS one news item of the band, once, and record exactly what opens: the article's own text, a link out, a panel, or nothing.
  Capture before and after the press. Read the item's source name as the page shows it: a plain publisher name, or a code.
- **FWD-12.** On BA, find every place the page states which inputs the thesis used (source, last run, result). Count the places.
  The repair is ONE statement, carrying a filings row that says what the page used. If the page still shows two, or the two
  disagree, record both with captures; the page half may not be on the ref, and the GO says whether it is.
- **FWD-7.** Open /freshness on a first visit. Read the "Seeking Alpha last read" column on 5 rows and record each cell exactly.
  The reader of that column is NOT changed by this round (its repair waits on another team's records): record what it reads
  today, and whether any row reads stale. First-paint time of the first and of a second visit.
- **FWD-1 on AMD US.** The model numbers, the business description, and what the page shows where a segment breakdown would be.
  The segment table is built this round and NOT served: record what is on screen, and write `SEGMENT TABLE NOT SERVED THIS ROUND`
  beside the heading.
- **COVERAGE.** Open one company outside the covered set (the GO names it; MSFT US unless it says otherwise). Record every place
  the page says, or implies, that the company is not covered, and every empty panel that gives another reason (for example "No
  articles collected this month"). The repair is one plain statement in one place. Then open BA and record that no such
  statement is drawn.
- **OFFICERS.** On BA, HD and one name the GO adds, read the management list in the order drawn: the first three rows with their
  titles. The repair puts a chief executive first, then a chief financial officer, where the list holds them.
- Then disarm.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W303-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. No plant by you: a planted read is the issuer's act, named in the GO.
3. No `bun install`, `bun add` or `bun update` in this worktree.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~303/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-19"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb19.py"; echo "exit=$?"</invocation><expect>8 or more captures and a walk record naming every act; R78 BB19 WALK RECORD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-19"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-19" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~303 <0.9.0_WK_AMGT_RESAPP~303@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~303/AMGT_RESAPP.TO-AMGT-bb-19.the-walk-on-dev.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts;
- for FWD-16: what the one press opened;
- for FWD-12: how many places state the inputs;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-77 analysis @a1e519f9eb with ADDENDUM 1 @6d7cd1fe3c (FWD-16 one press; the round-78 walk) and rulings
file @f97be3fd6f. Staged until bb-18's redeploy closes. The GO names the worktree's portal ref, whether DSGN's page halves (the one
statement of inputs, the coverage marker, the plain source name) are on it, the outside-coverage name and the third officers name.
AC3 is the CVO's L9 read. Checks dry-run at the base: bb-19 AC1 base FAIL as expected (0 of 8 captures, no record, exit 1); AC2 as
round 77's ba-24 (the account reads disarmed).

<status>staged</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~303</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-08T08:25:16Z):** bb-18's redeploy closed: the live function reads CodeSha256 `+s6R0/rcpQ6lJgYsX2JtxfgoFoCmiaozTtMreyyymTQ=`, applied 2026-10-08T07:19:32Z.
- **Your worktree is `C:/tmp/r78-307`, NOT `C:/tmp/r78-303`** (an idle tree re-used so no new checkout is made; disk). Its branch is `wk-AMGT_RESAPP-303`, at CLOUD `d8b60bb5c4`. Wherever section 1 says `cd /c/tmp/r78-303`, use `cd /c/tmp/r78-307`. Your serial, your deliverables folder (`deliverables/0.9.0_WK_AMGT_RESAPP~303/`) and the check's paths are as written.
- **The portal ref is `d1b21c97`**, the origin/DEV head read by ls-remote at 08:1xZ (portal branch `wk-AMGT_RESAPP-303-portal`), with the main tree's packages linked (`tsc` reachable). No `bun install`.
- **Whether DSGN's page halves are on that ref is NOT known to the issuer.** For FWD-12, COVERAGE and the source name: walk and record what is drawn. If the page does not yet draw `research_coverage`, the one statement of inputs or a plain source name, say so under the act's heading; that is a finding, not a failure of your walk. To settle what the SERVER sends, read the same field from the signed-in dev build's own API client for one name and record it beside the screen.
- **The outside-coverage name is MSFT US** (`MSFT_US_Equity`). **The third officers name is BP/ LN** (`BP/_LN_Equity`, a slash name: record whether its management list is drawn at all, then its first three rows).
- **Port 5174 is yours first** (CTO msg 31634: 0 listeners at 08:2xZ). When you finish, STOP the dev server and say so as the last line of your report: another walk waits for the port.
- **The walker account** read `armed=no armedBy=none` at 08:2xZ.
- **FWD-1 on AMD:** the segment table is still not served; write `SEGMENT TABLE NOT SERVED THIS ROUND` as the order says.
- Gate limb: GATE (viii) on a modify (`<placeholders>` NONE).

<status>pending</status>
