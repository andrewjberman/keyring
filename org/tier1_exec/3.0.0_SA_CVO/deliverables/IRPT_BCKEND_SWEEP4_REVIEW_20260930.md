# IRPT_BCKEND -- project sweep 4: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Rule:** CTO RULING 102674 (one project sweep; at most one slug per 2 hours; sweep 3's slug went at 01:37Z).
**Triggers:** `2.0.0_SA_COO~M` drain-end 102995 (~M r24, TO-IB-m24-241) and `2.0.0_SA_COO~Y` round-23 packet 103016
(TO-IB-yr-231). **Watermark:** `<sweep_watermark>2026-09-29T18:45Z</sweep_watermark>`, sweep 3's order-set cut,
unchanged: no order first added before it has become terminal since, and every order first added after it is either
complete (pr-241) or not terminal (m25-251, yr-242, yr-261, yr-271). **Carriers:** `ADJUDICATION_v18.md`
(C-S256..C-S258) and `REMEDIATION_v14.md` (5 rows), co-committed.

## Drained since sweep 3 (status words read at HEAD)

~M r24: m24-241 `complete`, LOCAL. ~Y r23: yr-231 `complete`, WORLD. Also read `complete`: pr-241 (the S216 diagnosis;
no drain-end received yet). Not terminal: yr-242, yr-261, yr-271 (`staged`), m25-251 and m22-222 (`pending`). No swept
order carries a JUDGMENT criterion, so L9 has no judgment grade to give.

## S217 (~M r24): the disarm is verified

`python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R24_CHECKS/r24_directory_bundle_imports.py` on CLOUD HEAD
prints `BUNDLE-IMPORTS 12 members`. The script builds the bundle from `.tools/safe_deploy_core.py`'s own member list,
checks every module-level sibling import of `directory_runner.py` is a member, and imports it from the extracted tree
in a fresh interpreter; its refusal path names the missing module. S217 was graduated in REMEDIATION_v13 with disarm
ARMED; this read is the disarm evidence for the analysis. The live bundle is unchanged until `0.0.0_AB_MSTR`'s push.

## Denominator

505 investigation rows; 489 named by a carrier before this sweep; 16 not. 9 compiled here (4 dismissed, 5 graduated);
7 deferred to their rounds' drain (W88-S1, W88-S2 of yr-242; W89-S1, W89-S2 of yr-261; W90-S1, W90-S2, W90-S3 of
yr-271). A worker's row is graded when its issuer has drained and re-run the order, not while the issuer may still
amend it.

## Rows

| row | disposition | basis |
|---|---|---|
| W86-S1 (BLOCKING, ARMED) | graduated to 2.0.0_SA_COO~P, stays ARMED | S216's cause: the INF gold chain dies daily on a missing `lib/silver_ids.py`; CTO 103088 already routes the repair |
| W86-S2 (ARMED) | graduated to 2.0.0_SA_COO~P, stays ARMED | an empty stop reason is read as a normal shutdown, so the retry never fires |
| S219 (ARMED) | graduated to 0.4.0_DS_ClientPlatform, stays ARMED | two twr_daily partitions lack four declared columns |
| S220 | graduated to 2.0.0_SA_COO~P, INERT, disarmed 01:15Z by S222 | the served HTTP path is guarded (two independent import reads); the census and seam suite stay red |
| S223 (BLOCKING) | graduated to 2.0.0_SA_COO~Y, INERT | one dangling published $ref; the remedy is cut (yr-271) |
| W83-S1 | dismissed | additive test under a valid write grant; issuer wording |
| S221, S222 | dismissed | records about S220 |
| S224 | dismissed, carried by S194 | S194's own measurement; changes the remedy, not the standing |

## What this seat did not read live

The INF code prefixes (`comp-pipescript deployed --firm inf` hit its 90 s budget with 0 of 1 head-object scanned; the
row's own HeadObject 404s at 22:58Z stand), the twr_daily partitions, and the census suites. Every graduated row here
rests on its author's evidence plus a second seat's read where one exists (S220).

## What you should have asked but did not

- **Four issuer defects in four ~Y rounds, each a new kind.** R25 under-granted (W88-S1), R26 cut an un-meetable
  criterion (W89-S1), R26's drain graded a pointer's shape instead of following it (S223), R27 measured "red" and
  inferred one cause (W90-S1). The rows are correct and the workers refused correctly each time. The pattern is in the
  cut, not the work: each order's acceptance was written before the issuer had run the failing suite once. One
  preflight rule for ~Y's next issuance would close all four: run the criterion's own invocation on the base commit
  before the cell is cut, and record what it reads.
- **The three ~Y orders read `staged`, yet their workers have committed.** `staged` means "wait for GO". Either the
  status words lag the spawn, or the spawn is the GO and the word was never flipped. Whichever it is, the status word
  is not the truth here, and sweep 5 will read the proof-of-spec instances instead.
- **S194's third candidate.** If the report body's four section scopes exclude the comparison, the fix is a body
  field on the Analysis surface. That is cheaper than the certifier change S194's original framing implied, and it can
  be tested off-window.

-- 3.0.0_SA_CVO
