# NFRA_DEVPLN round 5 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-14 ~01:20Z)

Issuance `6d46d2db81` (PRD v0.3 @14a0501ee5, round-4 analysis @e8db882826, your messages 108974 and 108992). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 5` reads `reviewer=present (3.0.0_SA_CVO~L) orders=2 verdict=MAY-CLOSE`. Push state (ls-remote `cebc3266e9`): `6d46d2db81`, `367ce6ff40` and the round-5 record `ee17be347a` are on origin/box/laptop; the DP-f-2 merge `a7fb6b21b1` and the close commit are LOCAL. No SERVED or WORLD order this round, so no CVO packet.

## 1. The orders (2 of 2 complete, proofs VALID; every project suite re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-f-1 | `.tools/portal-hooks/dev_push_payload_gate.py` and its call from `.tools/portal-hooks/pre-push` for a push to `refs/heads/DEV`; routes A (an approved merge, read through `approval-status`), B (test-only), C (a PROD-into-DEV back-merge) and a live FAST lease; every other push fails closed. 19-case test | `367ce6ff40` |
| DP-f-2 | one test seam variable (`OPAL_GIT_READ_ROOT` removed; `OPAL_CLOUD_READ_LOCAL` also stands in for the git source; cloud-read test 8/8) and exit checks on the merge-forward self-test's fixtures through one helper (29/29; negative control: an unwritable fixture path aborts the self-test before any case is graded). Production read path unchanged (checked with the variable unset) | `a7fb6b21b1` |

Suites on the merged tree: cloud-read 8/8, withdraw 7/7, waiver 11/11, register 10/10, approval 13/13, open-calls 19/19, payload limb 19/19, merge-forward 29/29, release builder 10/10, DEV read 7/7.

## 2. Your three required demonstrations, run by the issuer through the REAL hook script (`.tools/portal-hooks/pre-push`, a pushed-ref line on stdin)

1. An unapproved plain commit onto DEV (`b5222d78` over PROD `10e7664d`): `DEV-PUSH-GATE result=REFUSED reason=unapproved-commit`, `ERROR: portal DEV is written only through .tools/portal-merge-forward.sh (an approved feature row)`, hook exit 1.
2. An approved merge (`24877b67` over `a577cba5`, row 9e8a): `ADMITTED`, exit 0.
3. An exempt route, read on real history: the PROD-into-DEV merge `63c4f9e3` over `15c97549` (route C): `ADMITTED`, exit 0. Also: a new ref named DEV is refused; a non-DEV ref is untouched by this limb. Routes B and the FAST lease are covered by the 19-case test, not by real history.

## 3. NOT live: the limb is not installed

The installed `portal/.git/hooks/pre-push` differs from the new canonical source (cmp). Install is a copy by `.tools/portal-hooks/install.sh`, the hook's lane owner's act, per your analysis. Until installed on a box, a script that pushes DEV directly is gated by nothing on that box. QUESTION for you (one): who installs, and on which boxes, first?

## 4. A second organic route run, measured

dell1's `cand/dell1/amgt-sa-header-money-and-dash-reasons` reached DEV as `5e40e541` with both trailers, approved by `1.0.0_SA_CTO~DELL1` (opal-internal, Security Analysis). The issuer read it from the laptop: the cluster-first reader found dell1's row, the payload limb admitted the push as route A against the row's bound head, the per-commit read lists it. Record: `NFRA_DEVPLN_DELL1_ORGANIC_ROUTE_EVIDENCE_20261014.md`. It is not the client-facing case.

## 5. Rows and watermark

Channel: 38 investigation rows, 7 adjudication rows, ARMED 0, 10 open observations. New this round: `W1-S15` (the order gave a live FAST lease "the whole push" and separate structural refusals with no precedence; the worker ran the refusals first, so a lease admits only the commit walk; stricter reading, awaiting the lane owner), `W2-S12` (the one-variable seam needs a guard keyed on `OPAL_STATE_ROOT` or a test case reads real `origin/box` refs; whether a production tool sets `OPAL_STATE_ROOT` is unverified).
Process facts, recorded: slot 2's first worker stalled for an hour with its edits uncommitted; the issuer stopped it (`TaskStop`) and reseated the slot with the edits as inherited state; the replacement finished in about 11 minutes.

## 6. Awaiting Andrew (client-facing; neither you nor the CVO can rule these)

dell2 rows `3635` (the YTD and export-modal feature), `8500` (anlreq-90), `7b45` (anlreq-88), `fde0` (anlreq-87), all OPEN on the cluster copy (`written_at` unchanged since 23:19Z); the law-edit card `laptop-20261013T223003Z-3d7e`. Until he rules, act A14 (the integrator's merge-forward of each approved feature, then the DT's chosen-set promote) cuts no order: there is nothing approved to merge.

## 7. ENRICHMENT candidates for round 6

1. After Andrew rules: A14, the client-facing close of FWD-1 (a DT order, SERVED, with the L8 packet).
2. The limb's install, as you direct (a lane-owner act, not a worker cell).
3. W1-S15's ruling and W2-S12's guard, as one small repair if you want them in code.
