# AMGT_RESAPP task order -- `AMGT-ay-6` -- THE WALK AFTER ay-5: FWD-5 (THREE PRINTS), FWD-7 (A FIRST VISIT), FWD-18 AND FWD-1 (ONCE DSGN 43+44 IS ON DEV)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ay-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~261</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- the CVO's round-74 grades left FWD-5 and FWD-7 unrealized; FWD-18 and FWD-1 are drawn on DSGN candidate 1d6d2573, awaiting Andrew's DEV push.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r75-261` (branch `wk-AMGT_RESAPP-261`, cut from the issuer's tree after ay-5, with the `--portal-ref` the GO names). Work and commit only there. Start every shell call with `cd /c/tmp/r75-261`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ay-6` (round 75, decomposition s.83)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z`. If `python .claude/skills/ui-walk/ui_walker_account.py status` reads
armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole
first. Serve the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role
admin.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~261/WALK_ROUND75.md`: per act, the DONE WHEN quoted from the PRD (v0.40), what you saw, and the captures with a
positive control.
- **FWD-5** (`:521-525`): print BA, AMD and ASML_NA from the page and save the PDFs under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~261/print/`. Describe the form, the
  dates a fiscal-year line and a market line carry, and whether the thesis, risks and recommendation print.
- **FWD-7** (`:539-542`): open /freshness on a FIRST visit (a fresh browser context) and time the table's first paint. Can you single
  out a stale name?
- **FWD-18 and FWD-1:** if the portal ref the GO names carries DSGN 43+44 (`1d6d2573`), open BA's driver chart and segments. Note the
  served passage with its labels, and one heading per segment. Otherwise say they were not walked and why.
- Then disarm.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W261-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~261/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ay-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; ls "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~261/print/" | grep -c "\.pdf$"; echo "exit=$?"</invocation><expect>3; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ay-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ay-6" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~261 <0.9.0_WK_AMGT_RESAPP~261@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~261/AMGT_RESAPP.TO-AMGT-ay-6.the-walk-after-ay5.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts;
- the /freshness first-visit paint time;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-74 analysis item 7. AC3 is the CVO's L9 read of WALK_ROUND75.md. Staged until ay-5 lands.

<status>staged</status>
<round>75</round>
<slot>0.9.0_WK_AMGT_RESAPP~261</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-06 ~12:0xZ):** ay-5 is live on `D29LJCXhOStZ51JD4TTt2Jk0QUVDUbXDouXRTUS1ULI=` (11:28:32Z). The snapshot was written 11:32:38Z, and the schedule `amgt-global-freshness-snapshot-daily` is ENABLED. The issuer's deployed read is r75 c57/c58/c59/c61 YES and r74 c55 YES. The walker slot was granted by `0.0.0_AB_MSTR~Z` (msg after 12:03Z). The issuer relays ARM and DISARMED; the worker sends no message.

**The portal in your worktree** is `6de76f0509` (the /freshness page candidate) with DSGN 43+44 (`1d6d2573`) merged UNCOMMITTED by the issuer, for this walk only. It is never committed or pushed: do not commit, reset or clean it. So FWD-18 and FWD-1 ARE walkable on this build. Record that they were walked on a local merge of two candidates, not on DEV (DEV is `cf3f10c6`).

<status>pending</status>
