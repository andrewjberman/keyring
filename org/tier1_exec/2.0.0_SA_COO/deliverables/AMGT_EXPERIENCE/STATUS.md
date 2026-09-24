# AMGT EXPERIENCE + SERVED RUNTIME

Seat: `2.0.0_SA_COO~Z`. Current thread: Peers B04/P1, mandate `AMGT_COMPLETION_20260923/COO_Z_PEERS.md` and CONTRACT at `7b26e2ac1c`. Reviewer: `3.0.0_SA_CVO~Z`.

## Pins and write claims

- Parent starting pin: `7b26e2ac1cb9f602e012cf439c0d6ee64e6e9e18` on CLOUD.
- Isolated worktree: `C:/tmp/closer-amgt-peers-z-20260924`, branch `closer/amgt-peers-z-20260924`.
- Portal starting pin: `c1ac41ecc17994dea48448b15c90535636711c24`; separate nested worktree on the same task branch name.
- Owned surfaces for this thread: identity crosswalk, peers producer, SecurityAnalysis frontend and existing API boundary. No gate or ownership-map edits. No source edits yet.
- Shared trunk is CLOUD. MSTR owns shared pushes; isolation branches remain intact.

## Live thread and acceptance

E0/B00 and P1 remain NOT_EVALUATED. The required first journey is real sign-in -> served `/security-analysis/BA_US_Equity` -> Peers, identity BA US, derived badge, 12 comparables, 5 present / 12 absent of 17. A `/market` redirect fails.

BLOCKER: no browser connector is exposed to this seat; localhost CDP endpoints 9222 and 9223 are unreachable, and no accessible signed-in admin+Dev session is in hand. Evidence: `PEERS_BROWSER_PROBE.json`. Andrew owns this input. An asynchronous request asks for the browser connection endpoint, not credentials. No synthetic login, token extraction or auth bypass was attempted.

Per mandate, the other three steps continue while E0 is blocked. Offline tests and backend measurements bank no live acceptance credit. Every case must cover the Posture subject/comparable reader as well as Peers.

## Next proof

1. Widen crosswalk registration using the existing universe/v1 identity set; retain ranker fall-through, refuse ambiguous/unmeasured names, never resolve from peers artifact identity. Measure all 191 prior pool keys, with named refusals if any.
2. Carry price/ev/ey onto member rows and map ey_ntm from factors with reciprocal P/E and the R-1 NTM display label. Verify five carried columns and actual per-column denominators, including Posture reads.
3. Own the batch trigger: after each crosswalk/v1 or universe/v1 re-mint, run peers engine over the current crosswalk. Prepare one current batch with exact set equality and the three previously missing names. Served-output writes retain the never-widen pair and review requirements; prepare the concrete candidate before requesting any missing review.

## Prior results and dependencies

Exact no-span guard deployed and backend C4 PASS relayed by CTO25099; `C4_RELAY_RECEIPT.md` preserves direct-invoke and overlay limits. Incident reach measured per R-11, historical remediation not closed. B08/Price local integration is preserved in the older experience worktree; it is not in this fresh Peers branch or the deployed signed ZIP. NO_COVERAGE reader scoped PASS was relayed by Y; integration/live acceptance remains separate.

## Parked and limits

Scanner-universe refresh: upstream owner unknown, un-park on owner assignment. FX band and 12 absent CSC columns: Andrew's data-source decisions. No vendor or Bloomberg call authorized. GitOps split stays with CTO's parked brief. No deployment, pool write, schedule change, or shared push performed in this Peers thread yet.
