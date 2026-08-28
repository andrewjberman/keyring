# 0.4.0_DS_ClientPlatform~Z — D1_CATVIEWS pre-stage scorers (TM1-AC1 + CATV-TON1-AC3..AC7)

**archetype:** IMPLEMENT

**Session:** 2026-08-28 20:14Z–21:1xZ · **Seat:** `0.4.0_DS_ClientPlatform~Z` · **Device:** site Z
**Issuer:** `2.0.0_SA_COO~Z` msg 13861, amended by 13869 / 13877 / 13885
**Commit:** `d6ef49905f` — **PUSH STATE: LOCAL** (`ls-remote` read; `origin/SITEZ` = `6c00aebdbc92`;
positive control `bc9d11dd8e` reads ON ORIGIN, so the is-ancestor probe discriminates)

---

## Current State

**Six pre-staged scorers BUILT, SELF-TEST-GATED, COMMITTED.** The subjects do not exist yet — all six
criteria score against a SERVED artifact the next scheduled fire produces. Per the mandate: build the
instrument, prove it discriminates, commit, stop.

| criterion | state | instrument |
|---|---|---|
| `TM1-AC1` | **STAGED** | tri-state L2 walk under `Models`, STRICT + DECLARED readings |
| `CATV-TON1-AC3` | **STAGED** | structural A/B/C + literal D (`NA_BY_DATE` off-date) |
| `CATV-TON1-AC4` | **STAGED** | structural incl. independent `total_aua` anchor + literal |
| `CATV-TON1-AC5` | **STAGED** | both limbs (gone where false / kept where true) |
| `CATV-TON1-AC6` | **STAGED** | per-artifact `D1-inv-4`, full + rendered sums |
| `CATV-TON1-AC7` | **STAGED** | served → `source_keys` → gold `_provenance.trigger` |

Self-test: **22 checks, ALL OK, rc=0**, both directions. Live run today: **gate refused, rc=3,
nothing scored** — G1=OK, G2=NO on 4 of 4 scopes.

---

## What Was Done

1. **Startup.** `/watcher` — NOT REGISTERED at load, no orphan for this serial (4 live watchers, none
   mine). Registered, armed Monitor `bplsjz1da`, drained 2 unread; 6 further messages arrived and were
   ACKed in-session (13848, 13861, 13869, 13875, 13877, 13882). `org/XXX.md` startup read.
2. **Resolved the served plane by measurement, not by brief.** The TO calls the *gold* object "served";
   the brief names `platinum/...`. Neither guess was used: the CVO control's own
   `_provenance.written_by = opal-assets-mdpf-portal-publisher` settles it. Served =
   `s3://opal-data-portal-v2/platinum/mdpf/{scope}/category-views.json`, fixed keys, 13:50:5xZ.
   A first probe of `opal-data-assets/portal/platinum/` returned `None` — treated as OUT-OF-CORPUS,
   not absence, and re-pointed.
3. **Closed an open precision.** 13869 s.2 / 13875 s.2 both said the control was "NOT claimed
   byte-identical to an `s3api` read — that comparison was not run." Ran it: **4 of 4 scopes, size and
   sha256 IDENTICAL** (denominator 4). Retired by the issuer in 13885 s.2 and by `3.0.0_SA_CVO~Z` in
   13882 s.3. **A COMPARISON, not a second capture** — nothing committed, no second carrier.
4. **Built + self-tested + committed the scorer.**
5. **Surfaced two findings** (13879/13880/13881), both accepted; AC3 amended @`43efa180f1`.
6. **RAVC close** to `2.0.0_SA_COO~Z` + `3.0.0_SA_CVO~Z` (13909/13910), 2 DELIVERED / 0 QUEUED /
   0 REFUSED, denominator 2.

---

## ⭐ The Finding That Changed Another Seat's Scoring Plan

`CATV-TON1-AC3` reads *"the delta must equal $22,794,766.25 exactly — not approximately."*
That figure is the sum of two **market-valued** balances at `as_of 2026-08-27`, measured off
`aggregate-aua-timeseries.json` (`by_model[].model_value`, 455 dates):

```
  as_of        opal_div_sma        opal_growth_sma      SMA total
  2026-08-27   18,783,379.8116      4,011,386.4409    22,794,766.25   == the TO's figure
  2026-08-26   18,929,318.4129      4,034,142.4692    22,963,460.88
  2026-08-25   18,906,505.6493      4,076,231.4513    22,982,737.10
```

The arithmetic reproduces **to the cent** at 08-27 and only there: `non_model_aua = 290,426,813.47`
equals the served `Client.aum` (unnetted — the pre-fix signature), and minus the SMA total gives
`267,632,047.22`, AC3's own expected Client-after.

>> **ARITHMETICALLY RIGHT, TEMPORALLY WRONG.** The "after" comes from a fire whose `as_of` is not
   08-27, so the delta differs by ~$170k–$250k. **A scorer applying AC3's literal text to tomorrow's
   artifact returns FAIL ON A CORRECT FIX** — the same false-verdict shape this TO was cut to fix,
   pointed the other way.

**And the acceptance date is a SATURDAY** (2026-08-29). Every brief in the thread, including this
seat's own reading, had said "tomorrow's fire" without naming the day. `3.0.0_SA_CVO~Z` — the seat
that scores tomorrow — recorded that it holds CLAUDE.md's trading-calendar NEVER, cites it at other
seats, and had not applied it to its own plan.

**Remedy adopted verbatim by the issuer:** A/B/C exact-to-the-cent on any `as_of`; D scores the
literal constants only at `as_of 2026-08-27` and reports **`NA_BY_DATE` — never PASS, never FAIL**
— otherwise. Nothing relaxed to "approximately"; what changed is what it is exact *against*.

**⚠ `CATV-TON1-AC4` carries the SAME defect** ("byte-identical before and after" assumes a shared
`as_of`). Flagged to the issuer rather than assumed covered by the AC3 amendment.

---

## ⛔ The Defect The Self-Test Caught In My Own Guard

The first version scored AC4's *"Client is UNNETTED"* as `Client == non_model_aua`, with
`_non_model_aua()` **deriving non_model FROM Client** when the field was absent. The planted mutant
moved cottonwood's `Client` by $1.00 — and **PASSED**, because the mutation moved *both sides* of the
equality. A guard comparing an expression to itself.

**It would have shipped.** The mutant existed only because AC4 and AC6 *correctly pass on the pre-fix
control* — so the control alone proves nothing about them, and without the mutant arm the criterion
would have looked verified. The same vacuity silently infected AC3's limb B.

**Fixed** by giving the netting limbs an anchor the mutation cannot move: `total_aua` (an independent
field on the same artifact) and `non_model_aua` from the **aggregate-aua-timeseries** — a *different*
artifact, since a second read of the same file is repetition, not corroboration. With no independent
source the verdict is now **UNSCOREABLE**, never a vacuous PASS. The mutant is retained permanently.

---

## Two Design Facts Measured, Not Assumed

- **AC7 needs TWO RUNGS.** The served object carries **no `trigger` field** — only `written_by`,
  `written_at`, `source_keys`, `source_vintages`. `_provenance.trigger` lives on the **gold** object
  (`trigger: "scheduled"`, `process_time 13:30:37Z`). The tool dereferences the served object's own
  `source_keys` to gold. **A scorer looking for `trigger` on the served artifact reports a false FAIL.**
- **The gate is pinned to the DEPLOY, not to a clock.** G1 = `written_by == the publisher` (the right
  *rung*, structurally). G2 = `written_at > 2026-08-28T17:28:29Z` (the corrected code produced these
  bytes). A wall-clock guard does not survive a weekend, a holiday, a skipped fire or a late publish;
  this one does. Self-test proves G1 is load-bearing by refusing a gold-rung doc that *does* satisfy G2.

---

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-which "where is the served platinum category-views object…"` | near-tie, 3 candidates of 80 | **Did not take rank 1** — the router prints "TOP SCORES ARE TIED, the order is not a ranking." Routed to `comp-find`, which answered. |
| `comp-find 'category-views' --files` | 183 hits / **27,870 files** scanned, bands printed | Located producers *and* surfaced `3.0.0_SA_CVO`'s pre-deploy baseline — the control the whole build then pinned to. Denominator printed, not `head`-ed. **⚠ VINTAGE — see the corpus note below; this number will not reproduce.** |

> **⚠ THE 27,870 DENOMINATOR IS VINTAGED AND WILL NOT REPRODUCE.** It was measured under
> `corpus=default` **as that word was defined on `origin/SITEZ` during this session**. Rule 21 gained a
> T1 the same day (Andrew-direct "All approved", landed `9ed33c473e` on `origin/CLOUD`, relayed here as
> msg 13972) which **redefines comp-find's DEFAULT corpus to `all`** — tracked + untracked + gitignored
> minus a printed ephemeral floor, some **168,349 gitignored files at the root** that the old default
> missed. `default` is now the OLD population and `raw` is the only every-file denominator.
> **MEASURED at this seat: `9ed33c473e` is NOT contained in `origin/SITEZ`**, so a re-run on this fabric
> today still returns 27,870 — and a re-run *after* the merge will not, for a reason that has nothing to
> do with the estate changing. A denominator is an artifact, not a summary: this one now carries its
> vintage rather than inviting a false drift reading. Nothing in the scorer depends on it (it reads S3
> via boto3 and the control via `git show`).

> **⛔ RULE 21 T1 ALSO BANS RAW `grep`/`find` IN BASH, AND IT BINDS HERE WITH NO GATE TO ENFORCE IT.**
> `.tools/hooks/comp-tool-hud.sh` @`32d5967277` is on CLOUD only — **nothing on site Z will refuse a raw
> grep**, which is exactly the *"imperative enforced by nobody"* cell Rule 21 already names for raw-`aws`.
> **Do not infer permission from the absence of a refusal.** For the record of what this session ran
> *before* the relay landed: the directory-scoped `grep -rn "platinum" data/mdpf/scripts/` would be
> DENIED under T1 and should have been `comp-find`; the consolidator probe was a **single-file** grep,
> which T1 explicitly leaves ungated (T2, revisit ~09-04). Stating both rather than only the exonerating one.
| `.tools/commit-gate.sh` | **PASS** (py_compile + ds-precommit + ruff py39) | Run twice — the second after stripping 6 non-ASCII bytes, because **an edit after a green run invalidates the run**. |
| `.tools/safe-commit.sh` | rc=0, `d6ef49905f`, `[msg-verify] MATCH len=6280` | `-F` msgfile written by the Write tool (non-shell), unique scratchpad name — not a shared `/tmp` name. |
| risk-reflex (`comp-pulse diff`) | REFLEX CLEAN, 1 file vs 1,417 danger nodes | Fired inside safe-commit; danger map 8.4h old, disclosed. |
| `comp-pipescript io` | **NOT RUN — and why** | This deliverable is a *scorer*, not a gold script; it touches no pipeline tree and writes no artifact. The DS minimum binds on `data/*/scripts/gold/*.py`. Stating the reason rather than leaving it blank. |

---

## Blockers

**None at this seat.** Remaining acts, none of them DS — named per Rule 29:

1. **[the integrator]** push `d6ef49905f`. Out-of-lane.
2. **[the next scheduled fire]** the only event that can lift these six criteria. **No ad-hoc run** —
   it would destroy `TP1AE-AC4`'s discriminator permanently, and is barred by three seats.
3. **[`2.0.0_SA_COO~Z`]** whether `CATV-TON1-AC4`'s text is amended the way AC3's was. **The tool runs
   and prints both readings either way, so no verdict waits on it.**

---

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** score after ~13:50Z. The tool refuses on its own if handed a pre-fix or
   gold-rung object, so a wrong invocation cannot silently produce a wrong verdict.
2. **[whoever reads the fire tomorrow]** count trading days before calling anything broken —
   **2026-08-29 is a Saturday** and Friday is Monday's answer.
3. **[this seat]** nothing unblocked. Available for re-pointing.
