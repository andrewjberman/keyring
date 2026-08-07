# MDPF R-20 — sidecar / one-off-patch READER CENSUS + deletion proposals

**Author:** 3.0.0_SA_CVO. **TO:** `MDPF_REMED.W1-3` @ef7b320786 (2.0.0_SA_COO, GO 192940Z).
**PRD:** `docs/architecture/MDPF_REMEDIATION_REGISTER.md` §2g. **Date:** 2026-08-07.
**archetype:** VALIDATE

> ⛔ **THIS DOCUMENT PROPOSES. IT DELETES NOTHING.** S3 deletion is human-confirmation and happens
> only with Andrew's word attached to a specific object. `R-13`'s underscore twins are the precedent
> that RULED != EXECUTED.
> ⛔ **`pipeline-complete.json` is HELD-NOT-PROPOSED** — COO staged it on AE's `W1-2` (retire
> `_check_inf_spine` FIRST, then propose the object). It is censused below read-only; **its presence
> in this document is not a proposal.**

---

## 1. VERDICT TABLE

| # | object | shape | verdict |
|---|---|---|---|
| 1 | `opal-data-inf/gold/meta/pipeline-complete.json` | SIDECAR STATE OBJECT | **HELD-NOT-PROPOSED** |
| 2 | `opal-data-inf/gold/eclipse/_meta/dispatch_eclipse_status.json` | *(unclassifiable — see §3)* | **RETIRE THE WRITER, not the object** |
| 3 | `opal-data-assets/gold/mdpf_revamp/meta/cycle-complete.json` | *(unclassifiable — see §3)* | **RETIRE THE WRITER, not the object** |
| 4 | `.../_audit/legacy_account-distribution_pre-w6_20260723.json` | ONE-OFF PATCH ARTIFACT | ⛔ **TRASH — propose deletion** |
| 5 | `.../_audit/legacy_aum-timeseries_pre-a2_20260723.json` | ONE-OFF PATCH ARTIFACT | ⛔ **TRASH — propose deletion** |
| 6 | `.../global/non_model_assets_precutover_frozen.json` | **MISCLASSIFIED** | ✅ **KEEP — RECLASSIFY (deletion would be irreversible)** |
| 7 | `.../cottonwood/aggregate_aua_timeseries_interpolated.json` | sanctioned backfill | ✅ **KEEP — carve-out CONFIRMED at source** |
| 8 | `opal-data-mdpf/telemetry/…` (181) · `cache/` (1) · `bmkaud-evidence/` (10) | bulk | **AE's half — measured, not proposed** |

---

## 2. PER-OBJECT

### 6. `non_model_assets_precutover_frozen.json` — ⚠ THE HEADLINE. KEEP.

Register §2g lists it **TRASH** (ONE-OFF PATCH ARTIFACT). **It is a live read on the default build
path.** `data/mdpf/scripts/gold/dim_mdpf_non_model_assets.py` (493 lines):

- `:95-96` key + URI defined
- `:450` `ap.add_argument("--precutover-uri", default=FROZEN_PRECUTOVER_URI, …)` — **defaults to it**
- `:476` `doc = build(args.global_uri, args.inflection_uri, args.precutover_uri, args.cutover)`

A bare invocation reads that key. Docstring `:88-94`, verbatim: the pre-cutover history *"is NOT
monolith-derivable — parity requires it VERBATIM… now snapshotted ONCE to this revamp-native
opal-data-assets key… and read from HERE — so A4 is revamp-native with ZERO legacy dependency."*

**Deleting it breaks A4 on every build AND destroys history not derivable from the monolith.**

⛔ **AND ITS RECOVERY PATH IS ON ANOTHER TEARDOWN ROW.** `--snapshot-precutover` (`:473`) re-captures
from the **portal-v2 served artifact**, so recovery (a) re-introduces the exact legacy coupling A4
DECOUPLE removed, and (b) works only while `json/mdpf/*` survives — **and that teardown is PARKED but
live in this same program.** Delete this object *and* tear down `json/mdpf/*` and the pre-cutover
history is **unrecoverable**. Two individually-defensible steps, jointly irreversible; **neither row
names the other.**

**Why the classification went wrong — and it vindicates the discriminator rather than indicting it:**
the object genuinely *was* migration residue. **A4 DECOUPLE PROMOTED IT INTO A PERMANENT INPUT AND
ITS NAME DID NOT CHANGE.** Classify by filename → deleted. Apply *"a manifest read as a gate has
become a sentinel; THAT is the test, NOT THE FILENAME"* → survives. This is the register author's own
stated fear (*"or this ruling deletes something the contract requires"*) as a **second measured
instance**, beyond the carve-out he already caught.

**Denominator:** `comp-find 'non_model_assets_precutover_frozen'` = **18 hits / 24,877 files scanned,
1 UNREADABLE**; bands DEF=1 SURFACED=1 CONFIG=1 DOC=15. This is a **PRESENCE** verdict — one confirmed
reader refutes "nothing reads it", and unlike an absence it does not require exhaustiveness.

### 7. `aggregate_aua_timeseries_interpolated.json` — KEEP. Carve-out now SOURCE-CONFIRMED.

Accepted on the register's say-so; now verified. `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`:
`:107` key, `:698` `"source_key"`, **`:789` `s3.get_object(Bucket=ASSETS_BUCKET, Key=ONEOFF_BACKFILL_KEY)`**,
`:791` loud `ERROR: COTTONWOOD BACKFILL ABSENT … unreadable`. A hard dependency that fails loudly.
Also written by `build_cottonwood_interpolated_backfill.py:88`. The carve-out is correct.

### 4 & 5. `_audit/legacy_*` — ⛔ TRASH. Absence SHOWN, not asserted.

Both exist: `legacy_account-distribution_pre-w6_20260723.json` **7,720B** and
`legacy_aum-timeseries_pre-a2_20260723.json` **362,225B**, both 2026-07-23. `_audit/` holds
**exactly 2 objects** — these two, nothing else.

**Zero code readers, on two independent axes:**

1. **Literal name.** `comp-find` = **3 hits / 24,877** and **4 hits / 24,877** — **bands DOC only**
   (register + `MDPF_DEBTCLEAN_PRD.md` + two DS logs). Zero SURFACED, zero DEF, zero CONFIG.
2. **Prefix listing** — *the axis a basename scan structurally cannot see.* `comp-find 'mdpf_revamp/_audit'`
   = 5 hits / 24,877, **all DOC**. `comp-find '_audit/' data/` = 2 hits / 957, and the single SURFACED
   hit (`mdpf_aggregate_aua.py:70`) is a **comment about naming convention**, not a reader.

**⛔ WHAT I COULD NOT SEE** (criterion 4): deployed-but-uncommitted Lambda/EC2 code; untracked working-tree
files; another device's tree; a consumer building the key by runtime concatenation of variables (a
literal scan cannot resolve that); anything outside the 24,877-file scope, incl. the 1 UNREADABLE file.
**The proposal is sound against everything I could scan and no further.**

### 1. `pipeline-complete.json` — HELD-NOT-PROPOSED (census only)

SIDECAR STATE OBJECT: mutable, singular, **read as a gate** by `_check_inf_spine` (the reader AE's
`W1-2` retires). Written by `orion-gold-dispatch.sh`'s dispatcher.

**Same-week evidence of the class failing in BOTH directions** — measured today during the INF verify:

- **FALSE-STALE:** read `run_date: 2026-07-31` for eight days while data advanced — a *true reading of
  a stale description* (COO re-verified the marker at that date).
- **TRUE-BUT-UNINFORMATIVE:** today the chain ran, wrote both owed `canonical_performance` dates, then
  failed at `INF_C_01`; the dispatcher correctly did **not** advance the sentinel. So it now says "no
  complete run" — accurate — **while five dates of served NNA sit zeroed behind it.** A reader
  concluding "nothing moved" would be wrong.

**A description outside the state can be wrong when the data is fine AND right when the data is broken.**
That is the register's thesis with a measured instance of each limb inside one week.

### 8. `opal-data-mdpf/` bulk — measured, AE's half

`telemetry/mdpf-daily-runner/` **181** objects (register said 180) · `cache/` **1** · `bmkaud-evidence/`
**10**. Bucket also holds `code/` and `mdpf/`. Disposition sits with AE's detachment work
(`docs/briefs/opal-data-mdpf-bucket-retirement-20260807.md`); **I measured, I do not propose here.**

---

## 3. ⚠ STRUCTURAL FINDING — THE FOUR-SHAPE TABLE IS NOT MECE, AND TWO OBJECTS FALL THROUGH IT

Objects **2** (`dispatch_eclipse_status.json`) and **3** (`cycle-complete.json`) are **mutable,
singular, and have ZERO readers**. They fit **neither** shape:

- **not** SIDECAR STATE OBJECT — that shape requires *"read as a gate"*, and **nothing branches on
  them**. `mdpf_portal_publisher.tf:181` says of `cycle-complete.json` explicitly: *"may become an
  ACCELERATOR later; **it is never the gate**."*
- **not** IMMUTABLE RUN MANIFEST — that shape requires *append-only*, and both are **overwritten every
  run**, singular keys.

Under **CLAUDE.md Rule 24 postulate (i) MECE**, a classification schema whose values are not
collectively exhaustive is a **defect, not a style choice** — and this one is being used to authorize
deletions. **Proposed missing shape: WRITE-ONLY STATUS BLOB** — mutable, singular, zero readers,
regenerated every run.

>> **AND ITS DISPOSITION IS DIFFERENT FROM BOTH EXISTING VERDICTS, WHICH IS WHY THE GAP MATTERS:**
> **DELETING A REGENERATED OBJECT IS A NO-OP — IT COMES BACK ON THE NEXT RUN.** For this shape the
> question is never *"delete the object?"* but **"retire the WRITER?"**. A register row that says
> TRASH against a regenerated object will read as executed, and then quietly fail on the next cycle.
> This is the same shape as R-20's own ordering constraint on `pipeline-complete.json` (retire the
> reader before deleting the object) — one step further: **for a regenerated object you must retire
> the PRODUCER, or deletion is theatre.**

**Evidence:** `dispatch_eclipse_status.json` — `comp-find` 15 hits / 24,877, SURFACED=3 and **all three
are the writer** (`orion-gold-dispatch.sh:1990` comment, `:2020` the `aws s3 cp` write, `:2022` echo).
`cycle-complete.json` — 115 hits / 24,877; every SURFACED hit is a writer or a comment
(`mdpf-daily-dispatch.sh:655` write; `iam.tf:409/:471`; `mdpf_portal_publisher.tf:181`).

⚠ **`opal-data-inf/*` is INF's tree, not MDPF's** — object 2's disposition is a **proposal to its
owner**, never a plan.

---

## 4. INCIDENTAL — TWO STALE RECORDS FOUND WHILE CENSUSING (not edited by me)

1. **`infra/aws/terraform/mdpf-pipeline/iam.tf:471`** asserts *"meta/cycle-complete.json has NEVER
   been emitted and everything gated on that."* **FALSE as of today** — the object exists, **801 B,
   written 2026-08-05T13:36:17Z**. A live TF comment stating a non-existence that ended two days ago.
2. **R-13's underscore twins** — the register row calls them outstanding; they were **executed
   @46d3bf3f32** (COO caught this while decomposing). Flagged, not edited: the register is not my file.

---

## 5. COMPILER TOOLS

| tool | call | result |
|---|---|---|
| `comp-find` | `dispatch_eclipse_status` | 15 hits / 24,877 files, 1 UNREADABLE — SURFACED=3, all writer |
| `comp-find` | `cycle-complete` | 115 hits / 24,877 — SURFACED=53, no reader among them |
| `comp-find` | `non_model_assets_precutover_frozen` | 18 hits / 24,877 — DEF=1 (the live reader) |
| `comp-find` | `aggregate_aua_timeseries_interpolated` | 24 hits / 24,877 — DEF=2 (writer + reader) |
| `comp-find` | `legacy_account-distribution_pre-w6` | 3 hits / 24,877 — **DOC only** |
| `comp-find` | `legacy_aum-timeseries_pre-a2` | 4 hits / 24,877 — **DOC only** |
| `comp-find` | `mdpf_revamp/_audit` · `_audit/ data/` | 5 / 24,877 (DOC only) · 2 / 957 — prefix-listing axis |
| `aws s3 ls` / `head-object` | live existence + sizes | all objects confirmed present |

**Denominator hazard carried, per the 162256Z broadcast:** `comp-find` counts **LINES, not AST nodes** —
no count above is quoted frameless, and none is used as a structural total.

-- 3.0.0_SA_CVO
