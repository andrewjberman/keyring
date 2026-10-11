# AMGT_RESAPP task order -- `AMGT-ff-1` -- A CLASSIFICATION NAME NEVER OVERRIDES A REGISTERED COMPANY NAME THAT DISAGREES WITH IT (THE BARE-TICKER COLLISION: SANOFI SERVED AS BANCO SANTANDER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ff-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~387</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ff-1.a-classification-name-never-overrides-a-disagreeing-registered-name</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a name-chain rule and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r94_name_census.py reads the crosswalk, the classifications table and stored model blocks with the caller's own credentials (GET only).
comp-adversary: RUN at the cut -- r94_display_name.py FAILs D1 at the base and PASSes D2-D6, and PASSes 6 of 6 against a throwaway candidate; r94_name_census.py --where local reads 2 DIFFERENT companies at the base (SAN_FP_Equity 'Banco Santander S.A.' for Sanofi, CSL_AU_Equity 'Carlisle Cos Inc' for CSL Ltd), 243 of 243 judged against a reference name, and 0 against the candidate which flips exactly those two served names and no other of 243. Cause read: the classifications table is looked up by the BARE Bloomberg ticker (`SAN FP` -> `SAN`); `SAN` is Madrid's Santander and Paris's Sanofi.
EGRESS CLASS, declared: NONE (S3 GETs by the census; no vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-387` (branch `wk-AMGT_RESAPP-387`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-387` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ff-1` (round 94, decomposition s.102)

CTO~DELL1 round-93 analysis item 1 (row D1-S23, ARMED; breach of FWD-13). `lib/research/api/names_read.py::display_names(keys, classifications)` names each
key: the classifications table's name looked up by the key's BARE Bloomberg ticker, else the crosswalk's registered name, else the stored model-block name, else
the display ticker. A bare ticker is not a company: the table's `SAN` row names Banco Santander, so `SAN_FP_Equity` (Sanofi) serves "Banco Santander S.A." on the
overlay and the peers subject, and the held-name index (`scoped_amgt._held_name_index`, built from the same chain) carries Santander's name under Sanofi's key;
`CSL_AU_Equity` (CSL Ltd) serves "Carlisle Cos Inc" the same way.

Add ONE rule inside `display_names`, where the classification name is about to be served: when the crosswalk has a registered name for the key (non-empty and
not just the bare ticker, case-insensitive) and the two names DISAGREE, serve the REGISTERED name (cleaned by `scoped_amgt._clean_display_name`) with source
`crosswalk`, instead of the classification name. Two names AGREE when the token sets of `numeric_tickers.name_token(scoped_amgt._clean_display_name(name))`,
each with the GENERIC words {com, stk, cl, class, cos, holdings, holding, group, del, new, and, corp, co, inc, ltd} removed, share at least one token of two or
more characters. No registered name, or a registered name that is only the bare ticker: the chain is unchanged. Nothing else in the chain moves (the order, the
source labels, the model-block and ticker fallbacks, the batching), and `monthly_chatter.py`, `scoped_amgt.py` and every route are untouched: the held-name
index and every route follow from the chain.

Add `lib/research/api/tests/test_names_read_agreement.py` (pure, no network; replace `scoped_amgt._crosswalk_names` and `scoped_amgt.resolve_identity` with
fixtures as `r94_display_name.py` does): one test per arm D1-D6.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W387-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. `r94_name_census.py`'s S3 GETs are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `names_read.py` minimally: do not reformat it and do not touch `monthly_chatter.py`, `scoped_amgt.py`, `numeric_tickers.py` or any served route.

## 3. SURFACES

<paths>
lib/research/api/names_read.py
lib/research/api/tests/test_names_read_agreement.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~387/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ff-1"><invocation>cd C:/dev/wk-resapp-387 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_display_name.py"; echo "exit=$?"</invocation><expect>PASS D1 (a classification name that disagrees with the registered name is not served), PASS D2, PASS D3, PASS D4, PASS D5, PASS D6; arms passed 6 of 6; R94 DISPLAY NAME: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ff-1"><invocation>cd C:/dev/wk-resapp-387 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where local; echo "exit=$?"</invocation><expect>judged 243 of 243 subjects, UNJUDGED 0, DIFFERENT company 0, the spelling variants listed; PASS C1; R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ff-1"><invocation>cd C:/dev/wk-resapp-387 &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_names_read_agreement.py lib/research/api/tests/test_ay3_names_read.py lib/research/api/tests/test_display_name_case.py lib/research/api/tests/test_model_block_names.py lib/research/api/tests/test_feed_and_names_an3.py lib/research/api/tests/test_monthly_chatter.py lib/research/api/tests/test_price_identity_join.py lib/research/api/tests/test_am5_unknown_key_and_chatter_inputs.py lib/research/api/tests/test_az4_cold_cut.py lib/research/api/tests/test_lead_list_names_and_places_moved.py -q; echo "exit=$?"</invocation><expect>the control: the new test file and the nine existing names tests pass (no failed, no error); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~387 <0.9.0_WK_AMGT_RESAPP~387@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~387/AMGT_RESAPP.TO-AMGT-ff-1.a-classification-name-never-overrides-a-disagreeing-registered-name.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-93 analysis @bfa6b04c8c item 1: "A classification name never overrides a registered company name that disagrees with it, and the held-name index carries ONE company per key. Close: a census of every served subject whose display name differs from its crosswalk company, count printed: 0 wrong companies, spelling variants listed. It is a served change, under its own pair." The census (`r94_name_census.py`) judges each of the 243 MEASURED subjects against every reference name its record holds (registered identity name 68, `legal_name` 211, research folder 96, model-block header 100); 0 are unjudged. The base reads 2 wrong companies, not the 1 the packet named (CSL_AU_Equity served as Carlisle Cos Inc). 35 are spelling variants and are listed, not defects. Producer-side code; the served change is `AMGT-ff-4` (staged, its own pair).

<status>pending</status>
<round>94</round>
<slot>0.9.0_WK_AMGT_RESAPP~387</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
