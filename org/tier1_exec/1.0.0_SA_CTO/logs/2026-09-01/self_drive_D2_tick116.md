# /self-drive D2 — tick 116

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~13:1xZ
**Ticks covered:** 112–116 · **Carrier:** `org/XXX.md` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO`

```
COMPLETION: 2 of 10 -> NOT DONE                          ledger: 33 -> 34
  complete: ADVI_BDPLAT_RESTORE, ADVI_49FSRC
  active:   OPAL_ADVIPOINTERS ADVI_INSURE ADVI_STITCH ADVI_PERFRP ADVI_COTKEY ADVI_49F
            ADVI_BDPARITY ADVI_ROSTERCOLS
```

---

## The driver act: I ruled a call against MY OWN prior ruling, and it was the one thing blocking a lane

`0.4.0_DS_ClientPlatform~N` closed 91542 with *"Nothing else at this seat is unblocked.
`1.0.0_SA_CTO` holds 91420."* **The block was a ruling this seat owed on its own 87535.** Issued at
91555, 4 of 4 DELIVERED.

### RULED (B) — the ruling is amended, the code is not

```
  canon-json-v1 = sha256( canon_json_utf8 + lib_hash16 )     name STAYS v1
  87535 named only sha256(canon_json).  a07:293-296 computes the composition.
  NO code change · NO served value moves · NO rollback condition · V-1 FAIL -> PASS on the re-file
```

`v2` **refused**: every value ever served under the name was produced by the (B) composition, so a
`v2` moves nothing in value while splitting the claim vocabulary and implying to a later reader that
the served values changed.

**(A) refused on two MEASURED grounds**, not on preference: it would move a served field on 2 tables
a second time and restart V-4's two-fire clock — and **1,264 of 3,874 rows today classify by
`regex-name`, i.e. by the lib and not by DynamoDB at all.** A lib change **is** a classifier change;
a field named `_classifier_vintage` that cannot move for one is misnamed.

**Grounding, and it is on a DIFFERENT PLANE from the raising seat's** (Rule 22): DS~N's evidence is a
runtime re-derivation in a separate process over the live substrate; mine is a source read of
`a07_dim_asset_classification.py:293-296` at HEAD. Re-running its re-derivation would have been
repetition wearing corroboration's name.

## ⭐ The two things the driver added that nobody in the thread had

### 1. The carrier census is SIX, not four — and the uncorrected one cites this seat as its authority

| # | carrier | state |
|---|---|---|
| 1 | ruling 87535 (mine) | WRONG — amended |
| 2 | cell C02-g-13 V-1, decomp amendment `:210` | WRONG, **faithful** transcription of (1) |
| 3 | ⛔ `a07_dim_asset_classification.py:146-162` | **WRONG, AND NAMED BY NOBODY** |
| 4 | proof_of_spec V-1 `output_evidence` | WRONG — seat had already named it |
| 5 | change_management deploy ledger `:119-123` | **already corrected** (measured by me this tick) |
| 6 | `PROOF_OF_SPEC_A07_CLASSIFICATION_DIM_20260811.json:71` | **CORRECT — and it is the OLDEST** |

Carrier 3 asserts *"THE VINTAGE IS A PURE FUNCTION OF THE SUBSTRATE"*, enumerates rules covering only
the JSON canon, and **at line 147 cites 87535 — this seat's own ruling — as its authority.** A ruling
propagated into source as a comment. Correcting the ruling without the comment leaves the wrong
definition in the file the next implementer edits: **the `/watcher` doc's six-week failure, exactly —
a correction is only as complete as its LAST SURVIVING CARRIER.**

### 2. The OLDEST carrier was the correct one, and it supplies a limb nobody filed

>> Carrier 6 is dated **2026-08-11 — nineteen days BEFORE this seat ruled** — and reads at line 71:
   `vintage = sha256 over (DDB content payload + lib sha 943ff55e2e7bb16d)`.
   **THE ESTATE DOCUMENTED THE COMPOSITION CORRECTLY BEFORE THE GATE RULED IT WRONG. The ruling was
   NEWER than the accurate record, and being newer it overwrote it in every reader's eye.** <<

**And it is evidence, not just irony.** That `lib sha` is `943ff55e2e7bb16d`; today's is
`845dd86adb3c86dc` (`CLASSIFIER_LIB` last changed 2026-08-12 @`bd2a8f854a`). **The lib term
demonstrably held a different value before 08-12 — so the vintage moved on that date with no
DynamoDB change whatsoever.** The affirmative case for (B), stated as a measurement.

## Fabric state, ticks 112–116

- ⭐ **`2.0.0_SA_COO` IS BACK — and I had told Andrew the dispatcher was gone.** `LIVE, last seen 7s,
  PID 29020, mid-startup` (DS~N 91548, 13:1xZ), corroborated by a **different** instrument (its 91543
  returned DELIVERED, not QUEUED) and by **a third** — my own 91556 to that serial, DELIVERED. `3.0.0_SA_CVO`
  self-corrected the same claim at 91552. **A liveness claim has a vintage like a number does**, and
  mine ages the same way — this one is stamped 13:1xZ.
- `ADVI_49F.c02-VINTAGEDIGEST` **V-4 MET**, graded by CVO with no objection (91539), verified at source
  with a negative control. Then **the author amended it against its own filing** on CVO's s.4: the
  two-fire limb alone does not exclude a hardcoded constant; the outside re-derivation is the limb that
  does, and it had been filed under *"not counted in the acceptance."* Amendment verified additive.
- ⭐ DS~N's own transferable form, worth keeping: **"after assembling an acceptance, name the cheapest
  hypothesis that fits ALL of it, and find which single piece of evidence kills that one."** The
  unchosen perturbation — the limb it was proudest of — is precisely the one a constant survives.

## RESERVED cards still at Andrew

- D3's order relative to D8.
- Whether the flow-ingestion defect widens the ruled 22.

## Compiler Tools

`directives-check.py --json` + a python completion scan over 10 member JSONs (denominator printed) ·
**source read** of `a07_dim_asset_classification.py:146-162, 293-296` at HEAD · `comp-find "lib_hash"
--corpus all --files` for the carrier census (24 of 24, one page, no `head`) · `comp-read` on the
deploy ledger and on the 08-11 proof instance · `git ls-remote` for the push state.

**PUSH STATE, MEASURED:** LOCAL @`9eecb8cb54` + this log. `origin/CLOUD` = `5b28a64573` (ls-remote 13:1xZ).

**State:** `ARMED` · next tick on the cron.
