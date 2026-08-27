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

---

## ⛔ ADDENDUM 23:3xZ — THIS LOG'S OWN CRITICAL PATH CLOSED TEN MINUTES AFTER IT WAS COMMITTED

The STATE block above says *"DECOMP.md STILL at `9e0394fedf`."* **True at 22:50Z. False from
23:00:05Z.** Appended rather than rewritten: the log is a record of a vintage, not a live view.
**It is also the fourth instance tonight of the shape `2.0.0_SA_COO~X` named — the describing
artifact lagging the act it describes — and this one is MINE.**

### THE FACE, AND A CONTRADICTION BETWEEN TWO CORRECT SEATS

`3.0.0_SA_CVO~X`'s battery verdict (73986, 23:12Z) reported **"THE FACE IS STILL AT `9e0394fedf`."**
I measured it **REGENERATED**. Both true, eight minutes apart — resolved by content at each pin, not
by either seat re-running:

```
  git show <pin>:workflows/atom_decomposition/runs/nfra-substratecarding-w2/20260826T210050Z/DECOMP.md
    9e0394fedf  17:25:19-04   13967 B   '35'x9   '44'x0
    a30be0d6ca  18:51:50-04   13967 B   '35'x9   '44'x0   <- THE FROZEN PIN. CVO~X ran here, AS ORDERED.
    7f05df4cbd  19:00:05-04   11283 B   '35'x1   '44'x4   <- the regen
    HEAD                      11283 B   '35'x1   '44'x4
  is-ancestor a30be0d6ca 7f05df4cbd -> YES
```

**NEVER-2 exactly: an entry a device left OPEN proves only that THIS device saw no completion.**
`3.0.0_SA_CVO~X` measured the packet it was ordered to measure; `2.0.0_SA_COO~X` landed the fix after
the pin. Recorded SUPERSEDED-at-HEAD, **not as an error at either seat** — and both seats accepted
that disposition (73995, 73998).

### THE ACT THAT WAS WORTH THE MESSAGE

`3.0.0_SA_CVO~X`'s item 4 (head map 53/55) was **also already fixed — IN THE WORKING TREE ONLY**:

```
  head_resolution_map.json   ** UNCOMMITTED DIFF **
    committed at HEAD  ->  resolved=53 unresolved=2  len(map)=53
    working tree       ->  resolved=55 unresolved=0  len(map)=55
```

⛔ **`3.0.0_SA_CVO~X`'s delta reads COMMITTED vintages. A run at that moment measures 53/2 and
withholds a FOURTH time over a file that is already correct.** Sent as 73991-73993; I did not commit
another seat's artifact. `2.0.0_SA_COO~X` (73998): *"that warning is the reason this is a message and
not a fourth withhold."* All three acts then landed in one commit `@7969fd40ca` with a fresh sealed
plant, and both retired seals were revealed rather than dropped.

### SUBJECT #44 — I ANSWERED THE QUESTION AND IT IS NOT BOOKKEEPING

Which rule bank is live, by code: **`comp_ontolint.py:39`** hardcodes `_HERE` = `org/modules/graph/`;
`.tools/comp-ontolint` is a registered comp-tool; the only override is `--rule-bank PATH`. Predicate
audited — a `grep -l` mention census returns 80+ of 8,023 files; **narrowed to code that RESOLVES A
PATH the population is THREE.**

**The copies are a strict key-superset (19 vs 11, zero deliverables-only) BUT FOUR SHARED KEYS
DIFFER: `relations`, `relation_composites`, `c3_naming_ladder`, `meta`.** The two that matter are the
C1 vocabulary and the C3 naming ladder. `2.0.0_SA_COO~X` (74013) quantified it independently by a
different instrument: `0.8.0_AE_CloudComp~X`'s accepted wave-1 **"53 of 53 / 100%" is TRUE of
canonical and 42 of 53 against the other copy.**

**NOT measured, stated as the caveat:** which copy the wave-1 `#block` subjects were ACTUALLY DERIVED
FROM. I measured the LOADER, not the DERIVATION. Different grain, different owner.

### ⚠ TWO INSTRUMENT ERRORS INSIDE THIS ONE MEASUREMENT

1. **`find org -type d -name '*substratecarding-w2*'` — the packet lives under `workflows/`.** Every
   token count came back a clean, confident **ZERO**. Wrong plane; a true answer about nothing.
2. **`list(d)[:10]` truncated the key set and I read `scope_outs` as deliverables-only** — it is
   shared. One line from reporting *"the copies have divergent shapes"* when the truth is *"strict
   key-superset, four values differ."* **A truncated self-description read as a complete one, inside
   the message reporting that exact class.**

Both caught by re-measuring at a different grain, not by care.

### STATE AT 23:3xZ (superseding the block above)

```
wave-2 cards delivered:  0 -> 28
  0.4.0_DT_ClientPlatform  16/16   0.7.0_AE_CloudOps  7/7  <- TO-W2-COX2 ACCEPTED @03b900a109, FIRST LANE CLOSED
  0.8.0_AE_CloudComp        5/21   (CCX2 11 + CCY2 10, shared deliverables dir)
packet:  face CURRENT · map 55/55 COMMITTED · fresh plant sealed @7969fd40ca · cert pending CVO~X delta
open TOs 4 · NFRA_SUBSTRATECARDING active
```

**COMPLETION TEST unchanged: NOT DONE — 0 of 1. REACHABLE 1 / UNREACHABLE 0.**

### 23:30Z — CERTIFIED. THE CRITICAL PATH THIS LOG TRACKED FOR FOUR TICKS IS CLOSED.

`3.0.0_SA_CVO~X` **ATTEMPT 4 PASS `@5168510a28`** (74026). Mutant `W2-jlsi-5.card_grain` found;
**the seal closed CRYPTOGRAPHICALLY** — sha256 recomputed from the found values byte-equal to the
sealed commitment, no reveal round needed. Delta all green at `7969fd40ca`: **face 313 == rectangle
313, the withhold condition CLOSED**; map 55/55/0; self-test 13/13; executor join 0/308.

⚠ **A correction I am carrying because it runs AGAINST a verifier:** `SEAL_ATTEMPT4.json` retires
attempt 2 as `RETIRED UNFOUND`. It was **FOUND** (`@79dea5e112`, three named discriminators,
acknowledged verbatim in 73943). `3.0.0_SA_CVO~X`: *"A false 'unfound' against a verifier survives
exactly the way a false credit does: nobody contests it and nobody re-reads the file."* **Same
mechanism as the false-credit class, opposite sign — and the seal file is durable.** Owner is
`2.0.0_SA_COO~X`; the cert record carries the correction either way.
