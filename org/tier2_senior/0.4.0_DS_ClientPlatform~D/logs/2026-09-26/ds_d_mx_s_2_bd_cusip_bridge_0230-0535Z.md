# 0.4.0_DS_ClientPlatform~D -- MX-s-2: the Black Diamond cusip bridge

**archetype:** DIAGNOSE

Session 2026-09-26 ~02:30Z -- ~05:35Z. Continues
`../2026-09-25/ds_d_mx_s_1_trueshares_holdings_silver_2255-0230Z.md`.

## Current State

**MX-s-2 complete as far as this lane can take it. All three criteria FAIL, and two of them are
refusals rather than failures.** Both orders from `2.0.0_SA_COO~O` are now reported. Nothing is
self-marked `complete`; the issuer decides a status on failing criteria.

The order asked me to schedule `build_bd_assets_dim.py`, per ruling R-2 (2). I did not, and the
reason is the finding: **the builder's only input is frozen on the same day as the bridge it feeds.**
`silver/bd_assets.parquet` LastModified 2026-04-14T20:09:23Z, 35 minutes before
`silver/bd_assets_dim.parquet`, both holding the same 10,937 asset_ids. Of the 791 asset_ids missing
from the bridge, **zero** are in that source. The ruled remedy would have rebuilt identical bytes,
moved `LastModified`, satisfied AC1's own freshness limb, and fixed nothing.

The real cause is one level further up, and it was sitting in S3 the whole time: the nightly BD
portal login times out. **69 consecutive failures since 2026-06-23** -- all 119 daily logs read in
full, 69 FAILED / 50 OK / 0 unclassifiable, and 69 of 69 the same signature, so one cause and not 69.
It is invisible because the SSM wrapper **exits 0 on the failure path**, so SSM records
`Status: Success, ResponseCode: 0` for a run whose own stdout says
`ERROR: Asset-dim pipeline failed (download_rc=1 merge_rc=99)`.

Drained `705dd96375`; rows `Z-S8`, `Z-S9`, `Z-S10`; instance VALID rc=0.

## What I got wrong, and what caught it

1. **I twice reasoned ahead of the measurement and had to walk it back.** First I concluded there were
   three stacked blockers on the ETF side; a scheduled sweep existed that bypassed one, making it two.
   Then here I concluded a served re-run "would change nothing" -- DIAG then showed up to 1,798 of
   6,988 rows carry a ticker today's bridge could resolve. Both times the correction came from asking
   what the explanation does NOT cover. The second one never reached a message; the first would have.
2. **A bare zero nearly became a finding.** `ssm list_commands` returned 0 commands, which reads as
   "nothing ever ran". Using the exact CommandId from the lambda's own log as a positive control
   returned a full record -- the zero was blindness, not absence.
3. **A peer committed my uncommitted rows.** `2.0.0_SA_COO~O`'s `8fc747bc09` swept up `Z-S8..Z-S10`
   from the shared working tree along with its own `Z-S7`. The rows landed and the gate graded them,
   but the log attributes them to that seat. This is the shared-index race 14b accepts as the price of
   not isolating an append-only channel. Recorded in the artifact pin rather than left to imply
   authorship.
4. **My own row ids were wrong in a document before the append ran.** I drafted the result doc naming
   `Z-S7..Z-S9`; the append recomputed `k` from the file, found a peer had taken S7, and landed
   `Z-S8..Z-S10`. The doc was corrected. Recomputing the id rather than hardcoding it is what caught it.

## Blockers

**One, named and owned elsewhere:** the BD portal login on `opal-bd-asset-dim-download`
(EC2 `i-0e6f6dc014fdcf1cd`). Until it is repaired, no act in this lane can make the bridge current, so
AC1 and AC3 cannot move. Owner AE/CloudOps + DT; a credential rotation or vendor-side interaction is
Andrew's word. Not a stall -- measured, filed as `Z-S8`, and asked of the issuer.

The served rewrite is correctly STOPPED on a never-widen sign-off with both halves UNSIGNED. I wrote
the request in full (73 partitions, rollback VersionId per key, bucket versioning verified Enabled)
and recommended against signing it yet, because today the rewrite reproduces the same numbers.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-schedule` | (not run) | The preflight says RUN AT THE ACT. **No act was taken** -- no schedule created -- so there was nothing to grade. Recorded as not-run with its reason: a silently skipped preflight on a schedule-creating order would read as a clean one. |
| `comp-find` | `comp-find 'bd_assets\.parquet' --all --limit 60` | 68 hits / 75,160 files. **N=1 writer** (`convert_assets_to_silver.py`), which is what showed a single dead producer freezes the entire bridge. NEVER-1's count-the-writers rule, used before reasoning rather than after. |
| `comp-pipescript` | io / deployed / postdeps | NOT-APPLICABLE, measured -- the BD asset-dim and `data/assets` trees resolve in no indexed pipeline. Same gap as MX-s-1, now recorded twice. |
| `safe-merge.sh` | `bash .tools/safe-merge.sh wk-mcpindex-s2-d -m "..."` | Refused rc=2 on a peer's 18 staged paths -- correctly, since merging would grade a union that is not my branch. I did **not** clear another seat's index; I armed an until-loop that fired when it cleared, then drained rc=0. |
| `proof-of-spec-check.py` | the MX-s-2 instance | VALID rc=0, violations=0, surprises 3 of 3 resolving -- first pass, because MX-s-1's 14-violation refusal had already taught the schema. |
| live AWS | events, lambda logs, `ssm get_command_invocation`, s3 head / sweeps / `get_bucket_versioning` / `list_object_versions` | Every denominator printed. The decisive instrument was reading all 119 download logs rather than sampling. |

## Next Steps

1. **[AE/CloudOps, via `2.0.0_SA_COO~O`]** repair the BD portal login, and make the wrapper exit
   non-zero on failure (`Z-S9`) -- a producer reporting its own result honestly, not an alarm.
2. **[DT]** restore the compaction to `silver/bd_assets.parquet`, which stopped at 2026-04-14 while
   `silver/assets/` kept landing through 2026-06-18 -- a second, earlier break in the same chain.
3. **[DT/AE]** rebuild `opal-assets-silver-etf` (MX-s-1's `Z-S4`): one act closes that order's AC2 and
   disarms `Z-S5`'s guard flip. Before 2026-09-26T23:30Z avoids the flip entirely.
4. **[`2.0.0_SA_COO~O`]** re-cut AC3 against a measured delta baseline rather than an absolute zero
   (`Z-S10`), and decide the status of both orders given their failing criteria.
