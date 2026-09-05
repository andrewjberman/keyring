---
name: tax-newacc
description: Enroll a new Tax SMA account into the OPAL_TAXSMA registry so it flows into the daily ETL, and pull its data now: `/tax-newacc {schwab_account_number}` with the client name and trade-start. Resolves the EXACT account number to its BD id (fail-loud on absent or !=1; never fuzzy), enrolls, runs an ad-hoc pull. Workspace-agent operated.
---

# /tax-newacc {schwab_account} — enroll a Tax SMA account + pull immediate data (OPAL_TAXSMA_REGISTRY WS-R4)

**What it does (Andrew's mechanism):** a newly-onboarded Tax SMA account should (1) get immediate
data and (2) flow into the daily ETL forever, with no code change. `/tax-newacc {schwab_account}`
does both: RESOLVE the exact account -> ENROLL it into the registry -> AD-HOC data pull.

**THE NON-NEGOTIABLE (PRD ss.2, Andrew verbatim):** resolution is EXACT on the account number and
FAILS LOUD if the number is absent or resolves to !=1. **No fuzzy name / last-4 / surname match, EVER**
-- a fuzzy match could pull the WRONG client's tax data; an exact account-number match cannot.

**Mechanism (built + exercised):**
- `infra/aws/lambda/.../opal-assets-bd49f-reporting-pull/taxsma_newacc.py` -- resolve+enroll one account.
- `taxsma_resolver.py` (D2 ladder: tier-1 xref exact/zero-egress; tier-2 sanctioned exact-number query
  and tier-3 account-api are GATED on Andrew's egress word) + `taxsma_registry.py` (ETag-conditional
  RMW roster). These are enroll-context (pandas); run locally/agent, NOT in the producer Lambda.

**Never:** enroll on a fuzzy/last-4 match; silently activate an UNRESOLVED account (it enrolls
pending_resolution only, honestly); make a tier-2/tier-3 vendor call without Andrew's egress word.

## Steps (agent-run, Phase A)

0. **Gather the exact inputs from Alyssa's onboarding doc:** `{schwab_account}` (exact number),
   `client_name`, `trade_start` (YYYY-MM-DD), strategy (default `Opal Tax SMA 200/145`). Do NOT infer
   the account number from a name -- the EXACT number is the key.

1. **Resolve (dry-run first).** From the producer dir:
   `python taxsma_newacc.py --schwab {acct} --name "{name}" --trade-start {YYYY-MM-DD}`
   - `would_enroll_active` + `resolved EXACT (tier=xref): bd_internal_id=...` -> proceed to step 2.
   - `resolution_gated` -> the account is not in the zero-egress xref. **STOP and surface to Andrew:**
     resolving+activating it needs his egress word (tier-2 sanctioned exact-number query -- rides the
     standing 49F-reporting egress IF the surface supports an exact-number query; or tier-3 account-api
     -- a NEW egress, PRD D3). Optionally record it now with `--enroll-pending --confirm` (honest
     "known account, BD id pending") so it is not lost; it activates once resolved.

2. **Enroll (active).** Re-run with `--confirm` to write the registry entry (idempotent -- a re-run of
   an already-enrolled account is a no-op; a pending->resolved re-run promotes it). The account is now
   in `blackdiamond/49f/_ops/taxsma_roster.json` and the daily ETL's `discover_accounts()` will include
   it (once the WS-R3 registry-read producer is deployed).

3. **Ad-hoc data pull (immediate data).** For the just-enrolled account:
   - **Preferred (BD-direct, productionized):** invoke the PT2 producer for this one account --
     `aws lambda invoke --function-name opal-assets-bd49f-reporting-pull --payload
     '{"accounts":[{"bd_account_id":<bd_internal_id>,"schwab_account":"<acct>","inception":"<trade_start>"}],
     "q_start":"<window_start>","q_end":"<window_end>","pull_date":"<today>"}' out.json`
     -> lands bronze; WS-2/WS-3 (DS) roll it to silver `fact_taxsma_report` + gold `dim_taxsma_report`.
     (This path is fully live once the WS-R3 producer deploy lands; today the producer is manual-invoke.)
   - **Alternative (Schwab-derived, agent-run now):** `/tax-pt2 {acct}` reads the 0833 monolith and
     emits the lot-level cost-basis immediately -- use this for instant data before the BD chain runs.

4. **Report.** Confirm the enrollment + the data landed (registry `list_active`, and the bronze/gold
   keys or the pt2 artifact). Note the account now recurs in the daily ETL.

## Phases

- **Phase A (NOW):** a workspace agent runs this skill (resolver + registry + AWS invoke ride the
  agent's AWS access). Operator: Andrew or any workspace agent on his word.
- **Phase B (pending WS-R5 gateway IAM -- Andrew+CTO gate):** Alyssa runs `/tax-newacc {acct}` from
  her laptop via the MCP gateway. Her scoped role gains `lambda:InvokeFunction` on ONLY the tax-pt2
  producer ARN + `s3:GetObject`/`PutObject` on ONLY the roster key (D4) -- built + Rule-22a-verified +
  applied by CTO before this path opens. Until then, onboarding is workspace-agent-run.

## Notes / gates

- **Bump 0035940058 + Macy 0091939812** are seeded `pending_resolution` (not in the xref) -- the same
  tier-2/tier-3 egress gate; activating them is the concrete first use of this onboarding path once
  Andrew rules the egress question.
- The registry is the account-membership source of truth. `/tax-pt3`'s divest input stays Yang's
  `Tax SMA Accounts.xlsx` (a per-run business input, separate from account membership).
