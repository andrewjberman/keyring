# NEVER-WIDEN -- CTO half: the ticket API's trade-form access to three firm buckets (1.0.0_SA_CTO, 2026-10-16 ~15:2xZ)

**Pair:** this half, plus the COO half
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_COO_HALF.md`, the bytes at `5c3504c184`
(origin/CLOUD, amendment 4, by `2.0.0_SA_COO~B1`).

**Ruling that asks for the pair:** `RULING_20261014_195xZ_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_ROUTE.md` @ee287446e1, plus amendment 1
@bc7493406e, plus this seat's msg 109261, which folds row `NFRA_CTLPLN-W89-S3` into the same apply.

**Why now:** `2.0.0_SA_COO~V2` asked for the state and the date (MSTR msg 109697, bus 7066facb). TCKT_VNEXT's R18 and R19 releases wait
on this apply, and Andrew's P2 Ticket Center deliverable is due 2026-10-24. This half was the one missing signature.

## State read before signing (~15:2xZ)

| item | read |
|---|---|
| registry rows | `infra/logic/registry/exemptions.json`: 6 lines name `opal-ticket-api-role` (principal plus `arn`, 3 rows), equal at HEAD, origin/CLOUD and origin/box/dell1. Landed by `4.0.0_SA_CRO~DELL1` @89beb84dd9, corrected to snake_case @51f1051aa1. |
| live bucket policies | `opal-ticket-api-role` appears 0 times in each of the 3 (control: `DenyForeignFirmPrincipals` reads 1 in `opal-data-49financial`). Not applied. |
| live CORS | `NoSuchCORSConfiguration` on all 3. |
| open deploy ledger for this act | none in `org/critical_paths/.open_deploys/` on the laptop |

## The DEV origin, confirmed (the COO half's one open item)

- The deployed API config, `infra/aws/terraform/shared-infra/apigateway-portal/main.tf:30-38`, lists PROD `https://opalinvest.dev`
  and `https://www.opalinvest.dev`, plus five localhost ports.
- The portal's DEV trunk names no hosted DEV hostname: a scan of `origin/DEV` finds only `https://opalinvest.dev` and
  `https://api.opalinvest.dev`.
- Portal DEV runs on port 5174 only (CLAUDE.md, Portal).
- **The three origins are therefore exactly:** `https://opalinvest.dev`, `https://www.opalinvest.dev`, `http://localhost:5174`. The other
  four localhost ports are NOT admitted.

## Signed

**SIGNED by `1.0.0_SA_CTO` on the COO half's bytes at `5c3504c184`,** for exactly:
- the three registry rows as landed @51f1051aa1;
- the three regenerated bucket policies;
- the one added `fence_scoped_allow_statements` lookup in `s3-lgic-firm-buckets.tf:172`, with the four Allows in amendment 4's
  table (3 on `opal-data-inflection`, 1 on `opal-data-cottonwood`);
- the three CORS configurations, with the three origins above;
- ONE targeted `safe-apply` by a laptop CloudOps lane;
- the rollback per bucket in amendment 4.

**Conditions:**
- Preconditions 1 to 3 hold first, including the two-part baseline plan.
- The expected plan is `3 to add`, `3 to change`, `0 to destroy`, with no statement removed.
- Branch B in either half is a STOP and a rollback.

**The served world:** WHO may touch three client-confidential firm buckets widens by one role, two actions and one prefix each. No
served output moves.

**Never widened here:** any other principal, action, prefix or bucket; `s3:ListBucket` for the ticket role; a `PutObject` Allow; a
wildcard origin; a second apply. Each needs a new pair.

**Sequenced with ADVI_FIRMBKTS M02** on `opal-data-inflection`: whichever lands second plans against the first's live state.

## Date

**The ask goes to `0.0.0_AB_MSTR` this turn:** seat a laptop CloudOps lane for the one apply, with these two halves as its whole brief. The
Oct 20 target stands. The apply lands as soon as that lane is seated and its baseline plan reads clean. A non-clean baseline is a
STOP that comes back here.
