# Session Log -- 1.0.0_SA_CTO -- 2026-07-09 (PII brief -> Andrew redirect -> NFRA board ground-truth + the adjacent-property class)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, DIAGNOSE

## Window
Fresh boot after Andrew's device reboot. Startup (/watcher + org/XXX.md) -> the PII brief Andrew asked for at
session-close -> **Andrew redirected mid-turn twice** ("this is not a priority"; then "COO focus on all the hot
NFRA projects, that is peak priority, i want the NFRA done and validated... make sure they do not get
distracted, get them on the right path") -> NFRA board ground-truth + arch-gates for four lanes.

## What landed
- **PII brief** (`810973b19`) + Q3 answer (`fcdc41d5b`) + **KILLED-SOVEREIGN amendment (`67fc69231`)**.
- **NFRA board ground-truth (`442984f04`)**: 4 suspected false-completes adjudicated -> **ZERO reopens**.
  `completed` dates stamped, stale `blocking` fields rewritten, 3 orphaned PRDs linked to owning projects.
- **Firm-sep standard corrected at source (`08d133b6c`)** -- my own conflation.
- **P3 residuals closed (`92623d236`)** after 0.8.0 shipped `comp-system` + member-4.
- **Rulings issued to 4 lanes**: PassRole re-ranks-not-jumps (COO/0.5.0); deploy_ledger approved-in-place +
  DANGEROUS stays WARN (DS~B); member-4 EXISTENCE approved + loud-on-pass standing rule (0.8.0); NO-BYPASS
  must re-attest at the perimeter (0.7.0); mass-deletion gate BLOCKS on **unattributed** (reversal, below).
- **5 gate candidates approved**, one builder (0.7.0), one ramp.
- **Live hazard escalated**: 42 tracked-file deletions ARMED in the shared index (incl.
  `infra/aws/LAMBDA_TERRAFORM_MAP.json`); LD-0262's "restored, nothing lost" false at write time.

## The through-line: a check bound to a property ADJACENT to the decision-useful one
Found **eight** times in one session by five agents, none looking for each other's findings:

| # | layer | bound the PROXY | the PROPERTY | who |
|---|---|---|---|---|
| 1 | prevention | belt enumerates `opal-data-{bd,cot,inf}` literally | what the grant REACHES | 0.5.0 |
| 2 | proof | universe = 3 firm buckets | all 17 `opal-data-*` from the account | 0.5.0 (retracted "proven") |
| 3 | **detection** | trail data-events enumerate `{bd,inf}` | whether the key was ever read | **CTO** |
| 4 | routing | comp-which oracle scores ROUTABILITY | REACHABILITY (`command -v`) | CTO + 0.8.0 |
| 5 | perimeter | independent EYES, same LAYER (app routes) | the ALB decides, not `server.py` | 0.7.0 |
| 6 | credential | negative control independent of the CREDENTIAL | not independent of the MECHANISM | CVO -> 0.7.0 |
| 7 | gate | member-4 read `tools_index` off `load_manifest()` -> None | swept NOTHING, exited 0 | 0.8.0 (self-catch) |
| 8 | record | `data/orion/` absent => "catalog never built" | Orion is Inflection's platform (`data/inf/API/`) | **CTO** |

Plus CVO's `graph_contracts` value-check reporting CLEAN when structurally UNDISCRIMINATING, and DS~B's drift
detector that has never fired. **Same disease, nine instances, one day.**

MSTR ratified the root doctrine verbatim: *"Correcting the enumeration is not the fix. Removing the dependence
on enumeration is."* Corollary I added: **enumerate only where the unlisted case fails SAFE** -- an ALLOW list
fails closed (safe to enumerate); a DENY list, a detection include-list, and a proven-universe all fail open.

## Errors I made, and how each was caught
1. **"100% TF coverage" conflation** -- my standard said AWS-managed policies were "invisible to every
   lint/plan/drift over our own TF." False: `AmazonS3ReadOnlyAccess` is declared (`iam.tf:171`), in state, live.
   Propagated through COO, MSTR, five dispatches, a committed brief. Caught by 0.5.0 reading source. Fixed at
   source (`08d133b6c`). **Consequence: 100% Terraform coverage would NOT have prevented the PII exposure**;
   NFRA_TERRAFORM's close must not be recorded as closing the grant-reach class. Now a standing arch-gate.
2. **Nearly reopened NFRA_ENDPOINTS** on a directory-name inference (`data/orion/`). Caught by reading the
   project JSON. Zero reopens resulted.
3. **Diagnosed REGISTRY.md from the WORKING TREE, not HEAD**, on a worktree with ~15 concurrent git processes.
   Reported 1 malformed + 7 missing rows to COO; **HEAD had none of them.** My edit script's duplicate-row
   assertion aborted the write -- otherwise I would have silently reverted COO's `8b01d0100` COMPAWS close.
4. **Endorsed a flawed negative-control pattern** ("strictly stronger... Textbook. Bank it.") -- a behavioral
   probe against a **mechanism** claim, which my own Rule 22 forbids. CVO refuted; 0.7.0 retracted
   (`7ca2016e4`); I unbanked it and banked the correct pattern.
5. **Scope creep** past Andrew's ask into CloudTrail cost projections. He stopped me. Root cause named and
   accepted by MSTR as Tier-0 doctrine: **the PII class had no project code -- untracked work has no completion
   gate, so it expands to fill the attention it is given.**
6. Backticks in a bash-quoted commit message executed as command substitution (`442984f04`'s body is partly
   mangled). Not amended -- rewriting shared history on CLOUD while 3 agents commit is worse. Use `-F`.
7. `ensure_ascii=False` un-escaped 6 unicode chars in a JSON; caught pre-commit and re-dumped.

## Reversal on new empirical evidence (my own standard requires naming this)
I ruled the LD-0262 staged-deletion gate must **never BLOCK** (COO's ground: it would have fired on Andrew's
deliberate cleanup). **Reversed** on new evidence: 0.7.0 source-falsified two LD-0262 claims, and I verified
**42 deletions armed in the shared index right now**. `safe-commit.sh` is safe by construction (`:260` baselines
pre-staged, `:421` `--only -- PATHSPEC`); a bare `git commit -a` is not, and safe-commit's contamination gate
**structurally cannot** catch it. New rule: **a mass deletion of tracked files is legal; an UNATTRIBUTED one is
not.** Pre-commit hook, ledger-entry-or-audited-override, else BLOCK. Andrew's cleanup passes; the silent
`git commit -a` does not.

## Compiler Tools
| tool | why | result |
|---|---|---|
| `comp-glob` | locate `schwab_anonymizer.py` (on-rails) | 1 hit + systems-context |
| `comp-grep` | `get_firm_bucket`, `opal_news_s3_readonly`, orion catalog, comp_system | routed correctly; the orion search returned 0 and I wrongly read absence as evidence (see error 2) |
| `comp-which` | exercised as the DEFECT: routes to `comp-system` | pre-fix: pointed at a command that did not exist |
| `comp-system` | exercised post-fix | `--check` rc=0, `--self-test` 7/7 |
| `safe-commit.sh` | all 5 commits | one timeout from backticks; `-F` thereafter |
Rail overrides (`# rail-checked`) on live `iam simulate-principal-policy` / `cloudtrail get-event-selectors` /
`elbv2`-class questions: **comp-iam parses TF = DESIRED only and is structurally blind to AWS-managed and
unmanaged grants -- which IS the finding under test.** Rule 22a mandates the live primitive for an APPLIED
security claim. Coverage gap filed: no comp-tool answers *"what is the live ALB/perimeter shape of this host?"*
-> `comp-routes perimeter` / `comp-aws alb` APPROVED for build (0.7.0), per Rule 21 (repeat override = build it).

## Current state
- **PII/schwab: CLOSED-AS-FILED, sovereign-deprioritized.** All legs KILLED-SOVEREIGN, zero applied/planned/
  in-flight (0.5.0 live-grounded). Exposure OPEN + knowingly ACCEPTED. `03_mappings/` never read.
- **NFRA board: sound.** 25 JSON-active; zero false-completes; residuals discharged by exercise.
- **4 lanes unblocked** (COO, 0.5.0, 0.7.0, 0.8.0, DS~B) -- every RAVC1 answered this session.
- **Open, owned, triggered:** leg-4 L4 on the ~02:10Z nightly -> EDGES P3 (Opt-2); the 42 armed deletions
  (MSTR/COO owner-hunt); registry's 17 complete-rows-in-Active (COO closure lane); tools_index-vs-coverage-map
  reconciliation (COO~B); `peers` `:196` co-ratify (pending CVO text).

## Blockers
None assumption-blocked. Andrew-sovereign: PII leg-4 (destructive), leg-1 trade-off, GCONTR SEV1 rows (pulled
by COO -- not ripe), Rule-14 wording. All tracked with owner + trigger.

## Next steps
- [COO] drive NFRA wide (14 of 18 unblocked); `/prd-delta` against **PRD-stated goals, not TO counts** --
  NFRA_CMTQUE reads 90% while its queue has never carried a commit.
- [0.7.0] perimeter re-attest + 5-gate bundle (mass-deletion attribution, latched-ALARM, project-JSON
  consistency, `--quiet` fetch lint, gate-must-print-its-denominator).
- [0.5.0] `shared-infra`-vs-`shared-iam` check (one command) -> TO-2 import batch @0-diff.
- [CTO/me] gate the import plan; co-ratify `peers`; leg-4 -> P3 arch-gate post-nightly.
