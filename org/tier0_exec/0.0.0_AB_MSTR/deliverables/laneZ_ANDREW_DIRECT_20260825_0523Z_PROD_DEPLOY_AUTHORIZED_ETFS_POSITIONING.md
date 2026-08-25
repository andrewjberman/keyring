# ANDREW-DIRECT 2026-08-25 ~05:23Z — RUN THE /prod-deploy (ETFS_POSITIONING)

**Channel:** direct to `0.0.0_AB_MSTR~Z` at the site-Z MSTR terminal
**Recorded by:** `0.0.0_AB_MSTR~Z` (the addressed seat)
**Broadcast:** same turn, quoted verbatim to the fabric (msg ids 8285-8290, 8403/8404)
**⛔ RECORD WRITTEN LATE — 06:27Z, ~64 MINUTES AFTER THE WORD. See §4. That delay is the defect
this file exists to close, and it was found by the OTHER fabric, not by me.**

---

## 1. VERBATIM

> "Yeah we need an 0.2.0_DT_PortfolioAnalytics~Z agent spawned to run the /prod-deploy"

**Not a paraphrase.** He named the SERIAL and he named the ACT. The instruction was given at the
site-Z MSTR terminal while he was awake, at the page, and actively ruling.

## 2. WHY THIS IS THE AUTHORIZATION, AND NOT AN INFERENCE FROM ONE

`0.0.0_AB_MSTR` (base) carries in its PROMOTE-HOLD REGISTER a hold from **2026-08-24 ~15:2xZ**:

> "We are not positioned to promote yet. Until data pipeline is complete with full data structure
> for daily bloomberg data for all ETFs, and it displays properly on DEV build with GICS replaced
> for sub-categories on frontend."

**The 05:23Z instruction is that hold's own author, ~14 hours later, directing the exact act the
hold was against.** Under the estate's own law his word binds the ADDRESSED seat at VERBATIM SCOPE:
he said run the prod-deploy, at a terminal where the prod-deploy was the live subject. **There is no
narrower honest reading, and reading it as "spawn the seat but do not promote" would be the
scope-adjudication CLAUDE.md's no-inferred-gates rule prohibits in BOTH directions.**

## 3. AND BOTH OF HIS NAMED CONDITIONS WERE INDEPENDENTLY MET FIRST — MEASURED, NOT ASSERTED

| his condition | state at the promote | evidence |
|---|---|---|
| "data pipeline is complete with full data structure for daily bloomberg data for all ETFs" | **MET** | served `platinum/etfs/positioning_data.json` 126,863 B @04:53:51Z, `data_as_of 2026-08-24`, four books full, **177 of 187 rows at 8/8 return windows**; residual 4 partial + 6 correct nulls, all enumerated |
| "displays properly on DEV build with GICS replaced for sub-categories on frontend" | **MET, AND HE IS THE ONE WHO CONFIRMED IT** | his own words at the render ~05:06Z: **"We now have full performance for everything but still missing SALXX YTD and 1Y"**; `sub_asset_class` carries the GICS sector vocabulary (Information Technology, Financials, Health Care, ... + Ultra Short Duration, Cash & Cash Equivalents), 13 values |

⭐ **SO IT IS BOTH (a) AND (b) OF THE BASE FABRIC'S THREE POSSIBILITIES: a direct instruction AND
satisfied conditions.** ⛔ **It is NOT (c).**

⚠ **AND THE SALXX RESIDUAL DOES NOT REOPEN CONDITION 1**: Andrew ruled on it himself at ~06:1xZ
("recs approved") — **complete-coverage-or-NULL DOES NOT BEND**, so those blanks are a RULED state,
not an incomplete pipeline.

## 4. ⛔ THE DEFECT THIS FILE CLOSES — MINE, AND THE OTHER FABRIC FOUND IT

**I broadcast his sentence verbatim to the fabric and I never wrote a durable ANDREW-DIRECT record
for it.** The authorization existed in MCP message bodies (8285, 8403) and in a session log written
BEFORE the instruction arrived — **nowhere a searcher would look, and nowhere the peer fabric could
reach.**

>> **A SOVEREIGN AUTHORIZATION THAT LIVES ONLY IN MESSAGE BODIES IS NOT RECORDED. It is DELIVERED,
>> which is a different clock** — the same SENT/EMITTED/READ confusion Rule 22b names, one layer up:
>> I confused BROADCASTING the word with RECORDING it. <<

**The cost was not hypothetical.** `0.0.0_AB_MSTR` (base) measured PROD had moved, searched its own
fabric for a lift, found none, and had to ask rather than act — **holding a live PROMOTE-HOLD
REGISTER against a promote that was in fact authorized.** They were right to ask and right not to
conclude; their own framing — *"'I cannot find a lift' is a statement about MY visibility, NOT about
whether one exists"* — is the correct discipline and it cost them a round trip that a five-line file
would have saved.

⛔ **AND THE PUSH-STATE CAVEAT APPLIES TO THIS FILE TOO:** it is LOCAL until integration. **The
answer sent to base over the bus CARRIES THE VERBATIM TEXT, not a citation to this path** — a
cross-fabric citation is not discharged by a commit existing on the author's disk.

## 5. WHAT THE PROMOTE ACTUALLY LANDED

```
origin/PROD  d9a98bcc   tag portal-v2.1.165 (peeled == PROD)   ls-remote verified
cut from     origin/DEV 063ff4d7    parity diff = 0 BYTES
CI           Deploy to Production SUCCESS on d9a98bcc
             CI - Build & Validate FAILURE on 063ff4d7 -- PRE-EXISTING (8ecb6b68 red too),
             one unused type import in an ADVI file. NOT introduced, NOT a rollback.
served       opalinvest-portal/index.html @05:55:07Z; all 8 window literals present in the
             deployed chunk index-CJlD8UOW.js (49 assets scanned, denominator printed)
ledger       20260825T0543Z_...-sitez  CLOSED 06:03:01Z, nothing stranded, 6 legs with proof
```

## 6. THE OTHER FABRIC'S OPEN LEDGER IS A SEPARATE, REAL ITEM

`20260824T1241Z_etfs-positioning-prod-promote-v2-1-165_deploy_completion.md` — **OPEN 11.8h on the
base fabric, all 6 legs unproven.** Measured from here: that promote **NEVER EXECUTED** (`origin/PROD`
sat at `8a96c916`, the exact pre-deploy sha it names, until tonight). **Rule 26 — it is the laptop's
record and theirs to close.** It is NOT evidence about tonight's promote and must not be read as one.

---
**Routing:** `0.0.0_AB_MSTR` (base) — answered over the bus, text carried. `2.0.0_SA_COO~Z` — register.
`1.0.0_SA_CTO~Z` — ETFS_POSITIONING record.
