# ADVI_INSURE TO-R1-DS — step 0 MEASURED, and the stage entry built in the shape it found

**archetype:** MEASUREMENT + BUILD
**Seat:** `0.4.0_DS_ClientPlatform~R` · **Window:** 2026-08-30 00:56–02:10Z · **Predecessor log:**
`2026-08-29/session_2053-2135Z_reseat_and_first_fire_census.md`
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (PRD s.3, Andrew ~16:1xZ).

---

## Current State

**Step 0 is answered and the stage entry point is built, tested and committed. The MINT is gated —
correctly — on two other seats.** Two commits, both **on origin `@233da08b7f`** (is-ancestor, read
02:09:04Z — see Push State; they were LOCAL when this section was first drafted):

| commit | what |
|---|---|
| `d2201132d5` | design **s.7.2** — the step-0 measurement |
| `85abccfd68` | the **stage entry point** + battery, and a withdrawal of a false clause in my own s.8 |

⛔ **THE HEADLINE: THE SUBSTRATE IS A VENDORED LAMBDA PACKAGE, SO THE MINT IS 0 FILES — AND THE
PREFIX s.7.1 MEASURED IS ONE THIS PRODUCER'S CHAIN NEVER READS.**

```
  opal-assets-silver-blackdiamond/BUILD_MANIFEST.json -- 8 modules, FLAT at zip root
     raw_json_reader.py   PRESENT     <- the producer's :113 import
     silver_registry.py   PRESENT     <- the producer's :114 import
     bd49f_insurance_conversion.py    ABSENT (denominator 8)
  ...and the package reads NO S3 code prefix at run time.
```

**Three candidate substrates, measured, implying opposite mints** — full table and citations in
design s.7.2 `@d2201132d5`. The two rejected: the ADVI 49F gold chain syncs
`s3://opal-data-49financial/_code/` (all three files absent, denominator **79** keys, positive
controls `a00_runner.py` and `lib/trading_calendar.py` both present) and `safe-deploy` cannot even
target it from the silver repo home (`file_to_s3_target` EXERCISED, 2 positive + 1 negative control);
`s3://opal-data-mdpf/code/scripts/silver/` (still exactly **2** keys, live) is synced by the
**mdpf-daily-runner**, a chain nothing ties to 49F insurance.

⭐ **s.7.1's own branch-2 sentence predicted this outcome exactly.** What it got wrong was not the
2-of-20 measurement — that number is still correct about its prefix — but the assumption underneath
it: **that the DEPLOY TARGET is the EXECUTION SUBSTRATE.** Both branches did look identical from the
prefix, which is why 78473 put the measurement before the mint.

## What Happened

1. **`/watcher`** — `~R` NOT REGISTERED, no watcher of its own. Registered (PID 24400), Monitor armed
   (`bwl59vi0s`, banner `parent-tied: pid 116018`, `TaskOutput` → running). The two `inbox-watch.sh`
   processes matching the BASE serial were `~N` and `~C` — **live peers, left alone.**
2. **`org/XXX.md` startup** — A.1 written; A.2 returned **exactly the two known** findings XXX.md says
   not to re-file, no third; A.3 `105 of 105` resolve bare **and the exercise arm fired**; D, E done;
   **F: zero crons.** `to-check --all` on the base serial returned only `[complete]` rows — the
   measured lane-invisibility class again, so the TO and the dispatch stayed the authority.
3. **Step 0**, on 78473 (form re-confirmed at 84035 against my predecessor's "the AE lane's to state",
   which was superseded). Recorded as s.7.2, `@d2201132d5`.
4. **84193** ruled: mint HOLDS behind S5/S7; the code does not wait. **Built the stage entry.**
5. **84177** ruled `relationshipdetail` **(b)** — converter branch stays inert, not a gap in the stage.

## The stage entry — and why it is not the shape the design proposed

Design s.7 item 1 proposed a `<stage>_runner.py` CLI matching `a00_runner`, **on the assumption of an
S3-code substrate.** Step 0 refuted the assumption, so the entry is an **EVENT** entry:
`lambda_entry(family, event)` → `Records[]` | `{"mode":"sweep"}` | `{"mode":"convert","date":D}`,
anything else **REFUSES**. The CLI is untouched and stays the QA verb.

**HOST-AGNOSTIC ON PURPOSE:** `family` is carried and validated but **never used to pick a prefix**, so
`0.7.0_AE_CloudOps`'s ruling — 84193's own-family rec, or the blackdiamond family — consumes this code
unchanged.

Four decisions, each at its reason (long form in the commit body):
- **the pull_date comes from the KEY, never the clock** (s.7 item 2) — an off-grammar key RAISES;
- **a refusal RAISES `StageFinding` AFTER every feed has had its chance** — a Lambda has no rc, a dict
  with a FINDING field is a 200, and 200 is indistinguishable downstream from a clean run. The raise
  routes to the DLQ, which `silver.tf` calls the surface where *"an event lambda's silent death becomes
  visible"* and explicitly **NOT an alarm** — the only path the standing moratorium leaves open;
- **the sweep converts bronze dates with NO silver at all** — a silver-without-manifest date is not a
  miss but one of the three the 78473 backfill owns, and sweeping them would raise a finding **every
  day** over a known state, training a reader to ignore the finding that matters;
- **no silent no-op arm exists** anywhere in the entry.

## Verification — and the falsifier was RUN, not declared

`--self-test` → **`PASS (10 idempotence + 18 stage-entry = 28 arms)`**, rc=0.

⛔ **Green on the first run is not evidence.** Baseline measured CLEAN **first** (rc=0, 0 FAIL lines) —
a mutant battery from a failing base means nothing — then **4 mutants on a scratch copy** (the tracked
file was never mutated), each predicting one arm:

| mutant | fired on | failing arms | rc |
|---|---|---|---|
| dedupe removed | "two pages of one date -> ONE convert" | 1 | 0 → 2 |
| `StageFinding` suppressed | "one date rc=1 -> StageFinding RAISED" | 1 | 0 → 2 |
| unknown-feed guard removed | "an UNKNOWN feed ... REFUSES" | 1 | 0 → 2 |
| sweep's silver check removed | "bronze WITH silver is NOT a candidate" | 1 | 0 → 2 |

**4 of 4, each on exactly the predicted arm.**

⚠ **ONE ARM I DID NOT WRITE, NAMED RATHER THAN FAKED.** `unquote_plus` cannot be discriminated by any
arm in this key space — the grammar reads only the feed and date segments and neither can carry an
encodable character in these feeds — so a green arm would prove the arm runs, not the decode.
**UNARMED BY CONSTRUCTION**, said so in the docstring.

**EXERCISED ON REAL BYTES, not fixtures** — a real S3 envelope built from the three keys the 04:35Z
fire actually landed, dry (reads S3, writes nothing): 3 records → 1 date; detailsearch **77 rows ==
attested 77**; export **77 rows / 106 contracts / total_value 51,815,578.87**; `relationshipdetail`
correctly **SKIP** (absent day); receipt correctly **UNCONVERTED**. `STAGE OK`.

## ⛔ A correction to my own committed design

s.8 said *"`comp-validate` does not fail closed."* **FALSE — it returns `rc=1`.** I had recorded *"its
rc through a pipe is 0"*, which is literally true, and **read it as the tool's verdict when it was
`head`'s** — `$?` after a pipe is the LAST command's rc. Re-read unpiped: `comp-validate` **1**,
`comp-pipescript io` **1** in all five trees tried, `postdeps` **2**; positive control
`comp-pipescript io a00_runner --pipeline advi` → **0**.
**Only that clause is withdrawn.** The blindness stands and is still the finding; what I got wrong was
the failure **MODE**, by making the same instrument error one layer down from the thing the section is
about.

## Decisions Made

- **Did not mint anything.** Gated at `0.7.0_AE_CloudOps` (84035/84193) and behind S5/S7 (84193 item 1).
- **Did not run `--backfill-manifest`.** It WRITES to served silver, and I would rather have the
  issuer's word that 78473's window still stands than assume it 36 hours later. **Stated as a block, not
  done quietly.**
- **Did not touch `rebalancer_schemas.py`** — 84193 refused (ii) on lane grounds; another project's
  provenance guard is not this seat's.
- **Did not chase** the `safe_deploy_core.py:355` stale comment (mdpf reads "check-only" while
  `deploy_gated` is `True`) — surfaced to the deploy-rail owner, no behaviour change.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | A.3 mandatory **exercise** arm | a forwarder RAN (own banner) |
| `comp-find` | `code/scripts/silver`, `chain_49f_entrypoint`, `gold/advi/_logs`, `--name` × 2, **`--corpus aws`** | denominators printed each run; the aws plane self-declared **29h STALE** and was recorded, not leaned on |
| `comp-keys` | 5 prefixes, `--all` | the 79-key `_code/` denominator, the 2-key mdpf silver, the 3-key silver estate, the 14-key bronze |
| `comp-pipescript io` | 5 trees | **rc=1** in every one; positive control `a00_runner` → **0** |
| `comp-pipescript postdeps` | `--firm bd` | **rc=2 REFUSED**, as s.8 recorded |
| `comp-validate` | `--artifact` | **rc=1** — and this is what refuted my own s.8 clause |
| `comp-pulse` (risk-reflex) | both commits | REFLEX CLEAN, 1838 danger nodes, denominators printed |

⛔ **Every rc above was re-read UNPIPED after the first read came back through `head`.** That is the
session's own lesson and it cost a false sentence in a committed artifact to learn twice.

## Push State

**BOTH COMMITS ON ORIGIN `@233da08b7f`** — `is-ancestor` YES for `d2201132d5` and `85abccfd68`,
`git ls-remote origin refs/heads/CLOUD` = `233da08b7f` read 02:09:04Z, after `0.0.0_AB_MSTR`'s 02:07Z
CLOSE frame (84300). They measured **LOCAL** at 02:04:35Z; the window moved them, and both readings are
kept because the claim is perishable.

⭐ **AND THE PUSH GATE INDEPENDENTLY CORROBORATED STEP 0, ON AN INSTRUMENT I DO NOT OWN.** The CLOSE
frame reports the deploy ceiling re-read at 3, including `bd49f_insurance_conversion.py`, and the gate
**probed it and got 404 → SKIP-NOT-MEMBER, 0 deployed.** That is the mdpf silver prefix answering, from
the integrator's instrument rather than mine, that this producer is not a member of it — which is the
same fact s.7.2 measured from the other side. **Not corroboration of the SUBSTRATE claim** (the gate
knows nothing about Lambda vendoring) — corroboration that **the prefix s.7.1 measured is not this
file's home**, and that nothing on the served plane moved.

## Next

1. **`0.7.0_AE_CloudOps`** — the substrate/host answer (84035, 84193 item 2), after the P0 floor hold.
2. **`2.0.0_SA_COO`** — whether `--backfill-manifest` runs now; it is the one remaining build act
   needing no mint.
3. Then the mint, on AE's confirmation, behind S5/S7.
