# SESSION 2026-08-25 20:14Z–23:20Z — the TO wave, and six shapes of one defect

**archetype:** COORDINATE

**Seat:** `2.0.0_SA_COO` · **Registered** 20:14Z (predecessor died ~19:53Z) · **Zero crons armed.**

---

## What this session was

Andrew spawned a fleet and put the dispatch with me: *"All agents are spawned, let COO know its go
time, this is on them."* Nine seats dispatched, six spec amendments, one migration cleared end to
end, and a defect family that six different seats found six different faces of.

**The wave ran without a single seat halting.** That is the ~20:24Z ruling working, not luck.

## Andrew-direct received (2), recorded + broadcast same turn

**~20:24Z, verbatim** — the surprise-channel stop-bar:
> *"agents are expected to adhere to surprise-channel logic, they proceed with the task unless the
> task is untenable. if you do atom_decomp properly as you are supposed to that shouldnt be an issue."*

Recorded `@69910b81be`, broadcast to CTO/MSTR/CVO, carried verbatim into all nine dispatches. The
second clause is the load-bearing one: **it puts the cost of a bad decomp on the ISSUER**, which is
why the join-hole record sits at my seat rather than reading as seats being difficult.

**~22:48:48Z, verbatim** — *"Youhave vendor egress"*, received at `0.6.0_AE_PartnerETL`, recorded by
them `@a1e9fbcca7`. ⛔ **It landed 54 seconds before I told Andrew the ask was still open.** Their
same-turn broadcast closed that window in under four minutes — the exact reason the rule exists.

## Dispatched

| Seat | Work | State at 23:20Z |
|---|---|---|
| `DE~D` | ADVI_PERFRP.TO-R1-DE | build scope COMPLETE, 10 commits local |
| `DS~G` | 3 successive commissions | all three changed a dispatch decision |
| `AE~G` | ADVI_PERFRP.TO-R1-AE | at ceiling, AC4 built + exercised |
| `DS~Q` | ADVI_STITCH.TO-A1-DS | raw plane LANDED 931/931; silver running |
| `AE~J` | ADVI_STITCH.TO-A1-AE | landing role minted, grant held tight 3× |
| `DS~J` | ADVI_INSURE.TO-R1-DS | ceiling + design v1 |
| `DS~N` | D1_CATVIEWS read | NO-SHIP verdict, 4 findings |
| `AE~B` | D1-i-2 | prepared, apply held |
| `0.6.0` | ADVI_INSURE surface (a) | field→call map delivered, live released |
| `0.8.0` | NFRA_COMPTOOLS | PREFIX-READS complete, ARCH-GATE PASS |

**Wave 2 dissolved** — both D1 round-1 TOs were already executed and certified. **Wave 1 was 5 real
seats, not 6** — `~G` returned theirs as already-discharged, verified at the artifact.

## The two outcomes that mattered

**D1_CATVIEWS is NO-SHIP.** `DS~N` exercised it: it bricks the Lambda at import, and once un-bricked
aborts the entire gold chain on a **$0.01 comparison on $2.03B** — all four scopes, all artifact
types, including the global surface restored four hours earlier. **The naive fix lands worse than
today**: add the missing module, deploy reports clean, plan 0-diff, and the daily chain silently stops.

**The STITCH raw plane landed 931/931**, zero drift, zero failures, MECE closing, both directions
against a pinned manifest. `DS~Q` then attacked their own primary oracle unprompted — the sha256 is
computed by their own copier, so a self-consistent in-memory corruption would pass every layer — and
ran an independent MD5 oracle covering 679 of 931, **stating the 72.9% limit rather than averaging it
into a headline.**

## ⛔ The finding: six shapes, one mechanism — `@8ca4e07f00`, amended `@214bba9960`, `@2e0cd43c60`

> **Our verification instruments join on the record. When a fact lives where the join cannot reach
> it, every instrument agrees with every other, and all of them are about the record rather than the
> world.**

1. a decomp cell **carried by no TO** → 100% alignment, 9/9 PASS twice certified, artifact cannot run
2. a criterion bundling **two grounding layers** → scored at the weakest, a satisfied cell rides a gated verdict
3. a criterion **frozen before its downstream method existed** → AC PASS, grant does not do what the job needs
4. **dependency edges in `<status>` prose** → 0 of 13 TOs carry any machine-readable dependency element
5. **`<status>` stale on completion** → reads ACTIVE, discharged hours earlier
6. a verdict from an artifact's **ABSENCE** → SEAT, and the thing had been producing for six days

**All six are mine.** I cut every task order named.

**Two of my five remedies were falsified** by CVO, who *built* remedy 1 rather than reading it: it
returned `0` against a known `31` and over-captured 2.6× elsewhere — **the remedy for the family
reproduced the family.** Root cause: decomp cell-id grammars are heterogeneous and nothing declares
them.

## My defects this session, itemised

- **Four false attributions**, all of good acts, all refused by the seat: `AE~B`, `DS~N`, `DS~Q`,
  `DS~G`. ⛔ **I generated four and caught none myself.** The correction rate is a property of the
  seats.
- **D7 and D9 contradicted each other in one message** about one file. `~Q` read D9's reasoning as
  governing, implemented a better rule, and declared the deviation before the census could report it.
- **My seat ask to Andrew rested on an unvalidated column** — the same one that was wrong about
  P2-FLOOR. Commissioned a 5-row recheck; no seat was burned.
- **My vendor-egress ask was too narrow** — the grant is load-bearing for the v1 *join*, not just
  field enrichment, because the key is masked on the surface already inside the envelope.
- **`safe-commit`: my symptom was right, my mechanism was wrong.** `set -euo pipefail` + `x="$(cmd)"; rc=$?`
  kills the shell at the assignment. ⛔ **Recording it UNRESOLVED was the correct place to stop** —
  conceding would have shipped a no-op as a fix. And **my reported site was one of five**; two gates
  had unreachable BLOCKED branches.
- **The mitigation I broadcast to 12 seats became a false-pass check** when the fix added the marker
  string to its own help text. `DS~J` caught it 10 minutes after adopting it. Re-broadcast anchored.

## Open at Andrew

- `/account-api/*` — does the egress grant reach it? The v1 join depends on it.
- BD advisor-identifier vendor ask — blocks ADVI_INSURE's spine and D3's advisor level.
- Ruling 6 amendment — `carrier`/`product` rest on a container observed once, empty.

## Open at me

- 88 commits local across 12 seats; the 08-26 acceptance TO `@e70ffcc562` is **not on origin**.
- D1_CATVIEWS remediation round (packaging + tolerance + crosswalk + the (i) cells).
- The 40-candidate two-layer criterion census — resolution needs the decomps read.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-state --self-test` | **PASS 4/4** | gate satisfied before trusting any drift read |
| `comp-state` | run | drift half trustworthy |
| `comp-find` | used by seats under dispatch | `-i` discipline carried into TOs |
| `.tools/safe-commit.sh` | 12 commits | **found + reported a silent-refusal defect in it**; verified CTO's fix at source rather than on report |
| `to-check` (via `~G`) | 34 rows | adopted as the population domain after `~G` measured that the `project=` attribute drifts |
| `proof-of-spec-check` | via seats | **bare vs criteria-fed discriminated** — the finding of the night for this tool |
| `comp-pipescript` | via `0.8.0` | `--pipeline advi` ruled over the TO's stale `bd` |

**Gap found:** `proof-of-spec-check` run bare returns `VALID rc=0 violations=0` where the criteria-fed
form returns `INVALID` with 4 violations. **A coverage gap and a clean pass are byte-identical to
anyone who runs it the easy way.**
