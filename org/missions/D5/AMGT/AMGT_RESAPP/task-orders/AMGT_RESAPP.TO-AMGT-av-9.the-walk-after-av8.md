# AMGT_RESAPP task order -- `AMGT-av-9` -- THE WALK AFTER av-8: FWD-7 AND FWD-19 ON DEMAND (v0.39), FWD-31'S BYTE ARM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~244</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- the CVO's v86 left FWD-7, FWD-19 and FWD-31 not realized; v0.39 restated FWD-7 and FWD-19 as on-demand proofs.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r72-244` (branch `wk-AMGT_RESAPP-244`, cut from the issuer's tree after av-8, with `--portal-ref a3ab197f --node-modules link`). Work and commit only there. Start every shell call with `cd /c/tmp/r72-244`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-9` (round 72, decomposition s.80)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z` for your run. If `python .claude/skills/ui-walk/ui_walker_account.py
status` reads armed by anyone else when you start or between passes, file a BLOCKING row and stop. Read
`.claude/skills/ui-walk/SKILL.md` whole first and follow its safety model. The dev build is `http://localhost:5174` (start it if
down: `cd portal && bun run dev:live --port 5174`). The role is admin; role-gated differences are NOT covered.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~244/WALK_ROUND72.md`: the act, the DONE WHEN quoted from the PRD, what you saw, and the capture names with a
positive control. Screenshots stay in `tmp/ui-walk/<stamp>/`.
- **FWD-7** (`:539-542`): open the one place on demand, see every covered company with its last-refreshed date, and find a stale
  one without opening folders. The research read found all 95 last-refreshed 2026-10-04, with staleness only per input; say what
  the page shows.
- **FWD-19** (`:673-678`): walk one covered name's posture. The header line and the last tab name the comparable, give the reasons
  each linked to what it rests on, and carry the machine's-view marking. The page stores no decision.
- **FWD-31's byte arm** (`:857-868`): the roster's own rows are byte-unchanged against the same tab captured WITHOUT the passage.
  Use a harness render with `dossier_fields.management` removed (`portal/src/pages/SecurityAnalysis/__harness__/`, read only; run
  a copy in your folder), and diff the roster rows.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W244-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~244/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cat "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~244/fwd31_byte_arm.txt"; echo "exit=$?"</invocation><expect>a line `ROSTER ROWS BYTE-EQUAL: n of n` for each name walked; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-av-9" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~244 <0.9.0_WK_AMGT_RESAPP~244@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~244/AMGT_RESAPP.TO-AMGT-av-9.the-walk-after-av8.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folders and capture counts;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 8. AC3 is the CVO's L9 read of WALK_ROUND72.md (FWD-7, FWD-19, FWD-31). Staged until av-8 lands.

<status>staged</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~244</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~00:5xZ):** CLOSED -- drained @edba4192b6. Walked on deployed 2lUlZomo with portal DEV
327b7d8e (newer than the order's a3ab197f, so the walk saw the current page).
- **AC1:** FWD-31 byte arm, ROSTER ROWS BYTE-EQUAL 32 of 32 over 4 names (ASML_NA, BABA, SAP_GY, BA); the negative control broke
  4 of 4.
- **AC2:** the walker reads disarmed (DISARMED sent to MSTR~Z 00:47Z).
- **AC3** (judgment): the CVO's L9 read of WALK_ROUND72.md (FWD-7, FWD-19).
- proof VALID. Row Z-W244-S1 INERT: the /freshness pack clock reads NEVER for 95 of 95, while the packs/ prefix lists 105 objects.

<status>complete</status>

