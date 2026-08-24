# 2.0.0_SA_COO~Z — ADDENDUM: round 1 EXECUTED and five of six TOs CLOSED (2110–2245Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, COORDINATE, DIAGNOSE, SCRIBE

Continues `laneZ_etfs_ingest_stage3_decomp_and_round1_dispatch_1950-2110Z.md` @284b056db6.
**9 further commits.** ~20 MCP sends, ~55 messages read and READ-acked. **Zero crons, whole session.**

---

## 1. ⛔ CURRENT STATE — FOR A FRESH SEAT

### The chain, by rung — and the gap is the point

| tier | state |
|---|---|
| **BRONZE** | ✅ **EXERCISED** on the scheduled fire. DIVZ/IDVZ holdings captured for the first time ever |
| **SILVER** | ✅ **EXERCISED.** 114 → **187 rows**, four funds, weights 99.80 / 99.51 matching the oracles |
| **GOLD** | ⛔ **NEVER RUN.** `opal-data-etfs/gold/` = 0 objects |
| **PLATINUM** | ⛔ **UNMOVED.** 76,149 B, `2026-08-24T12:30:47Z` — unchanged all session |
| **SERVED SURFACE** | ⛔ **VERIFIED BY NOBODY** |

> **TONIGHT PROVED THE CAPTURE, NOT THE PRODUCT.** A fresh seat must not read "five TOs closed" as
> "the pipeline works end to end." **It does not yet reach the page.**

### The single critical path

**`ETFS_POSITIONING.TO-5`** — the only gold→platinum schedule in the estate. **Unblocked on both
fronts** (packaging ruled = MINT THE LAYER; DS~Z's handler shipped 22:38). `etf-positioning-producer`
does not exist on the applied plane; `comp-trigger` NO MATCH over 136 rules + 18 schedules. AE~Z holds it.

### TO ledger

| TO | seat | state |
|---|---|---|
| `ETFS_INGEST.TO-1` | AE~Z | ✅ **CLOSED** — deployed + **exercised on the scheduled fire**, 7 ledger legs |
| `ETFS_INGEST.TO-2` | DS~Z | ✅ CLOSED — four conventions ruled |
| `ETFS_INGEST.TO-3` | DS~Z | ✅ CLOSED — gold re-point + the separator fix |
| `ETFS_INGEST.TO-4` | DS~Z | ✅ CLOSED — vendor feed + conventions in code, `HOLDINGS_COLUMNS` 17→26 |
| `ETFS_INGEST.TO-5` | DE~Z | ✅ CLOSED — condition (ii) **determined**, not built |
| `ETFS_INGEST.TO-6` | DS~Z | staged, **re-sequenced behind** `ETFS_POSITIONING.TO-5` |

**Decomp CERTIFIED @fcdf042972 and NOT re-entered since the freeze** — six TOs cut against it, zero cells edited.

---

## 2. Rulings I made, and what each rested on

**CONV-1 fork → (a), blank IS the vendor's negative.** DS~Z stopped mid-build per AC2 and falsified
their own ruling. **I widened their n=1 to 15 files / 1,710 rows before ruling** — a single file
cannot separate *"this vendor never writes N"* from *"today's file has none"*, and the fork turned
entirely on that. Only `''` and `'Y'` ever observed. **Ruled with AC7, a runtime refusal**, because
the ruling rests on an inference about a vendor and *a ruling resting on a measured constant must
fail loud when the constant moves.*

**The TO-5 hold LIFTED** — precondition discharged. I verified **all four** parts of CTO~Z's ruling
in the corrected contract, going after the third specifically (`ListBucket` prefix `gold/`) because
it fails loud at runtime. **A correction fixing three of four would have read complete.**

**Re-sequenced** the three silver cells behind TO-5, in CTO~Z's framing: *they improve what flows;
TO-5 is whether anything flows at all.*

---

## 3. ⛔ My own defects this stretch — and the shape repeats

| # | defect | caught by |
|---|---|---|
| 6 | **I mandated a command that cannot run** — `comp-pipescript --pipeline etfs`, rc=2, in a TO whose criteria demand exercised evidence. **I required exercise and did not exercise the requirement** | DS~Z hit it; fixed before they reached TO-3 |
| 7 | **Pre-wrote a verdict beside a measurement, inside a validation** — "0 at the first commit" when it returned 1; my pattern matched line 762, the key composition | re-reading my own output |
| 8 | **"Three independent preservation paths"** — I read `get-bucket-versioning` → `Enabled` and stopped. A **bucket-wide 14-day fuse** lives in a different API call | CVO~Z |
| 9 | **A stale status line of my own** — `ETFS_POSITIONING.TO-5` read "queued behind TO-2's remaining leg" for hours while it sat on the critical path | found while re-sequencing |

⛔ **AND THE ONE THAT MATTERS MOST IS A PATTERN, NOT AN INSTANCE: TWICE TONIGHT MY CORRECTION FIXED
THE NUMBER AND KEPT THE FRAME.**
- §5's denominator 26→36 — and the fix **swapped which cell was orphaned** rather than closing the gap.
- Preservation paths 3→2 — and CTO~Z showed it was **still one axis short**, because *durable* and
  *reconstructs the bytes* are different properties. Only the pin is both; the manifest is a **hash,
  a verifier, not a copy** — 833 bytes cannot become 76,149.

> **A correction that only moves the value is the easiest kind to ship and the least likely to be
> re-audited, because it looks like the lesson was learned.**

**Two relay defects also stand** (SALXX; the `FUND_PCT_TOP_TEN_HOLD` overlap) — both caught by the
receiving seat, both banked as `a-relayed-measurement-loses-its-qualifier-in-a-spec`.

---

## 4. What the executing seats found that I could not

- **AE~Z closed the EXERCISED rung by declining a permitted act.** The TO allowed an ad-hoc QA
  invoke; they refused it, because an ad-hoc artifact is byte-identical downstream and firing one
  destroys the ability to say which run produced the result. **They gave up a convenience to preserve
  an oracle.** Objects landed inside the invocation window 22:00:08.209 → 22:00:12.027Z.
- **DS~Z stopped mid-build and falsified their own ruling**, then rebuilt CONV-1 as
  *declared-never-inferred* — rejecting the "no negative seen, so presume presence-flag" shortcut
  **because it makes the meaning of every row a function of its cohort.** Stronger than my ruling asked.
- **DE~Z answered Z-S12 with a third answer nobody had:** labels fine, **colour channel dead** — *"it
  renders UNDIFFERENTIATED, not wrong."* And showed the estate had **already decided** this exact
  vocabulary is text-not-colour on another page.
- **A THIRD CUSIP corruption mode, on tonight's own new rows:** RTX `7.55E+105` — `75513E101` read as
  a number. **I narrowed it: exactly three significant figures survive.** Worse than a null, because
  it renders, sorts and joins against nothing — and unlike the five zero-stripped rows, **there is no
  check digit to validate a repair against.**

---

## 5. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `proof-of-spec-check.py` | **5 instances re-run by me**, all rc=0 without a pipe | ⛔ **I ran a MUTANT on TO-2's** (bogus 6th id → rc=1, coverage-frame violation). A validator that cannot fail proves nothing |
| `comp-trigger` | ×5, denominator printed every time (136 rules + 18 schedules) | Its own honesty about scope is why the NO MATCH is usable |
| `comp-pipescript io` | ⛔ **rc=2 — `etfs` is not in the enum; `--pipeline all` rc=1** | **A CONFIRMED coverage gap for this tree**, and a mandate of mine that could not run |
| `comp-find -i` | portal censuses with denominators | My two-map figure was **a FLOOR I presented without saying so**; DE~Z found the third and the mechanism site |
| `boto3` direct | the 15-partition `MoneyMarketFlag` census; the parquet diffs | Used where no comp-tool models this tree; every raw `aws` call carried `# rail-checked` |
| `safe-commit.sh` | **9 invocations, 9× rc=0**, risk-reflex CLEAN with its denominator each time | 0 gate failures, 0 owned-paths refusals |

**Gap standing:** no comp-tool compares a Lambda package member to the source it was built from, and
none models the `etfs` tree. Both routed as §21 coverage gaps, neither as a build I started.

---

## 6. Blockers

**None at this seat.** Open and owned elsewhere: `ETFS_POSITIONING.TO-5`'s apply (AE~Z, the critical
path) · the layer mint, scope-bounded to NOT migrate the existing four · `INGEST-T3-4` inherits the
irreversible-CUSIP pricing · D4 register member-add (base MSTR).

⚠ **`org/missions/DIRECTIVES.yaml` at `origin/SITEZ` line 80 is STALE** — reads *"SITEZ — TEMPORARY,
TODAY ONLY"*; Andrew's word is **"until the project is done."** The correction landed on
`origin/CLOUD`, the branch this fabric does not read. **I measured all nine of my artifacts: ZERO
exposure**, because every placement line cites **the ruling, not the register** — which was a
stronger-citation habit, not foresight about this defect.

---

## 7. Next Steps

1. **[AE~Z]** `ETFS_POSITIONING.TO-5` — mint the layer, apply, **no gold env vars at all**, IAM to
   `opal-data-etfs/gold/*`. **The entire critical path.**
2. **[AE~Z / DS~Z]** First gold run, then the first platinum publish. **Nobody has seen either.**
3. **[DS~Z]** TO-6 (GICS field) once TO-5 discharges; A5-first-GICS-second still binds.
4. **[a fresh COO~Z]** The decomp is certified at **`@fcdf042972` and no other vintage**. A changed
   cell VOIDS the verdict rather than silently carrying it. **That contract is mine and I nearly
   broke it once.**
5. **[anyone]** Do not read the D4 register on this branch without reading §6 first.
