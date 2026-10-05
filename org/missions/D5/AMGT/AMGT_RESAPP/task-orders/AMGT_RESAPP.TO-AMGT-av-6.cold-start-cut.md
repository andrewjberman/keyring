# AMGT_RESAPP task order -- `AMGT-av-6` -- THE COLD START CUT WITH NO SPEND: THE FIRST REQUEST MAKES 15 AWS CALLS OR FEWER (CTO RULING 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~242</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- `BatchGetItem` on the classification table: name it in your report (av-8's pair checks the role allows it).
comp-adversary: RUN by the issuer at the cut -- r72 c46 FAILS (local, a fresh process per route): the first rankings read makes 153 AWS calls, the first chatter read 167. Init is not the cost (Init Duration median 214 ms).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r72-242` (branch `wk-AMGT_RESAPP-242`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r72-242`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-6` (round 72, decomposition s.80)

CTO ruling 2: measure the cold path and cut what is cuttable, with no spend. Provisioned concurrency is Andrew's act, listed only if
the cold read stays above about 2 s. au-6's per-container memo cannot reach a cold container.

The first request's reads, in `lib/research/api/scoped_amgt.py`:
- `_join_classification` (~`:761`): about 100 serial GetItems. Use `BatchGetItem` through the existing `_batch_get` (~`:1605`),
  100 keys a call.
- `_model_block_name` (~`:1158`): reads a whole model block per unnamed name just for NAME. Use the crosswalk name it already holds.
- `_dynamodb` (~`:383`): create the resource at module init, so the first request does not pay for it.

1. **Before any edit,** capture the bodies of the 9 Lead Panel reads plus BA, AMD and ASML_NA `/overlay` and `/peers` into
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~242/before/`.
2. **Make the cuts.** Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~242/after_equal.py`, which prints `EQUAL n of 15` (ignoring `generated_at` at any depth) and
   exits 0 only on 15 of 15.
3. Keep au-6's `served_cache.py` behaviour.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W242-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No served value changes (AC2).
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~242/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c46 --where local; echo "exit=$?"</invocation><expect>each route's first request makes 15 AWS calls or fewer; C1 PASS; R72 C46 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~242/after_equal.py"; echo "exit=$?"</invocation><expect>EQUAL 15 of 15; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~242 <0.9.0_WK_AMGT_RESAPP~242@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~242/AMGT_RESAPP.TO-AMGT-av-6.cold-start-cut.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- per-route calls before and after;
- any new AWS action;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 6, ruling 2; row Z-W236-S1. The deployed cold read is graded at av-8 (leadpanel_cold_warm.py).

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~242</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

## 4a. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-05 ~22:1xZ) -- AC1's bar moves from 15 to 75; the remainder is a producer item

The worker measured that the three named cuts reach 60 / 72 first-request calls (from 153 / 167), with values EQUAL 15 of 15.
- The remaining cost is the 23 ranked names held only in their model blocks. The crosswalk carries no name for them (row
  Z-W242-S1).
- Reaching 15 needs those names registered: a producer act plus an identity pull, outside this cell. Ruling: accept the cut, and
  carry the registration to round 73 with row Z-W236-S1.
- **Provisioned concurrency stays Andrew's act** (CTO ruling 2) if av-8's deployed cold read stays above about 2 s.

**AC1, as amended** (the issuer re-grades it on the shared tree at the drain):

<criterion id="AC1" cell_refs="AMGT-av-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c46 --where local --bar 75; echo "exit=$?"</invocation><expect>each route's first request makes 75 AWS calls or fewer; C1 PASS; R72 C46 SERVED: YES; and exit=0</expect></criterion>

Gate limb that graded this modification: GATE (viii) on a modify (`<placeholders>NONE</placeholders>`).

