# NEVER-WIDEN CO-SIGN -- COO HALF. Round 81, `AMGT-ee-6`: the redeploy of `opal-amgt-scoped-api` and the /freshness snapshot event

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~04:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND81_EE6_CTO_HALF.md`. Model: round 80's dd-4 pair (COO @db906ef3d1 + ADDENDUM 1
@c79b9318b8; CTO @f35ac7640a + ADDENDUM 1 @b7f8b30f32, condition 5).

## THE ACT

Order `task-orders/AMGT_RESAPP.TO-AMGT-ee-6.the-code-redeploy-and-the-snapshot.md`, two legs, from a DETACHED worktree at build pin
**`881540dcfd`** (carries ee-1 @21f7c2bee9, ee-2 @0f94216af8 and dd-1 @6e44bfec4a; not ee-3, whose `document.py` change the function does not
import):
1. **Code leg** on us-east-1 `opal-amgt-scoped-api`: one resource, `module.scoped_amgt_api.aws_lambda_function.this` (artifact object and
   hash), and the function's source-map entry.
2. **Snapshot leg:** one invoke of the existing scheduled event `{"amgt_scheduled_action": "refresh_freshness_snapshot"}`, which re-writes the
   /freshness snapshot object the route already serves (its existing writer; no new key).

## LIVE PRE-ACT STATE (the applier measures fresh)

CodeSha256 `OUOsYXaJSklKJ65vpIe2jWfcXm9jvP0bCyia15F8Bxs=` (dd-4, 2026-10-09T03:37:34Z, build pin 65532d8a7b); the snapshot object's current
VersionId, read before the event.

## BLAST RADIUS

**CONTENT-DIFF the build may print against the live package** (measured `git diff --stat 65532d8a7b 881540dcfd` over the closure roots and
the packaged registry members):
- `lib/research/api/scoped_amgt.py` (ee-1: the typed-name branch at the 404);
- `lib/research/freshness/long_day.py` (NEW), `lib/research/freshness/collector_record.py`, `lib/research/lists/owner_line.py` (ee-2);
- `lib/research/filings/section_coverage.py` (dd-1: `_WANTED["20-F"]` carries business);
- `lib/research/filings/fetch.py`, `document.py`, `section_census.py` ONLY IF the build's closure carries them (dd-1; the function's serve path
  does not import them), with that reason.
- The packaged registry members (`systems`, `scopes`, `tiers`, `exemptions`, `remediations`, `resources`, `reporting_policies`) and
  `NAMING_SCHEMA.json`: byte-equal to the live package at this pin (the registry files that moved -- `event_rules`, `key_rulings`,
  `name_rulings` -- are not packaged; measured 0 changed of the eight packaged members and `lib/opal_naming.py`). The one other
  closure-root change, `lib/opal_data_harvest/install-cycle-schedule.ps1`, is not a Python package member. Any other member printed is a STOP.
NO IAM, NO route added, NO memory, NO schedule change, NO S3 delete.

## WRITER CENSUS of the moved served properties

- `/security/<typed>/...` answers: one writer, the per-security arm of `scoped_amgt.py` (ee-1 adds a branch reached only where it would 404).
- the /freshness sentences: `collector_record.seeking_alpha_state` and `owner_line` (ee-2), read by `page_body` into the snapshot the
  scheduled event writes (one writer of the snapshot object: that event).
- each 20-F name's `passage_coverage`: `section_coverage.read_section_coverage` (dd-1).

## EXPECTED OUTCOME -- both branches, read from each producer's rule

- **Typed string:** an exact or single-candidate match serves that key's page (200); two or more -> 404 "N companies match ..." with the
  candidates; none -> today's 404; an unreadable name list -> 500 with /resolve's sentence (issuer ruling at ee-1's drain). Any string that
  resolves today: body byte-equal (ee-1 AC2).
- **/freshness after the event:** every served sentence carries the house long form and no `YYYY-MM-DD` day; every date field stays ISO. If the
  event answers that its read was incomplete and nothing was written, that is not a code rollback: report and stop before AC1.
- **20-F names:** `passage_coverage` lists Item 4.B as wanted and, for the five stored 20-F names, not covered until AMGT-ee-4 re-cuts them.

## PER-KEY ROLLBACK

Code: the kept live package (downloaded from `get-function` and hash-checked as `OUOsYXa`) through the module, one `safe-apply`, same
session. Snapshot: re-invoke the event after the code rollback (it re-writes the snapshot from the restored code); no delete.

## NOT COVERED

ee-3's `document.py` (its own site-Z pair); ee-4's store writes (their own pair); any build at another pin.

-- 2.0.0_SA_COO~R1
