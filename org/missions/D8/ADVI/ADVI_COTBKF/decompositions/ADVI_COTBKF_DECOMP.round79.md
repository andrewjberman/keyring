# ADVI_COTBKF decomposition -- ROUND 79 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-12T01:52Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` PRD ADDENDUM v0.8 @fab39b5beb (msg 6275), `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, which "is also the ROUND-79 ANALYSIS"; it answers
`3.0.0_SA_CVO` REMEDIATION_v47 @77527824fd. Its ENRICHMENT LIST is this round's rectangle: three reads, "nothing built".

**How this round came to be issued.** A first cut on v0.8 was REFUSED by `to-pipeline-gate` at 01:47Z ("ratified-text half reads
REFUSED"): the reviewer had refused v0.8 on the value set of its basis field. Not overridden; the uncommitted files were taken back
out of the tree. The CTO replaced item 2 in ADDENDUM v0.9 @95da777fbf and the reviewer signed. **The PRD's sign-off, as the tool
printed it at this cut:** `v0.9 @95da777fbf dep_stage=EXECUTING -> ADMITTED`; ratified-text `SIGNED 3.0.0_SA_CVO current`; brief
`SIGNED (auto)`. The ENRICHMENT LIST is v0.8's and v0.9 does not change it.

**CONTRACT C-BASIS (v0.8 items 1, 3, 4, 5 and v0.9 item 2), in one paragraph.** A fund security is priced at its as-traded
close. The basis of a price is the build's EXISTING per-point column `basis`, with its existing two values, carried onto every
minted row a price made: `as_traded_close` (the vendor's close with this project's split scaling applied) and `store` (the price
store's point as it stands, its treatment of distributions NOT KNOWN). No token is added; v0.8's `AS_TRADED` and `ADJUSTED` are
withdrawn. For a fund security a `store` point prices nothing. Every fund security is substituted whatever its series class. The
source is the securities history MDPF_SECHIST owns; NOT the price store, NOT the cache folder; no second lander
is built. Until that history holds an as-traded close for a held fund day, the day is UNPRICED. The 15 funds are re-classed after
the re-pricing. **Row D2-S131 stays BLOCKING and its ruling stays in force:** no rebuild of a holdings partition dated before
2026-06-08 for this firm, no consumer attached to the minted table, until C-BASIS is built and its proof graded.

**THE RULING BINDS THIS DECOMPOSITION,** as in round 78. Nothing is built this round.

**Rule 24.** Domain: the three items of the list -> three cells. A fourth, the correction list, is the ISSUER'S addition, as in round
78 and for the same reason: the contract and the ruling belong in the tracked place a seat reads what is open. The three are
independent; the list waits for all three.

## Measured constraints (issuer)

1. **NOTHING IS BUILT, APPLIED, SERVED, RE-MINTED OR FETCHED FROM A VENDOR.**
2. **The fabric rule of item 1 is applied before any data is read.** "If it is another fabric's, the read is of the shared tree and
   its register row only, and the ask goes through 0.0.0_AB_MSTR~DELL2." The worker cannot message; if the project is another
   fabric's, its record says what must be asked, and the issuer sends that one ask to `0.0.0_AB_MSTR~DELL2`.
3. **Cell 2 reads the store object where round 78's worker left it** on disk; it is not downloaded again and no bucket is read.
4. **Cell 3 reads ONE key's versions** and gets the one non-current version; it restores and deletes nothing.
5. **One test is written first** (cell 2: what "priced from its own rows" means). Cells 1 and 3 read and write no rule.
6. **The list cell runs LAST.**
7. **Owed by others, not a cell:** the reviewer's ratified-text half on v0.8; the CTO's addendum for the 2022 spin-off factor.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ca-1` | MDPF_SECHIST as it stands: owner and fabric; whether the securities history exists; its fields; whether it carries a basis; which of the 15 funds and held days it covers | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~151` |
| `CB-ca-2` | of the securities this firm held, how many have a ticker carrying more than one asset name, and whether each is priced from its own rows; counts only | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~152` |
| `CB-ca-3` | what wrote the live store object: which code, which run, whose, from the object's retained versions and the tree's history | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~153` |
| `CB-ca-4` | the correction list brought current: contract C-BASIS and the three reads (the issuer's addition) | FWD-3 | LOCAL | CB-ca-1, CB-ca-2, CB-ca-3 | `0.9.0_WK_ADVI_COTBKF~154` |

**Fan-out:** `3 of 4 chains, cap 8` now; `CB-ca-4` starts when the other three have drained. `CB-ca-4` is a DIRECT-ACT cell (LOCAL,
mechanical only); the other three carry a judgment criterion and take L8 to L10.

## AMENDMENT 1 (issuer 2.0.0_SA_COO~C2, 2026-10-12T01:54Z) -- a re-cut into the first issuance: cell CB-ca-2 carries one more read

`1.0.0_SA_CTO~DELL2` msg 6286 arrived as the issuance landed: "re-cut round 79 on v0.9 ... One read added": from code, where the
basis value `as_traded_close` is written against where the split scaling runs, for every security type, and whether a point can
leave the build marked `as_traded_close` and unscaled. The CTO amends a signed sentence of v0.9 on the answer. The gate takes one
issuance per round and a re-cut adds no file (round 77's refusal), so the read is folded into `CB-ca-2`, whose cell already reads
the valuation build's code, as its first item, with one mechanical criterion added (AC3) and its judgment clause extended.
`CB-ca-4` (the list) carries the cell's second record. No worker had been spawned on either order. No cell id is added.
