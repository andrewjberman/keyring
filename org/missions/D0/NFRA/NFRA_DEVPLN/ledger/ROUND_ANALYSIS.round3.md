# NFRA_DEVPLN -- ROUND-3 ANALYSIS (1.0.0_SA_CTO, 2026-10-13 ~22:3xZ)

**On:** the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND3_DRAIN_END_20261013.md` (2 of 2 orders,
MAY-CLOSE; no SERVED or WORLD order, so no CVO packet this round). **PRD:** v0.3, unchanged. **Next:** round 4 in ONE issuance on
section 3.

## 1. What round 3 moved

- **DP-d-1:** the waiver flag on registration. It excuses named commits only, is refused outside the overlap or without its ruling
  file, and is proven on the real portal (`waived=2`, with the unwaived control `REFUSED overlap=2`).
- **DP-d-2:** merge-forward handles a local-only branch (W2-S7).
- **FWD-2's declined arm was shown refused** by both scripts, with DEV unchanged at `24877b67`. It is named for the CVO's grade read
  beside the approve arm from round 2.
- The three dell2 feature branches were cut from PROD on portal origin. Registering them waits on a dell2 seat, because one box
  writes one list.

## 2. Ruling (W1-S12): the waiver set

**CONFIRMED: the four feature commits.** My ruling (`CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md`, bb8b) said "the three named
merge shas". The issuer is right that merge commits `73d8d3a4`, `0101dd66` and `a577cba5` lie on no feature branch, so they are never
in a registration's overlap.

The waiver covers exactly the commits those three merges brought onto DEV:
- `923f7d69` and `794b7df4` (`cand/dell2/anlreq-90-held-submit`);
- `9ef6a359` (`anlreq-88-advisory-fee`);
- `62d455f5` (`anlreq-87-model-order`).

No other commit is waived. This analysis is the waiver ref for those four. A `--waiver-ref` naming any other file for them is not
this ruling.

## 3. ENRICHMENT LIST for round 4

1. **S03, the gate edit, by this seat.** It is now the thread-breaker: the refusal arm (A7) and FWD-3's grade wait on it. It lands
   before the round-4 issuance is graded. The issuer then reads the refusal on a box seat and the gate bytes on all four box branches.
2. **The three dell2 rows:** registered by a dell2 seat with `--waive-overlap` naming section 2's commits and `--waiver-ref` this
   file. Andrew rules them (client-facing). The next chosen-set promote ships only what he approves, as a DT order at that time.
3. **dell2's next IRPT_ANLREQ change through the route.** This project's part is the registration check, the merge-forward and the
   read.
4. **One repair batch:** W2-S9 (prefer the stale-safe ref) and W2-S10 (the merge-base warning). W2-S8 goes to the CVO as an
   observation on `proof-of-spec-check.py`, outside this project's paths.

## ADDENDUM ~22:3xZ -- S03 landed, and what a command gate can and cannot see

**Landed** in `.tools/hooks/never-rules-gate.sh`: fate (ii), the DT's portal DEV admission ENDS, with a refusal that names the
route. The DT keeps PROD.

Read on five cases, all as intended:
- a DT pushing DEV is refused;
- a DT pushing PROD is admitted;
- the integrator pushing DEV is admitted;
- a CTO pushing DEV directly is refused;
- any seat running `portal-merge-forward.sh --push` is admitted.

The existing gate suites still pass: nested-repo 4/4 and halt-gate 3 arms.

**The finding that changes S03's shape.** The gate is a PreToolUse hook: it sees only the command a seat types. The merge-forward
script runs its `git push` inside itself, so the gate admits the approved route by construction. The script, which refuses without
an approved row, is the enforcement point. The gate needs no trailer-reading limb.

**What is still open:**
- Fates (iii) FAST lease and (iv) test-only stay as they are. Both are CLAUDE.md law ("lands product changes on portal DEV
  itself"; "a portal candidate touching NO product file lands on DEV by its author"), so they change only on Andrew's word. That is
  carried on this seat's list.
- A seat could still push DEV from a script of its own, which a command gate cannot see. The structural close is a payload check in
  the portal repo's git `pre-push` limb (`.tools/git-hooks/pre-push-safe-deploy.sh`): a push to `refs/heads/DEV` passes only if
  every new first-parent commit is a two-parent merge whose trailers name an approved row (`approval-status valid=yes`). It runs for
  every git push on every box, scripted or typed. That is a round-4 cell for this project. The file's lane owner signs the limb.
