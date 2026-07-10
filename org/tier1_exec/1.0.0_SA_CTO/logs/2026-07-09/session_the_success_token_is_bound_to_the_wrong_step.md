# Session log -- 1.0.0_SA_CTO -- 2026-07-09 (evening -> wind-down)

**Andrew's directives, in order:** drive NFRA to done-and-validated (COO manages `/prd-delta`, lanes undistracted);
verify NFRA PRDs are registered as projects; **"look into the MDPF aum tracking for Inflection"**; *"49 Financial
should not hold up MDPF, that is nonsensical"*; *"what are you guys doing with ycharts i didnt sanction any of
this"*; *"i do not want to deal with 49 right now ... not something we should pursue unless i explicitly ask"*;
**"make the inflection fix now"**; wind down.

---

## 1. THE ANSWER TO THE QUESTION HE ASKED

MDPF's Inflection AUM did not match ADVI's. **The feeder was never wrong.** `build_mdpf_wsc_inflection_feeder.py`,
unmodified, returns `$200,386,009.19` at `as_of=2026-07-09` -- the number Orion displays and ADVI serves, to the
cent. **MDPF simply had not run since 07-08**, because `mdpf-daily-trigger` ANDs Inflection's freshness with 49
Financial's, and 49F's Schwab RPS feed stalled at `date=20260706`.

The fix is the per-partner gate Andrew ruled for: dispatch on the INF spine alone, skip a stale partner's feeders,
roll its last-good block forward with `as_of_by_partner` on the artifact's face. **Zero 49F code** -- and the skip
makes the entire 49F residual guard *unreachable*, so WS-E can never fabricate again. Built by `0.5.0` (reassigned
when `0.6.0` went deaf), reviewed by `0.6.0`, three must-fixes gating the apply. **Not deployed.**

I got this wrong twice on the way. First I specced dropping WS-C's `on_or_before` clamp -- which is load-bearing:
it holds the custody minuend on the Eclipse model's date. **I specced, for Inflection, the exact residual defect I
had spent four hours ruling against for 49F, and called it "the easy fix."** Then I told `0.5.0` to roll 49F
forward from the last *published* aggregate (`07-08`), whose block has a correct total and a fabricated
composition. `0.6.0` refuted both.

## 2. THE THROUGH-LINE

> **The success token is bound to the step that succeeded, never to the step you cared about.**

Seven instruments, seven authors, one grammar. Each printed a true statement about a step nobody was asking about:

| token | actually observed | believed to mean |
|---|---|---|
| `outcome: "ok"` on an HTTP **403** | the gateway's tier check allowed the call | the vendor answered |
| `objects=0` over **1,034** objects | Windows cannot write `:` in a filename; `--quiet` ate 1,034 errors | the prefix is empty |
| `delivered` | the filesystem accepted the bytes | an agent will read them |
| `PASS` from `comp-freshness` | a filename contains a recent date | the partition has rows |
| `deaf=0` from `fabric-check` | a decoy directory nothing writes to | every lane is reachable |
| `grep -c` over `fatal:` | zero matches **in an error message** | the clause is missing |
| a clean `git status` | `.gitignore:183` ate the new file | the tree is unchanged |

And the two that nearly landed: **`ParameterNotFound`** from `aws ssm get-parameter --name /mdpf/custody_source`
(MSYS mangled the leading slash -- the exact hazard `CLAUDE.md` warns about, in the section I amended an hour
earlier), and **a `[STOP]`-blocked deploy** grounded on a function `:295` never calls.

**Two empty results, opposite conclusions, ten minutes apart.** Mine was caught only by an unfiltered sweep that
**printed its denominator**. `0.6.0`'s falsifier -- `"prefix": "schwab/silver/rps"` -- was in the decision log it
had quoted me 90 minutes earlier.

> **Exercising a function is not exercising the path. Before you act on an absence, ask what would have to be true
> for your instrument to see the thing.**

## 3. LANDED (governance -- the only rules that survive the session that found them)

- `57ba928e5` **vendor egress.** Pre-authorization covers **Opal-owned** APIs only and **excludes every egress off
  Opal-owned infrastructure**. Availability is not authorization; neither is a privacy sign-off nor a co-verified
  arg schema. **An args allowlist is a privacy control on the LOG, not an egress control on the WIRE**
  (`ycharts/client.py:169` forwards a freeform `query` verbatim).
- `0a9bf1c48` **Rule 18 / HALTGT.** The rule taught a safety property that never existed. `[STOP]` does not
  hard-block; the checkpoint reads only *unread* files and `inbox-watch.sh:120` archives a message **before** it
  announces it. *"Fails closed"* was true of the **rare** branch and advertised as the checkpoint's character.
- `80ae2ffa9` **MSYS `git show`.** Measured all four combinations rather than taking the broad rule: it mangles
  **only** when the ref *and* the path both contain `/`. Plus: **put the control on the retrieval, not the
  pattern.**

## 4. THE INCIDENT THAT WAS MINE

Every "curve point" of the overnight watch **I designed** was a live Black Diamond DataMining call on the 49F
account -- `download_export()` -> `run_query()` **mints a run_id on the vendor's platform.** I authorized it as
*"pure observation."* So did COO. Nobody traced the instrument to a source line. It violated `NEVER#4` from the
day it was written.

`0.6.0` caught it because it could not name the source of a byte count in **its own report**: the bytes were for a
workbook absent from S3, drifting 2-4 B per read (zip timestamps), and our own docstring says *"BD's empty export
is a well-formed ~4,592-byte workbook."* pt2 logged 4,590 B. The three fires all preceded both prohibitions; the
fourth would have breached both. **The curve is killed. The S3-only substitute never needed the vendor.**

> **"Observation" is a proxy. A category is not a property.**

## 5. YCHARTS -- closed on facts, bounded honestly

`34` invocations, `dt=2026-06-24..07-09`, `30,137` audit records. The on-box durable JSONL and the S3 lake
reconcile **record-for-record** (`except Exception: pass` has never fired), with a positive control and a negative
control. **19 by 5 agents; 13 by a person (`alyssa@`, standard tier, equity research); 2 a tier cert-probe.**
Egress source-confirmed: six public index queries, twelve public tickers. **No client data ever left.**

The `2026-07-01T22:32:50.937` / `22:32:52.006` pair -- `read_only` **DENIED**, then `master_admin` **ok**, 1.07s
apart -- is **the only control all evening validated on both rails**, and it is why the audit can say `denied` at
all. It also proves the gateway **can refuse**: *do not audit the prohibition, enforce it.*

## 6. WHAT THE FABRIC DID THAT I DID NOT

Nine refusals, every one correct:
- `0.8.0` refused to `--force` past owned-paths with a CTO GO in hand: *"your GO authorizes the work, never the lane."*
- `0.7.0` refused a CTO GO (bucket versioning) on **Andrew-lock** grounds -- and showed it would have made the
  nightly GC print `deleted=N` while reclaiming nothing. It also refused a cost argument it could have won, having
  measured (1.01 GB) and found the bill was pennies.
- `0.7.0` refused to close leg-4's L4 on a 02:11Z read: *"it passes on a transient and is false an hour later."*
- `0.4.0` refused to inherit my P0 severity trigger; refused to run a census whose denominator it could not assert.
- `0.4.0~B` refused to code against an unratified verb (`ABSTAIN` had two readings, differing by 17 consumers);
  refused to arbitrate a CTO/COO divergence and surfaced it instead; **exercised** the halt-gate with a control
  proving `rc=2` was reachable.
- `0.5.0` checked `0.6.0`'s liveness before touching a shared file and refused to resolve a two-authority fork.
- `0.6.0` refused to run my instrument, and refused to report numbers whose source it could not name.
- `3.0.0` refused to write the PRD it briefed: *"a verifier who drafts the architecture he will later certify has
  destroyed the only thing he was for."*

**And every retraction tonight was initiated by the person who had been wrong, before anyone acted on it** (COO).

## 7. OPEN -- ANDREW'S

1. **The frozen `$1,837,159,865.68`** on the client portal. *"Stop investigating"* and *"stop watching a
   client-facing number"* are different instructions and he gave one of them. **Both 49F ledgers
   `gate=sovereign/SUSPENDED`: neither closed nor advanced, verifies do not run.** On release: close as
   *"out of scope, sovereign -- VERIFY NOT RUN"*, an explicit gap, **never a pass.**
2. **`alyssa@opalinvest.com`'s YCharts access** -- untouched. The prohibition binds agents.
3. The seven unsubscribed SNS topics; 542 messages preserved.

## 8. OPEN -- MINE (nothing deployed, nothing stranded)

- **MDPF gate**: three must-fixes gate the apply -- (a) `GATE_ENFORCE` must gate the skip (`=0` currently means
  *"halt off, skip on"*: a rollback that does not roll back); (b) unknown `as_of` -> **DEFER, never skip**;
  (c) harden `_latest_bd_silver_partition` with the schwab path's content assertion -- **the bd branch is dormant,
  and one SSM write to `/mdpf/custody_source` re-arms a filename picker that reads a 0-row stub as fresh.**
- **`stamp_marker` merge**: HELD until `IfMatch` is proven in the **deployed** runtimes. Probe built (`8c0b67afd`),
  unrun. **Three verdicts, not two:** `412` = honoured; `ParamValidationError` = absent; **`200` on a wrong etag =
  accepted-and-discarded, a CAS that always succeeds and guards nothing.**
- **`operator.py:539`** writes every `~lane` GO to an unwatched decoy dir **and `mkdir`s it on demand**. Five
  resolvers of the canonical inbox path; **three wrong.** Conformance assertion committed by COO.
- **`halt-gate-check.sh` reads the decoy**: a `~lane` agent is **unhaltable by `[STOP]`, unconditionally.** Proven
  by exercise, not source.
- **`.tools/` is gitignored** (`.gitignore:183`). `check-inbox` and `inbox-watch` -- which `CLAUDE.md` tells every
  agent to run -- **are not in version control.** 192 tracked / 27 ignored-untracked / 19 of those scripts.
  **Do not narrow the rule without printing the inventory first** (`safe-commit.sh:287` force-adds).
- **`NFRA_TELEMETRY` PRD**: mine to author. **I reordered CVO's priorities on its own evidence:** a `seq` minted
  inside the lossy component drops with it, and the mechanism is UNDETERMINED -- **cross-oracle reconciliation is
  the P0; `seq` is P1; the hook source-read precedes both.** Detection of the vendor incident does **not** block on
  it (the gateway audit is a second oracle); **attribution does.**
- **Routed, not chased:** `read_file` returns `content:""` on an IRM-encrypted file (MSTR §4.1) -- **an unreadable
  file reported as empty**, in a tool we ship. The `2026-07-09` transaction partition carries `return_date =
  2026-07-07` for **100% of 204,043 rows**, on both firms: *the content carries its own as-of, in a column, and not
  one of our instruments reads it.*
- **`flat_orphans=4`** -- four MSTR charters stranded 41 days, one a `PROCEED ... GO`. **Preserved as evidence: not
  deleted, not delivered.** *A durable instruction that outlives its premise does not become safe by finally
  arriving.*

## 9. THE LAST ACT

COO's wind-down handoff adopted `0.6.0`'s refuted `[STOP]` finding into the closing state -- the one artifact a
fresh agent reads before anything else, at the hour nobody is left to check it. Corrected before stand-down.

> **A wind-down state is a durable instruction.**

**Safety at close:** `deploy_ledger check --red` -> `0 stranded, 5 HELD-SOVEREIGN-GATED, apply-proven`. HEAD ==
`origin/CLOUD`. **No deploy begun, so none stranded.** Zero writes to `bd` / `schwab` / `opal-data-schwab`. No
vendor call after 22:19:15Z.
