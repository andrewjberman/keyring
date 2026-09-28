# Two orders, three of my own conclusions overturned by the next measurement — 0.7.0_AE_CloudOps~I

**archetype:** DEPLOY

**Date:** 2026-09-26 1200Z – 2026-09-27 0130Z
**Task Orders:** `NFRA_MCPINDEX.TO-MX-s-5` (source-map ASCII) — COMPLETE. `NFRA_MCPINDEX.TO-MX-s-4`
(BD asset-dim login + honest exit), amended mid-flight to steps 1–2 — step 2 done, step 1 blocked at
the vendor.
**Status:** MX-s-5 complete, instance VALID. MX-s-4 instance VALID with AC1 FAIL recorded as a
refusal-with-measurement; status stays `pending`, because a vendor blocker is not a completion.

## Objective

Take the source map to pure ASCII so the canonical deploy recorder can run on this device (MX-s-5),
then repair the Black Diamond asset-dim producer and make its wrapper stop reporting Success on
failure (MX-s-4).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `'lambda-source-map' --band SURFACED --limit 30` | 14,486 hits / 75,716 files. Candidate enumeration only — far too wide to be an answer; the two real writers were then confirmed by reading their code. |
| `comp-find` | `'convert_assets_to_silver' --band HEAD --limit 10` | **A measured zero that was wrong to act on.** |
| `comp-find` | `'opal-bd-asset-dim-download' --files --limit 25` | 79 hits / 76,059 files. Its DEF-band hit on the trigger Lambda is what exposed the `$LATEST` pin. |
| `comp-find` | `'bd_assets_dim' --files --limit 20` | 595 hits / 76,190. Run to answer Andrew's "is this AMGT?" rather than assert an answer. It isn't. |
| `comp-read` | `lib/opal_naming.py --for "signature of name()…"` | 2,769 lines. Produced `blackdiamond-assets-dim-daily` as **builder output** for the step-4 spec (rule 30). |
| `comp-read` | `org/ref/SESSION_LOG_STANDARD.md` | 209 lines, 43 sections. The AE shape used here. |

**What worked:** `comp-read` on `opal_naming.py` turned a spec item from a hand-typed name into builder
output, and incidentally explained a failing check nobody had explained — an earlier AC1 read
`ENABLED=0` against a rule that exists, because the live name is `bd-asset-**dim**` and the check tests
for `assets-dim`. The check was measuring a naming gap and reporting an absent schedule.

**What failed:** `comp-find 'convert_assets_to_silver' --band HEAD` returned a **measured zero over
76,147 files** for a file that is named exactly that, is git-tracked, and sits at
`data/black_diamond/scripts/silver/`. I briefly concluded the script had no repo copy. A plain `ls`
found it in one call. The zero was convincing, which is what made it dangerous.

**Gap found:** two, both filed. `record-terraform-deploy.sh` does not merely *fail* on mojibake — its
unguarded read **manufactures** it (`Z-S13`). And the estate's honest-exit idiom **strands its EC2
runner** in 5 of 6 documents (`Z-S17`).

## Deployment Sequence

| # | act | instrument | result |
|---|---|---|---|
| 1 | 23 non-ASCII chars out of the source map | scripted, accounting asserted | 23 → 0, 8 of 218 rows, structure identical |
| 2 | Step-7 recorder re-run | `record-terraform-deploy.sh` | **exit 0** — and it computed the same commit I'd hand-written |
| 3 | MX-s-5 AC1 | `s5.AC1.sh` | **PASS** exit=0, run by me not carried from the issuer |
| 4 | Honest exit committed | `safe-commit` | `4b3a757410`, 59 → 60 lines |
| 5 | NEVER-2 ledger opened | `deploy_ledger open` | 6 legs, rollback corrected pre-act |
| 6 | Deploy v2 | `ssm update-document` | Hash `0be92f26…` → `5130ead6f5…`, live re-read |
| 7 | **ONE vendor-facing run** | `bd-asset-dim-trigger` | cmd `9ba8d9c9…`, on Andrew's word ×2 |
| 8 | AC4 evidence | `get-command-invocation` | **Failed, ResponseCode 1** — was Success before |
| 9 | Reorder committed + deployed v3 | `safe-commit`, `update-document` | shutdown@58 now precedes exit@63 |
| 10 | CTO's CR-strip patch | `git apply`, `commit-gate` | `765093b0e3`, claim re-measured first |

## Verification

- **MX-s-5 AC1 PASS** — `nonascii_chars=0 json=ok`. The arm that failed (`json.load(open(path))`, the
  recorder's exact bare form) now reads 218 functions where it raised at byte 32218.
- **MX-s-4 AC1 FAIL** — measured, and the failure *is* the deliverable. `written after issue` moved
  0 → 1; `download_rc0=no`, because the login still times out.
- **MX-s-4 AC4** — recorded UNVERIFIABLE-BY-INSTRUMENT for the CVO. The discriminator is not that the
  run failed (it always does) but that **SSM now says so**: identical log text, opposite verdict.
- Both instances validate `rc=0`.

## Decisions Made

1. **Held the lane on the operator's interrupt, not the issuer's clearance.** The issuer measured
   MX-s-5 passing and nudged repeatedly; a peer's measurement does not lift a hold placed by the
   person at the terminal.
2. **Parked rather than pretended to deliver.** With the broker down I could not ack or send, and the
   registry refuses me write access to peers' inboxes. Items were parked on my own carrier with an
   owner and an un-park condition instead of being written somewhere nobody reads.
3. **Did not reconstruct another seat's surprise row** from the handful of fields I'd printed when a
   lost-update race dropped it. Rebuilding it would have been fabrication wearing the issuer's name.
4. **Refused rather than routed around** on MX-s-4's step 3: the fix is a DS-owned script under rule
   13, and `--backfill` on a schedule was named and rejected rather than quietly not considered.
5. **Took the reorder to the estate's idiom and then past it** — copying gave honesty; reading gave
   honesty without a stranded instance.

## Files Modified

| path | commit |
|---|---|
| `infra/aws/lambda/ci/lambda-source-map.json` | `b25d506310`, then `22b5419f82` (recorder's own stamp) |
| `infra/aws/ssm/opal-bd-asset-dim-download.json` | `4b3a757410` (exit), `03e744ec3f` (reorder) |
| `infra/aws/ec2/safe-ec2-deploy.sh` | `765093b0e3` (CTO's patch, my lane) |
| surprise channel — `Z-S13`, `Z-S15`, `Z-S17` | `52ac1c0973`, `b629459239`, `18379da757` |
| two NEVER-2 ledgers, two Andrew-direct records, two instances, the step-4 spec | various, all above |

## Blockers

**One, and it is not the fabric's to clear.** The Black Diamond login has failed every run since
2026-06-23 across **all three** downloaders with the identical error. Three independently-written
scripts, one error, one day, is a shared upstream — the portal, the credential, or a new MFA. MX-s-4
step 1 carves that out as Andrew's word. He authorized one ad-hoc reproduction, which is spent; he did
not authorize a new credential, and none was sought.

**Owed and parked:** the report to `2.0.0_SA_COO~O`. The broker tools are down at this lane; peers are
routing as files and their inbox lanes refuse this serial.

## Current State

The source map is ASCII and the canonical recorder runs on this device. `opal-bd-asset-dim-download`
is live at v3 and is now the only one of six BD documents that both reports failure honestly *and*
stops its runner. `i-0e6f6dc014fdcf1cd` is running — left up by v2's exit-before-shutdown, its stop is
Andrew's under CLAUDE.md, and Monday's scheduled fire will stop it regardless, so the exposure is
bounded by the weekend. `Z-S17` stays ARMED until it is.

## Next Steps

1. **[Andrew]** Stop `i-0e6f6dc014fdcf1cd`, or let Monday's fire do it.
2. **[Andrew]** The Black Diamond login — a credential, an MFA device, or a vendor conversation.
3. **[`2.0.0_SA_COO~O`]** The four sibling documents with the same exit-before-shutdown order, queued.
4. **[DS lane]** `MX-s-6`, the compaction condition.
5. **[`0.0.0_AB_MSTR~Z`]** Push; everything since `9736741fe6` is local.

## What I got wrong, in order

Three conclusions this session were overturned by the next measurement, and all three were confident.

1. *"Step 3 is probably a non-issue."* Wrong — the compaction gate is `--backfill`, and fixing the
   login would never have restored it.
2. *"The script has no repo copy."* Wrong — from a band-scoped zero I should not have read as absence.
3. *"The pattern does not leak instances in this fleet."* Wrong, and the costliest — a single
   `describe-instances` snapshot answering a question about a standing property. The structural read
   takes one command and says 5 of 6 strand. I had that exact lesson banked and leaned on the snapshot
   anyway; it cost a stranded t3.medium and an ask to Andrew that should never have been needed.

The pattern is not carelessness in the measuring — each individual read was real. It is **reaching a
conclusion the read does not support, and stating it without the qualifier.** The controls caught all
three, which is the system working; but two of the three were stated to Andrew before they were caught.
