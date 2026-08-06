# 3.0.0_SA_CVO~Z — MDPF_PROPVALIDATION absence-class verification

**Session:** 2026-08-06 20:32–22:25Z · site Z · branch SITEZ (push is MSTR~Z's, :55–:00)
**Seat:** verification, ABSENCE claims. Seated on COO~Z's request, framed by MSTR~Z @c801ec9d5.
**Archetype:** verification / adversarial-grounding.

## Current state

- **P0-6 (H10 external-reader bounded negative) COMPLETE** — `49e236bff`, amended `8019d54b2`,
  `14e4ed291`, `068e1be34`, `140259476`.
- **Independent port denominator delivered** — `7cc215f0a`; folded by COO~Z into P0-7 criteria
  3a/3b/3c @4eb24256a.
- Six commits on lane. Nothing pushed (correct — integration is MSTR~Z's).
- **Zero crons armed.**

## Deliverables

1. `deliverables/MDPF_H10_EXTERNAL_READER_BOUNDED_NEGATIVE_20260806.md`
2. `deliverables/MDPF_PORT_INDEPENDENT_DENOMINATOR_20260806.md`

## Findings that changed someone's work

| # | Finding | Effect |
|---|---|---|
| 1 | `DeleteOnTermination=TRUE` on the sole volume — terminate and EBS-delete are **one** API call | COO~Z rewrote P6-1; the sovereign condition has exactly one enforcement point |
| 2 | Newest daily snapshot predated the run by 6h40m; runtime-installed state uncaptured | COO~Z ordered a fresh pre-enumeration snapshot (AE~Z executed, `snap-0fa2186f01fbc3785`) |
| 3 | EC2 ran today 09:40 ET — "zero invocations" must **pin the cycle** | goes into P6-2 |
| 4 | Port denominator is **33 dispositions, not 38 objects** (prefix mixes code, config, backfill data, handoff docs, a pickle cache) | P0-7 criterion 3a; 38-count named as forbidden shortcut |
| 5 | `EC2_MANIFEST.json` declares code S3-staged → denominator is S3+repo, **survives termination** | reframed the capture from "restore a snapshot" to "diff against a listing" |
| 6 | `opal-served-key-write-trail` names `platinum/` in a **data-event** selector but `readOnly=false` — structurally cannot record a read | prevents a false YES on "is platinum covered?" |
| 7 | Served platinum is **17 objects, not 12 or 14** — 3 stale July-31 underscore twins both denominators are structurally blind to | CTO~Z ruled the acceptance criterion two-part; count corrects CTO-base F7's "four" |
| 8 | pyarrow at `:517` is a **guarded self-heal** — normally does nothing, so the installed version has unknown provenance | AE~Z captures `pip list --format=freeze`, not presence |
| 9 | The `<5` pin's **rationale** is a necessary artifact that is not code | routed as a P6 clause; three file-shaped buckets don't cover it |

## The instrument catalog — reusable beyond this project

Every one of these produces evidence that looks entirely plausible.

| Instrument | Failure | Discriminator |
|---|---|---|
| `aws s3 ls` | prints **local time**; s3api prints UTC. On an ET box, artifacts read ~4h fresher (AE~Z) | cite the s3api ISO-8601 value with its `+00:00` |
| bare `grep` multi-alternation | MSYS mangles the pattern → **silent clean zero** | `comp-grep` prints a denominator and warns |
| `comp-grep` with BRE `\|` | Python `re` reads it as **literal** → clean zero (**hit me**) | the tool's own warning; bare pipe + positive control |
| `--no-paginate` | returns **first page only** (`list-functions`: 50 of 196) | materialize and count; forced `--page-size` walk |
| `--query 'length(...)'` on paginated `list-*` | returns **page** count | count the materialized list |
| `comp-blast` / graph edges | **0 vs 4 real** consumers at `c801ec9d5` | never cite an edge count as evidence |
| `comp-pipescript consumers` | wrong zero — key composed by f-string, **no literal to extract** (DS~Z) | for this pipeline a graph zero is the *expected* output for a whole dependency class |
| `comp-estate` mdpf census | lists `mdpf-freshness-checker` **live**; `get-function` → ResourceNotFoundException | the live primitive wins |
| a **correct query against a stale path** | clean confident zero **for objects that exist** (AE~Z) | re-pin before every read; H7 is a standing constraint |
| `simulate-principal-policy` | 3 independent false-deny modes (CLAUDE.md 22a) | one `--resource-arns`; isolated positive control |

**The unifying shape: absence is silent BY DESIGN in this estate.** Four instances in one session, four
unrelated layers — `_empty_feeder()` returning a correctly-columned empty frame (DS~Z); `|| true` on
both pip installs; `readOnly=false` on a data-event selector; a moved key answering a correct query
with zero. For P6-2 I will treat *"does this failure mode announce itself?"* as a first-class question
rather than assuming a broken thing looks broken.

## My own errors — the honest measure of a verification seat

Every one was caught by a control or a peer. **None by care.**

1. **Row 5 bucket** — attributed by inference from Rule 17b, never measured. Verdict survived only
   because I'd measured both candidate buckets.
2. **Rows 1–4 bucket** — accepted "the constant executes, the docstring is stale." Correct general
   rule, **wrong answer, because it silently assumes the write SUCCEEDED.** Execution is not success.
   MSTR~Z ran the live listing neither DS~Z nor I ran.
3. **pmc escalation** — framed `<5` as a correctness risk; source says it is a **Python-3.9 syntax**
   artifact. Withdrawn loudly, since COO~Z may have folded the original.
4. **A false mechanism, caught pre-send** — claimed the pipe loses pip's exit status; `:17 set -uo
   pipefail` says otherwise. Checked the discriminator before sending.
5. **BRE `\|` clean zero** — would have reported "no runtime installs." `comp-grep`'s warning caught it.
6. **Location misattribution** — said the pin's rationale "dies with the EC2" while reading it from a
   **repo path**. The retrieval path was the disproof, on screen.
7. **"Already retired"** — attributed a **27-minute-old move** to a months-old decision, and sent it to
   two seats. The bound ("confirm the target exists before scheduling removal") is why it was a
   correction and not a bad deletion plan.

**The dominant class across 1, 2 and 7: a document supplied a plausible mechanism and displaced the
measurement.** CTO~Z found the same shape in their own Clock-v3 read and COO~Z's "51 section signs"
— three senior seats, one session. My refinement, which CTO~Z routed into GENCHI GENBUTSU: **a
document does not have to be wrong to displace a measurement; it only has to be relevant. A wrong
document eventually contradicts something. One that is correct about an adjacent fact never will.**

## Compiler Tools

| Tool | Use | Result | **Blind spot** |
|---|---|---|---|
| `comp-which` ×3 | routing (mandated Phase 1) | routed to `comp-whoread`; **no coverage gap** | scored the right tool **third** behind two source-graph tools that would have duplicated DS~Z's half; no route for EC2 instance/package inventory (0.49, flagged fuzzy) |
| `comp-whoread` | who-DID-read, 2 prefixes | **rc=1 FAIL CLOSED** both times, 0 object-level events since 2026-05-11 | only CT-covered buckets; **fails closed rather than reporting a false clean — its silence is informative** |
| `comp-grep` ×8 | source grounding, runbook census | denominators printed throughout (1031/1034, 21250/22958, 1/1) | caught my own BRE clean-zero; cannot see uncommitted/gitignored |
| `comp-glob` | repo source_path enumeration | 4 tracked files | tracked files only |
| `comp-estate` (indirect) | — | **known phantom** on `mdpf-freshness-checker` | over-reports existence; live primitive is the discriminator |
| raw `aws` (marked) | 11 calls, each `# rail-checked:` | live plane, s3api UTC throughout | no comp-tool models EC2 lifecycle, EBS snapshots, CT selectors, bucket-logging config, or Lambda env values — **five genuine coverage gaps, routed** |

## Blockers

None at me. **Nothing of mine gates anything** — refused gate-by-invitation per the TO and said so to
COO~Z, MSTR~Z and DS~Z.

## Next steps

1. **[MSTR~Z]** SYSPARITY scope call. XXX.md:389 carries a live unstruck LD-0318 cron + LD-0319
   permanent load-check; my launcher pasted the **base-CVO row (:388)** and stripped its
   "a base-CVO load" qualifier. Zero armed pending his word. *The launcher paste should be fixed
   regardless of the scope answer — it will mis-seat every future CVO~Z.*
2. **[COO~Z]** P5-2 (un-targeted zero-diff plans) and P6-2 (negative route evidence, with my cycle
   pin) — mine when issued, neither blocked.
3. **[OPEN, unowned]** Deployed Lambda **CODE** for the nine `opal-data-portal-v2` bucket-carriers plus
   `opal-portal-data-proxy`. Named as the true shape of what H10 leaves unclosed. Bigger than any
   current TO; nobody should silently expand into it.
4. **[COO~Z]** Ledger cross-reference for @4a2651063 — a sovereign authorisation living only in a
   deliverable is discoverable by nobody at the moment it matters.
5. **[open]** The 3 underscore twins are **NOT DONE, not NOT-AUTHORISED** (Andrew ruled TRASH ~2137Z).
