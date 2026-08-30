# The 9-digit keys are a second custodian's grammar, and the departures left the feed 18 months ago while nothing downstream ever counted them — 0.4.0_DS_ClientPlatform~E

**Date:** 2026-08-30
**Task Order:** D3_MODELOVERLAY.TO-D3.1b (INVESTIGATION, report-do-not-fix)
**Status:** COMPLETE
**Window:** 02:09–03:20Z

---

## Objective

Answer the two halves of TO-D3.1b on evidence: what the 13 distinct 9-digit SmartX keys
(`KEY_OUTSIDE_ACCOUNT_GRAMMAR`) actually ARE, and what state the `KEY_VALID_ACCOUNT_ABSENT`
departure accounts are in — including, explicitly, whether anything downstream still counts
them. Report and route; remediate nothing.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `'smartx_bd_join_disposition'`; `'fact_allocation_account_map' --all --files`; `'dim_identity_crosswalk' --all --files`; `'in_account_universe' --all --files` | PASS with denominators (58/131,406 · 257/131,762 · 148/131,783 · **2/131,804**). The last one IS a finding: `in_account_universe` occurs twice in ONE file — the writer — so the residual flag has zero readers. The `[DEF]` band separated the 5 real definition-site consumers of the allocation map from 142 DOC-band mentions in one call, which made the consumer set *enumerable* rather than sampled. |
| `comp-which` | `"how do I validate a proof of spec instance"` | Honest NULL — "NO CURATED RULE MATCHED", with its own banner warning the 3 candidates scored below the vetted band. Took the warning rather than the top hit (`comp-lease`, 0.63, unrelated) and found the validator by listing `.tools/`. Recorded because the refusal was the useful output. |
| `proof-of-spec-check.py` | positional ids `D3.1b-1..D3.1b-5`, run unpiped | **First run INVALID rc=1, 6 schema violations. Final run VALID rc=0.** |
| `comp-system` | regen of `06_current_state.{md,json}` | PASS — discharged the two-phase override in-session. |
| boto3 S3/DynamoDB (read-only) | 540 + 659 fact_acc partitions; allocation map ×2 vintages; roster; 23 gold tables; 46 `fact_account_detail` partitions; full DynamoDB scan | PASS. |

**`comp-pipescript` / `comp-validate` NOT run, with the reason:** the DS role minimums attach to
touching or running a gold script. This TO is INVESTIGATION under a read-only cap — no script
edit, no deploy, no artifact emission to validate. The estate's own instrument
(`a06_dim_identity_crosswalk.py`) was **read at source rather than executed**, because executing
it would emit.

---

## Work Completed

### 1. Part 2 — the departure set (done first, per the GO's order over the face's)

Both accounts resolved to a state: **departed from the custodial feed 2025-02-26, not closed**,
with the evidence pointing to a Schwab→Vanguard custodian transition. Contiguous presence in
161 of 161 partitions through 2025-02-25, absent from all 379 since, 540 of 540 read.

**The positive control is what made the read honest.** A control account drawn from the current
universe appears in only 173 of 540 partitions — which looks like a lossy instrument until its
*shape* is read: it enters 2025-12-19 and is contiguous since. The universe is an accumulating
roster, so absence-after-contiguous-presence is a real exit. Without that control the 161/379
split was uninterpretable and I would have been reporting the instrument rather than the world.

### 2. D3.1b-4 — the downstream question, answered by scanning artifacts

Scanned all 23 dated gold tables, every column of each newest partition. The pair appears in
exactly 2 (both non-serving, both flagging it) and **zero** in every canonical/serving table.

**Reading the code would have produced the wrong answer.** b04 documents that it "carries
residual rows, never dropped" — true, and irrelevant: `account_model_membership` **has never
emitted** (0 data keys in S3). A code-first trace stops at the docstring.

### 3. Part 1 — the 13 keys characterised

A second custodian's grammar: FMT CO / FMTC registrations, 18 rows / $12,293,768.23. The
evidence is `account_name` — a column the contract's own instrument never selects.

### 4. Findings routed to their owners, not fixed

Four, including declarative drift on a RATIFIED contract and a falsified grounding clause in one
of its rejections.

---

## Decisions Made

- **Took the GO's reporting cap over the face's**, and said so rather than choosing silently: the
  face says cc CRO, the GO (later, same issuer) says nothing to CRO. Later + more restrictive
  binds; flagged in the ACK so COO can restore it.
- **Scoped the retraction of the `OTHER_CUSTODIAN` rejection to the refuted clause only.** Its
  evidentiary ground ("no evidence names a custodian") is falsified; its Rule 24(iii)
  cause-not-outcome ground stands alone and sustains the rejection. Retracting the whole thing
  would have manufactured a case for an enum change the taxonomy still forbids.
- **Left the served-AUM channel UNRESOLVED rather than inferring it.** "SmartX asserts open,
  therefore the vendor counts them" is available and is not a measurement. The planes do not
  overlap in time (served latest daily 2026-01-12; map history begins 2026-07-14), so the clean
  $2.83M discriminator cannot be run.
- **Did not decide D3.1b-2.** Framed both readings with the remedy each selects, named the owner,
  said it reaches Andrew.

---

## Files Modified

| File | Commit |
|---|---|
| `deliverables/D3_MODELOVERLAY.TO-D3.1b_INVESTIGATION_20260830.md` | `e4a4f3cbee` |
| `deliverables/D3_MODELOVERLAY.TO-D3.1b_PROOF_OF_SPEC.json` | `e4a4f3cbee` |
| `infra/system/06_current_state.{md,json}` | `383b122b87` (override discharge) |

**PUSH STATE: LOCAL @`383b122b87`** — `origin/CLOUD = 6e0e6e506582b1c759b7fbac3ea6ab2ff0437cac`
by `ls-remote` at 03:1xZ; `git branch -r --contains e4a4f3cbee` returns empty. Rides the next
integration window; the push is the integrator's. This claim ages the moment MSTR runs.

---

## Blockers

**None.** The TO is complete on all five criteria. Two items are *bounded unknowns* rather than
blockers, and both are named in the report with the reason they cannot be closed from this seat:
whether the Vanguard relationship persists today (needs a custodian call — outside the cap), and
whether the vendor-computed model AUM includes the pair (no account decomposition; planes do not
overlap in time).

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Investigation report | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D3_MODELOVERLAY.TO-D3.1b_INVESTIGATION_20260830.md` | COO (issuer), CVO (grades), CTO (contract owner, reads on its tick) |

---

## Current State

TO-D3.1b COMPLETE, proof instance VALID rc=0 (measured unpiped), both parts reported to
`2.0.0_SA_COO` + `3.0.0_SA_CVO` at msg-ids 84994/84995. Nothing remediated: the ratified axis is
untouched, no enum value proposed, no data corrected, no vendor call made. An audited
`STRUCTURAL-TWOPHASE/proof-of-spec` override was taken at `e4a4f3cbee` and **discharged in the
same session** at `383b122b87`.

Delivery ledger clean under the new LD-0480 `by`-field predicate: 12 of 12 rows READ, every stamp
`by 0.4.0_DS_ClientPlatform~E`, zero foreign stamps.

---

## Next Steps

1. **[2.0.0_SA_COO]** Route D3.1b-2 (the 49F custodial-scope question). It selects between two
   different remedies — upstream feed scoping vs a second universe source — and my read is that
   it reaches Andrew. Nothing in D3 should size that remediation until it is answered.
2. **[1.0.0_SA_CTO]** Two findings against the RATIFIED `smartx_bd_join_disposition` v1.0: the
   `as_of_universe` comment names the wrong account (substance unaffected; all its numbers are
   correct), and the `OTHER_CUSTODIAN` rejection's evidentiary clause is falsified while its
   24(iii) ground stands. Both are amendments to a ratified artifact — a taxonomy act with an
   owner, which is why I routed rather than edited.
3. **[0.4.0_DS_ClientPlatform, any lane]** Re-read `0042708566` on the next business day. It
   entered `KEY_VALID_ACCOUNT_ABSENT` on 2026-08-28 with a one-day absence; if it clears, the
   class is back to 3 and nothing is owed.
4. **[3.0.0_SA_CVO]** The `in_account_universe` observation: the residual flag has zero readers
   across 131,804 files. Not wrong today; unexercised, which is the failure mode that surfaces
   when a future consumer joins the crosswalk without it.
