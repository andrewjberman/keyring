# Holdings implementation and source handoff

Owner: 2.0.0_SA_COO~M. Written 2026-09-23 16:48 Eastern.
**archetype:** IMPLEMENT

Andrew-direct, current Codex chat, verbatim:
> Proceed to next steps.

This continues the existing Holdings closer mandate and requested 600-second drive.

## Implemented

- Backend b411e6f31e: actual Inflection native positions, independent account totals,
  signed/zero security rows, canonical Client display category, separate clocks.
  Dispatch now requires actual positions; portfolio totals cannot stand in for them.
  Exact existing producer helper is imported unchanged, with partition-shape guard,
  cutoff selection and version-bound input reads. No producer client/write is used.
  CTO3de4395fb5 is the locator ruling; ordinary commit gate passed, no override.
- Backend fec4f688e1: Cottonwood known custody now uses the same canonical Client
  category rather than a public Unresolved bucket. Security membership, fee taking
  and advisory classification remain unasserted. Targets remain private evidence.
- Latest focused check: 18 passed,71 unrelated deselected, including all13 INF
  adapter checks and5 Cottonwood custody/Client/zero-total/refusal cases.
- UI e5604c03 and shared projection patch206b5329de remain P integration inputs.
  P must package inf_positions.py and the COMPLETE unchanged producer helper
  data/inf/scripts/silver/_orion_api_silver_lib.py in the runner repository layout.
  Helper blob6ad80c3b007a3119ac536b94c05b99bffdbba1c9; no extracted formatter.

## Real data findings and next decisions

49F: Holdings_49F_SOURCE_CHECK is named HOLDINGS_49F_SOURCE_CHECK_20260923.json.
Exact Sept22 Schwab08335338 positions106499/6325accounts; roster and balance7522.
Sept23 SmartX joins5912custodyaccounts, leaving1610custodyaccounts without mapping.
Keep all7522 in the base; SmartX is the sole model authority, not the denominator.
There are14 duplicate position-grain keys,2 blank-side rows and26 account position
sum exceptions. No source currency column exists in these three files. No formula
was certified by numerical prevalence; CRO has the bounded cash/currency request.

INF: CRO8246fa72d2 corrected the earlier missing-currency research. Reporting/Scope
explicitly labels two retained accounts USD. I compared their six account/date
activities with version-readback original positions for June10,June18,September9.
Native account IDs and actual asOfDate match in all six, with no missing values;
NONE matches the reported amount within one cent. The exact receipts, hashes,
differences and counts are in INF_CURRENCY_BRIDGE_20260923.json. No tenant-wide or
current-date USD inference is made. CRO owns request/activity-semantic clarification;
CTO204629 bounds any eventual propagation to the exact proven scope.

COT: P214ddd6b3f reports Andrew-directed Anna positive control passed BOTH live
period/series dual-ID checks,15points and final parity. The prior empty response
was account-specific, not proof that is_managed=false blocks access. This is P's
performance proof, not M's Holdings proof. Currency is still not established;
CRO8246 found no retained/documented currency source and routed the firm-setting
or attestation decision to CTO. The5694 blank-value rows remain unsupported, not0.

All source candidates are LOCAL. No publish, deploy, vendor call or live Holdings
acceptance occurred in this turn. First accepted real account publication and
actual authenticated rendered Holdings remain open for all3firms.

## Andrew Tax SMA instruction received 16:50 Eastern

CRO~M message99757 relays Andrew-direct from its terminal, recorded verbatim at
ANDREW_DIRECT_20260923_204xZ_IRPT_HOLDINGS_49F_TAX_SMA_FROM_WORKBOOK.md@d70decd6b2.
The choice was whether to leave49F Tax in Client or show it under SMAs > ALT
Strategies > Tax from the SharePoint workbook. His answer, verbatim:
> B

His follow-up, verbatim:
> Also there is apparently 20m in assets for Tax, so we need to understand what we're missing and where if youre saying 6m. I would check the Yang Tax SMA spreadsheet sharepoint and corroborate real quick.

Consumed current MDPF_TAXSMA_DATA_CONTRACT v0.5.0 membership, category and canonical
value mapping. Traded=YES is current business membership; Ready is not a gate.
Historical membership cannot be backdated from today's workbook or modified date.
Canonical value is net_mv_plus_cash, not workbook AUM. CRO~M reports9traded,
7in0833custody and2missing from both landed masters; none of14numbered workbook
accounts in SmartX. Those are attributed CRO measurements, not M's reproduction.
Requested its exact protected retained snapshot/ETag/hash and canonical reader pin
for direct reuse. CTO owns amendment of a62f Tax line and the dated overlap semantics.
For actual Holdings, do not add Tax value on top of custody which already contains
those accounts; pending mapping must preserve one economic position once.
