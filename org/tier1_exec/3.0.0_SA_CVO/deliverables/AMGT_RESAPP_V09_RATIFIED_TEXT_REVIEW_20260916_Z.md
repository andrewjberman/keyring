# AMGT_RESAPP v0.9: ratified-text review

Reviewer: `3.0.0_SA_CVO~Z`. Verdict: **REFUSED** -- four corrections, each by pinned line, each one bump away.

PRD: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md@44269d05157fb53b3440aa7930016fd7908f7bbb`.
Reviewed half: `88e330dea809d3961a7dec34d07557cca9c0bcab8dba162b74b892eee3c90cfa` (ratified-text).
Brief half at the same commit: `0455fc3d1e95715a8043d5f9fbadddd8a72e8d5a178a961da57635a5cc15ebea`, unchanged from v0.8.
Deliveries: 23390 (notifier), 23391 (author summary). Read beside them: L10 ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` (23397).
Law applied: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:164-167` at HEAD -- *"every DONE WHEN, ACCEPT and PROOF in the ENDPOINT
section is verbatim from the ratified pins; every operative constraint is present; no annotation, history or seat name is inside the
SECTION (heading to next heading); the CONTRACTS section agrees with the counterpart."* The seat-name clause is a READING rule: `prd_signoff_lib.py`
carries no regex for it (measured), so nothing mechanical would have caught R3 below.

## What passes -- measured, not inherited from the delivery

| Check | Instrument | Result |
|---|---|---|
| Half hashes at 44269d0515 equal the delivered pair | `prd_signoff_lib.half_hashes` on `git show 44269d0515:<prd>` | PASS -- ratified `88e330dea809...`, brief `0455fc3d1e95...` |
| The v0.9 note sits in the preamble, neither half | brief hash unchanged across the note's insertion | PASS |
| Full v0.8 -> v0.9 diff read whole | `git diff 1170b4da69 44269d0515` : 103+ / 3- | PASS -- the three deletions are the header's `prd_version` line, the header's `"FWD-19"` array line (re-emitted with a trailing comma so `"FWD-20"` follows) and the BAR DISTRIBUTION line; no card body lost a line |
| No existing FWD-n text, contract, constraint or manifest row changed | same diff | PASS |
| ENDPOINT card and bar census | regex over the section at 44269d0515 | PASS -- 20 cards; `EXERCISED` 19, `APPLIED` 1 (FWD-9), as the BAR DISTRIBUTION line states |
| FWD-20 ACCEPT "scaled by how much the street disagrees with itself" is a faithful plain-language rendering | Andrew-direct record @`287d2c2619` :53 ("normalized by how much dispersion there is among analysts"), :55, :67 (`D = (F_model - F_cons) / s_cons`); CTO~W call 3 @`1685652d6e` (the CFPS/EPS proxy stands in for `s_cons`) | PASS -- the wording the author flagged for a hard read is CORRECT |
| FWD-20 ACCEPT "Model upside and the raw percentage disagreement are REPORTED beside it and are never ranked on" | record @`287d2c2619` :80-82 (`COMPANION (reported, not ranked)`: U model upside, Delta raw percent disagreement), :105-106 | PASS as substance -- see R2 for the citation |
| C-ROUND12-COMPARABLE-COVERAGE, C-ROUND12-THESIS-ASOF agree with ROUND_ANALYSIS.round11.md s.4 items 1-2 @`c708914c50` | text comparison | PASS |
| C-ROUND12-PRINT-SERVER-SIDE, C-ROUND12-SURFACED-OUTCOMES agree with A1.3 R2, R4 @`1db70c8e87` | text comparison | PASS (R4: see NOTE) |
| CONTRACTS section carries seat names | census: 17 serial-bearing lines of 177, 16 of them present and SIGNED at v0.8 | not a ground -- the spine's seat-name clause binds the ENDPOINT SECTION; CONTRACTS convention is established |

## R1 -- FWD-20 ACCEPT omits two operative constraints of its own pins (`:400-408`)

Corpus of the ratified text at 44269d0515: `source and time` 0 hits; `0.25` 0 hits; `sd(D)` 0 hits; `assumption` 1 hit (`:953`, outside
both halves). Neither constraint is anywhere in the PRD.

1. **Provenance of the seeded drivers.** CTO~W call 4 @`1685652d6e` :59-61, RULED: *"a forecast of FCF per company whose revenue, margin,
   tax, capex and working-capital drivers are seeded from dated filings and operating history, **every assumption stored with its source
   and time**, never copied from consensus."* The ACCEPT keeps "from the company's own filings and its history, seeded independently of
   consensus" and drops the stored-with-source-and-time clause. That clause is what makes "seeded from filings" gradeable: without it a
   cell seeds from filings with no provenance and FWD-20 passes as written.
2. **The pre-deployment degeneracy check.** Record @`287d2c2619` :94-96 verbatim from Andrew: *"DEGENERACY CHECK (pre-deployment,
   universe-wide) sd( D ) across universe < 0.25 -- drivers likely seeded from consensus; factor is not measuring disagreement"*, read
   narrowly at :107-109: *"the universe distribution of D is checked BEFORE deployment ... This binds the model-block producer, not only
   the page."* Call 4 @`1685652d6e` :61 repeats it: *"Andrew's sd(D) < 0.25 check runs before D is shown."* The ACCEPT shows Divergence with
   no such gate. A cell could serve D from consensus-seeded drivers, D collapses toward zero, and the outcome reads EXERCISED.

Correction, in the card's own register (cards carry no technical language, `:200`): after "seeded independently of consensus." add
*"Every driver assumption behind the forecast is kept with the filing it came from and that filing's date."* and after "does not yet
serve." add *"Before any Divergence is shown, the spread of Divergence across the covered universe is checked for the sign that the
drivers were seeded from consensus after all, and Divergence stays ABSENT, with that reason, until the check passes."* The formula and
the 0.25 threshold belong in a contract or the model-block producer's spec, not on the card; the card must carry the CONSTRAINT.

## R2 -- FWD-20 SOURCE cites the wrong pin for two of its three sentences (`:409-414`)

SOURCE names the slug @`5d3a04cab6`, call 4 @`1685652d6e` and the analysis @`c708914c50`. None of those defines D, the dispersion
scaling or the unranked companions. The pin for "scaled by how much the street disagrees with itself", for "REPORTED beside it and are
never ranked on" and for the degeneracy check is the Andrew-direct record @`287d2c2619` (the ~18:3xZ Model-tab word, recorded verbatim by
CTO~W), and call 4 itself descends from it. A sentence in ratified text whose pin is not on the card fails "verbatim from the ratified
pins" as a CHECK even when the rendering is faithful -- and it is faithful; the check exists so a later reader can re-run it.

Correction: add `ANDREW_DIRECT_20260915_183xZ_MODEL_TAB_SCORE_IS_DIVERGENCE_FROM_CONSENSUS_FCF_AND_PEERS_RESENT.md @287d2c2619`
(by title and pin -- see R3 for why not by path) to SOURCE as the pin for the Divergence sentence and the companions sentence.

## R3 -- seat names inside the ENDPOINT section (`:411`, `:413`)

Census of the ENDPOINT section (heading to next heading, 232 lines) at 44269d0515 for the serial pattern: **2 lines, both on FWD-20's
SOURCE** -- `1.0.0_SA_CTO~W's ruling 4 at` and `carried at L10 by 1.0.0_SA_CTO~Z`. The same census at 1170b4da69 (v0.8): 0 lines. Every
other card's SOURCE cites Andrew-direct words, the brief, a voice memo or a pinned carrier without naming a seat. Spine `:165-166` is
explicit and unqualified for the SECTION.

Correction: cite without the lane -- *"the CTO adjudication of 2026-09-15 ~19:5xZ, call 4 @1685652d6e; ROUND_ANALYSIS.round11.md s.4
item 3 @c708914c50; the round-11 slug REMEDIATION_v11.md @5d3a04cab6"*. A pin resolves the document; the serial adds nothing the pin
does not. Do not substitute the `org/tier1_exec/1.0.0_SA_CTO/...` path either -- it carries the serial in its first segment.

## R4 -- C-ROUND12-PULL-WIRED ratifies a consumer the L10 author has already found impossible (`:588-592`, the sentence at `:590`)

The contract, verbatim: *"the consumer is an EVENT-SOURCE-MAPPED Lambda rather than a poller a person starts."* ADDENDUM 2
@`06378dd3bd`, C1, by the same author fifteen minutes after v0.9: *"IT CANNOT BE ONE: pull_consumer.py calls the Bloomberg DAPI at
127.0.0.1:8194 ON THIS BOX, so a Lambda would drain the queue and fail every message at bloomberg_health ... THE CONSUMER STAYS ON THE
BOX, and its cadence is a card rather than a cell. No Lambda consumer is built."* The delivery at 23397 says the addendum does not
re-open the half because the bytes did not move. The bytes did not move; the CONTENT is now contradicted by the analysis the contract
cites. A half can be unchanged and wrong, and "the CONTRACTS section agrees with the counterpart" is a content check. Signing this
would ratify, as the project's contract, a design the CTO has ruled cannot work on this box -- and a round-12 cell cut against the
ratified text would be cut against the wrong one.

Correction: C-ROUND12-PULL-WIRED reads as C1 corrected -- the page calls the enqueue route, the adapter declares the queue carrier, the
consumer stays box-side (its DAPI dependency named as the reason), its cadence is a RESERVED card at Andrew and never a cell's act, no
Lambda consumer is built, and the moratorium clause stays. Cite ADDENDUM 2 @`06378dd3bd` C1 beside A1.3 R3.

## NOTE, not a ground -- C-ROUND12-SURFACED-OUTCOMES and ADDENDUM 2 C2

C2 narrows what a "page surface" for FWD-12 may be: *"L binds the stages that exist and the control REFUSES WITH A NAMED REASON where
activation is reserved, or ships READ-ONLY with the re-run stated as round 13 in the issuance data. Never a button that does nothing."*
The contract is not contradicted, but a surface that is a decoration would satisfy its text. Recommended: carry C2's last sentence
into the contract at the same bump. P2; the CTO's call.

## Scope of this refusal

This review authorizes nothing and grades nothing REALIZED. The brief half is UNCHANGED and `4.0.0_SA_CRO~Z` owes nothing on it. The
v0.10 bump re-opens ONLY the ratified-text half (R1-R4 all sit inside ENDPOINT or CONTRACTS); the CTO's own hash-before-and-after read
will confirm it. 2.0.0_SA_COO~Z's L5 decomposition is not gated by this; the ONE L6 issuance is, exactly as before. The refusal stamp
is bound to `88e330dea809...` with `--expect-half-hash`, so it cannot land against bytes this seat did not read. Review and stamp are LOCAL.
