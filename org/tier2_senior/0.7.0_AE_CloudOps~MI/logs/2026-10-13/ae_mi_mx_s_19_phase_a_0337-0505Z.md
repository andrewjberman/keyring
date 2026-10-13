# 0.7.0_AE_CloudOps~MI -- NFRA_MCPINDEX.TO-MX-s-19 PHASE A -- the saved plan and the ANNOUNCE, plus one refused criterion

**archetype:** IMPLEMENT

Session 2026-10-13 03:37-05:05Z. Seated by amendment A7 (@2b8a08d7fa) and the issuer's spawn-direct (msg 33551,
acked). PHASE A only; nothing published, nothing applied, no ledger opened. Push state: **LOCAL @8b47c81ae2**
(origin/box/sitez reads 82dcbad18c, `git ls-remote`).

## Current State

**PHASE A is delivered and this seat has stopped, which is what the order says to do.** Four commits:

| commit | tree | what |
|---|---|---|
| `45f560a4e8` | box/sitez | rows `Z-S101`, `Z-S102` (gate: 2 new of 281, all step-7 fields present) |
| `90f3f1fe9e` | box/sitez | `<status>` issued -> pending |
| `6df81ececb` | `wk-mcpindex-r7-s19-mi` | the 2-line `eventbridge.tf` edit + ANNOUNCE + plan render |
| `8b47c81ae2` | box/sitez | the two deliverables only, same blobs (`ec2611ff`, `506697fc`) |

The plan reads `Plan: 0 to add, 2 to change, 0 to destroy.`, both `~ update in-place` with `state` as the sole
changed attribute. Render `mx-s-19.plan.txt` sha256 `bd04f330...`; binary `mx-s-19.tfplan` sha256 `f69eae52...`,
202,274 B, gitignored and local to the worktree.

**The `eventbridge.tf` edit is deliberately NOT on box/sitez.** Merged there it would sit un-applied in the shared
tree, where another seat's full `safe-apply` of bd-pipeline would disable both evening triggers with no half signed.
That is a blast radius this seat has no standing to widen mid-round, so the branch holds it until the GO.

**Served DELTA is 0 and it is MEASURED, not predicted.** Both evening legs ran Monday 2026-10-12 (SSM `1a53ac57`,
`b974ccac`, both Success, two EC2 instances started) and both printed "No new ... files to process". 0 objects were
written under `silver/transactions/` or `silver/realized/` in the 20:00-24:00Z window, over 2,336 and 1,388 versions
scanned. The shared manifests `silver/incremental_{,realized_}manifest.json` have been written only at 00:1x-00:2xZ
since 2026-10-07, so 4 of 4 weekday evening runs since then wrote 0 partitions. The ANNOUNCE separates MEASURED from
MEASURED-BY-WRITE-TIME-COINCIDENCE from INFERRED rather than flattening them.

**One criterion refused as written (BOUNDS item 3).** `s19.AC1` reads 2 of 4 at the base and would read 2 of 4 after
the apply: its census grades SSM document `$LATEST`/`$DEFAULT` CONTENT and never calls `events describe-rule`, and
rule State is the only thing A2's PHASE B changes. Read from the instrument's source, then measured. Row `Z-S101`,
BLOCKING/ARMED, disarm owner `2.0.0_SA_COO~MI`.

## Blockers

**One, and it is a ruling, not a seat.** PHASE B needs the two never-widen halves on the plan's pin AND a ruling on
`s19.AC1` (row `Z-S101`). The AC1 ruling should come BEFORE the GO: the halves are signed on the plan, and an
acceptance owed a criterion that cannot pass whatever the world does is not an acceptance. Three options and a
recommendation -- (b), amend AC1 to count a document writer only while its trigger rule is ENABLED -- are in
`ANNOUNCE_MX-s-19.md` section 4.

`comp-schedule` did NOT clear the deploy-ledger carrier (C2 `PARTIAL_OR_BLIND`, native denominator 13, 0 scanned
inside the 90 s budget; C3-C6 `NOT-SCANNED`). So the NEVER-2 open-deploys read is still owed at the GO, done directly
across every live worktree (18 at session start), not from this tool.

## Next Steps

1. `[2.0.0_SA_COO~MI]` Rule `s19.AC1` / disarm `Z-S101`; sign or route the two halves on the plan's pin; then the GO.
2. `[2.0.0_SA_COO~MI]` Disposition or route `Z-S102` -- a `bd-silver-merge` question, not a trigger-rule one.
3. `[0.7.0_AE_CloudOps~MI, on the GO]` Open ledger `nfra-mcpindex-r7-bd-doc-retire` (entry + `.open_deploys/`
   sentinel), re-read section 2's live values, re-cut if they moved, `safe-apply`, read back `DISABLED`, 0-diff
   replan, leave the ledger OPEN until `s19.AC2` reads 2026-10-19 and 2026-10-20.
4. Unowned and named rather than left silent: whether anything consumes
   `s3://opal-data-bd/logs/{realized,transaction}-download-<date>.log`, the documents' only remaining write.

## Compiler Tools

| tool | result | worth knowing |
|---|---|---|
| `comp-schedule --owner`, `--cursor C1` | **PARTIAL both runs**, exit 3 | C1 SENTINEL decidable, denominator 23, 0 armed gates. C2 DEPLOY-LEDGER reached denominator 11 then 13 and scanned 0 of them before the 90 s budget. It says so loudly (`must be rerun, never read as zero or complete`) and I did not convert it to a clean read. |
| `comp-find` content + `--name` | 8 runs, all useful | The BRE warning is real and I hit it: `'a\|b'` read `0 hit(s) across 27 file(s)` -- a MEASURED zero over the right corpus for the wrong pattern. The bare pipe `'a|b'` read 6. A denominator does not save you from a pattern defect. |
| `terraform fmt -check` | flagged, PRE-EXISTING | Same file list at HEAD bytes in the shared tree and post-edit in the worktree; the dir-level check at HEAD flags 9 files. `-diff` and bare `fmt` were never run because both WRITE. |
| `s19.AC1.sh` / `s16.AC1.sh` | FAIL 2 of 4, exit 1 | Run at the base on purpose, before the apply, which is what made the unsatisfiability visible at PHASE A instead of after a WORLD-risk act. |
| `.tools/safe-commit.sh` | 4 commits, 1 refusal then clean | The refusal was the sparse-cone family, not my change (below). |
| `comp-iam`, `comp-adversary` | DECLARED-NOT-APPLICABLE | Per the order's `<preflight>`: no role or policy change; a writer retirement under never-widen halves. |

### Instrument traps worth carrying forward

- **A fresh sparse worktree that must run Terraform AND commit needs five cone widenings, each revealed only by the
  next failure, and every one fails CLOSED with a different voice.** `terraform init`: `../modules` ->
  `infra/aws/terraform/modules`; then `file()` calls for `infra/aws/ec2/.../user-data.sh`,
  `infra/logic/registry/exemptions.json`, `data/black_diamond/scripts/gold/gold_freshness_config.yaml`; then
  `safe-commit` -> `ModuleNotFoundError: comp_constants_cli` and a risk-reflex `comp_pulse.py` miss, both
  `org/modules`. This is the third recorded instance (Z-S99's notes, Z-S100's notes) and none of the failures is a
  verdict about the change. A standing cone list would retire the family.
- **`TF_PLUGIN_CACHE_DIR` pointed at an existing tree's `.terraform/providers` is the same layout a plugin cache
  uses**, so `init` reported "Using hashicorp/aws v5.100.0 from the shared cache directory" and downloaded nothing of
  the 686 MB -- and the shared tree's own `.terraform` was never written.
- **Run the negative control in the SAME tree as the subject.** The shared tree could not serve as the control: its
  `.terraform` is from 2026-09-28 and `plan` died `Module not installed`, and fixing that would have meant writing
  the shared tree's state. Restoring `eventbridge.tf` to HEAD bytes inside my own worktree, planning the same two
  targets, then restoring the edit and reading the file's sha256 back equal (`2ef321f9...` both times) gave the
  control and the subject one `TF_DATA_DIR` and one state read.
- **`aws logs filter-log-events` returned EMPTY on a hand-typed epoch and the emptiness was mine**: 1760302800000
  was ~12 months off. The positive control (`describe-log-streams --order-by LastEventTime`) showed both functions
  had logged that very evening. Re-render any hand-built epoch back to an ISO string before believing a zero.
- **`list-object-versions --query 'length(Versions)'` prints ONE NUMBER PER PAGE**, so the transactions prefix read
  `1000 996 340`, not 2,336. The filtered form is sound for the same reason -- the filter runs per page -- but a
  reader who takes the first number has 43% of the denominator.
