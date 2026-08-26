# ADDENDUM 2026-08-25 23:20Z – 2026-08-26 00:10Z — the migration closed, and four more defects of mine

**archetype:** COORDINATE · **Seat:** `2.0.0_SA_COO` · continues `SESSION_2014Z-2320Z_THE_WAVE_AND_THE_JOIN_HOLES.md`

---

## Delivered in this window

**ADVI_STITCH — all three planes landed, 16,125 keys, zero data loss.**

| plane | landed | independent md5 arm |
|---|---|---|
| raw `bronze_legacy` | 931 / 931 | 679 / 931 — **72.9%, limit STATED not averaged** |
| `silver_legacy` | 7,921 / 7,921 | 7,914, 99.9% |
| gold `reference/bd_legacy_*` | 7,273 / 7,273 | **100.0%** |

Every plane MECE-closed both directions against **pinned manifests**, never a live re-list.

**ADVI_INSURE** — vendor leg live on the 49F principal (first 200s ever for that principal on that
surface), field→call map delivered with **zero** vendor calls, `carrier`/`product` found on a
sanctioned surface, and the **row-selection predicate CLOSED, zero residual**. Bronze + silver landed.

**NFRA_COMPTOOLS** PREFIX-READS complete, ARCH-GATE PASS. **D1_CATVIEWS** finding 4 repaired; finding
1 held on a coordination I ordered. **S5** scoped and correctly NOT shipped.

## ⛔ Four more defects of mine, all caught by seats

1. **My "final" commit-verification command false-passed on hot paths.** `git log -1 -- <path>`
   returns any author's commit on a shared worktree, and — the mode `--author` does *not* fix — **your
   previous commit when the new one refused.** Reproduced on my own history: 3 commits to one file, so
   a refusal on the 4th reads green. **The check is weakest exactly on the paths you touch most.**
   → count delta, verified before broadcasting this time.

2. **My S5 seating at 20:43Z was SENT, never READ.** Three messages undrained at that inbox's top
   level; `read/` holds 4,800, so the drain works. ⛔ **The discriminator was in my own receipt** —
   live seats return `(filesystem + broker + channel push)`; that one returned two terms. I read
   "Message delivered" as the verdict. **And I told another seat it was seated**, giving the seat that
   had correctly surfaced it a reason to stop watching.

3. **D7 and D9 contradicted each other** in one message about one file — D9 named "split across D7" as
   the failure and D7 was the thing that did it.

4. **AC1's silver grammar forked the estate-wide framework.** Writing the TO's literal form would have
   made this **the only producer on that source outside `silver_registry.py`.**

## The mechanical causes — two of my errors were not attention failures

**`to_agent` and `to_agents` report the SAME undelivered condition in opposite registers.** Multi:
`QUEUED`, a named state in caps with "NOT a delivery." Single: the word *delivered*, with the failure
as a **missing substring in a parenthetical**.

> ⛔ **A condition that is a named state in one call form and a missing substring in another will be
> missed in the second form, by anyone, indefinitely.**

**And `safe-commit`'s silence resolved to `set -euo pipefail` + `x="$(cmd)"; rc=$?`** — the shell dies
at the assignment, so the printf never runs. **My symptom was right, my mechanism was wrong, and
recording it UNRESOLVED was the correct place to stop**: conceding would have shipped a no-op as a
fix. CTO's census then found **the site I reported was one of five**, with two gates carrying
*unreachable* BLOCKED branches.

## What the seats did that the record should keep

- **`~Q` built the exact defect they argued to me for two hours earlier** — a gate that only ever
  refuses, 7,273/7,273 on byte-identical data. ⛔ **"Had I only run the mutant arm it would have passed
  and shipped, since a gate that always refuses passes any test that only checks refusal."** They
  caught it by running the *no-op* arm — the one with nothing to prove.
- **`~Q` attacked their own primary oracle unprompted**: the sha256 is computed by their own copier, so
  a self-consistent in-memory corruption passes every layer. They ran an independent MD5 arm and
  **stated its 72.9% ceiling rather than averaging it into a headline.**
- **`~J` (AE) asked before opening a ledger** and found S5 is a **two-lane ship** whose precondition is
  a DS-lane edit. A would-be half-landed deploy became a scoping report at zero cost.
- **`~J` (DS) rejected my framing** — cohort membership is the *row set*, not a column, so **"a table
  with no row-selection predicate is not yet a table."**
- **`AE~B` corrected my instruction**: "align the key" understated it — `layers_expected` (AWS layer
  names) and `layer_dependencies` (module names) are **different kinds**; renaming would fix nothing
  and assert something false.
- **A fifth credit refusal.** `~G` refused a finding that was `~Q`'s — one character apart in the
  serial.

## Rulings issued

D6–D9 silver grammar (all as recommended) · AC3 destination grammar, five decisions · AC5's invariant
to the LANDED set against a pinned manifest · `silver_key()` over the TO's literal form, **on grain
rather than by override** · `--pipeline advi` over a stale TO value · S5 **HELD** · import-closure
Phase 1 authorized, **wiring held** · D1 findings 1+4 only, finding 2 reserved as an unmade ruling ·
decommission owner named on the TO's face.

## ⛔ Still open

- **MSTR has no session.** ~100 commits across both repos behind an integrator-only gate. `~D`
  measured that this is a **visibility gate, not a work gate** — only one seat's productive work
  depends on it.
- **`AE~G`'s data half** — Andrew's.
- **D1_CATVIEWS finding 2** — the $0.01 tolerance. Float noise and a genuine upstream inconsistency
  take **opposite fixes**; I did not make that ruling and said so.
- The 40-candidate two-layer criterion census; the estate-wide **multiple-id-spaces-no-declared-mapping**
  shape (two instances, unrelated subsystems).

## Compiler Tools

| Tool | Result |
|---|---|
| `safe-commit.sh` | 4 commits, all verified by **count delta** with a bogus-author control reading 0 |
| `git rev-list --count --author` | adopted as the commit oracle after two weaker forms failed |
| `git log --all --oneline -- <path>` | used to prove a commit had **never** landed (empty = never committed) |
| `comp-find` / `comp-estate` | via seats under dispatch |

**Gap carried forward:** the single-recipient send receipt buries an undelivered state where the
multi-recipient form names it. Routed to CTO; **not** broadcast — I had already sent four fabric-wide
corrections in three hours and a fifth would have cost more than it saved.
