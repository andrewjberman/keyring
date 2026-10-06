# AMGT_RESAPP task order -- `AMGT-az-1` -- THE /freshness PAGE RENDERED FOR THE CTO'S REVIEW: CAPTURES KEPT IN THE RECORD (CTO RULING 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-az-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~262</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one render pass by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- the CTO reviews a portal candidate only FROM A RENDER (since round 73). Round 75's walk captures lived in a gitignored folder of a removed worktree, so no render of 6de76f0509 is in the record.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r76-262` (branch `wk-AMGT_RESAPP-262`, cut from the issuance commit with `--portal-ref 6de76f0509 --node-modules link`). Work and commit only there. Start every shell call with `cd /c/tmp/r76-262`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-az-1` (round 76, decomposition s.84)

CTO ruling 1: the /freshness page candidate `6de76f0509` gets the CTO's review FROM A RENDER. It then joins DSGN rounds 43+44 as
ONE DEV ask to Andrew.

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z`. If `python .claude/skills/ui-walk/ui_walker_account.py status` reads
armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole
first. Serve the dev build on `http://localhost:5174` from YOUR worktree's portal (`cd portal && bun run dev:live --port 5174`). Role
admin.

Render the page against the deployed function and COPY every capture into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~262/captures/` (PNG). The walker's own folder is
gitignored and is lost with the worktree. Capture:
1. /freshness on a first visit (a fresh browser context), full page, with the first-paint time;
2. each sort button pressed, one capture per sort, with the first five rows' names in a caption file;
3. the stated never-collected input above the table, and one row's cells close up (contrast);
4. the page at 1280 and at 390 px wide.

Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~262/RENDER_FRESHNESS.md`: one line per capture (file, what it shows, the time). Then disarm.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W262-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit or
   commit.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~262/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-az-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; ls "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~262/captures/" | grep -c "\.png$"; echo "exit=$?"</invocation><expect>a count of 7 or more; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-az-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~262 <0.9.0_WK_AMGT_RESAPP~262@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~262/AMGT_RESAPP.TO-AMGT-az-1.freshness-render-for-review.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the capture count and the first-paint time;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-75 analysis ruling 1. The issuer sends the captures to the CTO; the DEV ask goes to Andrew through MSTR~Z after the review.

<status>pending</status>
<round>76</round>
<slot>0.9.0_WK_AMGT_RESAPP~262</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
