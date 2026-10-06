# AMGT_RESAPP task order -- `AMGT-aw-8` -- THE WALK AFTER aw-7 (PRD v0.40): FWD-18, FWD-31 (+ THE 44-NAME CENSUS), FWD-1, FWD-5, FWD-7

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~251</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- the CVO's v87 left FWD-7, FWD-18 and FWD-31 one step short, FWD-5 a data dump, and FWD-1 unwalked; PRD v0.40 restates FWD-1 and FWD-18 as on-demand seat acts.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r73-251` (branch `wk-AMGT_RESAPP-251`, cut from the issuer's tree after aw-7, with `--portal-ref <aw-4's portal commit, else 2146031c> --node-modules link`). Work and commit only there. Start every shell call with `cd /c/tmp/r73-251`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-8` (round 73, decomposition s.81)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z`. If `python .claude/skills/ui-walk/ui_walker_account.py status` reads
armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole
first and follow its safety model. Use the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run
dev:live --port 5174`). Role admin; role-gated differences are not covered.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~251/WALK_ROUND73.md`: per act, the DONE WHEN quoted from the PRD (v0.40), what you saw, and the capture names
with a positive control.
- **FWD-18** (`:660-661`, v0.40): click a driver-chart figure on BA and ASML_NA through to its passage.
- **FWD-31** (`:857-868`): a browser capture of BABA or SAP_GY Exec Management, with the route and tab-label control.
- **The 44-name census** (CTO ruling 5): write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~251/FWD31_CENSUS.md`, every covered name that serves the team passage but no
  roster object, each with its plain reason. Print `CENSUS n names, n with a reason`.
- **FWD-1** (`:487`, v0.40): on the 12 names that serve segments, the segment breakdown read on the page.
- **FWD-5** (`:521-525`): the rendered BA print pages, captured.
- **FWD-7** (`:539-542`): the /freshness page (aw-4's candidate on your dev build): find a stale name without opening folders.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W251-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~251/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cat "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~251/FWD31_CENSUS.md" | tail -3; echo "exit=$?"</invocation><expect>a line `CENSUS n names, n with a reason` with both counts equal; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aw-8" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~251 <0.9.0_WK_AMGT_RESAPP~251@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~251/AMGT_RESAPP.TO-AMGT-aw-8.the-walk-after-aw7.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts per act;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 8, rulings 3-5; PRD v0.40. AC3 is the CVO's L9 read of WALK_ROUND73.md. Staged until aw-7 lands.

<status>staged</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~251</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~05:3xZ):** CLOSED -- drained @cdc5184187. Walked on deployed satkY3HX with portal fb939c4a
(the /freshness candidate).
- **AC1:** CENSUS 42 names, 42 with a reason, over 93 readable covered names. BP/_LN and NG/_LN return 404 on /thesis (row Z-W251-S4).
- **AC2:** the walker reads disarmed (DISARMED sent to MSTR~Z 05:26Z).
- **AC3** (judgment) goes to the CVO's L9 via WALK_ROUND73.md.
- proof VALID. Rows Z-W251-S1..S4 INERT:
  - S1: FWD-18's served passage is not shown by the page;
  - S2: FWD-1's served segments are drawn by no tab;
  - S3: the /freshness page takes ~12 s, flags 95/95 stale, has low contrast, and its sorts are ineffective;
  - S4: the census is 42, not 44, and the slash-key 404.

<status>complete</status>

