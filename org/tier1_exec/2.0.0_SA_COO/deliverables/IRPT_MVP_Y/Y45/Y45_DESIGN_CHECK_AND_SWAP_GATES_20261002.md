# Y-4 / Y-5 design -- wire the check gate and the swap gate, and let a user continue without a new upload (CTO rulings batch 178, ruling 5)

**Seat:** `2.0.0_SA_COO~Y`, 2026-10-02 ~23:1xZ. **Status:** design, read from code; nothing built. **Order:** after st14's
V1 and the Y-3 packet.
**Ruling 5, verbatim:** "WIRE BOTH. The check gate offers a typo's likely ticker. The swap gate offers similar ETFs AND
accepts a user-named proxy ticker that YCharts verifies, so Case D's stated proxy (SGOV) is reachable whatever the gate
suggests." Kimi: VEW-3, "can be called freely". YCharts: Andrew ~18:1xZ for these cases, one at a time, queue empty.

## What exists (read in code)

- `intake/resolution_kimi.py` `KimiAdvisory`: bounded check and swap calls. It has no network client and no credential:
  the installer supplies `send` and a durable `telemetry` sink. Swap refuses (`KIMI_WEB_SEARCH_UNVERIFIED`) until provider
  QA pins a web-search tool configuration.
- `intake/security_resolution.py` `verified_suggestions`: keeps only suggestions the provider answers FOUND.
- The estate's transport, same model (`kimi-k3`): `infra/aws/lambda/v2_portal/_shared/etf_classification_model.py`
  `default_send` (urllib, `https://api.moonshot.ai/v1/chat/completions`). The key is read BY NAME from the estate's secret
  (`classify-residual-model.py:84`, ESTATE_KIMI_SECRET_ID in `infra/aws/terraform/estate-report/instance.tf`).
- Today a not-found row ends `TICKER_NOT_FOUND`, action `REPLACE_FILE`. A typo and a real untracked asset read the same.

## The change, in build order

1. **Check gate (Y-4), on the resident's resolve.**
   - When the freeze ends NEEDS_CORRECTION with TICKER_NOT_FOUND rows, the resolver calls `KimiAdvisory.call("check", symbol,
     context_symbols=<the file's other symbols, <= 20>)`, bounded to 10 rows per upload.
   - Each suggestion passes `verified_suggestions` (one securities_info read for all of them).
   - The finding gains `suggestion {symbol, provider_receipt_sha256}` and action `ACCEPT_SUGGESTION`.
   - Advisory only: nothing is substituted without the user.
2. **The correction revision.** A new owned write on the upload carries the user's choices per row:
   - `{row, replacement, basis: SUGGESTION_ACCEPTED | PROXY_NAMED}`;
   - the resident re-reads ONLY the replacements (YCharts FOUND exact) and freezes the next NORMALIZATION revision. The
     original bytes are untouched, and revision r stays readable.
   - The substitutions go into `disclosures.corrections` (the field exists, empty today), so the report says what was proxied.
   - Bounds: a replacement must itself verify; a row may be corrected once per revision; a refused replacement names its row.
3. **Swap gate (Y-5).** Two halves:
   - **(a) User-named proxy, now:** the page lets the user name a proxy for an untracked row. It is a `PROXY_NAMED`
     correction verified by YCharts, and needs no Kimi web search. Case D's SGOV goes through this, whatever the gate
     suggests.
   - **(b) Kimi swap suggestions, after provider QA:** pin the web-search request fields with a QA receipt (the module's own
     gate), then `call("swap", ...)` proposes up to three ETFs. Each is verified like a check suggestion.
4. **The resident's Kimi port.**
   - `send` is the estate pattern (urllib to the Moonshot endpoint). The deadline is enforced by the module.
   - The key is read by name from the estate secret into memory, never printed.
   - Telemetry goes to the job/normalization row (durable before the call).
   - IAM: the resident role gains `secretsmanager:GetSecretValue` on that one secret (`ycharts/resident.tf`).
   - Egress is the host's.

## Contracts (named for the CTO)

- The upload answer's findings gain `suggestion` and the action `ACCEPT_SUGGESTION`, an additive change to the
  correction finding shape.
- A new request (the correction revision) and its response: a new routes.json entry on irpt-ycharts-generate.
- The page (`2.0.0_SA_COO~D`):
  - shows "row 2 APPL -- did you mean AAPL?" with Accept;
  - shows "rows 14-17 are real but not tracked -- name a proxy" with a ticker field;
  - posts the correction.

## Proof plan

- **Typo file:** row 2 offers AAPL. Accept leads to NORMALIZED without a new upload.
- **Case D:** rows 14-17 named untracked; SGOV named and verified; NORMALIZED, then a READY Overview.
- Offline first (a replayed Kimi answer, replayed securities_info), then one live run per case under the solo gate.

## Ships as

Two packets:
- (1) check gate, correction revision and user-named proxy (resident, generate, IAM, route);
- (2) Kimi swap suggestions, after the web-search QA receipt.
