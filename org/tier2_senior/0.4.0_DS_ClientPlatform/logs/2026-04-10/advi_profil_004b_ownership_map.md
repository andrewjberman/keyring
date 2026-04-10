# ADVI_PROFIL.004b -- Advisor ownership map writer in D_00

**Date:** 2026-04-10
**Agent:** 0.4.0_DS_ClientPlatform
**TO:** `ADVI_PROFIL.004b.ds-client-account-ownership-map`
**Partner TOs:** `.004a` (AE 0.7.0, shipped today), `.004c` (AE 0.7.0, consumer)

## Summary

Added `_build_advisor_ownership_map` and `build_advisor_ownership_artifact` helpers to `D_00.portal_aggregates.py`, plus a `platinum_advisor_ownership_key(firm_id)` path helper in `lib/s3_layout.py`. D_00 now writes a firm-partitioned per-firm `platinum/{firm_id}/ownership_map.json` artifact at the end of its Step 2 build phase. The artifact is consumed by the Lambda@Edge ownership-check shipping in `.004c` (AE 0.7.0).

**S3 key (per AE + DT agreement):** `s3://opal-data-{firm_id}/platinum/{firm_id}/ownership_map.json`. Written to each firm's own opal-data bucket, one file per firm. Current D_00 is single-firm (`FIRM_ID='49financial'`), so this iteration writes exactly one file: `s3://opal-data-bd/platinum/49financial/ownership_map.json` (opal-data-bd aliases to 49financial per the shared-advisor-router FIRM_BUCKET_MAP).

**Schema frozen at schema_version=1. Any future change requires a coordinated .004c + frontend review per TO requirement #2.**

## ATTRIBUTION INCIDENT -- FLAG TO ANDREW

My code changes for this TO landed in commit `7ae0ef6b321ce3adeda1889023f6b66686d9fc45` attributed to `0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>`, not to me. The commit message is "log(0.7.0_AE): .004a test matrix validated + CloudWatch denial events confirmed" -- AE's session log work -- but the `--stat` shows my two files co-committed:

```
.../scripts/gold/D_00.portal_aggregates.py         | 122 +++++++++++++++++++++
data/black_diamond/scripts/gold/lib/s3_layout.py   |   7 ++
.../logs/2026-04-10/advi_profil_004a_scoping.md    |  91 +++++++++++----
3 files changed, 200 insertions(+), 20 deletions(-)
```

This is the exact attribution-corruption scenario documented in the memory rule [feedback_selective_staging_only.md](feedback_selective_staging_only.md) and in `org/XXX.md` lines 174-186:

> "During hectic multi-agent MCP sessions, several agents have dirty working trees at the same time. An agent that runs `git add -A` sweeps up other agents' in-flight work into their own commit -- the author line lies, the TO attribution is wrong, and downstream reviewers cannot tell who changed what."

**What happened (timeline reconstruction):**

1. ~19:02 ET -- DS (this agent) started session, registered, checked inbox
2. ~19:08 ET -- DS completed PROFIL.003 (no-op finding)
3. ~19:08-19:15 ET -- DS began PROFIL.004b investigation: comp tools, read D_00 source, sent AE S3-key agreement broker message (`20260410T230813Z`)
4. ~19:09-19:14 ET -- AE replied with firm-partitioned recommendation (`20260410T230953Z`)
5. ~19:13-19:16 ET -- DS edited `D_00.portal_aggregates.py` + `lib/s3_layout.py` (helper, sentinels, slugification, firm-partitioned key function, artifact body with firm_id)
6. **19:16:29 ET -- AE committed `7ae0ef6b` which swept DS's dirty working-tree files** (git Author date: `Fri Apr 10 19:16:29 2026 -0400`). AE's own work in that commit was a session log update -- not the gold-script files. The sweep was almost certainly `git add -A` or `git commit -a`.
7. ~19:17 ET -- DS dry-ran the helper against real `ACCOUNT_TEAM` parquet (162 advisors, 377 KB), verified sentinel containment and slug correctness, ran py_compile.
8. 19:17+ ET -- DS attempted `git add <files>` + `git commit --author="0.4.0_DS_ClientPlatform ..."`. Git reported exit code 1 with `git status` output showing "nothing to commit, working tree clean" because HEAD (the just-pushed AE commit) already contained the changes. DS initially read this as a hook failure; reflog + `git show 7ae0ef6b --stat` confirmed the sweep.

**Content verification (non-blocker for the fix, documentation only):**

`git diff HEAD -- data/black_diamond/scripts/gold/D_00.portal_aggregates.py data/black_diamond/scripts/gold/lib/s3_layout.py` is empty. My working tree and HEAD are byte-identical on these two files. The swept content is exactly the code I wrote -- no drift, no loss, no unwanted add-ons from AE's session. So while the author line is wrong, the code on disk and in HEAD is correct and ready to deploy.

**Recovery options considered:**

1. **Rewrite 7ae0ef6b's author** -- requires force-push to CLOUD. Per CLAUDE.md: "NEVER run destructive git commands (push --force, reset --hard, ...) unless the user explicitly requests these actions." Not taking this path without explicit Andrew authorization.
2. **Revert 7ae0ef6b entirely + re-commit separately** -- same force-push requirement, worse because it disrupts AE's already-merged .004a session log work. Not taking this path.
3. **Accept the mis-attribution and record it in a DS-authored commit** -- this log. DS authors a session log commit that names `7ae0ef6b` as the de-facto code commit, explicitly flags the attribution issue, and records the full deploy cycle. Audit trail stays honest even though the git author line is corrupted. This is the approach taken below.
4. **Andrew decides whether to force-push-fix** -- escalated to Andrew. See "Next Steps".

This attribution incident is the second such in this workspace (per memory the first was on ADVI_REBORN). Recommend a git hook (pre-commit) that refuses `git add -A` / `git add .` / `git commit -a` unconditionally, or at least warns if multiple files outside the commit author's known owned paths are staged. That is out of scope for .004b but flagging for Andrew / CTO to consider.

## Architecture Decision: firm-partitioned, NOT `platinum/shared/`

TO draft defaulted to `platinum/shared/advisor_ownership.json` (single global file). AE 0.7.0 overrode this after reviewing the existing `shared-advisor-router` firm-rewrite logic. Key points from AE's reply (msg `20260410T230953Z`):

| Point | Implication |
|---|---|
| `platinum/*` requests get rewritten by `shared-advisor-router` to `opal-data-{firmId}/platinum/...` based on `X-Firm-Id` header (v9 of the router) | A single global file at `opal-data-bd/platinum/shared/advisor_ownership.json` 404s for every firm other than BD because the rewrite points at `opal-data-49financial`, etc. |
| Workaround (a): replicate the file to every firm bucket | Ops overhead + staleness risk (multi-bucket writes are non-atomic) |
| Workaround (b): router special-case for `platinum/shared/*` | Code churn on a load-bearing Lambda@Edge. Breaks the "firm bucket" invariant hardened during ADVI_APISCP. |
| Cleaner: firm-partitioned `platinum/{firm_id}/ownership_map.json` | Writes to each firm's own opal-data bucket via the same pattern D_00 already uses for other per-firm platinum artifacts. Existing router rewrite is a no-op extension. **No Lambda@Edge change required.** |
| Cross-firm containment benefit (DT's .004c design, msg `20260410T224501Z`): | Travis at 49financial reads `platinum/49financial/ownership_map.json`. Even though .004c's admin bypass lets him skip the ownership check, the ONLY map he can ever read is 49fin's. Cross-firm data containment preserved at the edge. |
| Filename `ownership_map.json` vs TO's `advisor_ownership.json` | DT's .004c edge fetcher design names it `ownership_map.json`. AE agnostic. DS chose `ownership_map.json` because DT is the consumer and the producer/consumer names should match from day 1. |

## Schema (frozen at v1)

```json
{
  "schema_version": 1,
  "firm_id": "49financial",
  "generated_at": "2026-04-10T23:00:00Z",
  "advisors": {
    "alex_bright": {
      "accounts":      ["z0812883371", "z0812883501", ...],
      "relationships": ["0", "z08106011", "z08106026", ...]
    },
    "sam_owens":   { ... },
    ...
  }
}
```

- `schema_version`: integer, currently `1`. `.004c` checks this and rejects unknown versions.
- `firm_id`: self-describing sanity check (matches the path segment). Per AE's note: "cheap insurance against ops mistakes".
- `generated_at`: ISO8601 UTC. Used for .004c freshness diagnostics; not consumed for invalidation.
- `advisors`: map of advisor slug -> `{accounts: [...], relationships: [...]}`. Slug format matches `lib.mix_views.advisor_id()` (canonical, used by D_02 `advisor_book_key`, D_03 composition, D_04 platinum summary, frontend route params). Example: "Alex Bright" -> "alex_bright".

## Files Modified (for the record, even though mis-attributed in git)

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | Import `platinum_advisor_ownership_key` + `_canonical_advisor_slug` (from `lib.mix_views.advisor_id`). New helpers `_build_advisor_ownership_map(account_team)` and `build_advisor_ownership_artifact(account_team, firm_id)`. New Step 2 call after snapshots: unpacks `account_team` from `load_all()`'s return dict, builds the artifact, saves via `_save_json(ownership, platinum_advisor_ownership_key(FIRM_ID), dry_run=dry_run)`. Logs advisor/account/relationship counts in the `results` dict. |
| `data/black_diamond/scripts/gold/lib/s3_layout.py` | New `platinum_advisor_ownership_key(firm_id: str) -> str` function returning `f'platinum/{firm_id}/ownership_map.json'`. Comment block documents the firm-partitioning decision and the schema freeze. |

+200 / -20 lines total (per `git show 7ae0ef6b --stat`).

## Implementation Details

### Helper: `_build_advisor_ownership_map(account_team)`

Input: `account_team` pandas DataFrame with columns `{account_id, relationship_id, architect, implementor, consultant, local_ops, additional_advisor}` (ACCOUNT_TEAM parquet from C_07 via `gold/views/account_team.parquet`).

Algorithm:
1. Select the 2 id columns + 5 role columns.
2. `melt` into long form: `(account_id, relationship_id, _role, advisor)`.
3. Drop null advisor cells.
4. Strip whitespace on advisor values.
5. Lowercase-compare against `_OWNERSHIP_SENTINELS` frozenset to drop: `''`, `'nan'`, `'none'`, `'null'`, `'unassigned'`, `'unresolved'`, `'no {role} value assigned'` for all 5 roles.
6. Slugify via `_canonical_advisor_slug` (= `lib.mix_views.advisor_id`). Ensures consistency with D_02/D_03/D_04 slug form used everywhere else in the system.
7. Drop slugs that end up as `''` or `'unknown'` (mix_views fallback for fully-unparseable names).
8. Group by slug, dedupe accounts + relationships within each group, sort ascending.
9. Return `{slug -> {accounts, relationships}}` dict.

Edge cases handled (verified in unit tests):
- Advisor present in multiple roles on the same account -> one entry
- Advisor present in multiple accounts via different roles -> accounts correctly union-ed
- Whitespace-padded names (`'  Alice  '`) -> correctly stripped + slugified
- Sentinel-only rows (A4 in synthetic test) -> contribute nothing
- Mixed-case sentinels (`'Unassigned'`, `'UNASSIGNED'`) -> all dropped via lowercase compare

### Helper: `build_advisor_ownership_artifact(account_team, firm_id)`

Wraps `_build_advisor_ownership_map` with the top-level schema wrapper. Signature is `(account_team: DataFrame, firm_id: str)` -- firm_id is passed in from the caller (currently the D_00 `FIRM_ID` module constant), not hardcoded in the helper, so the function is reusable if D_00 ever becomes multi-firm.

### Path helper: `platinum_advisor_ownership_key(firm_id)`

Lives in `lib/s3_layout.py` next to the other per-firm helpers. Returns `f'platinum/{firm_id}/ownership_map.json'`. The bucket choice is implicit in the caller -- `D_00.main()` uses `S3_BUCKET` from `lib.config`, which is already `opal-data-bd` for the BD pipeline. Each firm's D_00 instance writes to its own bucket naturally.

### Wiring in `main()`

Two edits:

1. `account_team = data['account_team']` added to the `data = load_all(today)` unpack section. `load_all` already returns `account_team` in its dict; it was just not being unpacked because no existing Step 2 builder needed it directly.

2. New block after `snapshots = build_snapshots(...)` and before the `CloudFront invalidation` step:
   ```python
   ownership = build_advisor_ownership_artifact(account_team, FIRM_ID)
   _save_json(ownership, platinum_advisor_ownership_key(FIRM_ID), dry_run=dry_run)
   _own_advisors = len(ownership['advisors'])
   _own_accts = sum(len(v['accounts']) for v in ownership['advisors'].values())
   _own_rels  = sum(len(v['relationships']) for v in ownership['advisors'].values())
   results['advisor_ownership'] = (
       f"{_own_advisors} advisors, {_own_accts} accts, {_own_rels} rels"
   )
   ```
   Uses the existing `_save_json` helper -- no new S3 plumbing. Respects `dry_run` like every other D_00 artifact.

## Dry-Run Against Live ACCOUNT_TEAM (pre-deploy validation)

Pulled `gold/views/account_team.parquet` from `s3://opal-data-bd/` and ran the helper against it in-process:

```
account_team rows: 6,039
Advisors (post-slugify, post-sentinel-drop): 162
Account entries (dedup within advisor): 19,018
Relationship entries (dedup within advisor): 8,760
Size (minified JSON):  377,100 bytes  (368 KB)
Size (pretty JSON):    658,366 bytes
Size (gzip):            80,742 bytes  ( 79 KB)
Under 1 MB cap (TO #4): YES (38% of the cap minified, 8% gzipped)
No sentinel slugs in output: unassigned=0, unresolved=0, unknown=0, empty=0
```

**Spot-check (5 known advisors):**

| Slug | Accounts | Relationships |
|---|---|---|
| alex_bright | 1193 | 474 |
| sam_owens | 422 | 167 |
| collin_plotts | 720 | 377 |
| sydney_cobb | 540 | 240 |
| travis_penfield | 513 | 208 |

Alex Bright's account count is the firm maximum (consistent with his position at the top of every advisor-concentration ranking we've seen in the last 6 months of investigation). Sam Owens' 422 accounts + 167 relationships is consistent with his multi-role implementor + local_ops pattern documented in the ADVI_49PUSH.042 / .040 drilldown work.

**Sentinel containment (delta vs no-filter):**

Without the `unresolved` sentinel filter (initial first-pass implementation), the map had 163 advisors / 19,723 accounts / 9,160 relationships. The `Unresolved` pseudo-advisor claimed 705 accounts + 400 relationships. Adding `'unresolved'` to the sentinel frozenset drops it cleanly and gets us to the final 162 / 19,018 / 8,760 counts above. The only other sentinel in the real data is `Unassigned` (already caught pre-first-pass).

Verified by enumerating all 164 distinct role-column values and pattern-matching: exactly two are sentinels (`'Unassigned'`, `'Unresolved'`), 162 are real advisor names. No `'TBD'`, no `'N/A'`, no `'no * value assigned'` (those phrases exist in the D_00 header comment as a precaution but don't appear in live data).

## Deploy Cycle

| Step | Result |
|---|---|
| `git status data/black_diamond/scripts/gold/` pre-stage | Dirty on my two files (D_00 + s3_layout), as expected. |
| `python -m py_compile D_00.portal_aggregates.py lib/s3_layout.py` | OK (clean compile). |
| Dry-run against live ACCOUNT_TEAM | PASS (see counts above). |
| Commit | **MIS-ATTRIBUTED** to `7ae0ef6b` (`0.7.0_AE_CloudOps` author) by AE's session sweep. Content correct. See "Attribution Incident" section. |
| Commit SHA | `7ae0ef6b321ce3adeda1889023f6b66686d9fc45` (as of this log; may be rewritten by Andrew in a corrective commit) |
| Author (incorrect) | `0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>` |
| Author (correct) | `0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>` |
| Push | Already pushed via AE's `git push` (origin/CLOUD is at 7ae0ef6b). |
| S3 upload `D_00.portal_aggregates.py` | `s3://opal-data-bd/code/gold/D_00.portal_aggregates.py` |
| S3 etag (D_00) | `a9c0896833231ebd0fb63f84f527ab9c` |
| Local md5 (D_00)  | `a9c0896833231ebd0fb63f84f527ab9c` |
| Etag parity (D_00) | OK (exact match) |
| S3 upload `lib/s3_layout.py` | `s3://opal-data-bd/code/gold/lib/s3_layout.py` |
| S3 etag (s3_layout) | `786c405cca86fde4730af36f425af172` |
| Local md5 (s3_layout) | `786c405cca86fde4730af36f425af172` |
| Etag parity (s3_layout) | OK (exact match) |
| Gold runner trigger | **NOT invoked** per TO requirement #5 -- let the next scheduled `bd-gold-trigger` cycle pick up the new code. |

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp-pipescript io | `comp-pipescript io D_00` | Confirmed READS include ACCOUNT_TEAM (the input we need) and no existing WRITE to `platinum/shared/` or `platinum/*/ownership_map.json`. This is a new WRITE path -- additive. |
| comp-pipescript consumers | `comp-pipescript consumers D_00` | Consumers: D_00b, D_01, D_04 read D_00's existing outputs (CLIENTS_TAB, HEADER_METRICS, aua_certification_key). **None of them read `platinum/*/ownership_map.json`** -- the new artifact is consumed only by the edge Lambda in .004c (out of the gold graph). Additive-only, no gold-script downstream impact. |
| comp-routes | `comp-routes trace getPlatinumAdvisorSummary` | Confirmed the `platinum/**` CloudFront behavior routes through `auth-validator-edge` (viewer-request) + `shared-advisor-router` (origin-request). Same path the ownership_map.json will flow through, no new CF behavior needed. |
| comp-blast | `comp-blast D_00.portal_aggregates.py` / `comp-blast D_00` | No downstream matches in the compiler graph (known limitation -- D_00 appears under `gold:D_00.portal_aggregates` but isn't linked in the blast index for this key form). Fell back to `comp-pipescript consumers D_00` above which gave the definitive answer. Recommend a follow-up for CTO / compiler-team to fix the `comp-blast` node-name mismatch so `comp-blast D_00` works directly. |
| Grep | `tax_exposure` across gold/ | Not relevant to this TO; used it earlier for .003. Documented here only because the session log convention asks for the table even when empty. |
| py_compile | `python -m py_compile D_00.portal_aggregates.py lib/s3_layout.py` | Clean. |
| Unit-style synthetic dry-run | Inline exec of the helpers with a 5-row synthetic `account_team` DataFrame (Alice/Bob/Carol/Dave + Unassigned sentinel) | All 6 invariants pass. Alice's whitespace-padded name correctly stripped + slugified, dedup across multiple roles on same account correct, relationship-id union across accounts correct, sentinels dropped. |
| Live dry-run | In-process exec of helpers against real `ACCOUNT_TEAM` parquet from `opal-data-bd` | 162 advisors, 19,018 accts, 8,760 rels, 377 KB minified / 81 KB gzip. Spot-checks on 5 known advisors pass. |

Compiler tools log: to be appended.

## Broker Messages Sent This Session (.004b scope)

| Direction | Recipient | Subject | When |
|---|---|---|---|
| out | 0.7.0_AE_CloudOps | ADVI_PROFIL.004b -- S3 key proposal for advisor_ownership.json | 23:08:13Z |
| in  | (from) 0.7.0_AE_CloudOps | RE: .004b S3 key -- recommend firm-partitioned, not platinum/shared/ | 23:09:53Z |
| out | 0.4.0_DT_ClientPlatform | PROFIL.004b -- ratify filename: advisor_ownership.json vs ownership_map.json | 23:11:13Z |
| out | 0.7.0_AE_CloudOps (this log) | ATTRIBUTION INCIDENT + .004b ship notification | pending (sent in this session after log write) |
| out | 2.0.0_SA_COO + Andrew | Attribution corruption on 7ae0ef6b -- request guidance | pending |

DT's filename ratification was received implicitly via AE's quote of DT's `.004c` design note. DS chose `ownership_map.json` (matching DT's design) over the TO default (`advisor_ownership.json`).

## Acceptance Criteria Mapping

| TO # | Criterion | Status |
|---|---|---|
| 1 | S3 key agreed with AE | PASS -- AE recommended firm-partitioned, DS concurred, key = `platinum/{firm_id}/ownership_map.json`. Logged in both session logs. |
| 2 | Gold script modified | PASS -- D_00 helpers added, wired into main() Step 2. |
| 3 | Schema frozen at v1 with documented shape | PASS -- above. `.004c` contract explicit. |
| 4 | Active advisors only | PASS -- sentinel filter drops `Unassigned` + `Unresolved` + `''` + `nan`. All 162 remaining advisors are assigned to at least one real account row. |
| 5 | Size <1 MB | PASS -- 377 KB minified, 81 KB gzip. 38% of the cap / 8% gzipped. |
| 6 | py_compile + diff-before-ship | PASS on py_compile. Dry-run produces sane map (non-zero advisors / accts / rels). No diff-before-ship on a previous artifact because the file is net-new; the sanity is the count + spot-check. |
| 7 | Commit + push + S3 upload | **PARTIAL**: commit happened (attribution wrong -- see incident section), push happened (via AE's sweep), S3 upload parity verified by DS. Functionally deployable. Attribution is the only defect. |
| 8 | Runner pickup (broker message to AE 0.6.0) | PENDING -- will send after this log write. |
| 9 | AE 0.7.0 handoff | IN PROGRESS -- previous AE exchanges already established the S3 key. Final "first-run ship" handoff to follow after the first gold run lands the artifact. |
| 10 | First map population verified | PENDING -- after the next `bd-gold-trigger` cycle. Will append a follow-up section to this log with the actual S3 HEAD result. |
| 11 | Compiler Tools section | PASS -- above. |

## Next Steps

- **[Andrew]** Review the attribution-incident section. Decide whether to force-push a history fix on `7ae0ef6b` (rewriting the author line) or leave it and rely on this session log for the audit trail. DS recommends the latter -- force-push risk outweighs the attribution benefit, and a pre-commit hook blocking `git add -A` would be a cheaper durable fix.
- **[Andrew]** Consider adding a git pre-commit hook that refuses `git add -A` / `git commit -a` / `git add .` in multi-agent sessions. Would prevent this class of attribution sweep.
- **[Andrew]** Trigger `bd-gold-trigger` (mode=incremental is sufficient; D_00 has order 300 so incremental reruns it after upstreams). Output to verify: `s3://opal-data-bd/platinum/49financial/ownership_map.json`.
- **[0.4.0_DS_ClientPlatform]** On next session, after the gold run lands the first real artifact, HEAD the S3 key, spot-check 5 advisors' account lists against expected, and append a verification section to this log. Also: mark TO `ADVI_PROFIL.004b` status from `pending` to `complete`.
- **[0.7.0_AE_CloudOps]** (informational) Map is ready to consume. S3 key is `s3://opal-data-{firm_id}/platinum/{firm_id}/ownership_map.json`. Shape frozen at schema_version=1. First population lands after the next scheduled gold run. `.004c` edge fetcher can proceed with its design. See broker message to follow.
- **[0.4.0_DT_ClientPlatform]** (informational) Filename chosen to match your `.004c` design (`ownership_map.json`, not `advisor_ownership.json`). No other change on your side required.
- **[0.4.0_DS_ClientPlatform follow-up]** Consider consolidating the `advisor_id()` slug function into `lib.s3_layout` or `lib.helpers` -- currently it lives in `lib.mix_views` and is imported by D_00, D_02, D_03, D_00c, C_06. Moving it closer to the rest of the S3 layout primitives would reduce the conceptual coupling between "mix views" and "advisor slugs". Out of scope for .004b; log as technical debt follow-up.

## Do NOT

- Do NOT change the schema without coordinating `.004c` + frontend. The `schema_version=1` freeze is the contract.
- Do NOT drop the `firm_id` body field. Redundant with the path, but that's the point -- it's a self-describing sanity check.
- Do NOT re-introduce `'platinum/shared/'` as a global path -- the shared-advisor-router firm rewrite makes it unreachable for non-BD firms without router code changes.
- Do NOT hand-edit the published `platinum/{firm_id}/ownership_map.json`. Regenerate by running D_00.
- Do NOT trigger the gold runner from this TO. Let the next scheduled run pick it up. `.004a` is already at `portal-auth-v1.11.9` and `.004c` edge enforcement is not yet live, so there is no cross-dependency that requires a manual trigger.
- Do NOT add new advisor-name sentinels without also verifying them against the live `ACCOUNT_TEAM` parquet. The enumeration above (162 real / 2 sentinels / 164 total) is the authoritative count as of 2026-04-10.
- Do NOT `git add -A` or `git commit -a`. Selective staging only. This incident is the second such attribution corruption recorded; a third would justify a CI-level block.
