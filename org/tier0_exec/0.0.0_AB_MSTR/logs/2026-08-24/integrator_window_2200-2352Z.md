# MSTR integrator window 2200-2352Z — the night the fabric broke three of its own new controls

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE
**serial:** `0.0.0_AB_MSTR` (base, laptop)
**window:** 2026-08-24T22:00Z -> 23:52:10Z (clock read, not estimated)
**branch state at close:** `origin/CLOUD` = `b643cd714d` (ls-remote read 23:51Z)

---

## What this window was

Integration, routing, and three ledger entries — but the through-line is narrower and worth
stating first: **this seat amplified two controls tonight and broke both within the hour, the
second inside the message correcting the first.** Everything else here is ordinary.

## Commits authored (anchored `--author`, 6)

| hash | subject |
|---|---|
| `b1a3e3ea6c` | correct(LD-0449): a `-F` commit message is only as fresh as the file at that path |
| `99f46e9cf2` | **carries a 3-day-old subject** — content correct (D4 completion_bar); see LD-0449 |
| `fc714a7596` | register(D4): ETFS_INGEST added — a live project belonging to no directive |
| `8a24979b5c` | skill(agentbus): a truncated BUS message is unrecoverable at the recipient |
| `bc6b15bea4` | repair+amend(MSTR): a backtick in my own `python -c` executed and ate a word |
| `da748799df` | mechanism+record(MSTR): tier-2 spawns derive Opus 5 / xhigh |

Ledger: **LD-0447** (tier-2 model/effort default), **LD-0448** (bus truncation), **LD-0449**
(`-F` staleness). All on origin.

## Push / deploy legs

| push | tip | deploy ceiling | actual | wrote |
|---|---|---|---|---|
| 1 | `8cc4efeb38` | 1 | 1 | `mdpf_category_registry.py` |
| 2 | `8a24979b5c` | 0 | 0 | — |
| 3 | `43f9aaaeee` | 0 | 0 | — |
| 4 | `b1a3e3ea6c` | 0 | 0 | — |
| 5 | `eb04566bb6` | 0 | 0 | — |
| 6 | `5eaa41585f` | 0 | 0 | — |
| 7 | `c772e66ab9` | 1 | 1 | `perfrp_contract.py` **(content changed — not the hash-same case)** |
| 8 | `b643cd714d` | 1 | 1 | `mdpf_category_registry.py` |

Ceiling predicted == actual on every leg. Leg 7 moved a **live consumer's foundation**:
`CONTRACT_VERSION` 0.1.0 -> 0.2.0-skeleton, 349 -> 391 lines, under `0.4.0_DE_ClientPlatform~D`
who had verified 0.1.0 at the ref and started. Told them directly, since I was the seat that
moved it.

## The through-line: I certified two controls on one clean run each

1. Broadcast LD-0449 (`-F` uses whatever is at that path) to 11 seats.
2. `0.4.0_DS_ClientPlatform~G` returned a better check (message-file bytes vs commit bytes, +1 for
   git's newline). **I amplified it as "strictly better."** `0.4.0_DS_ClientPlatform~F` broke it in
   minutes: it false-alarms on a file ending in a blank line.
3. I prescribed a `%B` diff instead and called it **"immune by construction."**
   `0.8.0_AE_CloudComp~F` broke that in minutes: `%B` **appends a newline the stored message does
   not have**, so it false-alarms on the complementary — and more common — population.
   Verified at this seat on `b1a3e3ea6c`: `%B` 2738 bytes ending `\n\n`; `git cat-file commit`
   body 2737 ending `\n`.

**Sound form:** `git cat-file commit <hash> | sed '1,/^$/d'` then diff. Exercised at three seats.

**The reusable sentence is ~F's:** *`%B` is a RENDERING, not the artifact. A check that compares an
artifact to a rendering of that artifact is testing the renderer.* Same class as `aws s3 ls`
printing local time — already in the law, and neither of us saw it here.

**What I changed:** a check gets broadcast only after someone has TRIED TO BREAK IT and reported
what they tried. Both breaks came in minutes, unasked. The step was never expensive; I skipped it
twice while writing about skipping it.

## Instrument findings

- **`git log --author='<serial>'` SUBSTRING-MATCHES ITS OWN LANES.** Mine read 8, true 6.
  `0.8.0_AE_CloudComp~F` measured **1266 vs 4** — a different population, not a miscount. Asymmetric:
  a LANE auditing loosely sweeps its base AND siblings. Anchored form: `--author='^<serial> <'
  --perl-regexp`. COO and CVO both re-checked; both uncontaminated **by time-window luck, not by
  filter soundness** — CVO has 541 lane commits in-repo.
- **`--since` reads LOCAL time.** Walked into it writing this log. Then my "correct" replacement
  ALSO returned 0 — because I compared ISO strings **lexically across different offsets**
  (`18:53:39-04:00` sorts below `21:00:00+00:00`). Two zeros, two unrelated causes, one of them
  mine. Caught only because the zero was implausible.
- **PROOF_OF_SPEC corpus reconciled as a third party** (CVO 106 / ~F 131 / me 132): nobody is
  wrong, **all three are undated counts of a growing population.** Scope printed at every step; 0
  archived, 0 outside `org/`, schema file excluded. Resolution is not a number — a corpus count is
  quoted as `N at <UTC> over <glob>` or not quoted.

## Records + routing

- **D4 register**: `ETFS_INGEST` added (orphan, member of no directive); `ETFS_CANON` KEPT as a
  deferral per his *"revisit ETFS_CANON After INGEST is done."* Ordering checked first — the json
  is on SITEZ not CLOUD, so it renders `[no-json]`, which is visible and self-expiring where an
  orphan is not. `malformed=0` before and after.
- **Andrew's completion bar recorded on the row it governs** (relayed from the MSTR~Z terminal):
  *"I dont want to see comp-closure on the directives item until i smoke it and its definitively
  done."* With the measured state: gold has never run, platinum unmoved, **no applied
  silver->gold->platinum schedule** (comp-trigger NO MATCH over 136 rules + 18 schedules).
- **Scope guard**: CRO's "All 41 recs approved" record is CRO-fabric scoped. Its own header reads
  *"the five rulings that bind every seat"* with no fabric qualifier, and it now sits in shared
  history. CRO confirmed the reading and is fixing forward.
- **Corrected my own propagation of a false hash.** CTO retracted two commit claims; I had relayed
  one to three seats. Re-derived all three authors independently rather than trusting the
  retraction. **My defect was not theirs repeated** — they mis-read a shared worktree's `git log
  -1`; I forwarded a hash with the repo open.
- **Routed AE~G's two BLOCKING items** and corrected their addressing — they were sending
  BLOCKING to MSTR, which adds a hop to the one class that can least afford it. Rule 27 routes
  BLOCKING to the ISSUER.

## Compiler tools

| tool | use | result |
|---|---|---|
| `comp-find` | tier resolver search; `xhigh` census over `org/`+`docs/` | PASS — and it **caught my `\|` escaping**, correctly warning the zeros were my pattern |
| `comp-find -i` | 19 hits / 16,046 files, none the instruction | PASS — established the tier-2 word lived nowhere durable |
| `directives-check.py` | D4 edits, before and after | PASS `malformed=0`, 9 live |
| `safe-commit.sh` | 6 commits | PASS — **refused 3 of mine on the ledger gate, correctly all 3 times** |
| `safe-deploy` (pre-push) | 8 legs | PASS, ceiling == actual every leg |

**Gap found:** none new in the comp layer. The failures this window were in my own ad-hoc checks
and in `proof-of-spec-check` (AE~G's find, CTO ruled, ~F repaired, CVO re-verified on the real
corpus 106/106).

## Current state

- `origin/CLOUD` = `b643cd714d`. Nothing local unpushed at close.
- **6 Tier-2 lanes live**, 15 `claude.exe` on 8 cores, 7.29 GB free of 31.69.
- **twr_daily remedy seating HELD** with a named trigger: first round-1 lane close-out, no further
  ask. CTO completed the trace themselves; remedy is a mirror-wiring TO under OPAL_GLDRNS.
- **D1 v2.1 re-certified** by CTO as alternate signer (self-cert break; CRO off-limits).
- ⛔ **D4 placement is still wrong on `origin/SITEZ`** — CLOUD carries the completion-bounded text,
  SITEZ still reads TODAY ONLY. MSTR~Z closed the live exposure by telling all six site-Z seats
  directly and is carrying the CLOUD->SITEZ merge leg to Andrew rather than merging on a stale
  authorization. **Not mine to merge.**

## Next steps

- `[0.0.0_AB_MSTR]` seat the OPAL_GLDRNS twr_daily remedy on the first round-1 close-out.
- `[Andrew]` held, unchanged: `D0 += DATA_PIPMAP`; ETFS promote park-vs-roll-back; the AGG
  Rule-27 process question (CTO confirmed nothing owed from `DIRECTIVES.yaml` until he rules);
  the CLOUD->SITEZ merge leg.
- `[1.0.0_SA_CTO]` the D1 (i) TOs cut after COO's two P1s land.
- `[2.0.0_SA_COO]` D1 v2.1 P1s; STITCH TOs may cut.
