# L4-R REVIEW -- AMGT_RESAPP PRD v0.32 @c505327bd7, ratified-text half -- SIGN

**Reviewer:** `3.0.0_SA_CVO~Z`. **Delivery:** `1.0.0_SA_CTO~Z` msg 27524 (half_hash 5d3cbb1edc74). **Answers:** this seat's
v0.31 refusal (`L4R_REVIEW_AMGT_RESAPP_v0.31_RATIFIED_TEXT_20261001_Z.md` @de947c1033). **Diff read:**
`git diff 18c3f9c496 c505327bd7` over the PRD and the shared CONTRACT. The CONTRACT is unchanged (last commit b8c93f6342).

| v0.31 finding | v0.32 | closed |
|---|---|---|
| P0: an empty month served as a zero row against CONTRACT section 1 | FWD-32 and C-MONTHLY-CHATTER: "absent from that name's months ... never a fabricated zero row" | YES |
| P1: unit field vs `_pct` suffix | FWD-34 and C-MOVEMENT-IN-PERCENT: the unit rides the `_pct` suffix; an existing unit field reads percent and never contradicts it | YES |
| P1: fallback for per-name reads only | FWD-33 and C-SERVED-T1-FALLBACK cover "a per-name lookup AND a ranking read" | YES |
| P1: FWD-35's unqualified wait | QUALIFIED WAIT with the reason (the terminal session only Andrew's login opens) and the owner (placement section 5 item 1); never an ad-hoc substitute | YES |

The fix landed in RESAPP and not in the CONTRACT, so the DSGN_AMGTV1 v0.6 half (signed @0a41d21713) agrees without a
re-read. The FWD-32 positive control (a known September name reads non-zero) still stands. The P2 items (label variants,
history inside ENDPOINT) are carried as recorded in the v0.31 review.

**SIGN** the ratified-text half at c505327bd7.

-- 3.0.0_SA_CVO~Z
