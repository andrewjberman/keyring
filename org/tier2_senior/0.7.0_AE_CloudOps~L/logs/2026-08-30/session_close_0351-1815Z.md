# Five never-produced trading days now exist, a Sunday fire completed for the first time since the floor was built, and the enumerator that hid the gap stopped reading its own output — 0.7.0_AE_CloudOps~L

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE, DEPLOY

**Window:** 2026-08-30T03:51Z (prior log @c0dc3f09a0) -> 18:15Z. 16 commits, 171 inbound messages, 3 cells closed, 1 sovereign call answered and executed.

## Objective

Carry ADVI_49F's c02 series to close: produce the five trading days that had no `twr_daily`
partition (C02-g-7), fix the enumerator whose output-table domain hid them (C02-g-9), and retire
the re-emit capability on Andrew's word (C02-g-11).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `fact_rps -- runners_49f/` | PASS | **The run that carried E-1.** 0 hits / 108 files, a MEASURED zero with its 102-file ephemeral-floor exclusion printed. Established that a table with PERFECT 540/0/0 coextension is never read. |
| `comp-find` | `rc\.read_partition\( -- runners_49f/` | PASS | The 28 call sites that produced the halting set. Found `dim_transaction` (c01:232) that a DEF-band census could not see. |
| `comp-find` | `--name proof_of_spec`, `PROOF_OF_SPEC.schema` | PASS | Located standard + checker with denominators (279 / 295). |
| `comp-which` | "which tool validates a proof_of_spec instance" | WARN | Returned **NO CURATED RULE MATCHED**; top score 0.56 was unrelated. Recorded rather than resolved by taking the fuzzy first hit. |
| `commit-gate.sh` | on every `.py`, 6 runs | PASS | One real catch: ruff F541 (f-string, no placeholders) on the enumerator — fixed before commit, not suppressed. |
| `safe-commit.sh` | 16 commits, `-F` non-shell msgfiles | PASS | `msg-verify MATCH` on every one. |
| `deploy_ledger.py` | open/hold/release/close-leg x6/close/check --red | PASS | Entry HELD on a named external gate through the M-3 wait rather than aged out; closed with 6 legs proven, sentinel removed. |
| `proof-of-spec-check.py` | 3 instances, positional | PASS | c02-BACKFILL VALID (3 runs), c02-ENUMERATOR VALID (1st run), c02-REEMITRETIRE VALID (1st run). |

**What worked:** `comp-find`'s printed denominators and its explicit ephemeral-floor exclusion are
what made a zero usable as evidence rather than as an absence of evidence. The `[HEAD]/[DEF]/
[SURFACED]` banding is what exposed my own blind spot — the DEF band shows prefix CONSTANTS, and
the input I missed is an inline f-string, visible only when I swept CALL SITES instead.

**What failed:** `comp-which` had no rule for the proof-of-spec checker and said so loudly. Correct
behaviour; recorded so the catalogue gap is visible rather than papered over by its own top guess.

**Gap found:** none in the tools. The gaps this window were in MY instruments and are listed under
Corrections.

## Deployment Sequence

1. **C02-g-7 B-4 re-drive** — 5 SSM sends on `advi-49f-chain-dispatch` (i-01003b035d2988dfb),
   oldest-first, mutex limb (ii) re-read and PRINTED before every one.
   `2a813838` 08-11 · `62531fb9` 08-12 · `bd391e3a` 08-13 · `7b89b833` 08-14 · `3fc1f030` 08-17
2. **G5** — `a4de0c21`, AWS-RunShellScript, `c02_reemit_mirror_pull.py --date 2026-08-18 --mode upload`.
3. **C02-g-11 R-2** — no deploy. One act, two halves: driver refusal committed `9d37a3e211`, then
   `s3 delete_object` on `_code/c02_reemit_mirror_pull.py`. Refuse-before-delete, deliberately.

## Verification

Actual output, five dates identical in form:

```
map resolution: chose date=2026-08-28 of 46 partition(s); SKIPPED header-only: 2026-08-29
map date=2026-08-28: 7,359 rows | fact_acc universe 7,265 (date=2026-08-11) | map_carried=True
STAGE OK a06_identity_crosswalk rc=0 wall=1.3s
```

The 12:45Z scheduled fire, read from the floor-form S3 chain log (never SSM stdout):

```
CHAIN START date=2026-08-28 mode=production stages=17
map resolution: chose date=2026-08-28 of 46 partition(s); SKIPPED header-only: 2026-08-29
map date=2026-08-28: 7,359 rows | fact_acc universe 7,371 | map_carried=False
STAGE OK a06_identity_crosswalk rc=0 wall=1.2s
CHAIN OK date=2026-08-28 wall=104.4s
```

Version-delta arm, whole-tree BEFORE/AFTER over 23 prefixes (08:49:27Z / 09:01:01Z, 23,342 ->
23,480 objects): NEW KEYS 138 across 16 of 23 prefixes, **NEW-KEY DATES OUTSIDE THE FIVE: NONE**,
VANISHED 0, REWRITTEN 12 — all at date=2026-08-11, **every ETag UNCHANGED, signed size delta +0**,
so idempotency is measured by content rather than asserted.

C02-g-11 delete:

```
delete marker  YTU5bblWtea.A41gKJ39oCRfD5DleqSn (IsLatest)
RETAINED       1qPpKmV5CkFCG2pa06_CxQQAW.ntPlIG  13,909 B  ETag ccd557f5d383decd4f2abd8d2b2abacd
HEAD without a version -> 404 ; HEAD at the retained id -> 13,909 B (restorable, PROVEN)
```

## Work Completed

### 1. C02-g-7: the halt, and the defect that outranked the backfill

Date 1 aborted at `a06_dim_identity_crosswalk` on an empty allocation map. Measuring that produced
the finding: a06 reads the NEWEST map partition regardless of chain date; the map is header-only
every Sat/Sun (13 of 46, zero weekdays) and lands ~13:15Z, AFTER the 12:45Z fire — so every fire
reads yesterday's map. **Filed as Sunday-only; corrected by `0.4.0_DS_ClientPlatform~N` to Sunday
AND Monday**, from two facts that were in my own message one paragraph apart. And not a prediction:
08-23 and 08-24 had already aborted in production. My "masked by the hold" reading was retracted —
the hold was applied a week later; those fires failed in the open and nothing read the logs.

### 2. The re-drive, and 2026-08-18

All five dates through the full chain after the a06 fix was served. `2026-08-18`, which held 7,315
rows of `REFUSED-NO-BMV` because its previous trading day did not exist, moved to **6,382 OK
returns**. Domain census confirms 16 IN / 7 OUT on a second axis (distinct dates, not object counts),
which settled by measurement a claim the halt could only leave as inference.

### 3. C02-g-9: the enumerator stopped reading its own output

`A00_ATTESTATION_REDERIVATION.py` enumerated its date set from `gold/advi/canonical/flow_ledger/`
— an OUTPUT of the chain whose missing dates it exists to find. Replaced by dim_calendar trading
days AND a **seven-input halting set derived at source**, five denominators printed per run.
Four arms; the mutation restoring the flow_ledger read **correctly FAILS** the discriminating one.

### 4. C02-g-11: the capability retired on Andrew's word

Card filed once with both corpora, denominators, firing controls and grounds both ways; this seat
abstained from a REC and said why (I measured the object AND own its only caller). Andrew: *"5.)
Rec approved."* Executed as one act, refuse-before-delete.

### 5. Two task-order legs whose premises were false, both caught BEFORE the act

E-4 would have deleted a script whose only caller is laptop-side and was used four hours earlier.
E-3 would have deployed the enumerator to a host location where **no copy has ever existed**
(ABSENT of 81, positive control firing) — minting a second unreferenced writer, the exact hazard
E-4 was cut to remove. The two legs would have worked against each other. Issuer banked the cause:
both were written from a sibling cell's pattern without measuring where THIS artifact lives.

## Decisions Made

- **Refuse-before-delete** on C02-g-11: the halves are not commutative. The reverse order leaves a
  window where a live caller shells out to a missing file and fails deep in a shell — which is
  indistinguishable from a broken box.
- **No deploy ledger opened for E-3.** A ledger entry for a deploy that should not happen is itself
  a record of the wrong act.
- **Declined an exoneration.** A peer took ownership of the truncated VersionId as a card-format
  defect; the trace showed it originated in my own census script's `[:22]` slice. Accepting would
  have installed a card-formatting rule while the slice survived in an instrument that runs again.

## Files Modified

See commit messages: `39c11c552b`, `0ae699e57b`, `8cf9670ac2`, `c8f76b8c44`, `5d4e3c932a`,
`8845514939`, `3bda676e01`, `d4319e5b6c`, `998b7d0028`, `9d37a3e211`, `885e08055f`.

| file | note beyond the commit message |
|---|---|
| `deliverables/ADVI_49F.P14-VEHICLE_A00_ATTESTATION_REDERIVATION.py` | the enumerator fix; carries a pure `compute_domain()` seam so arms can drive synthetic sets |
| `deliverables/test_p14_enumerator_domain.py` | 4 arms + the mutation, which lives HERE and never in the module |
| `deliverables/ADVI_49F.c02-REEMIT_CAMPAIGN_DRIVER.py` | dispatch() now refuses; the pre-retirement body DELETED, not kept unreachable |

## Corrections against myself (5)

1. **`map_carried=True` written into the durable carrier as the expected literal, and False listed
   as a FINDING.** False was correct — the fire's chain date IS the map date. I transplanted a value
   observed under a different chain date. My own carrier would have had its reader file a false
   finding against a peer's correct fix; that peer flagged it unprompted, against their own interest.
2. **A `WARN: fact_fam DECLARED-STALE` line on all five re-drive logs, unreported.** My log reader
   filtered on a token list I chose and `WARN` was not in it. Five logs, five reads, one warning in
   every one, invisible throughout.
3. **Push state reported as LOCAL for two commits already on origin.** I compared my hash to the
   origin TIP instead of testing ANCESTRY. A real `ls-remote` hash printed beside an inference reads
   exactly like evidence.
4. **A token-level negative control fired on a peer's correct deploy** — matching a COMMENT
   describing the defect and a ruled fallback. Opened the context before reporting; a presence test
   cannot separate a defect from its own description.
5. **A truncated VersionId (22 of 32 chars) reached Andrew's decision card**, from a `[:22]` display
   slice in a scratch census script. The card's whole "recoverable" argument rested on that handle.

## Blockers

**NONE.** Nothing on this seat is blocked, gated or waiting. The one sovereign call
(C02-g-11) was answered at ~17:1xZ and executed the same hour.

## Current State

- **ADVI_49F c02 series:** C02-g-7, C02-g-9, C02-g-11 all CLOSED at issuer and grader.
- **`s3://opal-data-49financial/gold/advi/canonical/twr_daily/`** — 540 partitions (was 535).
  `date=2026-08-11/12/13/14/17` new; `date=2026-08-18` re-emitted, 6,382 OK rows.
- **`_code/a06_dim_identity_crosswalk.py`** — the DS fix, ETag `f8763326799bba70dac9edf5c55bdaf8`,
  11,148 B, exercised on 6 real runs and one scheduled fire before this log.
- **`_code/c02_reemit_mirror_pull.py`** — DELETED behind marker `YTU5bblWtea.A41gKJ39oCRfD5DleqSn`.
  Restore at VersionId `1qPpKmV5CkFCG2pa06_CxQQAW.ntPlIG` or re-deploy the untouched repo copy at
  `org/tier2_senior/0.7.0_AE_CloudOps~L/deliverables/c02_reemit_mirror_pull.py` — under a NEW cell.
- **Deploy ledger** `20260830T0554Z_advi-49f-c02g7-five-date-forward-production` CLOSED, 6 legs
  proven, sentinel removed; `check --red` scans 3 sentinels, none this seat's.
- **Proof instances** (all VALID): `ADVI_49F.c02-BACKFILL.proof_of_spec.json` @3948c766a7,
  `ADVI_49F.c02-ENUMERATOR.proof_of_spec.json` @3948c766a7,
  `ADVI_49F.c02-REEMITRETIRE.proof_of_spec.json` @eefe9e0a91 (CONTENT-resolved via `introduces`).
- **Lane clean**, 0 uncommitted, all commits on origin by ancestry.

## Next Steps

- **[0.4.0_DS_ClientPlatform~N]** — `a07:352` stamps a CLOCK under the `_ingested_at` name where
  Atom 9 makes it the asof partition date (two intents, one field, Rule 24 iii); and
  `anomalous_return_census` is NOT WIRED (`run_battery` receives `twr_daily=None`), reporting
  NOT-EVALUATED on all five dates this window produced. Both named, neither chased.
- **[1.0.0_SA_CTO]** — `.tools/deploy_ledger.py:90` `HELD_STATUS` is a module constant, so an
  `--gate-type external` hold is labelled HELD-SOVEREIGN-GATED; 2 of 2 held entries are
  external-gated and both carry the SOVEREIGN label. On the gate's NFRA queue.
- **[3.0.0_SA_CVO]** — `get_agent_status` on one's own serial prints "URGENT: N message(s) received
  while idle" for a broker queue this seat never drains; measured 159 already-delivered messages
  against 0 unread. A seat believing it would re-process a day of work. Filed, not chased.
- **[this seat]** — nothing. Idle and reachable.
