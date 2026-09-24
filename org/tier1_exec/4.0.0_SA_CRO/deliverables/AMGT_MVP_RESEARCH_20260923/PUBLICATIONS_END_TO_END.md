# Publications and chatter: current path and completion brief

**Proposed closer H.** Own the five publication channels through the timeline and ranked Chatter result. Authority: `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` v0.2, FWD-1..9; paired RESAPP format-retirement contract. All 18 issued orders are marked complete. The current project record explicitly says FWD-1 is not realized and identifies remaining cross-project/external dependencies.

## End-to-end assessment

| Connector | Measured or recorded present state | Required result |
|---|---|---|
| Publisher discovery -> original article/listing bytes | Article bronze exists for SA 29, Bloomberg.com 19, Barron's 15, WSJ 26 and FT 14 physical objects. Only WSJ has a `news_listing` family in the complete current census (two objects). | Received response and discovery provenance retained per actual fetch. Historical normalized records cannot be relabeled as original response bytes. |
| Access -> successful intended-security coverage | Latest closure records distinguish Bloomberg challenge, FT search 403, Barron's rejection after successful reauthentication. This research did not re-run those endpoints. | Separate per-publisher remedy and controlled validation. A login operation cannot be assumed to repair all three. FWD-1 needs the intended security and publisher, not a bucket-wide count. |
| Bronze -> lossless typed silver | Silver article objects: SA 12, Bloomberg.com 19, Barron's 15, WSJ 26, FT 14. Counts are files, not row counts or fidelity proof. Source contains bronze-to-silver replay and receipt handling. | Reproduce rows solely from bronze, retain every vendor field and all three clocks, verify dedupe/replay including failed fetches. Preserve unknown received-form history honestly. |
| Silver -> absolute mention/day/event gold | Two mention tables, three daily tables, two event tables exist. Latest daily table contains six securities across 266 days, 1,596 rows. | Repeatable article/security grades and event lineage; dense days with explicit collection status. Never present uncollected days as proven zero coverage. |
| Gold -> serving reader / ranking writer | Local `pool_reader.gold_window_read` and `chatter_axis.gold_daily_mention_scores` exist; local CLI default remains `legacy`. Both inspected deployed packages lack the new gold implementation. | Switch actual runtime caller/configuration and package, not just the CLI option; grade-weighted counts must reach the current generation selected by the page. |
| Role permissions -> gold objects | Inspected API and chatter-writer inline grants do not include `amgt/harvest/gold/`; attached policies are basic logging or none. | Narrow declared read grant and coordinated reader/writer retirement, following never-widen constraints. Do not add bucket-wide access. Full effective access was not simulated; absence is stated at the role-policy layer inspected. |
| Day/event gold -> timeline -> drilldown | Design spec and amendment exist; current project record holds build on approval of the amended spec. No timeline-specific AMGT route was found among the 16 deployed routes. | H builds the approved component and adapter; R integrates shared routing. A real click opens a day/event's strongest-first articles; absent, failed and partial states remain distinct. |
| Desktop outbox / Jan 1 backfill -> store | Closed orders record recovery work; this research did not recensus each local outbox item. Gold density alone does not establish five-publisher history. | Reconcile desktop receipt ledger; approved-security x publisher coverage/cost matrix from January 1, Lenovo first; repeat adds no duplicates. |

## LGIC and migration rules

Use `lib/opal_data_harvest/harvest_grammar.py`, registered sources and the existing address builders. Bronze is as received, including listings; silver is typed Parquet replayed from bronze; article/security linkage is Opal-derived gold. Store absolute mention counts and weights; compute relative normalization and breakout at the serving/axis computation boundary. Fetch date partition and publication date column remain distinct.

Legacy `publications/v1` and `publication-links/v1` still exist (seven objects each). Do not let new data feed one path while the production reader silently uses the other. H supplies parity/dedupe evidence and the proposed retirement; R integrates runtime/IAM cutover with S's identity contract. Retain old evidence; retirement does not mean deleting stored objects.

## Acceptance map

- FWD-1..3: H01/H02, per-publisher current access, exact bytes, lossless typed replay and discovery provenance.
- FWD-4: H02, rederive the stored article/security grade from retained text, including incidental and roundup controls.
- FWD-5..6: H04, authenticated visible timeline/day/event-to-article traversal.
- FWD-7: H03, deployed gold-based ranking; passing incidental-mention-versus-subject control; both Chatter movement axes.
- FWD-8: H02, reconcile each stranded local record to a retained receipt without duplication.
- FWD-9: H05, approved-name x publisher x day matrix, preflight cost/page count, idempotent backfill. Truthful partial states do not constitute complete backfill.

**Principal sources:** HARVST PRD/project/decomposition; `ledger/ROUND_ANALYSIS.round4.md` including both corrections; investigation Z-S14; timeline spec under `deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md` and amendment order HVST-r-1; `lib/opal_data_harvest/`; `lib/research/harvest/publication_gold.py`; `lib/research/{coverage/pool_reader.py,metrics/chatter_axis.py}`; fresh object/package/IAM evidence. The round-4 corrected channel count is not used as product completion evidence.
