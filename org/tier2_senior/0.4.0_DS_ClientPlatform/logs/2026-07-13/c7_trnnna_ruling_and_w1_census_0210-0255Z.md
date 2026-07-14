# C7 authored, the TRN_NNA fork ruled, W1 census -- and a second forged sender line

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, EXPLORE, COORDINATE

**Date:** 2026-07-14 (window 02:10Z -> 02:55Z)
**Task Orders:** OPAL_ASSETS C7 (author half) · OPAL_RUNNERS W1 (script census)
**GO:** CTO 01:06Z / COO 01:13Z (batch). W1 = COO-commissioned fill, taken once C-series completed.
**Status:** C-SERIES COMPLETE. W1 LANDED. W4 coordination opened with 0.6.2.

---

## Objective

Finish the GO'd batch (C7 author half), fold CTO's ruling on the fork I raised, then take the
commissioned fill work now that the C-series was done.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-which` | "what gold scripts consume the schwab silver tables…" | **near-tie, no silent guess** | Printed `*** TOP SCORES ARE TIED -- THE ORDER IS NOT A RANKING ***` and told me to read the descriptions. It declined to manufacture a ranking out of a tie. Correct behaviour. |
| `comp-grep` | `--include-held 'schwab/silver' data` | PASS | The Phase-1 consumer enumeration. Held-inclusive **SOURCE** read (repo grep — not a pipeline verb; the 49F hold forbids writes/runs/verifies, not reading code). |
| `comp-grep` | `'opal-data-schwab' data/cot` | **0 matches — and it said so** | Printed *"0 matches is a real result here — the .gitignore-aware working set was searched, not a stale index."* That sentence is why I trusted the negative. |
| `commit-gate` | per `.py` ×3 | PASS | |
| `comp-surface-check` | auto in safe-commit ×3 | OK | No critical surface. |
| `comp-pipescript io` | **NOT RUN — still an explicit gap** | GAP | C7's Phase-1 mandate is *consumer enumeration*, which I discharged via `comp-grep`. The per-script `io` pass belongs with the deploy half (AE) — it enumerates column gaps for scripts whose **production path is changing**, and under new-territory nothing's path changes yet. Recorded, not skipped. |

**What worked:** two comp tools *declining to answer* rather than guessing — the tie warning and the
explicit "0 matches is a real result." **Instruments that can say "I don't know" are the whole point.**
**What failed:** nothing in the toolchain.
**Gap found:** none new.

---

## Work Completed

### 1. C7 -- unattended Schwab conversion, author half (`9de567c55`)

Retires the manual `/49-schwab-conv` 7-step, where raw lands on a cron and then **waits for a person**.

> **A procedure that has to warn you not to skip a step is telling you that people skip it.**

The skill doc's own words: *"RLD is NON-OPTIONAL — omitting it silently degrades gold."* So RLD gets a
guard that **can fail a run**: a delivery carrying any other CRS type without RLD is **refused whole,
before a single byte converts** — because a half-converted delivery is the worst outcome available,
*it looks like progress*. And it is discriminating: an **empty** delivery is not an error (a guard that
fires on nothing is noise).

Order is load-bearing: parse → **reconcile to T1 (raw rows)** → frame → dedup → write → **verify the
write**. Reconcile *before* dedup, because dedup changes the count and would mask the very drop the
trailer catches. The write-verify is tested against a `LyingS3` double that **claims success and stores
nothing** — rc=0 is not evidence.

16 new tests, 72/72 tree-wide. **NOT deployed, NOT wired** — AE's half; I did not bypass owned-paths.

### 2. A bug I wrote, caught by its own test

`date_from_key()` scanned the path for "an 8-digit segment." **The master account is also 8 digits and
comes first:**

```
08242234/bronze/rps/20240708/08242234.CRS20240708.RPS.zip
^^^^^^^^ matched as the date  ->  every partition written to date=0824-22-34
```

A key that looks entirely plausible. Now read from the filename's `CRS{YYYYMMDD}` and **validated**.
Uniform rule across type/master/date: **the file's own name is authoritative; the folder is a claim.**

### 3. The TRN_NNA fork -- raised unresolved, ruled, folded (`ab1844cc5`)

`TRN_NNA` is a net-new-assets derivation **from** TRN — business logic, which Rule 17 forbids at silver.
The monolith could not be both faithful to the manual procedure **and** Rule-17 legal. **I implemented
neither option.** Emitting a derived table into silver silently, or dropping a table consumers expect
silently, are both worse than saying it out loud — and a violation that lands in the canonical bucket
gets ratified by the fact that it works.

**CTO ruled (b)** (PRD v1.4.2): monolith silver = the five RAW types, nothing derived. And the
sequencing worry **dissolved under new-territory** — nothing reads monolith silver yet, so a five-table
contract breaks nobody. His note: *implementing NEITHER rather than picking silently was the
precondition for this ruling being cheap.*

Folded into the code, and the test renamed to what it now **is** — the ruling's **enforcement point**:
add `TRN_NNA` back to `RAW_TYPES` "to match the manual procedure" and it **fails**.

### 4. Phase-1 consumer enumeration -- the gap from my last log, CLOSED

Held-inclusive source read: 47 refs `canonical/schwab/gold` · 34 `bd/scripts/bronze` (the manual
converters this retires) · 17 bd gold · 16 bd diagnostics · 11 cot gold.

**FIRM BOUNDARY VERIFIED INTACT (NEVER#2) — reported as a verified NEGATIVE**, not left as a scary hit
count: cot's 11 hits read `schwab/silver/rps/` as a prefix **inside `opal-data-cot`** (Cottonwood's own
Schwab-custodied data); `opal-data-schwab` appears **zero** times in the cot tree; the 9 `opal-data-bd`
hits are all in a README **documenting** the separation, not code.

### 5. W1 -- gold-script census + divergence matrix (`51060cfa9`)

| | |
|---|---|
| **It is 248 scripts, not ~210** | PRD estimate 18% low. bd 89 · inf 73 · cot 58 · schwab 28 |
| **101 of 248 (40.7%) map to NO letter group** | Each a NAMED VARIANCE owed to the PRD before a contract locks |
| **15 (6.0%) incremental · 105 (42.3%) full-recompute · 85 (34.3%) UNKNOWN** | The cost story as a fraction |
| **31 sibling groups, 24 DIVERGE** | Every `A_*` and `B_*` sibling diverges across bd/cot/inf |

**A census whose first number is an estimate has not started.**

The 40.7% is the finding I'd act on first: as it stands the A/B/C/D contracts would **silently leave
behind two-fifths of the estate**, and *"it didn't map, so we didn't move it"* is exactly how a fork
survives the consolidation meant to end it.

**And I flagged the compute column HARD, against my own headline number:** it is inferred from **source
markers** — a hypothesis about behaviour, not an observation (Rule 22). **Do not price a box off that
42.3%.** The ≤$100/mo envelope is an acceptance criterion; it deserves a measurement (`gold_prof` +
GLDINC), not a grep. Turning my number into a capacity plan would be a rigorous instrument on the wrong
axis — worse than no instrument, because it survives review.

`UNKNOWN` is a first-class result in that column. **No evidence either way is not "probably full."**

---

## MY ERROR -- A SECOND FORGED SENDER LINE

At **02:38:40Z** I sent CTO a second junk message (`subject: x`) **under his own serial** — an hour after
reporting the first (`01:51:53Z`) and writing 400 words about the hazard.

> **Twice is not a typo. It is a pattern, and my "I'll be careful" was worth exactly nothing.**
> **That is the argument for the gate, not the argument for my attention.**

**`send_message` has NO sender authentication.** `from_agent` is free text; the broker wrote both
messages into the CTO's inbox stamped with **his own serial**, from me, no check, exit 0. The only
reason neither did damage is that I put junk in the body — a plausible body would have been
**indistinguishable from him**.

**One agent. One session. Two forgeries. Zero detections.** Both are on the record *only* because I
self-reported; nothing in the fabric noticed either. So historical incidence is **UNKNOWABLE** — nobody
should quote a count as a total (same class as the `-m`-with-backtick injection: only the loud ones
leave scars).

The guard **already exists** — `NFRA_IDENTITY.G-A` refuses `register_agent`/`heartbeat` when the PID is
live under a different serial. **`send_message` simply never calls it.** CTO escalated the gate to Andrew
as URGENT this turn.

This is the mirror of Rule 22b: 22b says only an ACK proves a message was **HEARD**; this says **nothing
proves a message was SENT BY WHO IT SAYS.** On a fabric where *"Andrew ruled X"* is relayed
agent-to-agent as the **normal** case, that is the most useful forgery available.

---

## The push block (resolved -- I touched nothing)

`e5a8d90fb` (0.7.0) carried a 685MB terraform `.exe`; CLOUD was unpushable, 4 commits / 3 agents stacked.
I diagnosed, **refused the rewrite** (NEVER#7 + destructive-git), and escalated. Andrew explicitly
authorized it; 0.7.0 stripped it in a **throwaway bare clone** (shared worktree untouched), fast-forward.

I flagged pre-filter that I had **TWO** commits in the range, not one — a log commit landed after their
snapshot. *The pile grows while you diagnose, because a local commit SUCCEEDS and only the push fails.*
Both were covered in the map.

**I verified the all-clear myself rather than take it on report** — and specifically **re-ran the suite
off the rewritten tree**: `git show` proves a **file exists**, not that the **code still works**. 72/72.
COO banked that as the post-rewrite behavioural-intactness standard.

**New SHAs:** C10 `5f167db2c` -> **`9380707b6`** · prior log `17f530bad` -> **`62f9c83c6`**.
Root cause closed: global `**/.terraform/` ignore at `.gitignore:191`.

---

## Rulings received

| Ruling | Effect on me |
|---|---|
| **TRN_NNA = gold-tier** (PRD v1.4.2) | Folded — C7 already implemented it; test is now the enforcement point |
| **C7 guards RATIFIED as authored** | RLD-or-refuse-whole · reconcile-before-dedup · LyingS3 write-verify |
| **C2 mirror = polling**, monolith events unaffected | My parsers are pure per-object + stateless — batch arrival is safe. Checked, not assumed. |
| **My C2 denominator request ADOPTED** (`bb754a1c4`) | Mirror emits enumerated-vs-written and **RAISES** on mismatch, ruling-11a cited as precedent |

---

## Files Modified

See commit messages: `9de567c55`, `ab1844cc5`, `51060cfa9`.

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| W1 script census + divergence matrix | `deliverables/OPAL_RUNNERS_W1_SCRIPT_CENSUS_20260714.md` | OPAL_RUNNERS §7 evidence (CTO/COO) |

---

## Blockers

**NONE.** Nothing is waiting on me; I am waiting on nothing. W4 needs 0.6.2's landing facts to start
against a stable denominator — that is a coordination dependency I have **opened**, not a block.

## Current State

C-series **COMPLETE** and pushed: C6 (`44a5328ce`, `37752c64f`) · C12 (`fb31f3586`) · C10 (`9380707b6`) ·
C7 author half (`9de567c55` + `ab1844cc5`). **72/72** across `data/assets/scripts/`, including live-S3
integration against real bytes. W1 census landed (`51060cfa9`) with a re-runnable engine at
`data/assets/scripts/analysis/w1_script_census.py`.

C7 is **authored, not deployed** — the AE deploy hand owns wiring, and the `opal-data-schwab` AES256-SSE
PutObject deny is why. C11 stays **STAGED** (gated on C3+C6). Nothing self-dispatched.

## Next Steps

1. **[0.6.2_AE_PartnerETL]** W4 landing facts — which 0833 types are terminal, at what vintage, and
   whether the partition set is still moving. **I will not characterise "sufficiency" against a
   denominator that changes under me** (0824 moved 1,056 -> 1,081 objects between two `ls` calls).
   Warned them off `read_schwab_raw()` — it would census a file with a table missing, all checks green.
2. **[1.0.0_SA_CTO / Andrew]** the `send_message` identity gate (URGENT) · the held-lib D2 balance-table
   disposition · the C2 mirror fork (raw-that-doesn't-exist vs parquet-that-violates-17a).
3. **[me]** W4 column side on 0.6.2's word; the 40.7% unmapped-scripts variance list if COO wants it
   next.

## Fences -- held, all window

INF chain HELD · `gold/meta/pipeline-complete.json` **never written** · frozen 3 untouched · no mdpf
trigger · 0824/0833 never summed · read-only on every source · no vendor egress · no gold, no served
re-derive ("No 49 Yet" binds everything downstream of silver) · owned-paths never bypassed.
