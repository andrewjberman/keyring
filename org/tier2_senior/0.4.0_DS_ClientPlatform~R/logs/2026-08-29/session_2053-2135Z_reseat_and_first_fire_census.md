# ADVI_INSURE TO-R1-DS — re-seat 2053–2135Z, cut short by the sovereign wind-down

**archetype:** MEASUREMENT
**Seat:** `0.4.0_DS_ClientPlatform~R` · **Window:** 2026-08-29 20:53–21:35Z · **Predecessor log:**
`2026-08-28/session_close_1639-1745Z.md` (the release)
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (PRD s.3, Andrew ~16:1xZ).

---

## Current State — the handoff

**Re-seated on INS-a-5's first scheduled fire (`2.0.0_SA_COO` 83812), then stopped by Andrew-direct
controlled wind-down (`0.0.0_AB_MSTR` 83938, 21:29Z) before any build act.** The seat's tree is
**CLEAN**; nothing was left dirty and nothing was pushed.

⛔ **THE BUILD DID NOT START. NOTHING IN THE PRODUCER CHANGED THIS SESSION.**
`bd49f_insurance_conversion.py` is byte-unchanged from `@bb86c179db`. What this session produced is a
**measurement of the world the build will run against** — which is exactly the input step 0 needs and
the part a cold successor would otherwise re-derive.

| criterion | state, carried forward unchanged |
|---|---|
| **AC1 · AC5 · AC6** | **PASS** — ⛔ do NOT re-execute (`2.0.0_SA_COO` 83812, explicit) |
| **AC2 · AC3** | `APPLIED-GATED` — their APPLIED limbs are now measurable against real landed bronze |
| **AC4** | **NOT THIS SEAT'S** — `0.7.0_AE_CloudOps~K`, and it was ACCEPTED at 05:4xZ today (83850) |

---

## The census — the first scheduled fire, read at the artifact

`INS-a-5` fired **2026-08-29T04:35Z**. I re-derived the landing with **boto3 direct** rather than
inheriting the issuer's `s3api` read (Rule 22: a second seat's confirmation via the FIRST seat's method
is repetition). Full client-side pagination, denominators printed.

```
blackdiamond/49financial/bronze/    DENOMINATOR: 14 keys
blackdiamond/49financial/silver/    DENOMINATOR:  3 keys
```

### ⛔ FINDING 1 — THE FIRE LANDED **2 OF THE 3 CONVERTIBLE FEEDS**, NOT 3

```
  2026-08-29  insurance_relationshipaccountdetailsearch    page0 82,136 B  04:35:08Z
                                                           page1 41,688 B  04:35:09Z
  2026-08-29  insurance_insurancerelationshiplist_export   ...283068.xlsx 13,090 B  04:35:20Z
  2026-08-29  insurance_relationshipdetail                 ⛔ ABSENT
```

**`insurance_relationshipdetail` has NO 2026-08-29 partition — its only partition estate-wide is
2026-08-27.** This is the feed my own design s.5 names as *the one with no vendor-attested total*.

⚠ **STATED AT ITS REAL GRAIN: I have NOT determined WHY it is absent.** Whether the scheduled leg does
not yet invoke the S4 fan-out, or invoked it and it produced nothing, are different facts with
different owners, and **the prefix looks identical under both.** That question belongs to
`0.6.0_AE_PartnerETL` / `0.7.0_AE_CloudOps~K`, not here.

✅ **The stage's designed behaviour is already correct for this case and needs no change:** an absent
bronze day is `SKIP: an absent day is ABSENT — no roll-forward, no zero rows` (design s.4). **The
stage will convert 2 feeds and correctly decline the third.** ⛔ **But `rc=0` on a 2-of-3 day and
`rc=0` on a 3-of-3 day are the same byte** — the successor should decide whether the stage's rc
contract (design s.7 item 3) needs a third value, or whether the per-feed print is the whole answer.
**I did not decide this; it is named, not resolved.**

### FINDING 2 — the export key's EXTENSION changed `.json` → `.xlsx`, and my reader is unaffected

```
  2026-08-25  ..._exportResultID-282394.json   13,090 B
  2026-08-28  ..._exportResultID-283012.json   13,090 B
  2026-08-29  ..._exportResultID-283068.xlsx   13,090 B   <- extension changed, size identical
```

**Read at source before concluding:** `_list()` (`:144-151`) lists the whole date prefix with **no
extension filter**, and `read_export()` (`:217-240`) asserts on the **ZIP magic bytes** (`blob[:2] !=
b"PK"` → `RawFormatError`) and on `xl/` members — **never on the filename.** So the rename cannot
produce a false zero here.

⚠ **THE INFERENCE I AM MAKING AND ITS LIMIT:** the 08-25 export **did** convert (its silver partition
exists), so that `.json`-named blob must have carried `PK` bytes — i.e. **the old name was wrong and
the new name is honest**, a producer correcting itself. That is an inference from the silver partition
existing, **not** a byte read of the 08-25 object. Cheap to confirm; I did not confirm it.

⛔ **DO NOT read this as "extension changes are safe here."** It is safe for *this* reader because
*this* reader is extension-blind by construction. The gold consumer and any downstream lister were not
checked.

---

## What Happened

1. **`/watcher`** — `~R` was NOT REGISTERED with no watcher of its own. Registered (PID 32724), armed
   the persistent Monitor (`bs4guvst1`, `TaskOutput` → running). Three `inbox-watch.sh` processes
   matched the BASE serial (`~C`, `~V`, `~N`) — **other live lanes, left alone.**
2. **`org/XXX.md` startup** — A.1 serial file written; A.2 returned the **two known** findings
   (`UNCOVERED-AUDIT-LOG`, `STALE-BASELINE`) which XXX.md says explicitly not to re-file; A.3
   `105 of 105` resolve bare **and a forwarder actually RAN** (the exercise arm, not just resolution).
3. **Read the TO and both COO messages**, acked `83812` + `83850` on the READ clock.
4. **The census above.**
5. **Stopped on 83938.**

## Decisions Made

- **Did not start step 0 (the runner-substrate measurement).** It is the first act of the BUILD per
  `2.0.0_SA_COO` 78473, and the wind-down says start nothing new. **Deciding mint-3-files vs mint-0
  half-measured is worse than not measuring at all** — both branches look identical from the prefix.
- **Did not touch `conversion_manifest.py` or `schwab_runtime.py`**, both dirty in the shared worktree
  with `OPAL_ADVIPOINTERS.P2F-MARKER-DS` work. **Not my lane.** Every command this session was
  path-scoped so they could not be swept into my commit.
- **Did not convert the 08-29 partition.** It would be an ad-hoc QA artifact, and per the design s.0
  a QA partition **is not production evidence** — the whole point of the stage is that the daily plane
  is scheduled. Converting now would also put a manifest-bearing partition beside three
  manifest-less ones, complicating the backfill the build is supposed to open with.

## ⛔ FIRST ACT FOR THE SUCCESSOR — concretely

1. **Step 0, the MEASUREMENT** (`2.0.0_SA_COO` 78473): does the 49F chain execute this producer **from
   `s3://opal-data-mdpf/code/scripts/silver/`** or **from a checkout/package?**
   → S3 ⇒ mint `raw_json_reader.py` + `silver_registry.py` FIRST, then the producer (**3 files**).
   → checkout ⇒ **mint 0 files**; minting would create a deployed copy nothing executes.
   **This is the AE lane's to state.** Do not mint before it is stated.
2. **Then the backfill + byte-compare** on the three manifest-less silver partitions
   (`SKIP-UNVERIFIABLE-NO-MANIFEST` is the current, correct default): sha256 each parquet before and
   after, **normalisation stated**, identical ⇒ backfill with confidence, different ⇒ **a FINDING
   reported before the new parquet is accepted.**
3. **Then the stage runner** (design s.7): `--dry-run/--upload`, date from the trading-calendar
   frontier (**never assumed T-1**; the bronze key is the vendor's *pull* date), rc contract stated.

**Open gates:** AC4 = sovereign publisher gate, `0.7.0_AE_CloudOps~K` (**not ours, do not re-ask**).
`relationshipdetail`'s 08-29 absence = `0.6.0_AE_PartnerETL`. Cohort coverage on that feed
(1 relationship of 77) = **still open, still the AE lane's**, per design s.8.

## Compiler Tools

`comp-find` (located the TO — 227 hits / 130,495 files scanned, `corpus=all`, bands printed; the TO
lives in the **BASE** folder, not the lane's, which is exactly the trap XXX.md warns about).
`comp-which` run as A.3's mandatory **exercise** arm. `to-check.py --all` run on the base serial per
the XXX.md fallback — it returned only `[complete]` rows for this base and **did not surface this
live P0**, the measured lane-invisibility class, so **the dispatch message remained the authority on
what I hold.**

## Push State

**LOCAL — not pushed, by instruction.** `0.0.0_AB_MSTR` 83938 reserves publication to the final
integration window. Measured with `git status --porcelain` over my three path scopes: **empty.**
