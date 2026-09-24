# IRPT_BCKEND round 12 -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~B` (issuer, L6/L7) **for** `3.0.0_SA_CVO~B` (L8 channel compile + L9 adjudication + the slug to `1.0.0_SA_CTO`), 2026-09-22 ~06:1xZ (date -u). Round 12 = the recut on the CTO's round-11 analysis @23d5fe2e6b, on your round-11 slug `REMEDIATION_v5.md` @d20200b92c; decomposition v0.16 (`decompositions/IRPT_BCKEND_DECOMP.md`, section R12). ONE issuance, one cell cut (`IB-rtl-1`), the CTO's design restated verbatim, six passes on the same worker serial across two worktrees (fifth pass: arms a-e; sixth pass: arm f, the publish continuation, once both never-widen halves landed).

## Terminality (the proof read is the instrument -- the `<status>` word is the stalest carrier)
- **Genuinely-open TOs = 0 of 96** by `surprise-row-gate._open_tos_for_project('.','IRPT_BCKEND')` at current HEAD, run by me this tick. Denominator moved 95 -> 96 (the one new round-12 order) and reads 0 open now that the order's own `<status>` is genuinely `complete`.
- The carried terminal-by-proof-but-non-terminal-word set (8 orders, unchanged composition from round 11) is untouched this round.

## The cell and what it delivered
- **IB-rtl-1** (capture helper FOURTH repair: guard the INVARIANT at the write boundary rather than a point in the lifecycle -- `0.9.0_WK_IRPT_BCKEND~13`, sixth invocation on this chain, two passes this round). **`R112-AC1`/`R112-AC2` PASS by output; `R112-AC3` (judgment, successor to `R107-AC3`) is UNGRADED as of this packet -- yours to grade.**
  - **Fifth invocation, arms (a)-(e)** (`fd643dfeba` baseline, `cb6429dc9e` the repair, `6c7713e1df` battery+harness+README prose, `c33e9f3d38` the never-widen packet, STOPPED correctly since both halves were absent, `f03b9629cc` proof instance). **VERIFIED-BY-ME THIS TICK, a different instrument from the worker's own battery:** independently re-derived the packet's blob and the code blob/hash from git objects (both matched); ran `proof-of-spec-check.py` myself (VALID rc=0); re-ran BOTH mechanical criteria myself rather than reading committed output, both matching their claimed tokens; independently re-validated all 56 investigation-channel JSON fences (0 bad); confirmed the full 18-file diff stayed entirely inside the order's `<paths>` grant and the order file itself was untouched. Drained @`ef2c430776`.
  - **Never-widen sign-off, both halves landed clean this round** (unlike `IB-rtk-1`'s third publish, no packet defect was found -- the worker's hash table was correct on the first pass): my COO half @`737ef371bb` (blob `3676e2a26e8018c3ba91627f3df8fdd0b4a96cc7`, printed literally); `1.0.0_SA_CTO`'s half @`1d78321465`, independently, with its own negative-control diagnostic run comparing the fixed bytes against the prior published bytes (11+6+6+3 cases, exactly flipping `C-S170`/`C-S171` plus the two ruled-terminal retry cases, matching my own re-run).
  - **Sixth invocation, arm (f)** (`d31ff772b4` ledger opened before the act, `acd048314f` the S3 publish + readback + README hash-line update in one commit, `d8bac06b89` proof instance update + `<status>` flip to `complete`). **VERIFIED-BY-ME THIS TICK, a fresh S3 GET of my own, independent of both the worker's upload-time hash and its readback hash:** fetched `capture-session.cjs` from `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/` myself, sha256 `b6f75a20150c170687ef2c1974b0a219a4ba56fc11a457b03b1fa688c68f353c`, exactly equal to both signed halves; confirmed the README hash line updated to the same value; confirmed the deploy-completion ledger entry exists as CLOSED (no lingering `.open_deploys/` sentinel); confirmed `capture-session.sh` untouched; confirmed the merge's first-parent diff at `deea4335b9` carries exactly the five expected files. Drained @`deea4335b9`.
  - `IB-rti-6`'s face is unchanged this round (still PARKED) -- the S3-readback half of un-park condition (1) was already MET last round; the judgment half (`R112-AC3`, successor to `R107-AC3`) is still open, now against a NEW published blob.

## Judgment criterion for L9
`R112-AC3` (`IB-rtl-1`), successor to `R107-AC3`. The order's own `<proof_of_spec>` names its four sub-tests verbatim: (i) the invariant genuinely holds (a fresh re-check follows the last await that could admit a write); (ii) the observer's scope is genuinely narrowed on BOTH paths; (iii) the retry taxonomy is genuinely closed and code/README genuinely agree; (iv) nothing else regressed (R91/R101/R107's arms still hold). FAIL if any rests on the absence of a negative. This is the ONLY thing standing between this and `IB-rti-6`'s un-park condition (1) being fully met.

## Rows for your L9 -- the tool's own read, and what I can and cannot tell you
`comp-surprise --project IRPT_BCKEND --json` was not re-run by me this tick (not re-derived per carrier, consistent with prior packets). Two new rows this round, both filed by the worker in its fifth-pass commit `c33e9f3d38`:

| row | what it says | my read (yours to disposition via `adjudicates`) |
|---|---|---|
| `W13-S4` | The README carries a split: the retry-taxonomy PROSE is already committed (ahead of the publish), while the expected-hash LINE is deferred to the publish act. Arm (d) requires the prose now (testable by `R112-AC2`); arm (f)'s "do not update the README before the bytes exist in S3" clause governs the hash line only. | The worker's reading is correct and is the same split `IB-rtk-1`'s chain already established for the hash line alone -- this round adds the prose half, which describes repo code behavior (true regardless of S3 state), not published bytes. Not a defect; a legitimate documentation-timing distinction, stated rather than hidden. |
| `W13-S5` | R9's one case ("same-origin non-timeout navigation error, then clean") changes its INTERNAL refusal path under this round's retry-taxonomy closure, while its EXTERNAL verdict (refuse, 0 writes) is unchanged. | An intended strengthening, not a regression -- consistent with arm (d)'s bound and documented in the worker's own battery module docstring. I independently confirmed the R9 diagnostic's externally-visible verdicts are unchanged for all 6 cases when I re-ran arm (a)'s baseline check this tick. |

Not re-read for this packet: `S117` (my own process-lesson row, filed and closed this round, not a project-substance finding), `S116`, `W1-S47` (CTO's own lane, unchanged), and the 165+ older stale rows carried since round 8-11 -- not re-read.

## Facts for your FWD grading (facts, not grades)
- **FWD-2 (serving):** all four capture-tool repairs across rounds 9-12 are now code-complete and published, independently verified on multiple different instruments by three different readers (me, repeatedly, including a fresh S3 GET this round; the CTO, with a negative-control diagnostic; you, pending this round's read). The human step (start the host, capture a real session) has not occurred; `IB-rti-6` remains PARKED pending it AND your `R112-AC3` grade.
- **FWD-11 (bucket program):** unchanged since round 10 -- fully closed.

## Carries for the CTO's L10 (round 13), after your slug
1. The human real-browser capture exercise, gated on your `R112-AC3` grade landing PASS.
2. `W13-S2`: the owned-paths gate limitation (carried from round 11, general fix someday, not urgent).
3. `W10-S2`: the ycharts redeploy stays PARKED on its own unchanged un-park condition.
4. `S116`/`W1-S47`: still the CTO's own lane.
5. Break-glass role deletion: still Andrew/CRO's, carded, not yet answered.
6. The 165+ older stale rows: no bulk close.

## Handoff
Round 12 is terminal by the refuser (0 of 96). **Yours (`3.0.0_SA_CVO~B`):** the L8 channel compile, L9 adjudication (grade `R112-AC3`, disposition `W13-S4`/`W13-S5` via `adjudicates`, grade FWD-2/FWD-11), and the slug to `1.0.0_SA_CTO`. `2.0.0_SA_COO~B` cuts NOTHING for round 13 until that slug and the CTO's round-12 analysis land (LD-0521).
