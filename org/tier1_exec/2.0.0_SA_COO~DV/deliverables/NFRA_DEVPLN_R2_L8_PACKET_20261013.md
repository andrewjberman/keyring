# NFRA_DEVPLN round 2 -- L8 packet for 3.0.0_SA_CVO~L (issuer 2.0.0_SA_COO~DV, 2026-10-13 ~21:30Z)

Round 2 carries one SERVED order, `NFRA_DEVPLN.TO-DP-x-1` (the first chosen-set promote to portal PROD, executed by `0.4.0_DT_ClientPlatform`). It has NO judgment criterion, so there is nothing for L9 to grade; this packet puts the order's artifact and the issuer's independent read in front of the CVO so the SERVED close is on the record.

## The order and its artifacts

- Order `org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-x-1.live-chosen-set-promote.md` (status complete); receipt `deliverables/0.4.0_DT_ClientPlatform/NFRA_DEVPLN.TO-DP-x-1.receipt.md`; proof instance beside it (VALID, DPx1-AC1 and AC2 PASS).
- The DT's report is the seat's account. The issuer did not take it as the evidence.

## The issuer's independent read of the served artifact (origin, read ~21:15Z)

| claim | read | result |
|---|---|---|
| PROD tip | `git ls-remote origin refs/heads/PROD` | `10e7664d6c48` |
| what PROD gained since the settlement `63c4f9e3` | `git diff --name-status 63c4f9e3 origin/PROD` | exactly `A CONTRIBUTING-BOXES.md`; 2 commits (the feature and its release merge), 1 on the first-parent line |
| no unapproved DEV commit rode in | `merge-base --is-ancestor` for each of `62d455f5 9ef6a359 923f7d69 794b7df4 73d8d3a4 0101dd66 a577cba5` | all 7 "not on PROD" |
| the ancestry check on the real PROD | `bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e3` | `RELEASE-CHECK features=1 first_parent_commits=1 unapproved=0`, READY |
| CI | `gh run list --branch PROD --limit 1` | run 38466864693, `conclusion success`, `headSha 10e7664d` |
| tag | `git rev-parse 'portal-v2.1.214^{commit}'` | `10e7664d` |
| trunks after | `rev-list --count` both ways | `PROD..DEV` = 8 (the 7 unapproved plus the integrator's merge of the feature), `DEV..PROD` = 1 (the release merge) |

Approval chain for the one feature: row `laptop-20261013T200117Z-9e8a` closed `approved` by `1.0.0_SA_CTO` (class opal-internal), `approval-status` reads `APPROVED valid=yes`; DEV merge `24877b67` (pushed by `0.0.0_AB_MSTR` through `.tools/portal-merge-forward.sh`) carries `Feature:` and `Approved-By:`; PROD merge `10e7664d` carries the same two trailers.

## What this does not show (stated, not hidden)

- The "page a client opens" is a docs file in the portal repo root, class opal-internal, not a page. Hop 7 of FWD-1 is therefore read as a file on PROD, not a rendered page.
- DEV and PROD each hold their own merge commit of the same feature, so the two trunks cannot be fast-forwarded to each other again; the round-1 analysis expected this and ruled no change.
- The SERVED close here rests on mechanical criteria only. Nothing is asked of the CVO beyond reading.

## Channel watermark

`surprise-channel/investigations/INVESTIGATION_v1.md`: 28 investigation rows, 5 adjudication rows (the CVO's round-1 compile `0ad3906e16`), 0 ARMED. Round 2's 5 open rows for the CVO's next compile: `W1-S11`, `W2-S5`, `W2-S6` (BLOCKING; resolved by the issuer's amendment `4daa9baf69` and the merge `85ff4c9bee`), `W2-S7`, `W2-S8`.
