# NFRA_DEVPLN round 8 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-14 ~13:3xZ)

Issuance `7969c4a598` (PRD v0.3 @14a0501ee5; input: your round-7 list, your msg 109110 and 109118 carrying Andrew's ~11:4xZ word; no round-8 analysis file existed). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 8` reads `reviewer=present (3.0.0_SA_CVO~L) orders=2 proofs ok=2 verdict=MAY-CLOSE`. Push state: all commits named here are LOCAL on `box/laptop` (push state UNREAD; box-sync carries them; the DT reports `origin/box/laptop` lacks its `8ac6ae8599` and `8a351af853`).

## 1. The orders (2 of 2 complete)

| cell | result |
|---|---|
| DP-y-1 (SERVED, `0.4.0_DT_ClientPlatform`) | **FWD-1's client-facing close is on PROD.** The five dell2 features Andrew approved went out as five release merges, built by `portal-release-build.sh --features` in the order asked: `22bd0695` 8500 held-submit, `3e662b27` 7b45 advisory fee, `690caad5` fde0 model order, `87e55658` 3635 YTD and export modal, `501e998b` 7773 partner-firm stack (CI run 38563449756 success, tag `portal-v2.1.218`, `PROMOTE-CLIENT-FACING count=5`). Issuer reads: 5 `Approved-By: andrew @dell2-` trailers; `--check PROD` `features=10 first_parent_commits=10 unapproved=0 ref=refs/remotes/origin/PROD` (ten because dell1's `6a5926fc` released after); the live `opalinvest-portal` bundles carry the shipped strings (packet below). |
| DP-j-1 (LOCAL, worker ~1, merged `75b81d396c`) | Your law edit's follow-on: the payload gate no longer admits a live FAST lease or a plain test-only commit. Route B is now a test-only MERGE with `Approved-By: test-only @-`. `/closer-drive` step 5 lands through `portal-merge-forward.sh`. Suite `cases=21/21`, merge-forward 29/29, release 12/12. |

Preceding acts: A14a, the integrator pushed the merge-forward of `3635` and `7773` to DEV (DEV `22795405`, then `97c66c93` with dell1's work). MSTR had deleted those two `cand/dell2` refs from origin after the push and restored them at the row-bound shas when I asked; it holds the other deletes no longer.

**Amendment, for your read:** I amended `DPy1-AC1`, which counted `features=9` on a trunk another box also writes (it read 10 once dell1 released). It now expects `unapproved=0 ref=refs/remotes/origin/PROD`; the five are counted by `DPy1-AC2`. No gate limb graded the amendment (a modification of an order with `<placeholders>NONE`). The DT re-graded its proof instance PASS (`8a351af853`).

## 2. State of the project (measured ~13:3xZ)

- Portal DEV `97c66c93`, PROD `6a5926fc`. PROD holds ten approved features since the settlement (laptop 1, dell1 4, dell2 5), `unapproved=0` at the tip.
- The L8 packet is with `3.0.0_SA_CVO~L` (`org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_R8_L8_PACKET_20261014.md`, sha256 `3ea4b65e6a2f6a56`; no judgment criteria; read only).
- Rows: 47 investigation rows, ARMED 0. New this round: `W1-S19` (worker: `.tools/hooks/never-rules-gate.sh` still has the lease and test-only DEV carve-outs), `S6` (DT: the moving count), `S7` (my disposition and the repair list), `S8` (the carrier that dispositions `S6` and `W1-S19`).
- `P4-PROMOTE-49F` is flipped `superseded` (`1575b56f75`, your msg 109136); its acceptance re-check stays open and is not mine.
- S5 (the unblock tick reading another box's call) is served: `NFRA_CTLPLN-S9123`, COO~C's `TO-CT-ac-6`, merged `2d35ab062c`; verified on real dell2 rows (`WAITING`, `empty=0`).

## 3. What this does not show

- No signed-in client or partner session was used. The partner-firm flow is reachable only on a dev build (its route gate is DEV-only), so FWD-1's client-facing hop is read as deployed code, not as a user clicking through.
- The deployed bucket's objects date 12:42Z, which fits dell1's later release; I inferred that, I did not read it from CI.

## 4. ENRICHMENT list for round 9 (one repair cell, if you agree it is worth a round)

1. `.tools/hooks/never-rules-gate.sh`: remove the FAST-lease and test-only DEV carve-outs (W1-S19). It is MSTR's integrator gate and not in this project's paths: your ruling on whose file it is, or a path grant.
2. `dev_push_payload_gate.py`: `walk =git(` spacing. `.claude/skills/closer-drive/SKILL.md` step 5 example: `--project NFRA_DEVPLN` should be `<CODE>`. Both are DP-j-1's defects (the worker could not be resumed).
3. Not mine, listed so it is not lost: Andrew's other ~11:4xZ answers (dell1 restart, Kimi drafting, the asset manager, the S3 delete) belong to other projects; I cut none of them.

The client-facing close was the last item in the plan I know of: the grades are yours to read on the record above. Items 1 and 2 are a clean-up round, not an endpoint.
