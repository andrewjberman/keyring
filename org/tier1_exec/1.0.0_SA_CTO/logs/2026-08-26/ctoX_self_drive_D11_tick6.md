# /self-drive D11 — ticks 5-6

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 22:21Z–22:50Z

---

## SCOPE

```
D11 "Substrate Analysis"   device LAPTOP (guard PASS)
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 4
  denominator: 1 of 12 live directives
```

**Open calls in scope: 0 across both ticks.** No empty pitch sent.
**RESERVED at Andrew (D11 scope): 0.**

## VERDICTS / FINDINGS RECEIVED, ticks 5-6

Four, none of them an adjudication of a pitched call — all cert or lane findings I acted on in my own
lane.

| id | operative | my act |
|---|---|---|
| 73916 | W2 cert attempt 2: **MUTANT FOUND, CERT WITHHELD** — DECOMP.md never rewritten by `b918167857`; CCY2 refs resolve **0 of 63** against the face | confirmed by a **different instrument** (`git show --stat` = 0 DECOMP.md files) + added the partial-fix framing |
| 73934 | DT~X BLOCKING UPHELD — derivation never read `co_resident_stores`; **13 heads, 12 named only there**, incl. `.comp-graph/graph.json` | **root is my schema**; `x-names-parts` @`109111dac3` |
| 73946 | W2 cert attempt 3: mutant found again, **cert still withheld**, face stale through BOTH amendments; adopting *amend-until-stable-then-certify-once* | ran the closure test to let the freeze be measured |
| 73857 | positional cell ids repointed 7 live ids silently | recorded the derived-identity generalization @`96af540402` |

## DRIVER ACTS (own lane only — no TO, no dispatch, no apply)

1. **`declared_opinions` gap closed @`9660f526d8`.** COO~X dispatched wave 2 with it on every TO face:
   the field was in the L0 manifest and **not** in the card schema, though it is the one field the
   canonical-materializer consumer reads. **Added OPTIONAL** — no in-flight card invalidated, no TO
   face amended.
2. **`x-names-parts` @`109111dac3`.** Four fields named parts and **none was marked as a class**, so
   the only way to know the set was to remember it — and `SC-m-4`'s oracle froze a remembered subset
   into an accepted one. **I reviewed that oracle and did not catch it either.**
3. ⛔ **Corrected my own marker @`e789861948`.** See below.
4. Confirmed the face defect independently; framed it as a **partial fix**, not a second defect.

## ⛔ THE CLOSURE TEST — and I nearly manufactured a third gap with it

`3.0.0_SA_CVO~X` is holding the battery until the subject set is **declared** frozen. `x-names-parts`
made the class enumerable, so I ran the test to let the freeze be **measured**:

```
  heads via composes + projection_of + co_resident_stores    68
  heads via invents                                          21
  named ONLY via invents                                     21   <- ALL of them
```

**For about a minute that read as a SECOND missed field of exactly the class COO~X had just been
caught by. Then I read the heads instead of counting them:**

```
  "the >=2-member domain-promotion threshold"       PROMOTE_MIN -- an OPINION
  "the SIM_TWIN = 0.60 functional-twin threshold"   a THRESHOLD
  "the 'orphan' motif classification"               a DEFINITIONAL CHOICE
  "the lifecycle_class enum (7 values)"             a TAXONOMY
```

**ZERO of the 21 is a store.** A parts-derivation reading `invents` would have enumerated **21
CONCEPTS as STORES** — the CARRIER-3 error (*a population is not a store*) at 21x scale, injected into
a wave already twice re-emitted. **My marker was wrong; removed against the measurement.**

**THE FINDING UNDERNEATH IS A GIFT:** those 21 are **`declared_opinions` content.** Wave-1 lanes
recorded the semantic-defect axis in `invents` **because it was the only slot that fit** —
`declared_opinions` did not exist until `9660f526d8`, hours after those cards were written. **21
opinions already harvested at zero cost**, on the axis that has no instrument, feeding the one field
the canonical materializer reads.

**Reported to COO~X as INPUT to their freeze, not as a freeze.** Explicitly not claimed: heads are
pre-dedup, subjects are post-dedup, **their 41 is not certified by this.**

## STATE

```
WAVE 2   33->41 subjects / 292 cells (grew twice on upheld lane BLOCKINGs)
         cards delivered: 0
CRITICAL PATH: DECOMP.md STILL at 9e0394fedf -- 9 occurrences of "35" on the face.
         Lanes card fine (rectangle is authoritative); NO LANE CAN PASS THE GATE until regenerated.
         Remedy is the author's. Not blocked on me.
telemetry, all six seats inside 11 minutes:
  CCX 22:39:09 · CCY 22:41:31 · COX 22:48:19 · DTX 22:50:07 · COO~X 22:50:11 · CVO~X 22:47:38
```

**COMPLETION TEST: NOT DONE — 0 of 1 complete.** REACHABLE 1 / UNREACHABLE 0.

## CARRIED — not D11 scope

At Andrew: **D12** · **cover vs partition** · **identity grain** · two **CLAUDE.md** fixes ·
COO~X's **vantage-vs-world** doctrine candidate.
⚠ **Cover-vs-partition and identity-grain should now be weighed with OPTION C restored** — I told
Andrew the canon's 10 relations and the graph's 53 edge types were a map-vs-territory divergence;
`0.8.0_AE_CloudComp~X`'s 73802 falsified it (`binds_up` declares the mapping, 53 of 53), and I
verified independently: `owns -> ['OWNED_BY']` exists and is computable.

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; this loop dies with the
session and no successor re-arms. Law-file edit held under Andrew's standing instruction.

## Compiler Tools

`.tools/directives-check.py --json` (both ticks) · `org/mcp/agent_telemetry/*.jsonl` as the **work**
oracle · `git show --stat` as an independent instrument on the face defect · `jsonschema` Draft
2020-12 for every schema change (all exercised both directions) · `.tools/safe-commit.sh`.
⚠ A non-ASCII character in my own closure-test print crashed it on cp1252 — the estate's own
no-non-ASCII rule, second time today at this seat.

**state: ARMED** · next tick :17
