# MDPF_CANON task order -- `CN-s-1` -- THE MUNI ACCOUNT BECOMES A REGISTERED CUSTOM MODEL, "OPAL MUNICIPAL BONDS" (PRODUCER; FWD-9 head g)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~32</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell registers one more model key in code the scheduled run already executes.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read, no new key prefix, no IAM change; the code reads the same gold and silver inputs the producer already reads.
comp-adversary: RUN by the issuer on DELL1 at the base -- `r11_cn_s_1.py pure` pure 4 of 6 (A1 and A3 red; A0, A2, A4, A5 are controls the base already meets), `seams` seams 1 of 4 (S1, the byte-equal control) (S1 the byte-equal control); a scratch reference reads 6 of 6 and 4 of 4 (the arms can pass); planted mutants (only one crosswalk copy edited, the key left out of GLOBAL_MODEL_KEYS, the vendor name mapped to the sleeve's key, a substring match) each turn their named arm red; `selftest` prints OK.
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-s-1` (round 11)

**The cell, verbatim from the decomposition:** Muni becomes a registered custom model (head g): the vendor account named exactly `Opal_Muni_Income` routes to the new key `opal_muni_income`, display "Opal Municipal Bonds", leaving `income_non_model_residual` and entering `by_model` / `model_aua` on Cottonwood and, through `GLOBAL_MODEL_KEYS`, the Custom sum of Global; `Opal Hewitt Moderate Income` stays in Other and `opal_muni_sleeve` is untouched; registered in the producer (`CUSTOM_KEY`, `CUSTOM_DISPLAY_NAME`), the crosswalk and its byte-identical Lambda copy (`ModelEntry`, `COTTONWOOD_CUSTOM_MODEL_KEYS`, `GLOBAL_ACCOUNT_DIST_DISPLAY`; `GLOBAL_MODEL_KEYS` reads that tuple, so it needs no edit), and the existing custom-model test.

**Why (Andrew-direct 2026-10-15, "Muni is in Custom Models, yes"; "Nothing wider is ruled"):** the Cottonwood account named `Opal_Muni_Income` is about $63.2M and today sits in `income_non_model_residual` (Other AUM). It must move to Custom Models. The residual also holds a second account, `Opal Hewitt Moderate Income` (about $1.75M), which Andrew did NOT name: it stays where it is. Do not move the residual's aggregate; move the ONE account, by its exact vendor name.

**The mechanism is already in the code.** `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` has a REGISTERED custom model route ("a model with a key, never the residual -- it wins over both residual routes", near L802-806). The precedent is `Opal_Muni_Sleeve` -> key `opal_muni_sleeve`, display "Opal Muni Sleeve" (Andrew-direct 2026-10-01). Read how that one is registered and register the new one the same way, in exactly these places:

1. `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`: one `CUSTOM_KEY` row mapping the vendor name `Opal_Muni_Income` to the key `opal_muni_income`, and its `CUSTOM_DISPLAY_NAME` entry "Opal Municipal Bonds". The match is on the EXACT vendor name (not a substring, not a pattern): `Opal_Muni_Income_2` or `Opal Hewitt Moderate Income` must NOT match.
2. `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py`: one `ModelEntry("opal_muni_income", None, "Opal Municipal Bonds", "model", False)` mirroring the sleeve's entry (~L159); the key `"opal_muni_income"` in the `COTTONWOOD_CUSTOM_MODEL_KEYS` tuple where `opal_muni_sleeve` sits (~L167-171); the `GLOBAL_ACCOUNT_DIST_DISPLAY` entry (~L239) mapping it to "Opal Municipal Bonds".
3. `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py`: this file is a BYTE-IDENTICAL COPY of (2). Apply the same three edits so the two files stay byte-identical (check with `cmp`).
4. **Do NOT edit `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`.** Its `GLOBAL_MODEL_KEYS` (~L164) already ends with `+ COTTONWOOD_CUSTOM_MODEL_KEYS` read from the crosswalk ("so the two cannot list different keys"), so Global sums the new key into Custom through your edit (2). A literal added there would make a second list, which that file forbids. The check's arm S3 reads the resulting tuple.
5. Test: in `data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py` (27 tests pass today; keep them unedited) ADD at least one test for the new key: a fixture account named `Opal_Muni_Income` lands under `opal_muni_income` with display "Opal Municipal Bonds" and is not in the residual; `Opal Hewitt Moderate Income` stays in the residual; `opal_muni_sleeve` is unchanged and a different key. Use synthetic numbers; never a real account id or firm level.

Nothing else changes: no other key, no `meta` key, no existing model's value, no residual rule. The new key is a SEPARATE key from `opal_muni_sleeve`: never merge, rename or double count them.

## 2. BOUNDS

1. **No AWS contact of any kind**: no read, write, invoke or deploy. The deploy of this code is CloudOps's, in its own window, after a never-widen pair; none of it is yours. No install, no push.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Everything else is read-only; in particular `lib/`, the registry rows and every other gold script.
3. **CLIENT DATA:** never print an account id, a firm name beyond what is written here, or a client figure in your report, a row or a file. Test data is synthetic.
4. No non-ASCII character in any line you add. Keep each file's line endings as you find them (read them first). Use the Edit tool.
5. Do not edit the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/`. If a step cannot be done as written, file a row naming the step and stop on that step.

## 3. SURFACES

<paths>
data/assets/scripts/gold/build_cottonwood_mdpf_slice.py
data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py
data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py
infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-1.muni-to-custom-model.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~32/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/`.

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_1.py" pure; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-1 PURE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_1.py" seams; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-1 SEAMS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python -m pytest data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py -q; echo "exit=$?"</invocation><expect>no failure, at least 28 passed (27 pass at the base; your added test makes it 28 or more) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 runs the producer's routing code on synthetic fixtures; AC2 reads the registration across the producer, the crosswalk and its Lambda copy, and `GLOBAL_MODEL_KEYS`; AC3 is the regression guard (the base already passes 27; it must stay green with your added test). They cannot prove what the served objects read after a fire: that is the issuer's and CloudOps's read after the deploy (a never-widen pair first), and there is no judgment criterion on this build.

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~32/MDPF_CANON.TO-CN-s-1.muni-to-custom-model.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for). **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your paths), and only when every criterion passes. Commit through `.tools/safe-commit.sh` with a message file written by the Write tool; the commit gate (py_compile, ds-precommit, ruff py39) must pass -- if it refuses anything this order did not foresee, file a row and stop.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W32-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11, issuer 2.0.0_SA_COO~D1, on the CTO's round-10 analysis `ledger/ROUND_ANALYSIS.round10.md` (msg 6731) item 3 head (g), PRD v2.23 @1fb9ac96ab, Andrew's records `ANDREW_DIRECT_20261015_152xZ_*` and `_184xZ_*`. The mechanism was read from the code at HEAD on 2026-10-16 ~02:0xZ and recorded in `round11/draft/ROUND11_RECTANGLE_DRAFT.md` (@a9a212fe6b).
- **Measured against the served Cottonwood object (2026-10-14, VersionId `ZddlHckHDbRRcROx6aaIZQH76Lm5xd3T`):** the residual holds $64,990,553.26 for 2 accounts: `Opal_Muni_Income` $63,241,218.96 and `Opal Hewitt Moderate Income` $1,749,334.30. After the change the same date reads Custom about $88.07M and Other about $285.38M with the Total unchanged. The existing `opal_muni_sleeve` ($554,036.75) is a different key already inside `model_aua`.
- **Because the producer recomposes every date from the gold dim partitions each run, adding the row moves the ENTIRE served history of both objects (Cottonwood and Global) on the next fire**, from the account's first date. The never-widen pair counts that, with a per-key rollback (prior VersionIds), the writers of each moved leaf (N printed), and the Happyland identity flag as its precondition (a printed match flag, no name; a mismatch stops the deploy). The account's first date, and whether it exists before 2026-10-07, are still unread.
- **Deploy surfaces:** the gold lambda package AND the daily-emitter Lambda package (the crosswalk copy). That the copy is a SECOND deploy surface is INFERRED from its path and is to be confirmed at the CloudOps order with `comp-pipescript io` / `comp-estate`; both CodeSha256 values are read afterwards. Terraform, never `update-function-code`.
- **Deploy order:** one gold change per fire; round 10's change fired 2026-10-16 13:30Z and read 11 of 11. This lands no earlier than the 2026-10-17 13:30Z fire.
- **Not in this cell:** the Cottonwood Trend page (CN-s-3), the deploy, the pair, the identity check, any change to `opal_muni_sleeve`, to the residual rule or to the Hewitt account.

**Never-widen pair (COO half drafted after the cell builds; CTO half):** the act is a gold-package and a daily-emitter deploy that moves served bytes at two firms (Cottonwood and Global, and the Global fold). The pair names the blast radius (what the act may touch: the two objects and their parquet partitions; the rollback per key), reads the expected outcome from the producer's own rule at signing (both branches: the account present and absent on a date), counts the writers of each moved leaf, and carries the identity flag.

**Fanout:** 2 of 2 chains (`CN-s-4` -> `CN-s-5` -> `CN-s-3`; `CN-s-1`). Slot ~32. No shared file with the portal chain. Base: box/dell1 at the issuance commit.

<status>complete</status>
<round>11</round>
<to_id>MDPF_CANON.TO-CN-s-1</to_id>
<slot>~32</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
