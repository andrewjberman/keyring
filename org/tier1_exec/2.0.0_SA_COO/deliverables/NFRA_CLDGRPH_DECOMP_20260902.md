# NFRA_CLDGRPH -- step-5 atom-decomp (COO)

**Author:** `2.0.0_SA_COO` · 2026-09-02 · **Step 5 of the canonical loop. NO TO IS CUT.**
**PRD:** `docs/architecture/NFRA_CLDGRPH_PRD.md` v0.1 @`52d14feb79` (`1.0.0_SA_CTO~A`), rulings R1-R12.
**Register:** `org/projects/NFRA_CLDGRPH.json` (D0, `dep_stage: PRD`) + `DIRECTIVES.yaml` D0 @`c778e3c3d1`.

⛔ **STEP 6 IS SHUT AND THIS DECOMP DOES NOT OPEN IT.** Two independent holds: `comp-adversary`
effective admission is **RC5 PARTIAL** (`3.0.0_SA_CVO~A` @`47f1045c7f` -- the battery runs during
import, so `collect-only` takes 111.95-135.14 s and dies silently under a 90 s ceiling; the planted
production mutant limb is open), and **this project has no `fabric` key**, so L3 refuses every TO
against it. Both are named in s.5. **Rows below are DECOMP CELLS, not task orders.**

⚠ **THIS DECOMP BUILT ITS OWN SURFACE MANIFEST, WHICH THE STEP-4 CONTRACT EXISTS TO PREVENT.**
`_PRD_TEMPLATE.md` carries no manifest section (0 hits / 140 lines / 26 sections), so the PRD arrived
without addresses and step 5 opened with discovery. **That is a carrier gap, not an authoring fault
at `1.0.0_SA_CTO~A`** -- surfaced at 92697/92698/92699, not blocked on.

---

## 1. The rectangle

**Domain (postulate i):** the PRD s.3 **OWNS** cell, six items. Every OWNS item has >=1 row; every row
maps to an OWNS item. RELIES-ON appears only as `depends_on`; out-of-scope only as `bound`.

```
  OWNS item                                     rows
  where it is COMPILED (worker + trigger)       S1, S2
  where it is SERVED FROM (plane + contract)    S3, S4
  how an agent REACHES it (gateway + client)    S5, S6
  the vintage bound + plain-words rendering     S6 (render), S3 (the bound)
  the operator status read                      S7
  the RETIREMENT of the local copy              S8
  DENOMINATOR: 6 of 6 OWNS items covered, 0 uncovered.
  S9-S12 are INPUTS the PRD's own "Open for the decomp" list names -- verify/measure rows, not work.
```

| id | outcome | surface | claim | evidence | lane | verb | depends_on | acc | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-2 | S3 event notification on `warehouse/_branch_head.main.json` -> SQS + DLQ | **absent** | comp-trigger: NO MATCH; lens BLIND on S3-notification triggers by its own disclosure | AE_CloudOps | wire | S12 | A2 | **R5: the marker write is the commit point.** NOT the CloudTrail queue (one writer of five), NOT a cron. item2b pattern |
| S2 | FWD-2, FWD-4 | worker running the existing incremental engine -- `infra/aws/globgrph/kuzu_incremental_refresh.py` | measured | 350 lines @`aebe0d0a67` | AE_CloudOps | port | S1, S10 | A2, A4 | **KUZUSPLIT O-1 (serve-labeled-stale, never full) survives as WORKER-INTERNAL** (R9). Runtime Lambda-vs-ECS is decided by S10, never by the document |
| S3 | FWD-3, FWD-7 | versioned artifact + `_build_manifest` + ONE pointer object on S3 | **absent** | contract not yet written; PRD names it as open | AE_CloudOps | wire | S2 | A3, A7 | **artifact-first, pointer-last** -- the projection can never run ahead of Nessie. Pointer atomicity is an open input (S11) |
| S4 | FWD-1, FWD-5, FWD-7 | small always-on service on the existing `opal-globgrph` ECS cluster | **absent** | cluster ACTIVE, 2 services / 3 tasks (CRO brief, attributed) | AE_CloudOps | wire | S3, S11, S12 | A1, A5, A7 | **R3: scoped exception to GLOBGRPH s.0 serverless-light**, same footing as Nessie warm. Cost delta -> NFRA line. **The gateway is NEVER the host** |
| S5 | FWD-1, FWD-5 | gateway traversal registered via `IntegrationSpec` (existing framework) | **absent** | framework proven by 2 live integrations (opal_portal, ycharts) | AE_CloudOps | wire | S4, S13 | A1, A5 | **The framework is NOT modified** -- a new integration through its 5-step checklist. Gateway `i-07dccb1615503ac99` t4g.nano, `--workers 1` MANDATORY: thin proxy only |
| S6 | FWD-3, FWD-6 | `.tools/comp-kuzu` becomes a thin client that prints vintage in plain words | measured | 28 lines @`0215abf3ec` | AE_CloudComp | port | S4 | A3, A6 | **FWD-6: no refresh choice may exist where an ordinary user works.** Plain-words rendering is an open input |
| S7 | FWD-8 | operator status read -- repoint `comp-graph status` at the projection pointer's manifest | **absent** | brief F6: it reports on the WRONG artifacts today ("kuzu_db 81d", "stitch_graph 38d") | AE_CloudComp | wire | S3 | A8 | ⛔ **R4: a PULL-style READ. NO alarm, SNS, checker or monitor.** FRESHGUARD alarm legs stay torn down |
| S8 | FWD-7 | RETIREMENT: local `kuzu_nessie_db`; `kuzu_cli.py`; `.tools/comp-kuzu-full`; `.tools/comp-kuzu-inc` | measured | `kuzu_cli.py` 179 @`834c87c00a`; `comp-kuzu-full` 16 + `comp-kuzu-inc` 17 @`7288d12675` | AE_CloudComp | retire | S4, S6 | A7 | ⛔ **R7: PORT WITH A RETIREMENT.** Indefinite coexistence IS the duplicate output path CLAUDE.md s.5 forbids. Fires when FWD-7 reads EXERCISED -- not before, not never |
| S9 | A9 | `kuzu_nessie_load.py` node/edge key asymmetry | measured | 417 lines @`e445642c5f`; substrate card @`5da9e7fffc` verdict QUALIFIED, defect at `:150` vs `:184` | AE_CloudOps | fix-at-port | S2 | A9 | **R10: FIXED AT THE PORT, not carried.** The port is the moment; a ported defect is a defect shipped twice |
| S10 | -- | **the full-fallback duration of the projection** (KUZUSPLIT P0-INSTRUMENT) | **unmeasured** | PRD names it the first measurement owed | AE_CloudOps | measure | -- | -- | ⛔ **SIZES S2.** Four figures from three sources exist for two different operations and CRO deliberately refused to reconcile them. **Do not pick one -- measure** |
| S11 | -- | gateway -> serving-service network reachability (VPC / subnet / SG) | **absent** | brief Part V item 5: UNMEASURED | AE_CloudOps | verify | -- | -- | If unreachable, S5's whole shape changes. Verify BEFORE S4 is built, not after |
| S12 | -- | IAM for the worker and the serving service | **unmeasured** | -- | AE_CloudOps | verify | -- | -- | ⛔ **comp-iam CANNOT answer "is this denied?"** -- silence from it is not "allowed" |
| S13 | -- | which existing `AuthKind` an agent traversal fits | **unmeasured** | brief Part V item 4 | AE_CloudOps | verify | -- | -- | An answer here is a precondition for S5, not a detail of it |

---

## 2. The arc as an ordering, and what each stage unlocks

```
  S10 + S11 + S12 + S13   MEASURE FIRST -- none is work, each decides a shape
        |                 S10 sizes the worker; S11 can invalidate S5's design
        v
  STAGE 1  S1 -> S2 -> S9 -> S3      the projection becomes a CONSUMER of the marker
        |                            unlocks: an artifact exists to serve
        v
  STAGE 2  S4 -> S5 -> S6            the serving plane + the reach
        |                            unlocks: FWD-7 becomes EXERCISABLE
        v
  STAGE 3  S7, then S8               the status read, then THE RETIREMENT
                                     S8 IS LAST. It cannot precede a working S4/S6
```

⛔ **THE ONE ORDERING THAT IS A RULING, NOT A PREFERENCE (R7):** S8 fires when FWD-7 reads
EXERCISED. **Retiring early breaks the estate's only graph; retiring never is the shadow-pipeline
violation.** The decomp names the cell; it does not get to choose "later".

⭐ **AND S9 SITS INSIDE STAGE 1 DELIBERATELY.** R10 says the key asymmetry is fixed AT THE PORT. If
S9 slips behind S2 it becomes a defect that shipped twice and then needs its own remediation --
which is the shape the substrate card already flagged as QUALIFIED.

---

## 3. `<preflight>` -- PROVISIONAL, and stated as such

⛔ **NOT A STEP-6 PREFLIGHT.** Step 6 is shut on two independent holds (s.5), so this block cannot
be submitted with a TO and is recorded as decomp evidence only. `comp-adversary` is deliberately
absent: its effective admission is RC5 PARTIAL, and per `3.0.0_SA_CVO~A` @`af981709a1` a held
admission has NO truthful legal disposition -- neither RUN nor DECLARED-NOT-APPLICABLE.

```
<preflight>
comp-trigger: RUN -- 140 events-rules + 18 schedules scanned, us-east-1; NO MATCH for kuzu.
  BLIND BY THE LENS'S OWN DISCLOSURE on S3-notification triggers, and R5's trigger IS an S3 event
  notification -- so S1 is UNRESOLVED by this instrument and needs a different one.
comp-read --enumerate: RUN -- retirement + port surfaces resolved with dated pins:
  kuzu_incremental_refresh.py 350 @aebe0d0a67 · kuzu_nessie_load.py 417 @e445642c5f ·
  kuzu_cli.py 179 @834c87c00a · comp-kuzu 28 @0215abf3ec ·
  comp-kuzu-full 16 / comp-kuzu-inc 17 @7288d12675
comp-blast · comp-dataflow · comp-iam · comp-pipescript · comp-denytest: NOT RUN -- deferred to the
  step-6 preflight, which cannot be composed while step 6 is shut.
comp-similar: ADMITTED @0d272d257c. NOT CITED -- b8a73cc064 is LOCAL, so the vintage line must be
  confirmed to RENDER before any number from it is used.
</preflight>
```

---

## 4. What this decomp REFUSES to assume

- **S10 is unmeasured and I did not estimate it.** Four figures from three sources exist for two
  different operations; `4.0.0_SA_CRO` refused to reconcile them because picking one manufactures a
  measurement. That refusal is inherited here.
- **The `opal-globgrph` cluster state is CARRIED from the CRO brief, ATTRIBUTED, not re-measured** --
  agreement is not corroboration when one artifact inherited the claim.
- **S11 is `absent`, not `unmeasured`.** Nobody has established reachability, and a `verify` row
  before S4 is the difference between finding that out now and finding it out mid-build.
- **No IAM change is proposed**, so `comp-denytest` has no population -- a truthful non-application
  at the subject grain, not a skipped lens.

## 5. The two holds, and neither is mine

1. **`comp-adversary` admission -- RC5 PARTIAL** (`3.0.0_SA_CVO~A` @`47f1045c7f`). Fabric-wide; owned
   by `0.8.0_AE_CloudComp` + `3.0.0_SA_CVO` under `NFRA_COMPEFFICACY`.
2. **`NFRA_CLDGRPH` declares NO `fabric`.** L3 (`to-pipeline-gate.py`) refuses every TO against it.
   The PRD records placement LAPTOP and D0 is a named laptop hold -- but **placement on the directive
   is not the `fabric` key on the project row**, and the gate reads the key. Andrew's review, per his
   2026-09-02 ruling that unfabricked projects are held deliberately. **This seat does not set it.**

**When both clear, S10-S13 are the first TOs** -- measurement before build, because two of them can
change what gets built.
