# AMGT_RESAPP task order -- `AMGT-ax-6` -- THE WALK AFTER ax-5: FWD-5 (THREE RENDERED PRINTS), FWD-7 (THE PAGE), FWD-4 (FEED LINKS AFTER HARVST GOLD #6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ax-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~256</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- the CVO's round-73 grades left FWD-5, FWD-7 and FWD-4 unrealized.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r74-256` (branch `wk-AMGT_RESAPP-256`, cut from the issuer's tree after ax-5, with `--portal-ref <ax-2's portal commit> --node-modules link`). Work and commit only there. Start every shell call with `cd /c/tmp/r74-256`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ax-6` (round 74, decomposition s.82)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z`. If `python .claude/skills/ui-walk/ui_walker_account.py status` reads
armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole
first. Serve the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role
admin.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~256/WALK_ROUND74.md`: per act, the DONE WHEN quoted from the PRD (v0.40), what you saw, and the captures with a
positive control.
- **FWD-5** (`:521-525`): print BA, AMD and ASML_NA from the page and save the PDFs under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~256/print/`; describe the form
  (font, headings, layout).
- **FWD-7** (`:539-542`): open /freshness and find a stale name without opening folders; time the table's first paint.
- **FWD-4** (`:505-507`): on BA's feed, follow one item's link out (stop at the link target URL; do not load third-party pages).
  If HARVST's gold rebuild #6 has not landed, say so: it is visible as the feed serving `url` on 0 items.
- Then disarm.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W256-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~256/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ax-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; ls "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~256/print/" | grep -c "\.pdf$"; echo "exit=$?"</invocation><expect>3; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ax-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ax-6" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~256 <0.9.0_WK_AMGT_RESAPP~256@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~256/AMGT_RESAPP.TO-AMGT-ax-6.the-walk-after-ax5.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts;
- the /freshness first-paint time;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-73 analysis item 7. AC3 is the CVO's L9 read of WALK_ROUND74.md. Staged until ax-5 lands.

<status>staged</status>
<round>74</round>
<slot>0.9.0_WK_AMGT_RESAPP~256</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-06 ~08:3xZ):** ax-5 is live. The function is `0MZWPl7nGZzFI53w+vsKdS7hQpcxu4Mrd5wEMWWZQpA=` (08:00:43Z), and the gateway has 11 security routes including the greedy one. The issuer's r74 c53, c55 and c56 deployed checks read YES. The portal ref is ax-2's candidate `6de76f0509`. The walker slot was granted by `0.0.0_AB_MSTR~Z` (msg 29971, status disabled/armed=no at 08:28Z). The issuer relays ARM and DISARMED to MSTR~Z; the worker sends no message. HARVST gold #6 has landed (r71 c35 deployed YES: 602 of 657 feed items carry a url).

<status>pending</status>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~08:5xZ):** CLOSED -- drained @46094b6b0f. AC1 reads 3 PDFs; AC2 disarmed, re-read by the issuer at 08:52Z (status=disabled armed=no); proof VALID. AC3 (`WALK_ROUND74.md`) is the CVO's at L9. DISARMED was relayed to 0.0.0_AB_MSTR~Z at 08:52Z. Rows Z-W256-S1 (print: thesis/risks/recommendation read 'not written' while the page shows drafts; every 'as of' reads 2026-10-06, including fiscal-year lines) and Z-W256-S2 (/freshness 95 of 95 flagged, first row 9.1 s on a cold load, the read 8.1 s for 2.85 MB) are INERT and carried to the drain-end read.

<status>complete</status>
