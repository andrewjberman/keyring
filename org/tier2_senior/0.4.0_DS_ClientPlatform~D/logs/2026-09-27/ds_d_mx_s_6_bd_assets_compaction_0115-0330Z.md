# MX-s-6 step 1 -- the bd_assets compaction fixed as a streaming MERGE, deployed and verified; step 2 released

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE, DEPLOY

**Serial:** `0.4.0_DS_ClientPlatform~D` · **Window:** 2026-09-27 01:15Z -> 03:30Z · **Issuer:** `2.0.0_SA_COO~O`
**Order:** `NFRA_MCPINDEX.TO-MX-s-6.bd-assets-compaction.md` `@3e972dac5d` · **Risk class:** WORLD
**Full record (every figure measured at run time):**
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/bd-assets-compaction.result.md`

---

## Current State

Fresh session after the predecessor died ~10h earlier. Registered lane `~D` (it was NOT registered), armed the
inbox Monitor, and worked the one open order. **MX-s-6 step 1 is COMPLETE, deployed and verified; step 2 is
gated and the issuer has RELEASED this seat.** MX-s-2 is SUPERSEDED `@8668dd09a5` and was not executed.

**What step 1 actually is.** `data/black_diamond/scripts/silver/convert_assets_to_silver.py` gated
`write_compacted` on `--backfill` while the SSM document `opal-bd-asset-dim-download` passes `--latest`, so no
scheduled run had ever written `silver/bd_assets.parquet` (frozen 2026-04-14). Row `Z-S15` by
`0.7.0_AE_CloudOps~I` measured this; I re-confirmed it from this lane rather than inheriting it -- the document's
only converter line is `python3 convert_assets_to_silver.py --latest`, and the bytes I patched are sha256
`0b99836672`, the same sha Z-S15 recorded for the repo AND the deployed S3 copy.

**The order's literal fix was refused, and the refusal is the substance of the session.** "Fix the condition"
taken literally is `if not args.no_compacted: write_compacted(df)`. `write_compacted` REPLACES the key, and
under `--latest` the frame is ONE forwardfill export -- so that one-liner would have replaced **3,449,107
consolidated rows** with a single day's export, on the exact input `build_bd_assets_dim.py` reads, **and it
would have turned the order's own AC1 GREEN while doing it, because AC1 only reads LastModified.**

Cut instead, split on mode: `--backfill` REPLACES (unchanged, its frame IS the consolidated set);
`--latest`/`--file` MERGE -- stream the existing file row group by row group, drop the `transaction_id`s this
run re-issues, append this run's rows. Same "later export wins" rule `dedup()` applies in-frame. It streams
because peak memory is then one row group (largest 63.2 MB uncompressed) not the 172.3 MB whole: the runner is
a t3.medium with 4 GiB. `_align_to_schema` casts each run onto the compacted file's own arrow schema so the
schema the bridge reads cannot drift; a column the schema lacks is dropped LOUDLY, one the export lacks is
filled null.

**Deployed artifact (read back, not taken from rc=0):** `s3://opal-data-bd/code/silver/convert_assets_to_silver.py`
sha256 `d78c31853ab6374b0950346b1e0163ad635754f1b212faa8df86d71001e91bfd` == `git show HEAD:<path>`, and
!= base `0b99836672` (negative control). LastModified `2026-09-27T02:08:44+00:00`, 14,443 bytes.

**Commits (4), all under this lane's author line:** `a2d25dd90b` fix+test in linked worktree
`ds-d-mcpindex-s6` (rule 14b; worktree and branch removed after the drain) -> `74db08f005` merge to CLOUD via
`safe-merge.sh` -> `97351a613e` row Z-S18 -> `4c0ecdfcf1` the result record.
**PUSH STATE, measured by `git ls-remote origin CLOUD`:** `a2d25dd90b` and `74db08f005` are ON ORIGIN
(origin/CLOUD read `74db08f005` -- the integrator's push, not this lane's; standing no-push honored).
`97351a613e` and `4c0ecdfcf1` were LOCAL at the time of that read.

**Criteria: AC1 and AC2 both FAIL, by design.** Both read a LastModified-after-issue predicate on the two
artifacts, which is step 2's outcome. `silver/bd_assets.parquet` = 2026-04-14T20:09:23Z,
`silver/bd_assets_dim.parquet` = 2026-04-14T20:44:16Z. **The proof-of-spec instance is deliberately NOT
written** -- the issuer confirmed in its release ruling to leave it unwritten.

**I did not fire an ad-hoc `--latest` run to turn AC1 green.** It would have worked. The newest forwardfill
export is 2026-06-18 (48 exports, none after 2026-06-19), so it would have satisfied a timestamp predicate on
JUNE data while the order's words say "one real ... run has converted **current dates**". Recorded so it is
visibly rejected rather than silently unconsidered.

## Blockers

**ONE, evidence-cited, and it is NOT this lane's and NOT an order in flight.** Step 2 (confirm the rewrite,
rebuild the bridge, report the asset_id count against the 791 formerly-missing ids) is gated by the order on
MX-s-4's Black Diamond login fix. At `9736741fe6` `0.7.0_AE_CloudOps~I` filed MX-s-4's instance: **AC1 fails
on a VENDOR blocker**, routed to Andrew under MX-s-4 step 1's own carve-out. The login times out navigating to
`bd3.bdreporting.com`; all three BD downloaders fail on the identical error with the same boundary (last clean
2026-06-22, first failing 2026-06-23).

Independently consistent from the data side: **1,890 silver partitions, newest `2026-06-18`** (written
2026-06-19), and no forwardfill export after 2026-06-19.

**So step 2's precondition is a sovereign call at Andrew, not an AE task in progress** -- a different condition
than the order assumed. Reported to the issuer, which ruled RELEASE at 03:19Z: "an idle seat buys nothing",
MX-s-6 stays open with step 1 recorded, step 2 re-issues to a live DS seat at the fix, and **the cut
(`--backfill` replaces, `--latest` merges) is accepted as the step-1 design.**

## Rows filed

**`NFRA_MCPINDEX-Z-S18`** (`97351a613e`) -- OBSERVATION / INERT, disarm owner `2.0.0_SA_COO~O`. Ruled and
adjudicated by the issuer at `590c4f1786` (DISMISSED_WITH_REASON, `adjudicates: [Z-S18]`), sweep routed to
`1.0.0_SA_CTO~O`.

`64b6b9d65a` -- a commit whose subject is `log(COMP_LEARNS.session13)` and whose stat is 275 files / 4,018
insertions / **16,609 deletions**, including whole test files -- stripped `from __future__ import annotations`
from 98 files, reverting the ADHC_DSFLOW.004 sweep (`a5ac27a275`). **60 are still missing it at
`74db08f005`**; of the 60, three carry PEP-604 unions in annotations. Filed INERT rather than ARMED because
the runners' Python version was NOT measured and on 3.10+ the import is unnecessary.

**A denominator reconciliation worth keeping:** my row says 60, the issuer's ruling says 59. Both are right --
60 files total, of which **59 are `.py` and 1 is `infra/aws/lambda/ci/record-terraform-deploy.sh`**. Measured,
not assumed, and it changes no action. The same `.sh` file is why my first AST classifier pass said "four"
PEP-604 exposures instead of three: `ast.parse` raised on a shell script and I had put the UNPARSEABLE marker
in the same list as real hits. Recorded in the row as an instrument artifact.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `.tools/commit-gate.sh` | both files, twice | PASS (2 of 2) | FIRST RUN BLOCKED on the missing `__future__` import -- that refusal became row Z-S18 |
| `.tools/safe-commit.sh` | 4 commits | PASS | `-F` msgfile written by the Write tool per rule 14a; `msg-verify MATCH` each time |
| `.tools/safe-merge.sh` | `ds-d-mcpindex-s6` | PASS | `74db08f005`, row gate clean on the MERGED index |
| `.tools/safe-deploy.sh` | the converter | PASS | `DEPLOYED [bd]` + `VERIFY OK comp-pipescript deployed` |
| `.tools/halt-gate-check.sh` | via safe-deploy | BLOCKED x2, then PASS | fail-closed and right both times -- see Gap |
| `.tools/surprise-row-gate.py` | INVESTIGATION_v1.md | PASS | 1 new row of 59 graded AT COMMIT |
| `comp-pipescript io` | `convert_assets_to_silver --pipeline bd-silver` | PASS | now shows the key as BOTH a read and a write (my merge's read-modify-write) and confirms `-> build_bd_assets_dim` |
| `python .tools/audit-archive-invoker.py` | startup A.2 | WARN | findings are an OWNED class (ESTATE_GOVERNANCE channel) -- measured before deciding, NOT re-filed |
| `python -m pytest` | the new suite | PASS 7/7 | plus both negative controls, below |
| `.tools/aws` (`ssm get-document`, `s3api head-object`, `list-objects-v2`, `s3 cp`) | schedule + vintages + 1,890-partition census | PASS | `--query length()` printed TWO PAGES (1000, 890); re-counted client-side for the true 1,890 |
| `pyarrow.parquet` over a ranged-GET file object | compacted schema + row-group sizes | PASS | 65,536 bytes fetched instead of a 69 MB download |

**What worked.** Running BOTH negative controls instead of asserting the test was meaningful. At base bytes
`0b99836672` the suite reads 5 of 7 FAIL (the 2 passing are regression guards, correct at base). With the naive
one-line widening PLANTED, `test_latest_writes_the_compacted_file` goes GREEN and
`test_latest_retains_rows_it_did_not_re_issue` FAILS -- "rows absent from this export were dropped". The mutant
that satisfies the order's literal ask is caught by the test that matters. That is the whole value of the
session and it cost two file swaps.

Also worked: a **scale exercise** against the REAL 3,449,107-row file and the newest REAL export, with a stub
serving both from disk and capturing `put_object` locally -- **nothing written to S3**. Result: 3,474,490 rows
out (3,449,107 kept + 25,383 appended), schema preserved, **0 duplicate transaction_ids**, 7.0 s, arrow pool
826 MB, **peak RSS 919 MB against 4 GiB**. The unit test speaks to logic; only this speaks to a t3.medium.

**What failed.** The site-Z heredoc trap, exactly as banked: `\\n` inside a Bash heredoc was unescaped to a
real newline, so my first patch wrote a broken f-string and `py_compile` caught it. Reverted from HEAD, verified
the restored sha, and re-applied through a Write-tool patch script. The banked lesson existed; I used the
heredoc anyway.

**Gap found.** Running gates from a SPARSE linked worktree narrows what they can SEE, and two fired on it.
(1) `halt-gate-check.sh` BLOCKED for an unresolved principal -- fixed by writing
`org/mcp/sessions/<session-id>.serial` -- then BLOCKED again because it scans `$REPO_ROOT/org/tier*_*/*/` for
the seat's home folder, which the cone excluded; fix is adding `org/tier2_senior/<base>` to the cone. (2) The
naming gate could not read `infra/logic/registry/systems.json` from the worktree and graded NOTHING, saying so
in its WARN window. **Neither failed silently, which is why neither is a row** -- the halt gate refusing rather
than guessing is correct behavior and its message named the remedy. But under LGIC_ENFORCE a sparse cone
silently narrowing the naming gate would matter, and the next seat should not re-derive this.

Also a gap in a separate sense: two properties I INTRODUCED and named rather than left to be discovered.
(a) The real-data run shows `superseded by this run=0`, so the supersession arm was exercised by the unit test,
not by that run. (b) Row groups accumulate one per incremental run (4 -> 5 here); ~365/year, bounded and benign,
with the existing periodic `--backfill` rewrite as its remedy.

## Files Modified

See commit messages: `a2d25dd90b`, `97351a613e`, `4c0ecdfcf1`. Additional context:

| file | change |
|---|---|
| `data/black_diamond/scripts/silver/convert_assets_to_silver.py` | compaction condition split by mode; `merge_compacted()` + `_align_to_schema()` added; docstring states the compaction contract; `from __future__ import annotations` added (gate) |
| `data/black_diamond/tests/test_convert_assets_compaction.py` | NEW, 7 tests, no network (boto3.client stubbed pre-import) |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/bd-assets-compaction.result.md` | NEW, the step-1 record |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | +1 row, Z-S18 |

## Next Steps

1. **[Andrew]** The Black Diamond vendor login. Everything below MX-s-4 and MX-s-6 step 2 waits on it, and no
   agent act substitutes for it. Routed by `0.7.0_AE_CloudOps~I` under MX-s-4 step 1's carve-out; this lane
   only confirms it independently from the data side (no export after 2026-06-19).
2. **[`2.0.0_SA_COO~O`]** Re-issue MX-s-6 step 2 to a live DS seat once the login is fixed and one run has
   converted current dates, citing `bd-assets-compaction.result.md`. The proof instance is owed then, not now.
   Step 2's own content: confirm the rewrite, rebuild with `build_bd_assets_dim.py`, print the asset_id count
   and how many of the 791 formerly-missing ids it carries.
3. **[`1.0.0_SA_CTO~O`]** The Z-S18 sweep -- re-add `from __future__ import annotations` to the 59 `.py` files
   still missing it, and separately consider whether `64b6b9d65a`'s 16,609 deletions reverted anything else.
   **This row measured ONE line and deliberately makes no claim about the rest.**
4. **[whoever holds the served fix]** The `holdings_lots` correction stays MX-s-2's, under its own sign-off, and
   only after the bridge is current. Untouched here.
