# AMGT_RESAPP task order -- `AMGT-af-3` -- THE PRICE RANKING OVER THE COVERED NAMES (FWD-35)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-af-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~199</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the issuer at the cut -- the producer is the 07:00 ET `:price_leg` step of the Scheduled Task OPAL_BBGTML_daily_pull on this box, which runs the site-Z WORKING TREE; this order changes no schedule. Its served effect lands only when the issuer merges it (af-6, under both never-widen halves).
comp-iam: DECLARED-NOT-APPLICABLE -- the producer already writes the same DynamoDB generation; the S3 list of research_dossier/ is by the box's own identity (the same one that runs the pull).
comp-adversary: RUN by the issuer at the cut -- AC2 FAILS at the base (C1: no load_covered_universe). The crosswalk resolves 95 of 95 decoded covered keys to a Bloomberg form (the two slash names as `BP/ LN`, `NG/ LN`).
EGRESS CLASS, declared: NONE for this order. Do NOT run the producer against Bloomberg; every proof here is offline or a dry run with a stub client.
</preflight>

**Your worktree:** `C:/tmp/r56-199` (branch `wk-AMGT_RESAPP-199`, cut from the issuance commit). Work and commit only there.

## 1. THE ACT -- `AMGT-af-3` (round 56, decomposition s.64)

`integrations/bloomberg/research/price_axis_pull.py` ranks 34 names from an old worker file (`UNIVERSE_PATH`, the `--universe` default
at `:239`). FWD-35 wants every covered name with at least two price observations in the 30-day window, and every other covered name
counted and named in the generation's own exclusion record.

1. **`load_covered_universe()`** in `price_axis_pull.py`, returning
   `{"tickers": [sorted, distinct], "mapped": {security_key: ticker}, "unmapped": [{"security_key", "reason"}], "denominator": int, "source": str}`:
   - population = `lib.research.coverage.covered_universe.covered_security_keys()` (fresh; decoded keys; 95 at the cut);
     `denominator` = its length; `source` names `research_dossier`;
   - each key's ticker = `lib.research.api.scoped_amgt.resolve_identity(key)["bloomberg"]` -- the crosswalk's own form, never a string
     transform of the key; a key with no `bloomberg` form goes to `unmapped` with a plain reason.
2. **`main()`** uses `load_covered_universe()` by default. `--universe PATH` may stay as an explicit override, but its default is no
   longer `UNIVERSE_PATH`. Log the denominator: `universe: N of D covered name(s) mapped (source: ...)`.
3. **The exclusion record.** Names dropped for fewer than 2 observations (`insufficient`, `:273` at the cut) and every `unmapped` key are
   written into the generation's own `excluded` record with a reason each (`lib/research/price/generation.py` `compute_price_axis`
   already carries `excluded`; pass them through, do not invent a second record). Nothing covered is silently absent.
4. **Test** `integrations/bloomberg/research/tests/test_price_universe.py`: a stub `blp_client` module returns a usable series for some
   tickers and fewer than 2 rows for one; a `--dry-run` (no write) proves the generation's `excluded` names the thin ticker and an
   unmapped key with reasons, and the ranked rows cover the rest. Stub the covered-universe and identity calls; no network.

## 2. BOUNDS

1. Write only the paths below. Do NOT run the producer for real (no Bloomberg call, no DynamoDB write); do not edit the Scheduled Task,
   the `.cmd`, the breakout rule or the chatter axis. Do not edit `lib/research/api/scoped_amgt.py` (sibling cells own it).
2. Standing: no S3 delete, no push of shared branches, no portal change.

## 3. SURFACES

<paths>
integrations/bloomberg/research/price_axis_pull.py
integrations/bloomberg/research/tests/test_price_universe.py
lib/research/price/generation.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~199/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-af-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider integrations/bloomberg/research/tests/test_price_universe.py lib/research/price/tests/; echo "exit=$?"</invocation><expect>every test passes, test_price_universe.py included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-af-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round56/checks/af_3_universe.py; echo "exit=$?"</invocation><expect>C1-C5 PASS; THE PRICE PRODUCER RANKS OVER THE COVERED NAMES: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~199 <0.9.0_WK_AMGT_RESAPP~199@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~199/AMGT_RESAPP.TO-AMGT-af-3.price-ranking-over-the-covered-names.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, the mapped / unmapped counts, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** addendum D FWD-35. The merge of this branch into the site-Z working tree IS the served act (the 07:00 ET task runs the
working tree): the issuer holds it for af-6's pair. FWD-35 itself is graded on the scheduled generation, a QUALIFIED WAIT (v0.32): the
terminal session is Andrew's login (placement s.5 item 1).

<status>pending</status>
<round>56</round>
<slot>0.9.0_WK_AMGT_RESAPP~199</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
