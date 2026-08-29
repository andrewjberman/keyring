# /self-drive D2 & D3 — tick 16 (2026-08-28 19:20Z) — state: ARMED

Covers tick 16 (tick 15 logged @30b8069e0b). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: INSURE's chain wiring DEPLOYED on this
seat's plan-gate GO; PERFRP round 2 measured before it is built; a premise in this seat's own brief
corrected at source.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342, 0 claimed-not-member.

## Calls (§1-2)

**Zero.** No adjudicable, no RESERVED. GATE A unchanged.

## Verdicts / rulings since tick 15 (§3)

- **TO-A4-AEC DEPLOYED (~K 78799) on GO 78677 — NEVER#6 ledger CLOSED 5/5.** Apply's own line
  "3 added, 2 changed, 0 destroyed" == the plan; 0-diff on the target AND on the whole bd-pipeline
  root (78677 item 2 discharged by measurement); read-backs: rule `bd-49f-insurance-session-daily`
  `cron(35 4 * * ? *)` ENABLED, target input `{mode: session-refresh, runner: insurance}`,
  `INSURANCE_RUNNER_FUNCTION_NAME` present with the 7 priors intact, session-trigger CodeSha256
  byte-identical to the build's printed sha (resolved through the source map); act (c) five IAM arms
  as separate invocations on both fence axes (resource-axis: same role → gold-dispatch implicitDeny;
  principal-axis: keepalive-role → reporting-pull implicitDeny); AC5 positional VALID.
  **THE CANONICAL CHAIN NOW CARRIES THREE RUNNER TARGETS — main 00:00Z, insurance 04:35Z, fees
  22:20Z MON-FRI. AC4 = the first scheduled fire 2026-08-29T04:35Z (time-gated; the same day's main
  run as the negative control; no manual invoke spends it).** `INSURANCE_EGRESS=1` re-measured live
  at ~K's seat. RAVC closed at this seat on (a)-(c); ~K kept for the fire read (my read to COO).
  Surprise lines routed: `record-terraform-deploy.sh`'s source-map write silently no-ops under bun on
  this device (`git -C "/cygdrive/c/..."` from a native binary — the MSYS-argument class, a THIRD
  caller) and still commits "ci: record deploy" → 0.8.0, obligations row 7 item (k); tag bd-v2.56.0
  imprecise (contains all four deploy commits) → integrator's call; commit 17db393744 swept 0.6.0's
  artifact sha under ~K's line (value true, authorship wrong, disclosed).
- **TO-R2-DS STEP 0 / AC0 DISCHARGED (DS~V 78801 @07727aef87)** on CVO's step-zero PASS (78735:
  10/10 cells at decomp pin 1ce9b2d6bc; CVO (i)/(ii) verbatim + mechanical; AC6 in the right member;
  CVO's own first cell read printed 10/10 ABSENT on backticks crossing a bash-quoted `python -c` —
  the seventh firing of that class today — re-run from a file). Census: **11 of 11 round-1 leaves
  NEVER EMITTED to any served plane** (three instruments each with a positive control: the tree;
  `platinum/advi/49financial/` = 12 objects, 0 perfrp, all predating the emitters;
  `git log --all --diff-filter=A` = 0) — the DESIGNED round-1 end state (the emit core has no S3
  write path). **(b) = the SERVING GATE, narrower than pitched:** `PERFRP_AVAILABLE_LEAVES` gates
  ONE of five cards (gain_loss); the four visible cards are emptied by `payload={null}` at
  `AdvisorBookView.tsx:868` because no artifact is served at all; the contract handshake is NOT the
  gap (both constants `perfrp-contract-0.5.0-skeleton`). Campaign pinned on the COMMITTED plane
  (`7c6aa7cea7`, 63 of 534; working tree 85 at 19:13Z, named and not pinned). COO's two issuer
  clauses were on the face (78748): the per-table pin = `{max_last_modified_utc, n_partitions_read}`
  + campaign ledger commit + dates_complete_of_534; the serving-gate branch pre-decided — build
  proceeds, DE~D re-seats on the first FIXTURE-CONSUMABLE QA emission or the serve word (re-based
  from my 78741). PRF-b-2 started.
  **Two premises corrected:** (1) the D2 brief's P4.1 "(Activity/Allocation already ship)" — THIS
  SEAT's artifact — FALSE on every plane measured; corrected at source, dated, cited
  @1d4b2ddf2c. (2) the pitch chain's "the leaves constant blocks the DE lane" — the proximate cause
  of DE~D's 7 UNCOMPUTABLE rows is no served artifact at all, the same serving gate; the re-based
  re-seat trigger needs no change.
- **Campaign:** 88 of 534 distinct dates ARTIFACT-COMPLETE in the working tree at 19:20Z, 0
  non-complete; committed pin 63 @7c6aa7cea7. Pause bundle at 12:45Z agreed at four items
  (DocumentVersion pin; `StateReason.Code` read-before-start as CODE in `ensure_host_running` — ~L
  corrected its own "operator procedure" framing; row-6 card scope; the bounded OS-journal read with
  the volatile-journald caveat stated up front). Halt trigger UNRESOLVED, six candidates excluded.
- **CVO 78735 P2s** applied by COO (78748); my 78683 "twice at 12:45:41Z" relay struck (tick 15).

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @f41fdaa7e7, ls-remote read 19:20Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · ledger read · campaign
  ledger working-tree count (distinct dates, not rows) · `git ls-remote` + MERGE_HEAD.
