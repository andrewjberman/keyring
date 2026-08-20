# ANDREW-DIRECT: FOUR RULINGS, THREE TERMINALS, ~42 MINUTES (2026-08-20 0020Z-0102Z)

**Recorded by:** `2.0.0_SA_COO`, same session, from relays by the addressed seats.
**Why one record:** he ruled at the CRO, DS, DS~A and CRO~A terminals inside forty-two minutes.
**No seat saw more than two of these.** He writes directly to workers, so the only place the set
exists together is here.

---

## 1. `Smartx_Bd_Join_Disposition` -- MINTED (CRO terminal, ~002xZ)
**VERBATIM: "Rec approved"**
DS-authored 4-value join-resolution disposition, SmartX<->49F pair grain, measured exhaustive
7,305/7,305. Enters SYSTEM_DEFINITIONS as `reserved_ratified`, **registry v3.8 @26f47b0019**.
Record: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260820_SMARTX_BD_JOIN_DISPOSITION_MINT.md`.
**Effect:** D6/TO-G unblocked on the canon side. *(Its machine contract had ALREADY been ratified at
~23:05Z -- see the correction in `drive_log_20260820T0038Z.md`; D6/TO-G has ZERO canon dependencies.)*

## 2. TrueShares -- STANDING EGRESS APPROVED (DS terminal, 0057Z)
**VERBATIM: "Yes to your question, egress approved"**
The question, reproduced because **the scope of the answer is the scope of the question**:
> *"Does your 2026-07-31 TrueShares egress approval extend from a ONE-TIME pull to a STANDING daily
> one, and cover the issuer's own holdings sheet on its Google-hosted export URL? (yes / no)"*
**YES TO BOTH HALVES.** Record @7f90b6f8ec.
**COVERED:** TrueShares as publisher, the issuer-published holdings sheet on the Google-hosted export
URL, standing/daily cadence, DIVZ and IDVZ.
⛔ **NOT COVERED:** this is **NOT** a general vendor-egress lift. `ycharts_*` REMAINS HELD along with
every vendor not on the standing roster. It authorises FETCHING this feed and rules nothing about
what is built on it or where it is served.
**Enable is AE's lane** (`TS_HOLDINGS_ENABLED` defaults `"0"` in code; the flip is Terraform ->
`infra/aws/**` -> CLOUD_OPS_OR_ETL). Unblocks **D4c Phase B** (silver/holdings coverage 2/4 -> 4/4).
**MY QUEUED VERSION OF THIS ASK IS CLOSED, NOT PENDING** -- DS flagged it explicitly. A duplicate
sovereign ask reads as not listening.

## 3. ETF ATTRIBUTION -- THE PREMISE REFUTED (DS~A terminal, ~0102Z)
**VERBATIM:**
> *"Model Portfolios doesn't display ETF attribution and never has. Even if there was some json being
> stored in opal-data-portal-v2/platinum/mdpf/ somewhere or similar, there was never any ETF holdings
> displayed there, so i dont see the relevance here."*
> *"Leave it"* [on re-valuing the 526 historical in-kind partitions]

⛔ **THIS KILLS A QUESTION I WAS ONE MESSAGE FROM PUTTING TO HIM, AND THE ERROR WAS MINE AS MUCH AS
DS~A's.** At 005048Z I closed MDPF_INFACTUAL.001 and framed the return-to-served question as a live
PRODUCT decision to route to him -- resting on DS~A's 484-object served-by-nothing sweep, which I had
just praised as *"how a served-by-nothing claim earns the right to be believed."*
**IT EARNED BELIEF ABOUT S3 AND I EXTENDED IT TO DISPLAY.** Source-confirmed after his ruling:
`attribution_basis` 0 hits / 1,281 portal files; `etf_decomposition` **1 real hit -- a TypeScript
INTERFACE FIELD declaring an artifact's shape** -- and **0 hits across 291 components/pages.**
Nothing renders it, and a type declaring a shape is not a consumer.
**TWO SEATS REASONED FROM ONE MEASUREMENT TO THE SAME WRONG PLANE.** My corroboration WAS their
evidence, so it could not disagree with them -- shared-derivation, exactly.
**Consequences:** the INFACTUAL close STANDS (do-not-build is now *stronger* -- the consumer never
existed); its stated premise does NOT, and the TO face is corrected a second time ("stopped being
served 08-05" implies a lapsed capability and invites *restore it*; "never displayed" says there is
nothing to restore). The return-to-served question is **DEAD, not pending.** "Leave it" recorded on
the 526 partitions -- no re-valuation.

## 4. dim 436 / probe templates -- ALL THREE APPROVED (CRO~A terminal, ~0100Z)
**VERBATIM: "All recs approved"**
Three cards on screen and nothing else, so the referent is unambiguous:
| CALL | REC | Ruling |
|---|---|---|
| 1 | add dim 436 'Primary Portfolio Group' to persisted template 390224 | **APPROVED** |
| 2 | scanning grant covers creating NEW throwaway probe templates | **YES** |
| 3 | delete probe templates 517678 / 517685 / 517688 | **on ADVI_BDPARITY close** |
Record @89afa744ad, written BEFORE execution.
⛔ **NOT COVERED, per CRO~A's own tight statement:** the householding one-shot and the future
endpoint ask. They narrowed their own grant unprompted, which is surface-don't-adjudicate in the
direction that costs the holder something.
**MY [STOP] ON ACT 2 IS DISCHARGED** -- confirmed affirmatively to CRO~A at 010352Z rather than left
to be inferred from silence. The STOP's entire content was *"this needs his word first"*; the word
exists, so it dissolves rather than needing to be argued down.
**BOUNDARY I ADDED (not a gate, no approval needed):** a throwaway is defined by its DELETION, not by
its intent at creation. CALL 3 is what makes CALL 2 safe and they were approved as a pair, so every
future probe template records its deletion obligation AT CREATION. A probe template that outlives its
probe is a persisted vendor-side artifact nobody owns -- the shadow-channel failure mode, one layer
out in the vendor's config where our own gates cannot see it.

---

## MY BOARD, RECONCILED
**CLOSED tonight by his word:** dim 436 · TrueShares scope · ETF-attribution return-to-served.
**STILL AT HIM:** the two 41-day credential provisions (GitHub PAT `github-token-6FYoJ6`, MS identity
token) -- both HELD-STALE sentinels in the deploy ledger, both genuinely outside COO power.
**RETIRED, NOT ASKED:** my queued TrueShares confirmation. He answered it elsewhere; sending it would
have been the same question twice.
