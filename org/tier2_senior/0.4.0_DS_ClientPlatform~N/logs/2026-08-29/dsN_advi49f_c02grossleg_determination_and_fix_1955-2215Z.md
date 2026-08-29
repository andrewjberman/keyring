# `0.4.0_DS_ClientPlatform~N` — ADVI_49F.c02-GROSSLEG: determination, fix, and one live hazard

**Date** 2026-08-29 · **Window** ~19:55–22:15Z · **Archetype** INVESTIGATE→BUILD
**TO** `ADVI_49F.c02-GROSSLEG` (the only TO this seat holds) · **Cell** `C02-g-1` · **Issuer** `2.0.0_SA_COO`

---

## Current State

**G-1 through G-5 are all closed. The fix is on origin and DEPLOYED. The determination that justifies
it is LOCAL ONLY. And a BUILD-ONLY cap was overrun by the window's deploy leg, which is the one live
item.**

| criterion | status | instrument |
|---|---|---|
| G-1 DETERMINE | **PASS** — outcome **(a) CODE WRONG**, accepted by `2.0.0_SA_COO` 83867 | source re-derivation at a named pin + a ratified-definition citation + two sibling implementations + a live signed measurement |
| G-2 CONVENTION GATE | **N/A-BY-CONSTRUCTION** — NOT-TRIGGERED (fires only on (b)) | (b) refuted by citation, (c) by measurement |
| G-3 FIX | **PASS** | 2 sign sites + 2 docstrings; linking method untouched, proven by a census of the DIFF's changed lines |
| G-4 SIGNED GAP | **PASS** | signed both legs, no `abs()` on the gap anywhere |
| G-5 CARRIERS | **PASS** | 2 DELIVERED / 0 QUEUED / 0 REFUSED; third carrier verified already annotated by its author |

`proof-of-spec-check … G-1,G-2,G-3,G-4,G-5` → **VALID, violations=0** (positional id form; rc read
UNPIPED, because a piped rc is `tail`'s).

## The finding, in one paragraph

`c02_twr_engine.py:286` built `cf_gross = cf_net - fee_cf` with `fee_cf` already negative, and
`:190-191` SUBTRACTS `cf` from `emv` — so the fee was removed a **second** time and `r_gross` came out
**below** `r_net` by exactly the fee rate. The ratified sentence
(`SPEC_49F_GROUP_C_TWR_ENGINE_20260811.md:34` @`bfaa0a6e6e`, approved by `1.0.0_SA_CTO` 60281) says
*"gross adds back FEE-MANAGEMENT"*, and an add-back RAISES a return. **The half that was right is what
located the defect:** `cash_cf` at `:276-282` admits only `(EXTERNAL, INTERNAL)`, so the fee never
entered `cf_net` and `r_net` was correct all along — the file implemented the ratified sentence's
first half correctly and its second half inverted.

## What actually decided it

⭐ **The strongest evidence was the piece that is not another reading of the subject file.** A
`comp-find 'add.back'` sweep wide enough to leave the 49F tree surfaced
`runners_inf/c02_twr_engine.py` and `runners_cot/c02_twr_engine.py` — **two sibling firms implementing
the same sec8 sentence, both putting the add-back on EMV, one carrying an executable fixture asserting
`(gross - net) == +addback/100`.** A grep scoped to `runners_49f` would never have found them. Ruled a
legal CONVENTION read (not the cross-firm DATA law) by `2.0.0_SA_COO` 83867.

⭐ **And one stored account-day settled it with no convention argument at all** — `0062640151` @
`2025-12-10`: `emv == bmv - 46.31` exactly, so the market was flat and the fee was the only mover.
Correct gross is **zero**; stored was **−2.13%**, exactly twice the fee rate.

## ⛔ The one live item — BLOCKING × ARMED → DISARMED, not remediated

**The BUILD-ONLY artifact is on the deployed plane.** Verified at the served object, not on the
report: `s3://opal-data-49financial/_code/c02_twr_engine.py`, `2026-08-29T22:02:12Z`, ETag
`2f709fc66ed6cb2e9a853704ef0e83c6` == md5 of the local fixed file. The deploy was **not this seat's
act** — it rode window 55's deploy leg, which reads the tree and cannot know a cell's scope cap.

> **The next scheduled `c02` fire emits `r_gross` with the corrected sign into a table whose 534
> partitions all carry the inverted one. Both are labelled `r_gross`; `schema_version` is still
> `"1.0"` and no manifest field carries a gross-leg vintage, so nothing in the artifact distinguishes
> them.** Nothing is corrupt yet. What the deploy removed is the property that made cell §4 safe to
> defer — that the corrected leg could not appear anywhere until someone decided it should.

Owner named same-turn: `2.0.0_SA_COO` (issuer), `1.0.0_SA_CTO` (serve-gate limb). **83979 DELIVERED**
to `0.0.0_AB_MSTR`; 83980/83981/83982 QUEUED. Addendum committed at `a9ca90b54b`.

## Blockers

**None at this seat, and the two open items are both out-of-lane — named per Rule 29:**

1. **[`2.0.0_SA_COO` / `1.0.0_SA_CTO`]** the mixed-vintage disposition above. Rolling back a deployed
   served object needs sign-off this cell does not give me; ruling a re-emission range is the issuer's.
2. **[`0.0.0_AB_MSTR`]** `cee023004c` is **LOCAL ONLY** (`merge-base --is-ancestor` → NO against
   `origin/CLOUD 0ba022953e`, ls-remote). It missed window 55 by minutes. **Not pushing** — publication
   is MSTR's and the final window is closed.

## Commits

```
946b5c5a3c  the G-3 FIX          ON ORIGIN, DEPLOYED   authored by 0.4.0_DS_ClientPlatform~V
                                                       ("NOT THIS SEAT'S WORK") during the wind-down
                                                       sweep; bytes are this seat's and were verified
                                                       identical to the tested state before I relied
                                                       on them (`git diff 946b5c5a3c -- <files>` EMPTY,
                                                       13 passed against the committed bytes)
cee023004c  determination + proof-of-spec + evidence    LOCAL (ls-remote read)
a9ca90b54b  ADDENDUM 1, deploy state corrected          LOCAL (ls-remote read)
```

## Compiler Tools

| tool | invocation | result / what it did |
|---|---|---|
| `comp-find` | 6 sweeps: `--name 'SPEC_49F_GROUP_C*'`; `'gross-of-fee\|gross of fee\|gross_of_fee'`; `'add.back'`; `'SPEC_49F_GROUP_C'`; `'PRF-inv-6'`; `'r_gross' data/assets/scripts` | **The load-bearing tool of the whole determination**, and it earned it by breadth: the `add.back` sweep (86 hits / 130,258 files) is what surfaced the two sibling-firm engines — the single best piece of evidence, and one a 49F-scoped grep structurally could not find. Denominators printed on every sweep; `--corpus all` throughout; **no census headed.** |
| `comp-pipescript io` | `comp-pipescript io c02_twr_engine.py --pipeline advi` | rc=0, `Group: C \| Order: 240`, `READS/WRITES (none detected)` **with its own WARN that manual review is required** — c02 takes paths from argv and emits via `runner_common.emit`, so the static reader cannot see them. **Read as a denominator-zero, not an absence.** Flagless refused rc=2 as designed; `--pipeline data/assets` refused with the valid choice list, which is how `advi` was resolved. |
| `.tools/commit-gate.sh` | on both source files | `OK: pre-commit gate clean for 2 of 2 file(s)`. Later **BLOCKED** the first deliverables commit on ruff E702/F401 in the two evidence scripts — correctly; fixed by splitting semicolons, then re-ran both instruments to confirm identical output before committing. |
| `pytest` (as an instrument, not a formality) | 4 runs: baseline / STEP A / STEP B / STEP C, + once against the committed bytes | The falsifier. **Baseline was 12 passed / 1 FAILED and the failure was at the schema guard, not the assertion** — the fee arm had been *dead*, not merely wrong, since `cab1f8bff9`. STEP A 13 passed (arm reaches the field under test), STEP B FAILED on the assertion (the falsifier `2.0.0_SA_COO` 83888 required), STEP C 13 passed. |
| `proof-of-spec-check` | positional id form, 4 iterations | VALID, violations=0. **Caught two of my own errors:** my `(cell C02-g-1)` suffix broke `decomp_ref.to_ref` so it no longer resolved (a non-resolving declared reference is a false citation), and adding `cell_ref` to each criterion turned violations=0 into 5 because the acceptance item is a closed set. |
| `git` (as an evidence instrument) | `rev-parse HEAD:<path>` vs `hash-object`; `show <pin>:<path>`; `merge-base --is-ancestor`; `diff <a> <b>` | **The pin-plus-blob discipline is what made the determination survive a shared worktree**: HEAD moved four times underneath this session (`bfaa0a6e6e → 8b56c0651d → 68a513db3f → 65e0d13e64`) and every citation still resolves. Also produced the "linking method untouched" proof — `link_geometric` appears in the diff exactly once, in a hunk *header*. |
| `aws s3api` / `s3 cp` | 21 partition pulls; `list-objects-v2` on `_code/` | Real-data legs for G-4, and the ETag read that caught my own record going stale. |
| `comp-which` | startup A.3 | `PATH: 105 of 105 resolve bare`; the EXERCISE half **timed out at 120 s** on the natural-language form and was re-run bounded to get the banner. Recorded because A.3's own doctrine is that resolution is not execution. |
| `.tools/audit-archive-invoker.py` | startup A.2 | rc=1, 2 findings — **both the known OWNED-UNTIL-`rv0057-f001` pair named in `org/XXX.md`**. No third finding, no shrink/absence row, so nothing surfaced and nothing re-filed. |

## What I would tell the next seat

**A wrong arm and a dead arm are different failures, and this file had both.** The wrong sign was
visible by reading; that the arm had not executed since `cab1f8bff9` was only visible by *running the
baseline first*. Had I flipped the assertion and gone straight to the fix, the suite would have gone
green and I would have reported a falsifier that never fired.
