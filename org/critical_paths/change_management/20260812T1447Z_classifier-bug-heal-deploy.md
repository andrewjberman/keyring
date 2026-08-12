# Deploy-completion ledger: classifier bug heal (BUG-1 _RE_FI \b, BUG-2 dotted ticker)

**Status:** CLOSED
**Opened:** 2026-08-12T14:47Z (deploy-start) | **Closed:** 2026-08-12T14:50Z
**Operator:** 0.4.0_DS_ClientPlatform

**Authority:** ANDREW-DIRECT ~1430Z VERBATIM *"route the two classifier bugs to DS"* (record
`ANDREW_DIRECT_20260812_ROUTE_CLASSIFIER_BUGS_TO_DS.md`), spec + 4 controls from CVO 143643Z.
**CVO scope note, verbatim:** *"NOT A GATE: normal commit -> QA -> deploy cycle, yours... no seat
needs to sign before you proceed"* — flagged only because it changes client-facing served mix values.

## Scope
Deploy the healed classifier: `data/black_diamond/scripts/gold/lib/etf_classifier.py` (the ORIGINAL,
feeds the SERVED mix) and the byte-identical port
`data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py`. Committed @bd2a8f854a.

## ⚠ THIS IS AN INTENTIONAL SERVED-VALUE CHANGE
Names move UNCLASSIFIED -> fixed_income. **Measured:** Cottonwood $3,556,935 / 44 names + $793,815
(BRK.A) per CVO; **49F $2,428,594.60 / 5 names / 5 accounts** over a 2,313-row denominator, zero
equity moves (this seat, control 4 — NOT zero). Estate ~$6.78M reclassified.
Band **V35-CLASSIFIER-HEAL-INVERTED** declared PRE-EVIDENCE: on this band **divergence from the old
served value is the PASS and reproducing it is the FAIL.**

## ROLLBACK (stated BEFORE the deploy)
`git revert bd2a8f854a` + re-deploy the reverted bytes through the same `safe-deploy.sh` path. The
change is two regex edits in two files; no data is moved or deleted, so reversal is a redeploy, not
a restoration. Rollback trigger: the mandatory negative control failing on live data (a no-rate name
classifying fixed_income) or any equity->fixed_income transition appearing (measured: zero today).

## Verification plan
`safe-deploy.sh` does S3 cp + SHA verify + comp-pipescript confirm; the SHA verify is the evidence,
never the cp rc. Post-deploy: confirm MATCH on both keys.

## Execution log

**DEPLOYED 14:49Z via `.tools/safe-deploy.sh` (sanctioned path, explicit-files mode):**
- ✅ **`etf_classifier.py` -> `[bd] code/gold/lib/` DEPLOYED, `VERIFY OK` on
  `comp-pipescript deployed` (MATCH).** This is the ORIGINAL and the one feeding the SERVED mix, so
  **the heal is live on the path that carries the $6.78M.**
- ⏭ **`a07_dim_asset_classification.py` SKIP-NOT-MEMBER — the S3-membership guard working, not a
  failure.** Probe: `s3://opal-data-mdpf/code/scripts/assets_gold/runners_49f/...` -> **404**, prefix
  carries **0 members**. Per Rule 13, a shared-home script that does not yet exist in S3
  **first-mints EXPLICITLY, never via the push gate.** Consistent with the corpus's measured state:
  the whole `runners_49f` P1 set has only ever run locally (S3 gold held zero P1 artifacts before
  yesterday's fills). **The port's fix is committed and takes effect whenever A_07 next runs; no
  first-mint is performed here because none was authorized and none is needed for the heal.**

**Status:** CLOSED 2026-08-12T14:50Z — the served-mix heal is deployed and verified on the SHA, not
the cp rc; the port is committed-not-deployed by the guard's design and that is stated rather than
left to be discovered. No leg stranded.
