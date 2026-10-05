# AMGT_RESAPP task order -- `AMGT-au-5` -- ONE SIGNED-IN WALK OVER NINE OUTCOMES, FWD-5's THREE-NAME PRINT AND FWD-8's IDENTITY READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~235</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account with the operator's credentials (its own skill's mechanism); no other write.
comp-adversary: RUN by the issuer at the cut -- the round-70 sweep left FWD-1, 3, 6, 10, 15, 17, 18, 19 and 31 UNMEASURABLE for want of a seat walk; FWD-5 and FWD-8 restated at v0.38.
EGRESS CLASS, declared: NONE. Localhost dev build only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r71-235` (branch `wk-AMGT_RESAPP-235`, cut from the issuance commit with `--portal-ref e6ab82ad --node-modules link`). Work and commit only there. Start every shell call with `cd /c/tmp/r71-235`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-au-5` (round 71, decomposition s.79)

**The issuer holds the walker slot** from `0.0.0_AB_MSTR~Z` for your run and tells nobody else; you message no one. If
`python .claude/skills/ui-walk/ui_walker_account.py status` reads armed by anyone else when you start, file a BLOCKING row and stop.

Read `.claude/skills/ui-walk/SKILL.md` whole before the first run and follow its safety model (dormant account, one lease, never run
`secret`, disarm at once if a walk dies). The engine is `node .claude/skills/ui-walk/walk.mjs --route /security-analysis --security
"<name>"` against the dev build on `http://localhost:5174` (start it if it is down: `cd portal && bun run dev:live --port 5174` in the
background). The account's role is admin; role-gated differences are NOT covered, and your notes say so.

Walk BA, AMD and ASML_NA. For each act below, take a capture and a POSITIVE CONTROL in the same capture set (a thing that must be
there), and record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~235/WALK_ROUND71.md`: the act, the DONE WHEN quoted, what you saw, the capture file names. Screenshots
stay in `tmp/ui-walk/<stamp>/` (gitignored); never commit them or paste them anywhere.
- FWD-1: the pack is reached and downloaded (PRD `:481`).
- FWD-3: a figure is challenged and answered from the page (`:498`).
- FWD-6: two versions compared (`:526`).
- FWD-10: a refusal seen on the page (`:560`).
- FWD-15: the ranked list opened and a row clicked through (`:614`).
- FWD-17: the profile answers a management question (`:636`).
- FWD-18: a filing figure clicked through to its passage (`:651`).
- FWD-19: a posture read (`:664`).
- FWD-31: the team's passage rendered beside the roster, the roster unchanged, an absent-with-reason arm, a positive control (`:844-854`).
- FWD-5 (v0.38, `:515-519`): print the pack for the three names on demand; save each file under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~235/print/`.
- FWD-8 (v0.38, `:540-543`): write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~235/fwd8_identity.py`, which reads on the DEPLOYED function, for every covered name, the
  comparison block's subject identity against the page's, and prints `FWD8 WRONG n of N`.

Quote each DONE WHEN from `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` at those lines. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W235-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Read-only on the product: the walker's network guard admits only reads and the sign-in posts; never press a button the skill's
   DO_NOT_CLICK list names. No deploy, no store write, no vendor or model call, no portal edit.
2. Disarm the walker when you finish, and on any failure; `status` must read disarmed in your report.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~235/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-au-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~235/fwd8_identity.py"; echo "exit=$?"</invocation><expect>FWD8 WRONG 0 of N with N the covered-name count; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads disarmed (status disabled, no live lease); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-au-5" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~235 <0.9.0_WK_AMGT_RESAPP~235@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~235/AMGT_RESAPP.TO-AMGT-au-5.signed-in-walk.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the walk stamp folder and capture count per act;
- the three print files;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-70 analysis item 5, ruling 2; CTO msg 29615 (admin role; captures + positive control are the CVO's L9 artifacts; analyst/PM accounts to Andrew's list). AC3 is the CVO's L9 read of WALK_ROUND71.md and the captures, per FWD. Wave 0: walks deployed GS//XHnV while the slot is free (CTO msg 29648, MSTR~Z msg 29644); none of the nine walked FWDs depends on au-1/3/4/6.

<status>pending</status>
<round>71</round>
<slot>0.9.0_WK_AMGT_RESAPP~235</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~18:0xZ):** CLOSED -- drained @0a0ba90abc. The re-seat at 16:06Z resolved Z-W235-S1. AC1: FWD8 WRONG 0 of 95. AC2: the walker reads disarmed (DISARMED sent to MSTR~Z 17:03Z). AC3 (judgment) goes to CVO L9 via WALK_ROUND71.md plus 3 print PDFs. proof VALID. Rows S2-S5 INERT.

<status>complete</status>
