# ANDREW-DIRECT 2026-08-05 ~1958Z — Orion rep 10 (Noel Soderblom) IS in Inflection scope

**Received by:** `0.7.0_AE_CloudOps~A` · **Channel:** AE~A terminal, structured decision prompt
**Recorded:** 20260805T195853Z · **Broadcast:** COO + CTO + MSTR, same turn

---

## The ruling, as delivered

Andrew was asked, verbatim as posed:

> **"Is Noel Soderblom an Inflection advisor whose book belongs in Inflection's reported AUA?"**

He selected, verbatim as presented:

> **"Yes — add rep 10"**
> *"Treat rep 10 as in-scope Inflection. DS lands the allowlist fix at all 10 sites, chain re-runs,
> both blockers clear. Inflection reported AUA moves $208,794,476.83 -> $209,431,383.43
> (+$636,906.60, 5 accounts). Guard B still satisfied. NNA history preserved, no excusal."*

**FORM NOTE — this was an OPTION SELECTION, not free text.** The words above are the option's
own text, which I authored and he chose; they are not a sentence he typed. The binding content is
the selection itself: **rep 10 is in Inflection scope.** Do not quote the description above as
Andrew's phrasing.

## Scope of what he ruled

**IN scope of this ruling:** Orion rep 10 (Noel Soderblom, rep code `TAN Inflection Lee/Soderblom`)
counts as an Inflection advisor; his accounts belong in Inflection's reported AUA. This resolves
the business question COO had escalated as sovereign-class and on which DS was holding.

**NOT ruled here** (do not widen — surface, do not adjudicate):
- The *durable* derived-predicate design. He agreed with it earlier in the same session
  ("I agree with the durable fix") conditional on the verification, which is now complete and
  filed at `@8e69ae4cb`. The immediate fix is what this ruling unblocks.
- The `INF_D_00` `'unknown'`-handling design (DS recommendation pending at COO).
- The NNA AT-RISK register residual.

## Consequences, pre-verified before the ruling

- Add `10` to `INFLECTION_REP_IDS` at all 10 sites (table: `INF_REPSCOPE_BRIEF_20260805.md` §4).
- Universe 864 -> 869 accounts; AUA $208,794,476.83 -> $209,431,383.43 (+$636,906.60).
- Inside `GUARD_B_AUA` bounds ($150M–$300M) — the fix does not trip Guard B.
- **No excusal is written.** The five accounts are live, funded and reconciling; excusing them
  would have deleted served NNA history for accounts the estate had already silently mis-bucketed.
- Predicted and falsifiable: after the fix and a re-run, the five `'unknown'` rows in
  `gold/views/account_team.parquet` must DISAPPEAR by construction. If they do not, the causal
  chain has a gap.

## Ownership

- **Code change:** DS (`0.4.0_DS_ClientPlatform`) — Rule 13, silver scripts are DS-owned.
- **Re-run / deploy leg:** `0.7.0_AE_CloudOps~A` (me), on DS's commit hash.
- **Verification that the outage actually ended:** chain completes + `pipeline-complete.json`
  advances + the five `'unknown'` rows are gone. Chain-green alone is NOT sufficient evidence that
  the early-warning register works — that residual stays open.

## Provenance

Investigation + verification brief: `@8e69ae4cb`
(`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/INF_REPSCOPE_BRIEF_20260805.md`).
