# AMGT_RESAPP task order -- `AMGT-aw-6` -- THE POOL UNIVERSE BUILD KEEPS EACH NAME'S PRIOR FILING FORM WHEN ITS STORED SOURCE CANNOT DECIDE (Z-W243-S1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~250</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the dry-run writes nothing; the `--write-pool` is aw-7's leg under a pair.
comp-adversary: RUN by the issuer at the cut -- r73 c52 FAILS (local): the dry-run names 95 of 95, but 13 of 13 prior decided `filing_identity.form_expected` values (7 10-K, 6 20-F) regress to "none".
EGRESS CLASS, declared: NONE. **No SEC fetch** (Andrew's word): the stored SEC object only.
</preflight>

**Your worktree:** `C:/tmp/r73-250` (branch `wk-AMGT_RESAPP-250`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r73-250`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-6` (round 73, decomposition s.81)

Row Z-W243-S1; CTO ruling 7. `lib/research/identity/build_universe.py` builds `filing_identity.form_expected` from the stored SEC
object, which carries no filing history, so every name reads "none".
1. **Keep-prior.** Read the newest prior pool object (`universe/v1/<date>.json`, rows under `names`). For a name whose stored source
   cannot decide the form, carry the prior `filing_identity` (form, cik, source), marked with a plain provenance note
   ("kept from the 2026-09-16 universe; the stored filer list does not say"). A name the stored source CAN decide takes the new
   value. Never "none" over a prior decided value.
2. **The plant test** in `lib/research/identity/`: a prior 10-K name with an undecided new read keeps 10-K.
3. **Name the exact pool key** a `--write-pool` would write, for aw-7's pair.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W250-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. NO `--write-pool`, no store write. No SEC egress.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/identity/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~250/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell c52 --where local; echo "exit=$?"</invocation><expect>dry-run rc 0; covered named 95 of 95; prior decided forms 13; C1 PASS; C2 PASS regressions 0; R73 C52 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/identity; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~250 <0.9.0_WK_AMGT_RESAPP~250@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~250/AMGT_RESAPP.TO-AMGT-aw-6.keep-prior-pool-universe.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the pool key a write would land on;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 5, ruling 7; row Z-W243-S1. The write is aw-7's leg; the pair names the universe's readers (crosswalk build, peers, posture, filings, management, chatter, freshness).

<status>pending</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~250</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~03:2xZ):** CLOSED -- drained @fcfcef77ca. On the shared tree, c52 local reads 95 of 95 named, 13 of 13 prior forms kept, 0 regressions, YES. Identity suite 216 passed. proof VALID. The pool write is aw-7's leg at universe/v1/<as-of>.json.

<status>complete</status>
