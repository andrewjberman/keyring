# NFRA_TRNSPT round 1 -- the CTO's L10 analysis

**Author:** 1.0.0_SA_CTO, 2026-09-30 ~21:1xZ. **Input:** `3.0.0_SA_CVO`'s slug 103392,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md` @ba199ff55b (ADJUDICATION_v1 C-S1..C-S5, REMEDIATION_v1
9 rows; L9 TR1-t4-AC3 PASS); `2.0.0_SA_COO~T`'s packet `R1_DRAIN_END_PACKET_20260930.md` @2b7372f583 (12 of 12 terminal). Rows read
from the channel at HEAD: S2, S3, S6-S10, W4-S8, W4-S10. PRD: `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.1.

## 1. What round 1 proved

- **FWD-1's thread, hops 3-6, is real and person-free:** `THREAD-TRACE hops=3 no_person=true negative_arm=NOT-HELD` on the real
  2026-09-28 Monday meeting, reproduced by the CVO at HEAD. Hops 1-2 (the scheduled pull) are not exercised: they wait on the
  gateway transcript tools and the headless route, accepted for intake by site Z's NFRA_OPLGTW (relay 103276), whose PRD addendum
  names the allowlist and auth boundary before any cut.
- **FWD-5 graded PASS at L9:** one command returns what was said about a named firm, with speaker and time, from real silver. Its
  stated limit (a literal token; a later "they" is not returned) is a round-2 recall enrichment, not a failure.
- **FWD-7 has run on no real row (the CVO's Q1, accepted as the round's headline).** The one real input broke at the envelope (S9),
  so silver, gold, the wipe and the slicer are proven on synthetic input only. Measured with the envelope unwrapped, BOTH real sample
  messages classify `ingest=false` (their only non-inline attachments are images, `ycharts_pdf=false`, `near_miss=true`). So the sample
  holds no message the criterion admits: even with S9 fixed, the thread for FWD-7 needs a real message that IS feedback with a YCharts
  report attached.

## 2. Rulings

1. **S2 (graduated to this seat): CLOSED by relay.** `read_email`'s missing `internetMessageId`, `ccRecipients`, `conversationId` and
   `sentDateTime` are item 4(iii) of the five NFRA_OPLGTW orders relayed to site Z at 14:42Z and accepted for intake (103276); the
   laptop's draft of that tool change is preserved on origin as scratch branch `gw-f1-read-email-fields` @5ec089b9a1 (MSTR 103294),
   for site Z to adopt or supersede. Until it lands, every mail row carries `id_source=fallback` (C-DEDUP's stated fallback), which is
   honest and changes when the field arrives.
2. **S3 (graduated to this seat): cosmetic, no standing act.** The CVO measured 12 of 13 generated targets identical and one portal
   target differing only in its hash mark line (content identical); this seat's own read at 18:0xZ agreed (content identical, marks
   drift). A mark-only drift is restamped by the next content-changing regenerate of that target; no seat regenerates for the stamp
   alone. CLOSED as INERT.
3. **Q1 / S9 / S10, the FWD-7 thread: round 2's first two cells, in this order.** (a) S9 and S10 together: the lander unwraps the Graph
   `value` envelope (with a fixture in the real envelope shape) and `load_tables` reads the ruled `authors.json` and the registry's
   tenant email domains alone. (b) A real run that lands ONE message the criterion admits: the date-sliced dredge of Andrew's mailbox
   (v3 addendum 8, today's tools) picks a Manav message with a YCharts report attached; the PDF test stays the stated heuristic until
   site Z's attachment tool lands, and the run prints the criterion's three booleans for every message it scanned (the precision
   measurement C-CRITERION asks for, near misses included). Its silver is READ by this project's two named readers before any other
   reader is admitted (the CVO's condition, adopted).
4. **W4-S8, the wipe's limits: measured, not assumed.** Round 2 adds the two classes the builder named as missed (a standalone
   lower-case name with no same-message capitalised sighting; an English-word surname at sentence start) as PLANTED cases in the
   planted-token gate. Each either passes (the wipe improved) or is recorded as a stated limit in C-WIPE; the gate's result stays "the
   planted classes were removed", never "no PII remains".
5. **W4-S10, the slicer's real replay set: through the READY hook's abstract fields, never a firm bucket.** `irpt-requests` holds no
   composition; the compositions live in client-bearing artifacts in each firm's bucket. The slicer never reads a firm bucket (C-FIRM,
   C-KIMI: abstract fields only). The real replay set arrives with IRPT_BCKEND's READY hook (S18), which hands the slicer the abstract
   request (variant, model keys, account type, category weights); until then the six fixture requests stand and the replay says so.
6. **S6 / S7 / S8 and the CVO's Q2, the combined suite red (23 of 118 fail together): one batched repair cell,** proved in the
   deployed layout. The collision (two packages each exposing top-level `land_bronze` and `pull`) is the same shape as a deployed
   Lambda importing both; the fix is package-qualified imports or unique module names, and the criterion imports the Lambda's modules
   from its built bundle (the deployed-layout issuer rule, 103370-103374), not only a green pytest. S6's CRLF fixture split and S8's
   missing `list_objects_v2` on the fakes ride the same cell.

## 3. Outcome read

FWD-1: hops 3-6 EXERCISED on a real meeting; hops 1-2 wait on site Z. FWD-5: EXERCISED (L9 PASS). FWD-7: NOT exercised on a real row
(ruling 3). The other outcomes are built on synthetic input or not yet started, as the packet states. None REALIZED.

## 4. Enrichment for round 2 (~T; one issuance)

1. S9 + S10 (ruling 3a), first.
2. The FWD-7 real-row run and the precision print (ruling 3b), second; its silver read by the two named readers.
3. The batched repair cell S6/S7/S8 with the deployed-layout import criterion (ruling 6).
4. The two planted wipe classes (ruling 4).
5. FWD-2's first archetype beyond Monday, as the transcript tools allow (the Research Meeting's refusal investigation, S07 of the
   manifest, runs read-only now).
6. Carried: FWD-1 hops 1-2 (site Z's tools and headless route); the READY hook (IRPT_BCKEND S18); the slicer's real replay (ruling 5).

-- 1.0.0_SA_CTO
