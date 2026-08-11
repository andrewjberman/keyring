# CVO INSTRUMENT REVIEW -- P5 debt-identification methodology spec @edcd9e75b2

**3.0.0_SA_CVO 2026-08-11 ~1808Z · VALIDATE.** Route: CVO (this) -> CTO -> Andrew. Attacked the
three surfaces CRO~A named; grounded against live estate where a finding rests on a claim.

## VERDICT: APPROVE-WITH-AMENDMENTS -- the method is SOUND; two ADDITIONS (one load-bearing) + one
## demonstration fix. The core asymmetry (evidence scales with irreversibility; LIVE rests on one
## positive, DEAD on a conjunction) is exactly right and inherits the session's hard-won controls
## (comp-iam floor-not-warrant, the 0.0% trap, positive-controls, search-FOR-the-name, denominators).

## FINDING 1 (LOAD-BEARING -- surface 2, the roster): TWO CONSUMER NAMESPACES ARE MISSING, and a
## closed-world enumeration that omits a namespace produces a FALSE-DEAD verdict for everything that
## namespace consumes -- the exact silent hole the spec exists to prevent.
- **THE LAKEHOUSE / ICEBERG QUERY LAYER is absent from the §3 roster -- CONFIRMED LIVE AT SOURCE.**
  The estate runs an Iceberg/Nessie/Trino lakehouse (`pyiceberg-nessie-deps` Lambda layer;
  `infra/aws/lambda/globgrph/incremental_updater`; the graph consumers under `org/modules/graph/`
  read `s3://opal-313476888478-globgrph/warehouse/` Iceberg tables). **NONE of these consumer paths
  is in any listed namespace** -- a Trino view / Iceberg table-reader / Glue job consuming a
  warehouse prefix is invisible to repo/Lambda-code/EventBridge/S3-notif/SSM/CF/IAM/EC2/comp-tool/
  served-JSON/FE. So a P5 kill-census of a `warehouse/` prefix would enumerate the full roster, find
  ZERO consumers, and conclude DEAD on a prefix Trino actively reads. **LIVE SPECIMEN, measured this
  session:** the snap-ingest Iceberg tables (`ms_heat`/`code_heat`/`fedobs`) -- their consumers are
  the graph platform, all lakehouse-layer, all roster-invisible. Add: **the lakehouse consumer
  namespace (Iceberg table refs / Nessie catalog / Trino-Athena-Glue query layer).**
- **STEP FUNCTIONS state machines** are also absent (a state machine's states invoke Lambda / read
  S3 / write DDB -- a distinct consumer namespace from Lambda async-destinations). Lower live-weight
  (unconfirmed heavy use) but the roster is NORMATIVE and closed-world, so it must be listed -- even
  as "measured empty today" -- or the completeness claim is false by omission.
- **The fix is the spec's own discipline turned on itself:** a closed-world roster must carry EVERY
  namespace with a denominator, including the empty ones, exactly as the spec demands of every other
  census. Amending the roster is a spec-amendment event (the spec says so) -- so land these before
  ratify, not after.

## FINDING 2 (surface 1, the ladder): RULE-12's BLIND SPOT IS NAMED BUT HAS NO HOME IN THE SCHEMA --
## an invoked-but-serving-nothing artifact is forced to LIVE, so the method structurally CANNOT
## identify actively-invoked-dead debt, which is a MISS of exactly what debt-identification hunts.
Tier-1 correctly names "invocation is not outcome (Rule 12): an invoked-and-erroring function reads
LIVE while serving nothing." And the ladder law grants LIVE on any single tier-0/1 positive. So an
erroring-but-invoked function → tier-1 positive → **LIVE → keep, forever.** For the DELETE stage
that is the safe error (keep-is-reversible). **But this is a debt-IDENTIFICATION methodology, and its
job is to FIND dead things -- a function that invokes-and-errors IS debt, and the schema has no state
for it** (LIVE/DORMANT-EXCEPTED/SUPERSEDED/SOVEREIGN-RETIRED/DORMANT-UNEXCEPTED/DEAD-EVIDENCED --
none fits "invoked, outcome-plane dead"). This is the marked-gap-with-no-state class: the blind spot
is named in the ladder and then discarded by the schema. **Remedy (CRO~A's call on form): either add
an `INVOKED-OUTCOME-UNVERIFIED` / `DEBT-SUSPECTED-LIVE-WIRE` state (invoked but outcome-plane not
confirmed serving -> a cleanup CANDIDATE, never a kill), OR declare outcome-plane debt EXPLICITLY
out of scope for P5 with the reason -- named, not silent.** The asymmetry is right for KILL; it just
can't silently double as the IDENTIFY bar.

## FINDING 3 (surface 3, the worked examples): mostly discharge from the rules -- ONE skips links.
Checked each: `account_quality_tiers` (date-stamp → closed-period-immutable candidate, PENDING
declaration) and `partner_analytics/header_metrics` (family-resolve → SUPERSEDED PENDING one
equivalence read) both discharge cleanly and honestly say "candidate/pending" rather than asserting
a reached state. BUT `firm_composition.json` → "no live sibling → DORMANT-UNEXCEPTED" ASSERTS the
state while DORMANT-UNEXCEPTED's entry-evidence is a CONJUNCTION (>=90d AND no-exception AND
successor-check-negative AND tier-0-2-consumer-absent); the example shows only the successor leg.
**A methodology demonstrating itself must model the no-skipped-links discipline it mandates, or a
reader copies the shortcut.** Remedy: expand the worked examples to one-line-per-entry-link (cheap;
it is the PROOF_OF_SPEC row form the spec already defines for teardown TOs, applied to the examples).

## WHAT I DID NOT CONTEST (it holds)
The deny-probe as the terminal reversible control (bronze-parquet precedent, per-class ruling,
last-link-only) · the window-clock-starts-at-positive-control rule · consumers-first / instruments-
second / regenerated-artifact / guarded-set-whole ordering · the five named GAPs as DEFECTS-routed-
not-built · every record-as-hypothesis / verify-live-plane stance · moratorium honored (no
detector/monitor built; enablements are ruled proposals). These are the estate's own controls
correctly assembled; I attack none.

-- 3.0.0_SA_CVO
