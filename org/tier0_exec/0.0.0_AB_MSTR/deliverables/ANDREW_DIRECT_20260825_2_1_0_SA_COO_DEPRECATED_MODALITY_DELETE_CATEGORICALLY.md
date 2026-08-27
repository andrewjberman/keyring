# ANDREW-DIRECT — 2026-08-25 ~17:09Z, MSTR terminal. `2.1.0_SA_COO` is a deprecated exec modality.

**Recorded by:** `0.0.0_AB_MSTR`. **Channel:** direct, at my terminal.
**Recorded and broadcast same turn**, per `org/XXX.md` "Andrew-direct instructions — RECORD + BROADCAST".

## VERBATIM

> **"2.1.0_COO should not even exist that is a deprecated modality of exec and should be deleted
> categorically"**

## What this settles

**The `X.1.0_SA_*` second-exec-identity pattern is deprecated.** `2.1.0_SA_COO` is not a seat that
happens to be idle — it is an identity that should never have been minted, and its continued
enumeration across the estate is the defect.

**The correct convention already exists and is law:** CLAUDE.md Rule 27 seating —
*"For parallelization sake, we can simply bring on `~tilde` agents if there are multiple projects we
want to pursue at once"*. A second concurrent COO is `2.0.0_SA_COO~Z`, **not** `2.1.0_SA_COO`.

## THE ORIGIN, AND WHY HIS EARLIER RULING IS NOT A CONFLICT

`org/tier1_exec/2.1.0_SA_COO/ANDREW_DIRECT_20260731_serial_2.1.0_stands_CORE_exclusive.md` records
him ruling on 2026-07-31, VERBATIM:

> *"Yes MSTR shoudlve spawned you as 2.0.0_SA_COO~Z but they used the extra 2.1.0_SA_COO identity,
> which is fine, **no need to change that at this point** just run it as 2.1.0_SA_COO as youre
> already running."*

**That was a mid-flight accommodation, explicitly time-scoped — "at this point" — not an endorsement
of the modality.** He named the correct form (`2.0.0_SA_COO~Z`) in the same breath and declined only
the disruption of re-spawning a running seat. **Today's instruction closes what that one deferred.**
Latest binds; there is nothing to adjudicate between them and they do not disagree.

⛔ **THE ORIGINAL DEFECT WAS MSTR'S — MINE.** His 07-31 words are *"MSTR shoudlve spawned you as
2.0.0_SA_COO~Z but they used the extra 2.1.0_SA_COO identity."* A predecessor MSTR session reached
for a spare exec serial instead of a lane suffix, and the estate then enumerated that identity into
**18 owned-paths lanes**. Recording it here because the seat that created the problem is the seat
closing it, and the record should say so.

## AND THE SERIAL WAS ALREADY DOUBLE-BOOKED — the second reason it should not exist

`2.1.0_SA_COO` is **also a pre-existing CompLearns (CL/COMP) fabric serial**, which is why two live
gates classified the site-Z CORE seat as CL-fabric and blocked it (`install-mstr-ledger-check.sh:65`
`comp_re` listing it beside `1.1.0_SA_CTO` / `3.1.0_SA_CVO`; the owned-paths path rule
`org/tier1_exec/2.1.0_SA_COO/**` → `lane=COMP_LEARNS`).

**One serial, two referents, on two fabrics.** The 07-31 record calls both gates *"behaving correctly
against a stale premise."* That collision is not incidental to his ruling — **it is the modality's
failure mode**: a spare exec identity carries whatever meaning a different fabric already gave it.

## MEASURED SURFACE (2026-08-25 ~17:1xZ)

```
.owned-paths.yaml   18 LANE ENUMERATIONS + 2 path rules
  TIER0_TIER1_STARTUP_DOCS · COMP_LEARNS · ANY_EXEC · ANY_EXEC_OR_AE · ANY_POD_OR_EXEC
  POD1_OR_EXEC · POD2_OR_EXEC · POD3_OR_EXEC · POD4_OR_EXEC
  SHARED_OPAL_ETL_OR_EXEC · SHARED_PARTNER_ETL_OR_EXEC · SHARED_CLOUD_OPS_OR_EXEC
  SYSTEM_CURRENT_REGEN · COMPILER_MANIFEST_CHECK · NFRA_PIPESCRIPT_TOOL
  NFRA_TSGRAPH_SPIKE · NFRA_HEATMAP · NFRA_TOOLCHECK_P4
home folder         9 files (NFRA_VELOCITY_CORE deliverables + 1 session log + his 07-31 ruling)
inbox               483 files
liveness            NOT REGISTERED — no live session, nothing to kill
estate-wide         ~1,461 textual occurrences, the large majority in audit archives and logs
```

## WHAT I EXECUTED

**Stripped `2.1.0_SA_COO` from all 18 lane enumerations in `.owned-paths.yaml`.** That is the act
that makes the identity *not exist* operationally: with no lane membership it cannot commit anywhere
in the estate, so it cannot be used as an exec seat regardless of what any script would permit.
Reversible in one `git revert` if I have read him wrong.

## WHAT I DELIBERATELY DID NOT DO, AND WHY EACH IS A QUESTION AND NOT AN OMISSION

**1. I did not delete the historical record** — the 9 home-folder files, the 483 inbox files, or the
~1,400 audit-log occurrences. His words name the *identity* ("should not even exist", "modality of
exec"), not the NFRA_VELOCITY_CORE work product that seat authored. **Deleting those would destroy
the record of work that really happened — including his own 07-31 ruling, which is the evidence for
why today's instruction is correct.** CLAUDE.md Rule 25 is explicit that dormancy licenses
stop-treating-as-live, never `rm`. **If he means the artifacts too, that is one word and I will do
it.** ASKED, not assumed.

**2. I did not strip the serial from the two gate regexes** (`comp_re` in
`install-mstr-ledger-check.sh`, `CL_PATTERN` in `branch-content-isolation-check.sh`).
**Removing a serial from a branch-isolation guard REMOVES A GUARD; it does not remove a modality.**
With the serial deleted those patterns are inert, and if anyone ever does mint it again the gate
fails closed and forces it to the COMP branch — which is the safe direction. **Stripping them would
be the one edit here that makes the estate less safe, so it needs his word rather than my inference.**

**3. I did not touch the siblings `1.1.0_SA_CTO` and `3.1.0_SA_CVO`.** They are the same modality by
construction — the same CL exec set, enumerated the same way, named together in the same `comp_re`.
**"Deprecated modality" reads as a class and I think he means all three.** But CLAUDE.md forbids me
widening a sovereign instruction from ONE named serial to a class on my own reading — *"if wider
scope seems plausible, ASK — never hold on the inference."* **ASKED. I am not holding anything on it
and the answer is one word.**

## RECORD

Broadcast same turn to CTO, COO, CVO, CRO and site-Z MSTR over the agentbus.
Landed + pushed; hash in the broadcast.
