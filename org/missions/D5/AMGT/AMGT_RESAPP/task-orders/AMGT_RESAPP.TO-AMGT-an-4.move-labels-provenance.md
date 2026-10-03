# AMGT_RESAPP task order -- `AMGT-an-4` -- FWD-38 c + d: EVERY SERVED MOVE NAMES ITS AXIS AND WINDOW; THE OVERLAY'S PROVENANCE BLOCK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~213</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; every pool or table access is a read the function already makes.
comp-adversary: RUN by the issuer at the cut -- r64_served c13 FAILS at the base: 0 of 94 chatter moves labelled; no provenance block on any overlay.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r64-213` (branch `wk-AMGT_RESAPP-213`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r64-213`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-an-4` (round 64, decomposition s.72; FWD-38 c, d)

PRD FWD-38 (v0.34) clauses 3 and 4 (SAUX-22, SAUX-25).
1. **Move labels.**
   - Every collected/chatter row with a `places_moved` serves `places_moved_axis` (the axis it was read from) and
     `places_moved_window_days`. Today monthly chatter reads TRENDING/PRICE (`monthly_chatter.py` about :166) while the overlay's
     `breakout_price.places_moved` reads BREAKOUT/PRICE.
   - Label each so the two are told apart. Do not change which axis each reads.
   - The ranking rows and the overlay already name `movement_measure` and `window_days`; keep them.
2. **Provenance.** `/security/{key}/overlay` serves `provenance: {inputs: [...]}` with one entry for each of `filings`,
   `harvested_news` and `bloomberg`. Each entry is `{input, last_run, source, reason}`:
   - `last_run` is the ISO time of that input's newest landed artifact for the name: the filing in the M-1 or input ledger, the newest
     gold mention row or snapshot vintage, the Bloomberg model block's vintage.
   - When none can be read, `last_run` is null with a plain `reason`.
   - Read only what the overlay already reads, or one stored object per input. No new source.
3. Tests for both.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W213-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-an-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c13 --where local; echo "exit=$?"</invocation><expect>C1 PASS (every chatter places_moved names its axis and window); C2 PASS for BA, AMD and VLO (provenance names filings, harvested_news, bloomberg with a last run or reason); R64 C13 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~213 <0.9.0_WK_AMGT_RESAPP~213@opal.agent>" -F <msgfile> -- <paths>` (message file written
with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~213/AMGT_RESAPP.TO-AMGT-an-4.move-labels-provenance.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~22:0xZ) -- the round-63 analysis @8642d76ceb

**Package watch (analysis section 3):** the artifact is at 96.8% of the 262,144,000 B ceiling. In your worktree, after your commit, run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only /c/tmp/r64-pkg-<slot>.zip` and report its `SIZE:` line and `CONTENT-DIFF SUMMARY`. A build past the ceiling is a STOP: report it, and do not trim to fit.

Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order; GATE (viii) does not apply, `<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD v0.34 FWD-38 clauses 3-4 (SAUX-22, 25). Served by an-7.

<status>pending</status>
<round>64</round>
<slot>0.9.0_WK_AMGT_RESAPP~213</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~23:3xZ):** ACCEPTED. Worker ~213 `bd60106e45`, drained `40e52072ce`. Re-graded on the shared tree: union (peers + management + api + harvest + coverage) 1012 passed exit=0 after the drain repairs `949b24cadb` (the am-1 day-route tests) and the an-3 fake; c13 YES (94 of 94 chatter moves labelled TRENDING_PRICE + window; provenance on BA/AMD/VLO; filings serves null with a reason where the ledger holds no filings run). Package 96.8%. Served by an-7.

<status>complete</status>
