# AMGT_RESAPP task order -- `AMGT-az-6` -- THE WALK ON DEV AFTER ANDREW'S PUSH: FWD-7, FWD-18 AND FWD-1 ON THE DEPLOYED PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-az-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~266</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- FWD-7, 18 and 1 are built and were walked on a local merge; the CVO grades them on the page as deployed to DEV (PRD v0.40).
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r76-266` (branch `wk-AMGT_RESAPP-266`, cut from the issuer's tree after az-5 and Andrew's DEV push, with `--portal-ref 6b4e89a8`, the origin/DEV head carrying 1d6d2573 and 6de76f0509). Work and commit only there. Start every shell call with `cd /c/tmp/r76-266`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-az-6` (round 76, decomposition s.84)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z`. If `python .claude/skills/ui-walk/ui_walker_account.py status` reads
armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole
first. Serve the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role
admin.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~266/WALK_ROUND76.md`: per act, the DONE WHEN quoted from the PRD (v0.40), what you saw, and the captures (COPIED into
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~266/captures/`) with a positive control. The CVO names the companies per v0.40; walk BA, AMD and ASML_NA unless the GO names
others.
- **FWD-7** (`:539-542`): /freshness on a first visit; the first-paint time; can a stale name be singled out?
- **FWD-18:** open a driver-chart point; its filing passage with the cite and, for a table passage, the row and column labels.
- **FWD-1:** the segment breakdown, one heading per segment.
- **FWD-16** (if DSGN round 45 is on the ref): the top band.
- Then disarm.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W266-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~266/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-az-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; ls "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~266/captures/" | grep -c "\.png$"; echo "exit=$?"</invocation><expect>a count of 6 or more; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-az-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-az-6" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~266 <0.9.0_WK_AMGT_RESAPP~266@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~266/AMGT_RESAPP.TO-AMGT-az-6.the-walk-on-dev.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-75 analysis item 6. Staged until Andrew's DEV push (DSGN 43+44 with the /freshness page) and az-5. AC3 is the CVO's L9 read.

<status>staged</status>
<round>76</round>
<slot>0.9.0_WK_AMGT_RESAPP~266</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-06 ~21:2xZ):** both preconditions are met. Andrew's DEV push landed (MSTR~Z msg 30198, portal DEV e2130d42; DEV is now 6b4e89a8 and still carries 1d6d2573 and 6de76f05). az-5 is deployed and closed @1014126140 (CodeSha256 OVpDhfwD). The portal ref is `6b4e89a8`. Companies: BA, AMD and ASML_NA. FWD-16's top band is NOT on this ref (DSGN round 45 has not landed), so that act is skipped. Gate limb: GATE (viii) on a modify (`<placeholders>` NONE).

<status>pending</status>

