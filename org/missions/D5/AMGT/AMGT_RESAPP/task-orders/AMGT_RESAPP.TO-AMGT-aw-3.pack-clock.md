# AMGT_RESAPP task order -- `AMGT-aw-3` -- THE /freshness PACK CLOCK READ FROM THE STORED PACKS (FWD-7, ROW Z-W244-S1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~247</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- `packs/` is already read by the function.
comp-adversary: RUN by the issuer at the cut -- r73 c49 FAILS on deployed: 95 of 95 covered rows read pack NEVER while `packs/` lists 105 objects.
EGRESS CLASS, declared: NONE. No vendor, SEC, ft.com or wsj.com call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r73-247` (branch `wk-AMGT_RESAPP-247`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r73-247`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-3` (round 73, decomposition s.81)

Row Z-W244-S1. `_child_stamps` (`lib/research/api/scoped_amgt.py` ~`:5308`) looks for a stamp folder, but 103 of 105 keys are
`packs/<slash-safe key>/input_ledger.json` with none. The folder names are slash-safe encoded and must be decoded to the security key.
1. **The pack clock** for a covered name is the newest date of its stored pack: the ledger's own date field if it carries one, else
   the object's LastModified (`_pool_keys` currently discards it; keep it).
2. **Every covered row's `pack`** is that date, or NEVER only when no pack object exists for the name.
3. **The plant test** `lib/research/api/tests/test_pack_clock.py`: an encoded folder decodes, and a ledger-only pack yields a date.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W247-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No other freshness field changes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~247/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_pack_clock.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell c49 --where local; echo "exit=$?"</invocation><expect>population covered rows 95 status 200; C1 PASS NEVER 0; R73 C49 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~247 <0.9.0_WK_AMGT_RESAPP~247@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~247/AMGT_RESAPP.TO-AMGT-aw-3.pack-clock.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 3, ruling 3; row Z-W244-S1. Served by aw-7.

<status>pending</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~247</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~03:2xZ):** CLOSED -- drained @829ba218dd. On the shared tree, c49 local reads 95 of 95 dated, NEVER 0, YES. proof VALID. /freshness now reads ~105 ledgers per request; timed at aw-7. Served by aw-7.

<status>complete</status>
