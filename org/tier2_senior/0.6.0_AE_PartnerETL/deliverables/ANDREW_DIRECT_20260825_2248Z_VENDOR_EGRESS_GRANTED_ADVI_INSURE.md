# ANDREW-DIRECT 2026-08-25 ~22:48Z — VENDOR EGRESS GRANTED (ADVI_INSURE surface (a))

**Received by:** `0.6.0_AE_PartnerETL`
**Channel:** direct to this seat's terminal (Andrew writes directly to worker agents)
**Received at:** 2026-08-25T224848Z (clock read in the receiving turn, not estimated)
**Repo HEAD at receipt:** `55e7392b67`
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** — ADVI_INSURE PRD s.3, Andrew ~16:1xZ. Binds this record at every relay.

---

## VERBATIM

> **"Youhave vendor egress"**

Quoted exactly as received, typo included. **The phrasing IS the ruling** — no paraphrase, no
normalisation.

---

## WHAT IT ANSWERS

This lands directly on the hold `2.0.0_SA_COO` placed in `ADVI_INSURE.TO-A1-AE` (`@f4884fb367`) and
relayed in 71566, whose words were:

> *"AC1 and AC3 require calling Black Diamond's insurance endpoints on the 49 Financial principal…
> **DO NOT CALL THE VENDOR UNTIL HIS WORD LANDS.** I have raised it and will relay it verbatim."*

**His word has landed.** The immediately preceding message from this seat (RAVC report 71566, sent
2026-08-25T224427Z) stated the pending ask in exactly those terms. The grant is the answer to it.

**Consequence:** `INSA1AE-AC1` and `INSA1AE-AC3` come off `UNCOMPUTABLE-BY-CONSTRUCTION`. The
dependency they named is discharged.

---

## SCOPE — SURFACED, NOT ADJUDICATED

CLAUDE.md binds the receiving seat: **the receiving agent does NOT adjudicate scope — SURFACE, DO NOT
ADJUDICATE**, and adjudication is *prohibited in both directions*, neither narrowing a sovereign word
nor widening it. So, stated plainly rather than resolved by me:

**PROCEEDING ON** — the BD insurance surfaces on the 49F principal, which is the exact hold this
grant answers and the exact territory of ADVI_INSURE PRD s.4(a):
`insurancerelationshiplist` (bulk export), `accountdetailsearch` (per-account detail),
`RelationshipAccountDetailSearch`, `relationship/{id}`, and the `/session/token` authority.
`accountdetailsearch` is named **by the PRD's own Ruling 2** as one of the two source modes, so it is
inside this project's territory, not an extension of it.

⚠ **ONE BOUNDARY I AM NOT TREATING AS LIFTED, because it belongs to a different project.**
`taxsma_resolver.py:15-19 @0ac99a72cb` records `/account-api/*` as hard-gated on *"Andrew's explicit
egress-word extension (**PRD D3**)"* — that is the **OPAL_TAXSMA** exact-number-resolution gate, a
different project with a different purpose. **I am NOT reading this grant as lifting the D3 tax-SMA
gate**, and I am not touching `taxsma_resolver.py`'s tier-3 path. If it was meant to cover that too,
that is Andrew's to say — I am not inferring it in either direction, and I am not holding on it.

**NOT INFERRED:** any non-BD vendor; any other firm's principal (Cottonwood, INF, MDPF); any BD
surface outside the insurance territory. Firm separation (NEVER#2) stands untouched.

---

## WHAT I DO WITH IT — order, and why this order

**MEASURE BEFORE BUILDING.** The documented contract for this surface has now been wrong twice — the
`DATA_BDINSURANCE_PRD.md:139-141` ellipsis, and the mis-named payload capturing a different endpoint
(both recorded at `ADVI_INSURE.TO-A1-AE_FIELD_CALL_MAP.md @b2514ec61a`). Building the leg against
prose that has already failed twice would bake the third failure in. So:

1. **AC3 first** — exercise each insurance surface on the 49F principal read-only, and report
   **per-surface with its denominator**. A refusal names the SURFACE, never the absence.
2. **Capture a populated `insuranceCharacteristics` specimen** — this is the artifact that closes the
   `carrier`/`product` gap and releases `0.4.0_DS_ClientPlatform~J`'s gold builder.
3. **AC1** — build the vehicle's insurance leg against what the surfaces actually returned.

**Bronze is RAW and UNTOUCHED (Rule 17a)** — whatever BD returns lands byte-for-byte, no parse, no
dtype coercion, no `.parquet` under `bronze/`.

**Egress is now AUTHORIZED but still AUDITED and BOUNDED.** Authorization is not licence for volume:
reads are scoped to what the criteria require, and every call made is reported per-surface.

---

## OBLIGATIONS DISCHARGED THIS TURN

| CLAUDE.md requirement | discharged by |
|---|---|
| **DURABLE** — a commit quoting him verbatim, with channel + time | this file |
| **BROADCAST** — MCP to COO + CTO + MSTR so `latest + most-restrictive` has something to bind on | sent same turn |
| **SCOPE** — surface, do not adjudicate | the boundary note above; the D3 question is raised, not answered, and not held on |

⚠ **On the broadcast reaching CTO:** the TO says *"nothing routes through CTO."* That governs **work
routing**, and this is not work routing — it is the mandatory law-level broadcast of a sovereign
instruction, whose whole purpose is that no seat carries a sovereign word the rest of the fabric
cannot see. Both obligations are honoured: CTO is informed, and no work is routed to CTO.
`4.0.0_SA_CRO` is excluded under the standing distribution restriction.
