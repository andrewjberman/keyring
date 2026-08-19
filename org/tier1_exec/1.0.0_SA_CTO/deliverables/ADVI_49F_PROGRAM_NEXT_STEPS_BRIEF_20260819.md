# ADVI 49F PROGRAM -- NEXT-STEPS BRIEF (CTO, 2026-08-19 ~1355Z; for COO decomposition per Andrew-direct ~13:16Z)

**State in one line:** P1 CLOSED; the gold-home re-point CLOSED end-to-end (home =
`opal-data-49financial/gold/advi/`, IAM complete, old prefix deleted on Andrew's word);
P2->P4 is BUILT-AND-WAITING on one external event -- the vendor's fam feed resumption
("R") -- with every gate ordered and instrumented; P5 preconditions accrue behind the flip.
Authority chain: push plan @a2f27c8d0a + supersession @f481ab00ac + re-date @f79760179a +
today's ledgers (all CTO-validated). Fleet: 10/10 logged; wind-down spares CTO/COO/CRO~A.

## A. THE R-ANCHORED CRITICAL PATH (order fixed, calendar floats on R = fam resumption day)

| # | act | owner-class | trigger | close criterion |
|---|---|---|---|---|
| A1 | R-detection: fam bronze/silver present past 08-10 | the daily 02:30Z pull + a READER (see D1) | vendor delivers | fam partition > 08-10 exists, stated w/ denominator |
| A2 | P2D-3 QA + TWR sequential catch-up on the NEW root | DS~A-class respawn | A1 | measured chain duration in writing (pins the cron value) |
| A3 | P2-FLOOR TF apply (dedicated advi_49f_floor_dlq; 12:45Z candidate cron re-derived from A2; silver-completeness event accelerator) | AE-class respawn; CTO gates | A2 | plan expected-rows-bounded, 0-diff, tag; then THREE unattended daily green writes (the P2 close bar) |
| A4 | P3-CLOSE attestation (dims from the scheduled chain at the new root; incl. the a07/a06 pair = the 2 non-ready twins' inputs) | DS~A-class; CTO attests | A3 first green | live listing: every table's newest partition = T-1 by the scheduled stage |
| A5 | P4-EMIT: publisher writes platinum/advi/49financial (13 ready twins + 2 on A4; P4-PUBIAM grant + publisher schedule) | DS~B-class + AE-class; CTO gates IAM | A4 (13 can emit on grant alone) | 15/15 twins live, census-frozen shape, instance per key |
| A6 | P4-PINS + per-key oracle table exercised on the one day both serves exist | CVO + CTO/COO halves | A5, = R+2 | pin file per key (vs the 04:00Z T-1 serve per @19854bcba3); oracle FAIL-pre/PASS-post per key |
| A7 | P4-FLIP: portal firm-config repoint -> DT PROD promote (pending @744841dba1) | DE-class + DT-class respawns | A6, = R+3 | rendered + behavioral acceptance per key (AC-P3 pattern) |
| A8 | P5 opens: legacy bd teardown under the ratified methodology, census-informed | AE-class; CTO gates each | A7 + agreed serve window | per-path applied-plane absence w/ positive control |

## B. DATED ITEMS THAT DO NOT FLOAT (independent of R)

| # | item | owner-class | date/trigger | note |
|---|---|---|---|---|
| B1 | 13:30Z scheduled run = PB-1/PB-2 PROOF READ (T-B executing-plane fix applied @1349Z ledger) | needs a NAMED READER (D1) | 2026-08-20 13:30Z | on PASS -> B2 discharges |
| B2 | held `json/mdpf/49financial/aggregate-aua-timeseries.json` DELETE | AE-class | B1 PASS only | one object; both NEVER#3 halves signed; needs only the proof citation |
| B3 | INF-ONEWRITER fix (likely mechanism of the 08-12 INF fee-split defect) | DS-base-class | 08-20 | writer-log read first, then consumer .get->refusal leg |
| B4 | SILVER-DTYPE | DS-base-class | 08-21 | behind B3 at the same seat-class |
| B5 | BDMERGE-CONVERGE | DS~A-class | 08-21 | as ruled R-2 |
| B6 | 0.8.0 gates: REG-SCAN-ATOMCHECK REG (08-19 residue) + J3 comp-atomcheck (08-20, REQUIRED before INF binds at P2-open) | 0.8.0-class respawn | 08-19/20 | CTO arch-gates; J1/J2 already done + validated |
| B7 | MSTR deploy-ledger dispositions + HELD-STATE schema TO + CBD-PAIR TF lint (Andrew-approved ~1537Z 08-18) | MSTR-successor/0.8.0 + AE-class | 08-20 | carried from the plan §5 |

## C. RESIDUALS FOR THE RECORD (not acts; carry into whatever survives)

- R-4c urgency: the bundled-vs-canonical two-planes class has TWO measured members at
  mdpf-gold-lambda alone; the deploy-census fork-or-drift DECLARATION per bundling Lambda
  is the remedy candidate (CTO to route post-R; BUILD_MANIFEST.json vintage stamps, landed
  today, are the pattern to generalize).
- The "who may invoke this lambda" comp-tool gap (AE log) -- toolscape backlog, 0.8.0 lane.
- P4E-5 disclosure ledger + per-key oracle rows carry the 4b twin determination verbatim;
  the frozen list @5f1076e9c1 + addendum @6211c4f0f4 are the key universe. Do not re-derive.
- Andrew's two accelerators (enumerate word; Schwab/vendor human contact) ride MSTR's card;
  either shortens R but neither is a precondition.

## D. DECOMPOSITION ASKS (COO -- your discretion per Andrew's word)

- D1 **The R-watch + proof-READ seat**: ONE respawn (or an event-respawn recipe) that (a)
  reads tomorrow's 13:30Z run for B1, (b) watches fam presence daily for A1. Cheapest
  continuous obligation in the program; everything else can event-respawn behind it.
- D2 Cut the respawn roster against section A's owner-classes ON R-DETECTION, not before
  (your stated read -- concur: pre-R respawns burn context against a vendor clock).
- D3 The B3/B4/B6/B7 dated items need seats on their DATES regardless of R.
- D4 INF binds as instance 2 at P2-open (transposition map ruled: daily-TWR tier YES,
  unified+labeled floor carry), COT third at its cutover -- sequence AFTER 49F A3 proves
  the template's first unattended green.

-- 1.0.0_SA_CTO. Every claim above traces to a validated ledger, ruling record, or
   commit named in the master log (same folder, 2026-08-19).
