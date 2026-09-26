# Clause 3 cannot complete on the current harvest universe: 6 of the 95 securities are not in it at all

`1.0.0_SA_CTO~Z`, 2026-09-26 ~19:0xZ. Self-adjudicated under `/self-drive` call routing (Andrew-direct
2026-09-17: *"if there is an open-call (of any kind) you use your recommendation"*). Arming record
`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` @`f3b85ff6a5`.

## 1. THE FINDING

The GOAL's clause 3 is *"complete backfill for all of these securities through the opal-data-harvest
channels"*, and its completion test is his: *"Only when all of this is done for every single security in the
Asset Management research folder is the goal complete."*

**`opal-data-harvest`'s security universe holds 89 names. The application's population is 95. The harvest
universe is a STRICT SUBSET, and the six absent securities are:**

```
AIA Group
AMD Advanced Micro Devices
Alphabet GOOGL US
Eli Lilly LLY US
Quanta Services PWR
UnitedHealth Group UNH US
```

**So no amount of backfilling can satisfy clause 3 as written.** The six are not under-harvested; they are
not in the universe the harvester iterates.

## 2. THE CAUSE IS ONE FOLDER READ AT TWO TIMES, NOT TWO FOLDERS

`lib/opal_data_harvest/config.json` -> `universe_source` ->
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json` @`628b975b49`:

| field | value |
|---|---|
| `corpus_root` | `...\Asset Management\Research` |
| `corpus_root_mtime` | `2026-09-09T14:25Z` |
| `read_finished_at` | **`2026-09-10T23:18Z`** |
| `denominator_folders` | **89** |

The application's pinned population (`AMGT_RESAPP` round 45 `checks/population_at_cut.txt`) reads the **same
corpus root**, `read_at` **`2026-09-26T13:29:01Z`**, **95 folders**.

> **Same folder. Two read times, sixteen days apart. The research library grew 89 -> 95 and the harvest
> universe is pinned to the older snapshot.**

**AND THE SHAPE OF THE SIX CONFIRMS IT.** Four are plainly US-listed (`GOOGL US`, `LLY US`, `UNH US`, plus
AMD and PWR) -- exactly the names `infer_sa_symbol`'s stated US rule resolves most easily. **They are absent
because they postdate the snapshot, not because they are hard.** A missing-rule diagnosis would have
predicted the opposite shape.

`AMD Advanced Micro Devices` is one of the two names `AMGT_RESAPP` round 45 pins as a served control fixture
for `FWD-30`. **A name can be load-bearing in the application and absent from the backfill universe at the
same time**, because nothing joins the two populations.

## 3. THE JOIN IS SOUND, AND THE ZERO IS THE CONTROL

Comparison key: the harvest universe's `identity_source` (its `row["folder"]`) against the population file's
folder lines.

```
IN APP, NOT IN HARVEST UNIVERSE : 6
IN HARVEST, NOT IN APP          : 0
```

**The 0 on the second line is the positive control on the join key.** Inconsistent folder spellings would
have produced a non-zero count on BOTH sides; 89 of 89 matching exactly is what licenses reading the 6 as a
true absence rather than a naming artifact.

## 4. I AM CORRECTING MY OWN PUBLISHED FIGURES

I have twice stated clause 3's ceiling as *"25 usable `sa_symbol` of 95, 45 NEITHER"*, including to
`3.0.0_SA_CVO~Z` today, which accepted it. **Measured now from the producer's own `universe` command
(`PYTHONPATH=lib python -m opal_data_harvest universe`, rc=0):**

| figure | I published | MEASURED |
|---|---|---|
| denominator | 95 | **89** (producer-printed, and asserted by its own `denominator_folders` check) |
| carries an `sa_symbol` value | 25 | **25** (stands) |
| does not | "45 NEITHER" | **64** |
| `identity_status` | not stated | INFERRED **20**, UNRESOLVED **64**, absent **5** |
| no `bloomberg_ticker` value | not stated | **57 of 89** |

**The 25 was true and I carried it into a population it never measured** -- the app's 95, not the harvester's
89. That is the error class I logged against myself this morning and repeated by lunchtime.

The `20 INFERRED + 5 absent = 25` identity reconciles: the 5 are `pilot_securities`, which carry a symbol
directly and no status.

**AND THE DOMINANT BLOCKER IS NOT THE ONE I NAMED.** I said clause 3 was ceilinged by the missing ex-US slug
rule. Measured: **57 of 89 carry no `bloomberg_ticker` at all**, and `infer_sa_symbol`'s FIRST branch returns
UNRESOLVED for exactly that reason (*"no bloomberg_ticker value to derive a slug from"*). The ex-US rule gap
is real and secondary; **the primary gap is upstream identity, not slug inference.**

## 5. WHAT THIS DOES NOT CLAIM

- It does **not** say the 89 were harvested well. Coverage within the universe is a separate question.
- It does **not** grade any outcome. `AMGT_HARVST` round 7 stands at **20 of 21** on the record plane
  (`TO-HVST-v-2` is `pending`; `2.0.0_SA_COO~Y` is mid-drain), and `3.0.0_SA_CVO~Z` holds L8/L9 until it
  lands. **No analysis is cut here.**
- The 95 is the application's population at round 45's cut. If the research folder has grown again since
  `13:29:01Z` today, 95 is itself a snapshot -- which is the general form of this defect.

## 6. REC, AND MY RULING

**REC:** treat the universe snapshot as a DERIVED artifact with a freshness obligation, not a fixture. The
`AMGT_HARVST` enrichment list gains one cell: **re-derive `universe.json` from the live corpus root
(`lib/research/identity/build_universe.py`) and make the harvester's denominator a read of the library rather
than a pinned 89**, with the app population and the harvest universe reconciled by a printed two-sided delta
whose expected value is 0 on both sides.

**RULING -- adopted, as a cell on the HARVST enrichment list, not an act taken now.** The re-derivation is
`2.0.0_SA_COO~Y`'s to cut and a worker's to run; it touches `universe_source` and therefore the harvester's
denominator, so it is a round cell with its own criteria, never a rider on a drain. It needs no Andrew word
and no vendor egress: the corpus root is Opal infrastructure and `build_universe.py` reads a folder.

**One consequence to state plainly:** while the universe holds 89, the goal's own completion sentence
(*"every single security"*) is unreachable by construction, so clause 3 cannot be graded REALIZED on any
backfill evidence produced against the current universe. **That is a blocker on the GOAL, not on a round.**

## Compiler Tools

The producer's own `universe` command used as the oracle rather than re-deriving its census by hand -- the
two-sided set difference with its `0` reported as the join's positive control -- `corpus_root` compared
across both artifacts, which is what turned "two populations" into "one folder at two times" -- and the
shape of the six absent names (four trivially US-listed) used to falsify my own missing-rule diagnosis
rather than to illustrate it.
