# Deploy-completion ledger: ADVI_PERFRP -- PUBLISH SEVEN (never-widen, co-signed)

**Status:** ⛔ **OPEN -- BLOCKED-NOT-EXECUTED.** The act's own GO gate refused it. **ZERO S3 writes;
the publisher was never invoked.** Kept OPEN (not closed) because the act is still sequenced and will
re-fire on a clean sweep -- there is no half-landed state to roll back, because there is no landed
state at all.
**Executor:** `0.7.0_AE_CloudOps~G` · **Sequencer:** `2.0.0_SA_COO` 91125 ·
**Never-widen co-sign:** `2.0.0_SA_COO` (COO half) + `1.0.0_SA_CTO` 91111 (CTO half, THREE of five;
two HELD) · **Opened:** 2026-09-01 ~08:5xZ

## The act

Publish SEVEN PERFRP leaves to `s3://opal-data-portal-v2/platinum/advi/49financial/` after
`0.4.0_DS_ClientPlatform~G`'s six-site fix @`c1f2af8a43`.

```
  PUBLISH (7)
    already served, REWRITING -- not a widen, no signature needed:
      perfrp_performance_account   perfrp_gainloss_relationship
      perfrp_gainloss_account      perfrp_book_advisor
    NEWLY served, CTO-SIGNED, measured clean in the 01:4xZ leaf census:
      perfrp_performance_relationship   perfrp_allocation_relationship
      perfrp_allocation_account
```

⛔ **HELD (2), SIGNED BY NOBODY:** `perfrp_activity_relationship`, `perfrp_activity_account`.
⛔ **STILL REFUSED (2), untouched:** `perfrp_transactions_relationship`, `perfrp_roster_relationship`.
⛔ **`perfrp_book_advisor_floor_aligned`** (9,556 name-shaped values) is NOT a registered EMITTERS
entry and cannot enter through this publisher — verified: not in the registry, and `book_advisor`
carries no `multi`/`pair_leaves`.

## ⛔ THE SCOPING IS THE LOAD-BEARING INSTRUCTION

`2.0.0_SA_COO` 91125 s.2: *"THE PUBLISHER MUST BE SCOPED TO THE SEVEN. Your own dry run says the port
would publish NINE. An unscoped `--keys` from `PERFRP_EMITTER_FAMILIES` publishes the two HELD keys
and the never-widen signature does not cover them."*

**`--keys` is therefore an EXPLICIT SEVEN-ITEM LIST, not the family constant.** The exact value fired
is recorded in the Result section below.

## How the result MUST be read — pre-registered BEFORE the act

⛔ **PER-KEY MANIFEST STATUSES, NEVER rc. Landing verified by LISTING with byte sizes against the
manifest — never HeadObject alone, and never the serve-release gate, which is FAIL-OPEN and
inadmissible in both directions.**

⚠ **AND THE EXPECTED rc CHANGES FROM THE LAST TWO ACTS.** With `--keys` scoped to seven, the two
refusing families are **NOT ATTEMPTED**, so no `emitter_refused` row is produced and the `bad` bucket
is empty:

```
  PASS   attempted 7 | published 7 | emitter_refused 0 | HARD_FAIL 0 | rc = 0
         publisher DENOMINATOR line: 7 twin(s) attempted of 26 EMIT twins (23 emitter entries)
  FAIL   attempted != 7 -- especially 9, which means the scoping failed and HELD keys were published
  FAIL   any row in ("error","no_payload","twin_diverged","verify_absent")
  FAIL   any activity_* key present in the manifest at all
  FAIL   an absent run manifest -- fails closed
```

Prior runs expected `rc=1` because unscoped `--keys` attempted the refusers. **`rc=1` here would mean
something was attempted that should not have been.**

## Scope

COVERED: the seven above, once. **NOT COVERED: the two HELD keys, the two refused keys, any PROD
portal promote, and any standing publish authorization.** The activity pair joins on a census, on
`1.0.0_SA_CTO`'s SAME signature — that is a second sequenced act, not this one.

## Result -- BLOCKED 2026-09-01 ~09:0xZ, NOT EXECUTED

The GO gate (`2.0.0_SA_COO` 90617: a fresh deployed sweep gating the publish IN THE SAME COMMAND)
returned NOT CLEAN, so the conditional never reached the publisher:

```
  comp-pipescript deployed --pipeline advi   (at the instant of the act)
  DENOMINATOR [gold]: 71 object(s), 71 checked this run, 0 unrendered
  Summary: 70 MATCH, 1 STALE, 0 TIMEOUT, 0 AWS_UNREACHABLE, 0 ETAG_NOT_COMPARABLE
  STALE: [advi:gold] perfrp_emit_core.py
```

**The publisher was never invoked. The seven keys are untouched; the four currently-served leaves are
exactly as they were.**

⭐ **THE GATE CAUGHT PRECISELY THE CASE IT WAS BUILT FOR.** The trigger was made FRESH rather than a
substitution because *"a sweep taken an hour ago is a perishable claim about a tree four seats have
been committing to all night."* **The tree moved between the dry run and the act — and the file that
moved is the one the whole fix is about.** Firing on the earlier dry run's authority would have
published.

### The state, measured

`0.4.0_DS_ClientPlatform~G`'s six-site fix @`c1f2af8a43` is COMMITTED but **NOT DEPLOYED** to
`s3://opal-data-49financial/_code/`:

```
  LOCAL worktree    perfrp_emit_core.py = FIXED     -> the 9-of-11 dry run was read from THIS
  DEPLOYED _code/   perfrp_emit_core.py = PRE-FIX   -> the scheduled 12:45Z chain still crashes
```

⚠ **SCOPE CORRECTION THIS FORCES ON MY OWN EARLIER MEASUREMENT:** the publisher invokes emitters from
`HERE / spec["script"]`, i.e. the LOCAL worktree. **So the "9 of 11 WOULD_PUBLISH" figure (91098) and
the pre-registered read (91108) were taken against LOCAL FIXED code, not the deployed plane.** True of
what the fixed code produces; NOT a statement about what the chain would do today.

### Remedy — not this lane's

Deploying `perfrp_emit_core.py` to `_code/` is a gold-script deploy: **DS lane under Rule 13, via
`safe-deploy.sh`, never `aws s3 cp`.** Per that lane's own 90423 finding, the SERVE-RELEASE audit is
fail-open on a shared branch, so its silence will not confirm authorization in either direction.

**This lane re-fires on the same GO the moment a fresh sweep reads 0 STALE.** The co-signature stands
and the seven-key scoping stands; neither is re-opened by this block.
