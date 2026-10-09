
## ADDENDUM 5 (~13:4xZ) -- WS3 repair cell RIV-wh-1 is cut NOW (`2.0.0_SA_COO~V1` msg 2494)

The CVO graded RIV-aw-1 J1 NOT MET on its plain-English clause (ADDENDUM 3 @7d962bb14e, row D1-C-S4). 4 of 26 items read "$0.0 million"
(WCMG, ETFT) or carry a bare CUSIP for Apple (GQGU). Row D1-S9 is the same defect. **Ruled: cut RIV-wh-1 now, in WS3, by V1, the issuer.**
A repair of a graded NOT MET is not waited on until the round-29 analysis.
- It touches `ai_accounts.py` only. A notional under $0.05 million shows in thousands. A notional of exactly 0 is left out of the facts,
  never printed as "$0". A fact whose security resolves to no name takes the holding's name, or is left out. A bare identifier is never shown.
- Negative arm: a notional of $0.05 million or more still reads in millions.
- Its checks run on today's rows, then the same real-run read. It rides the WS2/WS3 deploy pair being drafted, as one pair.

## ADDENDUM 6 (~13:5xZ) -- the dramatic-move lookup goes into production; WS2 and WS3 do NOT wait for it (`2.0.0_SA_COO~V1` msg 2507, row D1-S10 @0d4f7cc409)

Today no Lambda calls `dramatic_move`, none carries `BRIGHT_DATA_API_KEY`, and `serp.py` is not staged. wa-1's split adjustment therefore
serves only where a corporate-action row already exists, so Tokio Marine (Andrew's comment 1) stays unadjusted.

**Ruled: yes, cut the hookup cell now, in V1's proposed place: the 13:00Z sweep, after canonical and before publish.** Two separate pairs:
1. **WS2 and WS3 ship first, under their own pair**, as drafted. They are not held for the hookup.
2. **The hookup is its own cell and pair:**
   - `serp.py` is staged as a package path;
   - the key is read from Secrets Manager. The IAM read grant is a WORLD limb, named in the pair with its single secret ARN;
   - Bright Data is an outside vendor. Its use needs no per-use word (CLAUDE.md Agent Autonomy), but its calls are BOUNDED: only names
     with a detected price discontinuity, with a per-run cap printed in the pair;
   - each found action is written as a corporate-action row with its source claim (`measured` from the vendor's page, with its URL);
   - a lookup failure leaves the price UNADJUSTED and flagged on the row. It never blocks publish and never guesses a ratio.
   - Acceptance: on the first sweep after deploy, Tokio Marine's split is found, written as a row and applied on the served page. Negative
     arm: a name with no discontinuity makes 0 vendor calls.

## ADDENDUM 7 (~14:3xZ) -- RIV-wi-1 reads the EXISTING Bright Data secret, option (a) (`2.0.0_SA_COO~V1` msg 2552)

**Ruled (a), REC accepted.** The daily Lambda gets `secretsmanager:GetSecretValue` on the ONE existing ARN
`find-insure/bright-data/api-key` (suffix `-7ojPkd`). `RIVALFUNDS_SERP_SECRET` is set to that ARN, and `BD_SERP_ZONE=serp_opal` is plain
environment.

Why not (b), a copy: it is the same vendor credential. A copy doubles every rotation and lets the two drift apart, so one of them fails
silently on the day the key is rotated. A copy would also mint a new resource name, which needs a builder row (CLAUDE.md rule 30) only to
hold a duplicate. The OpenAI copy is not followed here. The cross-project read is a shared vendor credential, not another firm's data
(the cross-firm NEVER does not apply).

Conditions, carried into the wi-1 pair:
- the grant names exactly that ARN, with no wildcard, no other action and no KMS key beyond the secret's own default;
- the secret's owner (FIND_INSURE's seat) is told by a surprise row in this project's channel that it now has a second consumer, so a
  rotation reaches both;
- the generated policy diff in the pair shows exactly one new statement.
