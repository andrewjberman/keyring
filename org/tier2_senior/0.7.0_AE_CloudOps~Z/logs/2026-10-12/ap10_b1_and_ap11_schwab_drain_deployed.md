# OG-ap-10 Phase B1 + OG-ap-11 schwab DLQ drain DEPLOYED -- two orders, both mid-flight on a clock

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Delta to `../2026-10-11/ap8_ap9_grant_and_grant_writer_complete.md`. Round 35. Written at 02:4xZ
because the next two acts are 8-10 hours out on scheduled gates and this log is the handoff if the
session does not survive to them.

## Where the two orders stand

| order | state | gate on the next act |
|---|---|---|
| `OG-ap-10` (.pptx pair release) | B1 done, AC1 PASS, both halves signed at `d9f2ebded9` | **B2 GO is effective at or after 11:00Z** |
| `OG-ap-11` (schwab per-family DLQ drain) | DEPLOYED, AC1 PASS, ledger CLOSED | **AC2 needs the SCHEDULED 12:15Z sweep**; plant before ~12:10Z |

## OG-ap-11 -- what is live now

`opal-assets-silver-schwab` runs `CodeSha256 YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=`, Active /
Successful, `OPAL_BUILD_COMMIT a11240c01c`. Prior (the rollback target):
`uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE=` at pin `b3e481b261`. Targeted re-plan reads
`No changes`.

Ledger `nfra-oplgtw-fd1-schwab-drain` CLOSED 20261012T020325Z, 3 legs proven, sentinel removed;
entry and sentinel were committed `@18d407b1cb` BEFORE any deploy act.

The applied plan was exactly the permitted shape -- one resource
(`module.silver_converter["schwab"].aws_lambda_function.this`, in-place), the code fields
(`s3_object_version`, `source_code_hash`, `last_modified` known-after-apply) plus the single
`OPAL_BUILD_COMMIT b3e481b261 -> a11240c01c`, with 28 attributes, 3 env elements and 3 blocks
unchanged. Applied 01:51Z, outside `[09:15,11:35)` `[12:00,12:50)` `[21:15,23:35)`Z.

**PARTIAL ROLL-OUT and it is recorded in three places** (ledger title, the `silver.tf` pin comment,
the source-map note) because the DLQ is SHARED: only the schwab sweep is per-family. The etf,
blackdiamond, orion and eclipse sweeps still drain the WHOLE queue until their own signed pairs land
(CTO half `@aafc1640e8`). Row `Z-S91` stays open until every sweeping family is per-family.

## Two premises I measured instead of inheriting

1. **"Schwab's 11 vendored files"** are NOT all in `data/assets/scripts/silver/`. Nine are; the other
   two (`backfill_status.py`, `stream_parquet.py`) come from `data/assets/scripts/lib/`, per the
   package's own `BUILD_MANIFEST.json`. The package dir holds 13 files -- those 11 plus its own
   `BUILD_MANIFEST.json` and `lambda_function.py`. Comparing only `silver/` would have "verified" the
   premise on 9 of 11 and read as complete.
2. **"The rebuild ships the drain change ALONE."** Before the re-vendor, 10 of 11 were already
   byte-identical to source. The re-vendor changed exactly ONE file's content, `schwab_runtime.py`,
   whose delta is +74/-14 in three hunks: a comment, `dlq_message_family()` plus the new
   `drain_dlq(..., family="schwab")` signature replacing `drain_dlq(sqs, queue_url, cap)`, and the
   call site. No unrelated drift.

Pin verified the way OG-ap-5 verified its own: `git log a11240c01c..HEAD` returns 0 commits over
`data/assets/scripts/silver/`, over `data/assets/scripts/lib/` AND over the package dir, and all 11
vendored modules are byte-equal between the package dir and that commit's blobs (11 of 11,
`git hash-object` against `git rev-parse`).

## Condition C -- the one thing a reader should not take at face value

Condition C wants a live DLQ record confirmed to carry `requestContext.functionArn`. **I could not
measure it**: the queue was EMPTY at 01:05Z (two APIs on the same working credential path --
`get-queue-attributes` 0/0/0, and a 20s long-poll receive at visibility 0 returning rc=0 with no
`Messages` key; depth 0/0 after, nothing consumed).

I declined to plant a synthetic as the shape evidence, because a body I author has whatever shape I
give it. The issuer agreed and ruled (amendment A1, msg 33435) that condition C is met by OG-dq-1's
real non-destructive read on file.

**Reading that cited artifact myself, it does not say quite what the ruling says it says.**
`deliverables/0.9.0_WK_NFRA_OPLGTW~57/DQ1_READ.json` is accurate about the read -- 12 distinct
MessageIds, 156 receive calls at visibility 0, 2026-10-11T15:55Z-15:58Z, nothing deleted -- but its
`bodies` field is a PROSE SENTENCE, it never contains the string `requestContext` (0 occurrences in
27796 bytes), and it says verbatim **"Only the key is recorded."** So it names the FIELD and not the
PATH, and retained no body.

`ap11_record_shape.json` therefore carries `claim: "held"`, not `measured`, and states both what the
source shows and what it does not. The reasons it was still sound to deploy:

- the three fields the source does name (`functionArn`, `condition RetriesExhausted`,
  `responsePayload errorType`) are all siblings of ONE documented shape, the Lambda async-invoke
  on-failure destination record, where `condition` and `functionArn` both sit under `requestContext`;
- TWO independent implementations parse that exact path (`schwab_runtime.py:261`,
  `mirror_conversion.py:934`), written as parallel code;
- **both fail CLOSED**: any `ValueError/KeyError/IndexError/TypeError` returns `None`, and `None` is
  never a family, so the caller LEAVES THE MESSAGE ALONE. A wrong path drains nothing; it cannot
  delete a foreign family's message and cannot lose data. That is what bounds the risk;
- AC2 on the real sweep is the actual oracle.

## Pre-grade exercise (`ap11_parser_exercise.json`, `@7dc59897b9`)

Ran the DEPLOYED parser locally against the two synthetic bodies before the planting window, because
a malformed body parses to `None`, leaves BOTH records alone, and would fail AC2 for my payload's
fault rather than the deploy's:

```
eclipse body -> 'eclipse' -> schwab sweep LEAVES ALONE   (AC2: foreign_survived)
schwab  body -> 'schwab'  -> DELETE + REPORT             (AC2: schwab_drained_and_reported)
5 malformed shapes -> None (leave alone)
```

This exercises `requestContext.functionArn` end to end through the live bytes. It does NOT establish
that AWS's real records carry that shape -- same circularity I refused above, and the artifact says
so in its own `what_this_does_NOT_establish` field.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `safe-apply.sh` | PASS | saved plan, 1 changed; `SAFE_APPLY_TERRAFORM` set explicitly |
| `build-and-upload.sh` | PASS | BUILD_ONLY first, then upload write-VERIFIED by head-object |
| `deploy_ledger.py` | PASS | open/3x close-leg/close, sentinel removed |
| `terraform plan` (targeted) | PASS | 1 change pre-apply, `No changes` after |
| `ap11.AC1.sh` | PASS | exit=0 |
| `ap10.AC1.sh` | PASS | exit=0 |
| `safe-commit.sh` | PASS | 5 commits, all gates clean |
| `naming-gate.py` | PASS | 0 graded on the ap-11 diff |
| `surprise-row-gate.py` | PASS | row Z-S96 |
| `comp-find` | PASS | `dlq_message_family`: 5 hits / 10086 files, 2 DEF |

**What worked:** the ledger-first discipline and reading each grader's bytes before building against
it. **What failed:** `terraform.exe` is absent on site Z, so `safe-apply`'s default binary had to be
overridden; and I read `rc=$?` through a pipe again on a `git apply --check` and had to re-measure
(4th time this session). **Gap found:** none in the tooling.

## Blockers

None owned. Both pending acts are gated on wall-clock, not on a decision:

- `OG-ap-10` B2 cannot start before **11:00Z** (issuer's GO is time-effective).
- `OG-ap-11` AC2 needs the **scheduled** 12:15Z sweep. An ad-hoc sweep invoke is forbidden by the
  order's bounds.

## Current State (handoff -- zero prior context assumed)

Five commits on `origin/box/sitez`: `191e8813b5` (ap-10 B1), `18d407b1cb` (ledger open),
`2bf592c841` (pin + re-vendor), `04c8836f50` (ledger close, source map, build record).
`7dc59897b9` (parser exercise) is LOCAL -- `box/sitez` is integrator-only (LD-0367/0368), so it
moves at the integration window under `0.0.0_AB_MSTR~Z`. Push is never this seat's act.

`OG-ap-10`'s release lives in worktree `C:/tmp/og-rel-pptx`, branch `rel-nfra-oplgtw-pptx`, commit
`d9f2ebded9` on base `28ba9532b6`. Its sparse cone had to be widened four times
(`infra/logic`, `org/standards`, `data/transcripts/scripts`, plus the initial set); it now carries
enough for the gates to actually run. **The naming gate silently did NOT run on that release commit**
-- its registry and `NAMING_SCHEMA.json` were outside the cone, so it printed `NAMING ERROR` without
blocking, i.e. rule 30 was VACUOUS there rather than passing. Re-run from the main tree with the full
canon it reads RC=0, WARN 3, all three pre-existing carriers in bytes taken from HEAD verbatim.

**What the next act needs, concretely:**

1. **11:00Z -- `OG-ap-10` B2.** Ledger `nfra-oplgtw-gateway-release-pptx`, entry AND sentinel first.
   Deploy from `C:/tmp/og-rel-pptx` via `infra/aws/ec2/safe-ec2-deploy.sh` with
   `DEPLOY_BASE_REF=28ba9532b648061cecafe426836d3e96af4529cd`. The release cone MUST include this
   seat's agent home `org/tier2_senior/0.7.0_AE_CloudOps~Z/` -- OG-ap-7's first deploy was blocked
   fail-closed without it, because the wrapper runs the WORKTREE's halt gate. No `HALT_OVERRIDE`.
   Then the triggers in `W/NEVER_WIDEN_ASK_OG-ap-10.md` section 7, then `W/AP10_SERVED.json`.
2. **before ~12:10Z -- plant `OG-ap-11`'s two synthetics** into `opal-assets-silver-dlq`
   (`https://sqs.us-east-1.amazonaws.com/313476888478/opal-assets-silver-dlq`): one naming
   `opal-assets-silver-eclipse`, one naming `opal-assets-silver-schwab`, each marked
   `"synthetic": "OG-ap-11"` and naming no real bronze key. **The staged payload files are on this
   device's Desktop, outside the repo, so another device cannot see them -- regenerate from the
   recorded shape in `W/ap11_parser_exercise.json` (`synthetic_body_shape`) rather than hunting for
   files.** Check the queue depth at planting time: OG-dq-1 records a 13:07Z daily refill of 12 and
   an UNNAMED consumer deleting the whole queue around 16:00Z, and 13:07Z is AFTER the 12:15Z sweep,
   so the queue should hold only these two.
3. **after the 12:15Z sweep** -- write `W/AP11_GRADE.json`, run `ap11.AC2.sh`, then ONE report to
   `2.0.0_SA_COO~O` covering AC1 and AC2 (the order says report once).

The order also says the foreign synthetic is "then removed by the 16:00Z eclipse sweep (old code) as
designed, or by you by its own receipt handle. Record which." Note that OG-dq-1 could NOT name the
16:00Z deleter -- it reads `actor.verdict: unnamed` and explicitly rules out the 12:15Z sweep and
OG-bh-1 -- so do not assume it is the eclipse sweep; record what actually happens.

## Next Steps

- [`0.7.0_AE_CloudOps~Z`] The three numbered acts above, on their clocks.
- [`0.0.0_AB_MSTR~Z`] `7dc59897b9` is LOCAL and moves at the next integration window.
- [`2.0.0_SA_COO~O`] Holds row `Z-S96` (OBSERVATION, step 2's release-tree `test_og_mu1.py` is
  unsatisfiable by construction) and the `OG-ap-10` ask. Also owed elsewhere, named so it is not
  lost: the NFRA_CTLPLN pointer row, `Z-S82`'s dashboard orphans (now with a denominator -- 7 named
  host extras, `dashboard/` absent from the repo at the live ref and at HEAD), and OG-rl-16 Phase C.
