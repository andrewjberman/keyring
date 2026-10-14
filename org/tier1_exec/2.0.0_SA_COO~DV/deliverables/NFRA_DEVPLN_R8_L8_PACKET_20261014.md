# NFRA_DEVPLN round 8 -- L8 packet for 3.0.0_SA_CVO~L (issuer 2.0.0_SA_COO~DV, 2026-10-14 ~13:1xZ)

Round 8 carries one SERVED order, `NFRA_DEVPLN.TO-DP-y-1` (the client-facing chosen-set promote of five dell2 features to portal PROD, executed by `0.4.0_DT_ClientPlatform`), and one LOCAL order, `NFRA_DEVPLN.TO-DP-j-1` (the DEV push gate drops its two direct-push exemptions). Neither has a judgment criterion, so there is nothing for L9 to grade; this packet puts the served artifacts and the issuer's own reads in front of the CVO.

## Andrew's word (the client-facing hold)

Andrew approved all five features himself, ~11:4xZ 2026-10-14: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md` rows 1-3, verbatim "1.) Yes. 2.) Yes. 3.) Yes." The rows (dell2 list) read CLOSED `by=andrew decision=approved`; `open-calls.py approval-status` read `state=APPROVED valid=yes` for each at the head in the order's table.

## DP-y-1: the issuer's independent reads of the served artifact (origin, read ~13:0xZ)

| claim | read | result |
|---|---|---|
| the five landed as five release merges, in the order asked | `git -C portal log --first-parent 7db035e4..origin/PROD` | `22bd0695` 8500 held-submit, `3e662b27` 7b45 advisory fee, `690caad5` fde0 model order, `87e55658` 3635 YTD and export modal, `501e998b` 7773 partner-firm stack, then dell1's later `6a5926fc` |
| each names Andrew as approver | `git -C portal log origin/PROD --first-parent --format=%B \| grep -c "Approved-By: andrew @dell2-"` | `5` |
| no unapproved DEV commit rode in | `bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e3...` | `features=10 first_parent_commits=10 unapproved=0 ref=refs/remotes/origin/PROD` (ten: the earlier four, these five, dell1's `6a5926fc`) |
| CI and tag | the DT's receipt (`gh run list --commit`) | run 38563449756 success on `501e998b`; tag `portal-v2.1.218` |
| the deployed site carries the five (the one real run) | live `s3://opalinvest-portal/assets/` downloaded and searched, the bucket's objects date 12:42Z, which fits dell1's later release `6a5926fc` (branch stamp 123810Z; a descendant of `501e998b`) but is INFERRED from the two times, not read from the CI run | 3635: the YTD label template `(from ${...})` is in `assets/resolveBundle-CjyC3Nrc.js`. 7b45: the form state `advisory_fee:""` is in no bundle; the words "Advisory fee" remain in two bundles only as a row of the read-only request summary (`['Advisory fee', typeof e.advisory_fee=="number" ...]`), which is existing behaviour for stored requests. 7773: "No firm is available to you", "Your profile names no firm you may file for", "No analysis requests for your firm yet" are each in one bundle. 8500: "Add a title for the ticket to create it" is in one bundle |

## What this does not show (stated, not hidden)

- It is a read of the deployed code, not a signed-in session. No client or partner login was used; a partner sees the new board only on a localhost dev build (the route gate in `7773` is DEV-only by design), so the partner flow is not reachable on PROD today.
- DEV and PROD each hold their own merge of the same feature; the three ANLREQ features keep their earlier unapproved direct merges on DEV (`73d8d3a4`, `0101dd66`, `a577cba5`) as before.
- `DPy1-AC1` was amended by the issuer: its first text counted `features=9`, a moving target (dell1 released after the promote); the five are counted by `DPy1-AC2`. The DT's proof instance still records AC1 FAIL against the old text (it lives in the DT's own folder, outside the issuer's lane); the issuer re-ran the amended AC1 and read `unapproved=0 ref=refs/remotes/origin/PROD` (PASS), and flipped the order on that re-grade (surprise row `NFRA_DEVPLN-S7`).

## DP-j-1 (LOCAL, merged `75b81d396c`)

`python .tools/tests/test_dev_push_payload_gate.py` reads `cases=21/21 ok=True` on the merged tree; the proof instance is VALID. A live FAST lease no longer admits a push and a plain test-only commit is refused; a test-only MERGE with `Approved-By: test-only @-` passes as route B. `/closer-drive` step 5 lands through `portal-merge-forward.sh`. Two small defects are listed for the next round in row `NFRA_DEVPLN-S7` (a spacing typo; a project code hard-coded in the skill example).

## Channel watermark

`surprise-channel/investigations/INVESTIGATION_v1.md`: round 8's rows `W1-S19` (OBSERVATION, was ARMED; disarmed by the issuer in `S7` with the pre-push containment read), `S6` (DT, ruled in `S7`), `S7` (issuer). The CVO's next compile reads them.

Nothing is asked of the CVO beyond reading.
