# IRPT_BCKEND round 19 -- the CTO's L10 analysis (workstreams ~P, ~M, ~Y)

**Author:** 1.0.0_SA_CTO, 2026-09-29 ~04:1xZ. **Input:** the CVO's slug
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R19_REVIEW_20260929.md` @`0a96d8a72c` (msg 102568; 64 rows
dispositioned; ADJUDICATION_v14, REMEDIATION_v10). PRD at the round's close: v0.19 @`82e1700237` (ADMITTED).
Round 20 was already cut from the three frozen next-lists on this seat's rulings (~M 102515, ~P 102519/102520); this
analysis reaches those orders as AMENDMENTS, which each issuer makes without a further ruling.

## 1. The slug's P0 is stale -- S176 is REMEDIATED on the page

The slug measured STATUS~P.md:34 at 01:xxZ, before its update. The retained-reopen guard is served: adapter
`qfxZ0DzB` (CTO half `af2388e240`, CRO half `ce4b4cfecf`), and the CRO's D1 AFTER-read, walk `20260929T001245Z`
(message 102506), reads the NEW-01 account's YTD and 1Y as a named refusal, the control 5.93% unchanged; both
adapter ledgers closed `7a7e7c13b8`. **S176 disposition: REMEDIATED.** Carried, not closed: S184's two near-miss
accounts (-0.9996, -0.99996), which retire with the holdings-basis gold (PRD v0.19 ruling 12).

## 2. The CVO's unasked question -- adopted as a written L6 rule for this project, not a new gate

"Whether a `complete` order means its outcome holds on the page." Answer, binding every IRPT_BCKEND issuer from
round 20: **an order that changes a served figure names EVERY reader of that figure in its criteria** (compute,
retained reopen, export, cache), each with its own check, and its proof reads the served page, not the path it
edited. STATUS~P.md:70 already practises it. This is issuer discipline, not a gate limb: CLAUDE.md section 2 bars
this seat from adding an approval gate on its own word. If Andrew wants it mechanical, it is a proposal for him.

## 3. This seat's eight remediation rows

| row | ruling | owner of the act |
|---|---|---|
| S173 (P1) | OPEN. ONE act with halves after the POSN owner's `etf-classifications` fill on site Z (coverage @9ab15461ca: COT 39.7%, BD 68.1%). The act includes the COT host role's read on the canonical table (today it has no DynamoDB read at all, so every COT run falls back to empty maps). Holdings-basis performance does not depend on it. | 1.0.0_SA_CTO, gated on site Z |
| S165 / S166 (P2) | The cot login box runs a script with no build input in its tree. First commit the RUNNING bytes (28dd27a0, 35,049 B) under `infra/aws/ec2/bd-cot-auto-login/` as the build input, with no behaviour change; then port the retry-capable script with `BD_MAX_LOGIN_ATTEMPTS` / `BD_LOGIN_BACKOFF_MS` under a deploy ledger, the diff read by this seat before it lands. | 2.0.0_SA_COO~M issues both as task orders to 0.6.2_AE_PartnerETL~S |
| S132 (P2) | Least privilege: the Lambda@Edge role's `secretsmanager:GetSecretValue` narrows from `opal/auth/*` to the two PUBLIC keys `auth-validator-edge` reads. It touches the shared edge validator: never-widen halves, a LIVE before/after of the human-token path. | 2.0.0_SA_COO~P (shared auth, writer table) |
| S191 | CLOSED -- ruled by ~P inside the ~E decomposition (row S192, E1-AC1 amended @5e273c614f). | -- |
| S187 | Worker slot ids across workstreams: each issuer takes `n = 1 + max(n)` over every `0.9.0_WK_IRPT_BCKEND~n` author line at HEAD, printed in its issuance commit. | every IRPT_BCKEND issuer |
| W42-S4 | GATE fix, this seat: `check_complete_flip()` reads the order's own `<proof_of_spec>` tag when present, the stem search otherwise (landing now). | 1.0.0_SA_CTO |
| W42-S3 | Hygiene: `lib.silver_ids` sys.path collision in `test_holdings_inf.py` / `test_inf_positions.py` (14 of 284); fixed at ~M's next drain. | 2.0.0_SA_COO~M |

## 4. Outcome read (PRD v0.19)

- **FWD-3 (holdings basis):** 49F thread hop 1 built (account 0010498003, 184 of 184 YTD days, recompute exact); all
  49F accounts built; the adapter switch is merged and awaits its halves after window 21. NOT YET REALIZED.
- **FWD-5 (Holdings):** R4 ENABLE signed by both halves; the first scheduled fire (Tue 10:15 ET) is the proof.
- **FWD-4 (Analysis):** resident st3 served; window 21 open (both halves) carries the first Comparison and the first
  certified INF and 49F reports.
- **FWD-12 / FWD-13:** the daily holdings-performance function is merged (er-203); comparison points not started.

## 5. The closer write lanes (return brief C6) -- deferred once more, with its reason

Round 20 still carries seat-authored ledgered acts on closer-lane paths (~M's R4 flip, ~P's adapter switch). The
lanes retire at round 20's L10, or narrow to the paths a named direct act still needs.

## 6. Enrichment for the next cuts (amend round 20 or cut round 21)

1. ~P: the adapter switch's halves after window 21; then Inflection and Cottonwood on the holdings gold, in that order
   (ruling 11); S132.
2. ~M: UIC-16 49F labels from the Schwab code table (Andrew's source, CTO msg to ~M 04:05Z); the S165/S166 orders;
   W42-S3 at the drain.
3. ~Y: window 21's traces; the branded Analysis export (item 7) when K8 grades.
4. ~E (via ~P): FWD-13 comparison points for 49F (4 landed Black Diamond pulls) and INF (weekly Orion factors).
