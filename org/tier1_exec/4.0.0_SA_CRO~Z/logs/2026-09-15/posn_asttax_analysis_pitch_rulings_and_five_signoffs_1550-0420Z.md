# 4.0.0_SA_CRO~Z -- POSN_ASTTAX: the state analysis, the satellite-source pitch, Andrew's fourteen rulings at this terminal, five brief-half sign-offs (v0.7-v0.11), and one harvest hazard recorded -- 2026-09-14 15:50Z to 2026-09-15 04:20Z

**archetype:** MIXED
**secondary_archetypes:** MEASURE, COORDINATE, VALIDATE, SCRIBE

## Window
Since `org/tier1_exec/4.0.0_SA_CRO/logs/2026-09-14/successor_log_identity_layer_and_card4_0000-1520Z.md`
@80fdcc3843 (pre-reboot). Post-reboot launch 15:50:53Z on Andrew's word ("Bring CTO~Z and CRO~Z online").
Eighteen commits by this seat, all LOCAL (origin/SITEZ `6f09a06dc9` by ls-remote at 04:20Z; site-Z pushes held
on Andrew's post-reboot advisory, `0.0.0_AB_MSTR~Z` carries). HEAD at writing `6aaf98db39`.

## Andrew-direct at THIS terminal (all recorded verbatim + broadcast same turn)
| clock | word (anchor) | record | effect |
|---|---|---|---|
| ~16:00Z | "analysis on ASTTAX ... brief on this to deliver to CTO~Z" | `deliverables/ANDREW_DIRECT_20260914_1600Z_*` @d5f883ce90 | the state analysis (delivered in-chat) |
| ~16:34Z | "GLD and VIX ... in the Satellite Portfolio as a whole, outside of the Model Portfolio(s) ... narrowing solely around the Positioning page" | `..._1634Z_*` @ebd1cca439 | the measurement that corrected the premise (below) + brief v0.1 |
| ~17:2xZ | six cards ruled: "they should be summed ... total GLD listed as Commodity Asset, Metals Sub-Asset ... Total VXX ... Structured Asset, Hedge Sub-Asset. Call 2 Yes. Call 3, mint some yellow color, yes. Call 4 Yes. Call 5 Yes. Call 6, definitely B ... an additional lambda to do weighted characteristics aggregates" | `..._172xZ_POSN_ASTTAX_SIX_CARDS_RULED.md` @727b82e8d2 (card-4 correction @8ba8fffd16) | brief v0.3; design R1-R4 as ruled |
| ~17:3xZ | "All recs approved. ... attribution ... staying to just Equities and Fixed Income ... we do not touch 'Attribution'" (eight breakdown items A-H) | `..._173xZ_..._ALL_RECS_APPROVED_ATTRIBUTION_UNTOUCHED.md` @e406e99122 | F4 OUT (eight cells), worker gate released, VNQ = Real Estate, one-off BBG pull (b) |

Later Andrew words relayed from the `1.0.0_SA_CTO~Z` / `~W` terminals (recorded there, acked here): heads-down no-MCP
rule (~19:4xZ); Structured = pink base (~19:5xZ); JEPI -> Structured (~20:0xZ) / Options Income (~20:2xZ); presence
rule + Satellites defects (~02:1xZ); fix Satellites tonight (~02:3xZ); "vendor change approved go get it" (~03:0xZ);
~W = AMGT only, ~Z = POSN (~03:5xZ); floats + ETFClassifier identity (~04:0xZ).

## THE FINDING THAT CHANGED THE DESIGN (measured, two instruments)
Raw rebalancer partition `s3://opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_model_detail/2026-09-14/`
(81 files): every `Opal Satellite N` has **0 root securities**; 13 of 13 sleeve ids equal the standalone BD model
ids. **GLD / VXX / CASH live inside Black Diamond's copies of the five models** (ST GLD 8.34%; INT GLD 3.99% VXX 1.40%;
LT GLD 2.11% VXX 1.87%; ULT VXX 1.87%; CASH 0.65-1.05% everywhere); Yang's served books
(`positioning_data.json` data_as_of 2026-09-11) carry no GLD, VXX only LT 1.50 / ULT 2.00, no CASH, and ICSH in 5 of 5
that BD holds in 0 of 5. The portal blends YANG's books to build satellites, so today's Satellites toggle is wrong on
gold for 7 of 9 and on VXX for 6 of 9 (both directions). Andrew's "outside the models" = outside YANG's version.
Row `POSN_ASTTAX-Z-S65` (ARMED, disarm owner `1.0.0_SA_CTO~Z`; disarm condition met by PRD v0.7 C-SATELLITE-SOURCE).

## Deliverables
- Brief `org/tier1_exec/4.0.0_SA_CRO~Z/briefs/POSN_ASTTAX_COMPLETION_BRIEF_20260914_Z.md` v0.1 @ee4b7e5539 -> v0.2
  @f846dd72da (file-location correction + four flags on the CTO breakdown, all four ACCEPTED) -> v0.3 @727b82e8d2
  (rulings folded; card-4 lane correction @8ba8fffd16). The CTO's breakdown (v0.5 @0949f2d53d) became the cell-level
  authority; round 5 = 9 cells, round 6 = B6/F4/F5.
- Five L4-R brief-half reviews, each SIGN, each with last-touch == pin and the bump scope diffed:
  v0.7 @3c42ed05d0 (review 87d06c1080, stamp f577a69a41); v0.8 @709d7b4221 (bfc0a4ff29 / 891ee40cae);
  v0.9 @8eabf98d81 (6021b8c00d / 8bd0f94608); v0.10 @59113e257a (7c39bfc5cb / c6f4706323; BRIEF COVERAGE
  denominator 6 of 6 verified at the brief's pin 03f1d00ec4; five cited commits resolve; bytes printed at :731/:855/:1851);
  v0.11 @ab2ee8052a (db381a909e / 2796d32c8b; identity basis re-measured: 25 satellite tickers, 25 of 25 rows with
  real names, management_style passive 16 / active 8 / unknown 1). Non-blocking notes returned by pinned line each time
  (unpinned citations x3; an ENDPOINT provenance line the CVO later refused; GLD returns computable from history --
  closed by Andrew's ~03:0xZ vendor word).
- Harvest estate (outside POSN): `2.0.0_SA_COO~W` found this seat's 2026-09-11 migration step 2 (`s3.tf` bucket rename)
  APPLIED but never COMMITTED -- HEAD names the deleted `opal-data-research`, a plan would DESTROY-AND-CREATE the live
  bucket. Re-verified here (diff = 2 lines; head-bucket harvest EXISTS / research ABSENT / bogus ABSENT). The `.tf` commit
  was REFUSED by the lane gate (`CLOUD_OPS_OR_ETL`, AE-only; audit log :5626) -- correct: this seat's five 09-11 commits
  there were MERGE commits riding the drain exemption. Ledger addendum @160ca062c5 records it with a standing DO-NOT-DISCARD;
  the edit stays UNSTAGED as the guard; convergence = an AE seat or the round-10 producer cell + drain.

## MCP traffic
~45 in (CTO~Z ~28 incl. five L4-R deliveries, MSTR~Z ~7, BBG 1, COO~W 1, CTO~W 1, notifier), all READ-acked; 14 out:
four multi-recipient Andrew-direct broadcasts (22822/22826/22842-22845/22861-22864), brief v0.2/v0.3 + hash notes to the
CTO, card-4 relay to `0.0.3_BG_BBGTerminal` (returned a RAVC blocker: no write fence -- this seat's lane field was wrong),
the card-4 re-route (22850/22851), the harvest RAVC close (22945/22946). Heads-down rule applied from ~19:4xZ: silent
read-receipts only; stamps as carriers.

## Compiler Tools
| tool | use | result |
|---|---|---|
| `comp-which` (A.3 exercise) | PATH check, 104 of 104 forwarders | PASS |
| `to-check.py --all --assignee` | 0 open TOs for ~Z and base (scanned 2618) | PASS |
| `sequence-check.py --project POSN_ASTTAX` | not sequenced (TRACK) | PASS |
| `audit-archive-invoker.py` | 14 findings, all the known cross-device baseline class | WARN (expected) |
| `comp-iam service cot-satellites-registry-producer` | "No AWS operations detected" (helper-built clients) -- fell back to reading the `.tf` | PARTIAL |
| `prd-signoff.py status/sign` x5 | ADMITTED after each stamp | PASS |
| `safe-commit.sh` x18 | 1 lane refusal (correct), 1 transient index-race refusal (retry landed), 1 heredoc quoting break (moved to a script file) | PASS/WARN |
| `comp-pulse` risk-reflex (per commit) | danger map STALE (84-91 h) -> NOT-DECIDABLE every time | GAP |
| boto3 DDB scans x3; `aws s3api` head-bucket / head-object / cp; `git diff`/`ls-tree`/`cat-file` | the live-plane and vintage reads behind every claim above | PASS |
What worked: the PRD diff at the delivered pin + bytes-at-cited-lines as the review method; a per-satellite portal-vs-BD
table as the discriminator. What failed: the comp-tool rail aborted a compound call containing one `grep` (the `git diff`
half never ran) and gated `aws s3 ls` -- rail-checked markers used; an inline python heredoc with a backtick fence line
broke bash quoting. Gap: the risk-reflex danger map has been stale all session, so NEVER-class pre-commit checks were
not decidable on any of 18 commits.

## Blockers
None at this seat. NOT blocked: the harvest `.tf` commit is routed (AE lane / drain), the edit is safe in place.

## Current state (zero-context reader)
PRD `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md` v0.11 @ab2ee8052a ADMITTED (ratified-text `3.0.0_SA_CVO~Z`,
brief `4.0.0_SA_CRO~Z`, both current). Round 6 (B6 identity + measures block and schedule; F4 adapter attach; F5 presence
filter / two-decimal label / footer / copy) is `2.0.0_SA_COO~Z`'s, with three issuer amendments pending on v0.11. The retag
has LANDED in `etf-classifications` (GLD commodities/Metals, VXX structured/Hedge, read 04:1xZ); served
`platinum/satellites/holdings.json` relabelled 03:02Z (Branch A, rollback VersionIds recorded). GLD/VXX Bloomberg history
backfilled (ledger closed @d3d2ffc4a5). Portal freeze stands: commit yes, promote no. `~W` lanes are AMGT only by Andrew's
word. Harvest: `infra/aws/terraform/harvest/s3.tf` two-line edit UNSTAGED in the shared tree = the guard; DO NOT DISCARD
(ledger `20260911T1915Z_*` addendum @160ca062c5). Watcher: persistent Monitor re-armed every 30 min (last `bmao49vjo`
lineage); registration LIVE PID 27812.

## Next steps
- [4.0.0_SA_CRO~Z] sign the next brief-half bump when delivered (v0.12 if the round-6 analysis adds constraints); disarm
  nothing -- `Z-S65`'s disarm is the CTO's citing row.
- [1.0.0_SA_CTO~Z] carry the two unpinned citations (`PositioningSummary.tsx:1011` without a ref; the ~04:0xZ word without a
  record hash) on the next brief-half touch; the `route_half` seated-lane fix is at Andrew as an open call.
- [2.0.0_SA_COO~W] the round-10 producer cell carries `harvest/s3.tf` with the "0 to destroy" guard; this seat disarms the
  AMGT row when HEAD reads `opal-data-harvest`.
- [0.0.0_AB_MSTR~Z] 18 LOCAL commits by this seat ride the next push on Andrew's word.
