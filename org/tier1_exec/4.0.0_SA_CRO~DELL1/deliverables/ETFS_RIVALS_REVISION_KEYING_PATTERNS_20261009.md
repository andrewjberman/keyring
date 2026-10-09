# ETFS_RIVALS -- how canonical_shape keys a revision, and the patterns for code-aware revisions (round-29 design fork)

- **Author:** `4.0.0_SA_CRO~DELL1`, 2026-10-09 ~08:3xZ. **Asked by:** `1.0.0_SA_CTO~DELL1` msg 2097.
- **Context:** `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md`
  ADDENDUM 3. Row D1-S6 (@570d152eda) ruled (a), a one-time scoped rebuild. (c), forward-only, is refused. (b), the
  code version joining the digest, is left to round 29 on this research.
- **Code read at:** HEAD `f980747a55` (box/dell1). **S3 read at:** 2026-10-09T08:21Z.

---

## 1. The mechanism, measured

**1.1 The key.** `data/etfs/scripts/rivalfunds/gold_canonical_shape.py:418-420` `_revision_digest`: sha256 of the
sorted `fund:source:capture_id` set, plus the G4 revision when one is read. `:423-435` `_revision_of` names the
revision `<greatest input capture time>-<digest[:12]>`. `:939-940` folds the issuer aliases into the digest when
present. **No term in the key depends on the code.**

**1.2 The skip.** `:944-955`: the stage lists the date's existing objects. `same` is the set holding the new
revision's name, the legacy name, and any object with the same digest and the same capture time. `hit` is the first
existing object in `same`, and on a hit it records `"this revision is already gold: a replay adds nothing"` and
continues. A replay of the same inputs at new code therefore writes nothing. D1-S6's real run read `written_new 0`
over 16 report dates (row D1-S6, `INVESTIGATION_v1.dell1.md:275`).

**1.3 The ordering.** `revision.py:115-118` `newest` orders by capture time, then by build sequence
(`with_build_sequence`, `:129-135`, `<ts16>-b<NN>-<sha12>`). A hash identifies and never orders. A forced rebuild at
one capture time is therefore served as the newer object, with no delete. That is what makes ruling (a)'s rollback
(the prior revision re-served) cheap.

**1.4 The store and its readers.** Store: `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<d>/`
(`homes.py:57-58`). Readers: `gold_trade_schedule` (G5, by marker outputs), `tools/g5_drift.py:184`,
`tools/g5_code_replay.py:108`, `publish_page._by_date` (`tests/test_v2_revision_contract.py:133`). All of them pick
the newest object.

**1.5 Counts.** Stored revision objects: **1,368 parquet objects over 507 report dates (2024-09-30..2026-10-07);
331 dates hold more than one revision** (`aws s3 ls --recursive` of the prefix, 08:21Z). The number of (fund, capture)
pairs whose claimed date differs from delivery is **NOT MEASURED here**: ruling (a)'s dry run, in progress, prints it.
The only figure on record is CGIC 10-02..10-08 (ADDENDUM 3).

---

## 2. The patterns

### (a) A semantic rule-version, bumped by hand, in the reuse decision

**How:** a constant in the stage (`CANON_VERSION = "gold_canonical_shape/N"`) is stamped into every object, and the
skip at `:944-955` reuses an existing object only when its stamped version equals the running code's. A new version
writes the next build-sequence revision.

**The estate already does this, one stage downstream.** G5: `gold_trade_schedule.py:136-138` `INFER_VERSION =
"gold_trade_schedule/4"`, `GOLD_VERSION`, stamped as parquet metadata `producer_version`. `:892-904` `_g5_target`
reuses the newest object only on the same held funds **and** the same `producer_version`; otherwise it writes
`-v<NN>`. This landed as RIV-gt-1 @33d93f7b86 (2026-10-05), and `tests/test_r11gt1_new_code_new_revision.py` pins it.
`producer_version` is also carried by `gold_peer_group_map.py:33`, `gold_holding_contribution.py:62`,
`gold_flow_reconciliation.py:28` and others: 10 non-test rivalfunds modules carry a version term (Grep over `producer_version|RULE_VERSION|code_hash|...`, 08:2xZ). **canonical_shape is the
exception in its own pipeline.**

**Cost:** one constant, one metadata key, one comparison. Daily mode re-derives only the date it runs on, so a bump
moves no history by itself. History moves only on a deliberate replay. Served churn per bump is limited to dates that
are rebuilt.

**Does NOT fix:**
- A forgotten bump. Measured: RIV-rg-1 @32f3f1943f (2026-10-07) changed what G5 reads (G4 as the union of every
  object of a date, not the newest) with no `INFER_VERSION` change. The bumps are only @1f94c90c4f (/3) and
  @bcc09bb9b1 (/4). Whether rg-1 moved any served G5 row is not measured.
- History. Old dates stay at their old version until replayed.

### (b) A code hash in the key

**How:** a hash of the transform's source, or of its build input, joins `_revision_digest`.

**Cost:** high. Every change re-keys, including whitespace, comments, refactors and changes to unrelated functions in
the same module. Any replay or backfill then writes a new revision for every date it touches, and each re-serve is a
served-output move that needs a never-widen sign-off naming its blast radius. The estate knows the churn trap from
the Lambda side: `infra/aws/terraform/harvest/lambda_src/build_zip.py:57,66` builds deterministic zips so that
`source_code_hash` does not force a spurious redeploy, and `.tools/drift_producer.py:252-259` compares
`source_code_hash` to tell a real code change from a version-id change.

**Does NOT fix:** history (same as (a)). It also gives no meaning: a hash says that code changed, not whether the
answer changed.

**Estate use for data revisions:** none found.

### (c) The key stays the input digest; version is metadata; a deliberate rebuild re-derives

**How:** today's key, plus a stamped `producer_version` that the skip does NOT read. A separate, deliberate act
("rebuild where version < N, for these funds") re-derives under its own pair.

**Cost:** the cheapest serving. Nothing moves until a person decides.

**Does NOT fix:** silence. Every fix stays forward-only by default, which is exactly D1-S6. It only makes the stale
objects findable by their version.

**Estate prior art for the rebuild act:** `tools/g5_code_replay.py` (RIV-rp-2) plans and dry-runs a replay of named
code classes into a LOCAL sink, never writes S3, and leaves the served replay to the issuer under its pair.
`tools/g5_drift.py` (RIV-gd-1) classifies live-vs-current-code drift, and `rebuild_funds` (RIV-nf-1 @0587516397)
scopes a rebuild to named funds. Ruling (a) for D1-S6 is this pattern applied once.

### (d) Other patterns found

- **Drift classification on demand** (`g5_drift.py`): the live object vs a current-code build, each differing row
  placed in one cause class. It is a READ run on demand. It must stay on demand: run as a standing comparator it
  would breach the "no standing parity comparator" veto.
- **Input manifest per object** (`gold_peer_group_map.py:12,57`: `input_manifest` naming inputs and sha256): this is
  lineage, not code-awareness.

---

## 3. How each interacts with the standing law

- **Never-widen (moving served output needs a sign-off naming its blast radius):**
  - (a) and (c) move served output only on a run that rebuilds a date, so the pair names the dates and funds.
  - (b) turns ordinary replays into served moves on every code change, so the pair cannot be scoped in advance.
- **No shadow pipeline and no standing parity comparator:** all four comply when replay and drift are run on demand
  into local sinks, as `g5_code_replay.py` does. None needs a second served path.

---

## 4. Recommendation (labelled: a recommendation, not a ruling)

**Adopt (a), as G5 already does it, and keep (c)'s deliberate scoped rebuild as the only way history moves.**

1. canonical_shape stamps `producer_version` (a hand-bumped `CANON_VERSION`, starting at the version that carries
   RIV-we-1) and the skip at `:944-955` adds "same version" to `hit`, mirroring `_g5_target`.
2. Daily runs then pick up a fix on new dates without a forced replay. History moves only through a
   `g5_code_replay`-style plan and dry run, then a served act under its own pair, scoped by `rebuild_funds`.
3. Reject (b). It churns served output on every edit and carries no meaning.

**Cost, named:**
- A forgotten bump reproduces D1-S6. This has already happened once in G5 (rg-1, above). Partial mitigation, within
  the no-new-gates rule: each stage's version test (as `test_r11gt1`) asserts that a fixture's output equals a pinned
  golden output. A semantic change then fails the test until someone updates the golden and, by the same edit, is
  reminded to bump. This is a test, not a gate; proposing a commit-time gate would need Andrew's word.
- One build-sequence revision per rebuilt date, and the dry-run compute per replay.

**What a round-29 cell would carry** (three mechanical criteria at most):
1. canonical_shape writes `producer_version`. A same-input pass at the same version writes nothing; at a new version it
   writes `b<NN>` (pattern: `test_r11gt1_new_code_new_revision.py`).
2. An object without `producer_version` reads as an older version, so the first post-deploy rebuild of a date is
   explicit. It is never triggered by a daily run on that date's inputs alone, because daily mode runs only today.
   Confirm this in the cell.
3. The golden-output test for canonical_shape.

**Not decided here:** whether to back-stamp the 1,368 stored objects (REC no: an absent stamp already reads as
"older").

## 5. What this note did not measure

- The D1-S6 differing-pair count (the dry run prints it).
- Whether rg-1 moved served G5 rows.
- Readers of canonical_shape outside `data/etfs/scripts/rivalfunds/` (the search was scoped to that package and its
  tools).
- The served-object version spread of G5 (no metadata read was run).
