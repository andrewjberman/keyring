# L4-R re-review -- TCKT_MTADTA PRD v0.2 @86f3caec3a, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-16 ~06:4xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 6557 and 6558 (both acked), answering this seat's
refusal `L4R_REVIEW_TCKT_MTADTA_v0.1_RATIFIED_TEXT_20261016.md` @c6a0aa8499.
**Graded:** the whole diff 315f7a19af -> 86f3caec3a. ENDPOINT is unchanged (still verbatim against @a7a7df4e6f); four CONTRACTS rows and one
OPEN AT ANDREW item moved.

## Verdict: SIGN

| Change | Read |
|---|---|
| C-FIELDS (c) | "Every address that is not one of the eight, internal (@opalinvest.com) or external, recipient, sharee, chat member or guest, is replaced before the first write by a class token: `internal-other` or `external`. No address and no external domain is stored." This closes the refusal's gap, and FWD-7 and C-FIELDS now say the same thing. The proof adds a planted INTERNAL recipient outside the eight, searched for across everything stored. |
| C-RESIDUAL (5) | File and folder names, kept for FWD-5, can carry the names of colleagues outside the eight and of clients. The statement Andrew holds stays honest. |
| C-CLIENTDATA | Restated to match: names remain only in file and folder names; addresses are tokens. |
| OPEN AT ANDREW | External domains are stored only on his word, reading "all other domains/accounts should be dropped at the outset" literally until he relaxes it. The conservative default is the right one. |

## Nit (not a ground to refuse)

C-FIELDS (c) carries "(v0.2, on the CVO's refusal @c6a0aa8499.)" inside the row: an annotation in CONTRACTS. Drop it at the next edit; the
commit message and this review carry the history.

## Carried for the build, not this half

FWD-2's "reads as leaving the team, not as a break" now rests on the `internal-other` and `external` tokens alone. The round-1 cell that
builds chains should show one hand-off to a token reading as a team exit.

-- 3.0.0_SA_CVO
