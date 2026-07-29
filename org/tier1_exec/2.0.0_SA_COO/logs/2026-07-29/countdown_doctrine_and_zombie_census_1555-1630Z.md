# A tool defect caught inside its own investigation, and a census that shrank by half — 2.0.0_SA_COO

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, SCRIBE, COORDINATE

Window 2026-07-29T15:59Z -> 16:29Z (since `cf3443cb4c`). 3 commits. Nothing deployed, nothing
executed against the estate — read-only throughout, freeze intact.

## Objective

Hold for the 16:15Z / 17:15Z fires with the baseline re-take queued. Two items arrived and both
were addressable without touching the frozen wave: CTO directing a doctrine line, and an
Andrew-direct zombie-path census routed to my teardown wave for ownership + scoping.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-pipescript deployed` | FULL PATH form, `data/mdpf/.../dim_mdpf_account_distribution.py` | **1 STALE** (rc=0) | Real finding. Auto-detects mdpf. Confirms the item-ZERO producer defect. |
| `comp-pipescript deployed` | BASENAME form, same script | **0/0/0 no-coverage** (rc=0) | Falls back to the bd tree. Same script, opposite verdict, IDENTICAL rc. |
| `comp-glob` | `**/_schwab_bd_match_v*.py` | PASS | Located the three diagnostics generations. |
| targeted `grep` | named files only (watchdog-shutdown.sh, D_04, lib/config.py) | PASS | File-scoped, not estate-broad; HUD nudged once on an earlier portal-wide `grep -rn` (React Query -> `comp-cache`) and I proceeded — nudge, not deny. |

**What worked:** running BOTH invocation forms of the same tool against the same target. That
comparison is the entire finding; either form alone looks authoritative.

**What failed — MINE, and it is the most useful thing in this window.** My first attempt to verify
the rc claim piped the tool through `grep | head` and read `$?`, capturing **head's** exit code, not
the tool's. A clean-looking `TRUE_RC=0` that measured the wrong process. **I reproduced the exact
defect class I was in the middle of verifying, while verifying it.** Caught only because the
estate's own rule (score on OUTPUT never rc; `PIPESTATUS` when piping) was in front of me. Re-ran
with rc captured before any pipe.

**GAP FOUND (AE base's, reproduced by me; AE carried it to CTO 161216Z):** `comp-pipescript
deployed` exits **rc=0 on a STALE**. The corpus's auto-logged PASS column is rc-derived, so it means
*"the tool ran"* and never *"the check passed"* — **structurally incapable of recording a STALE,
corpus-wide for this tool family.** Three states collapse to one glyph: *did-not-look* /
*looked-and-clean* / *looked-and-BROKEN*. The corpus header states CTO reviews it "to identify
recurring failure patterns and new gaps," and its verdict column cannot show a failure.

## Work Completed

### 1. Countdown doctrine line (`61934358e2`)
CTO ruled my escalation a SECURITY defect, adopted my distinction verbatim, and directed the line to
doctrine. Authored into section **IV (Guards)**, not III — III is *instruments that lie*, and this
control did not lie: **the deny held on every run; what was unsafe was the sentence next to it.**
Beyond CTO's four-part remedy I added the generalisation and flagged it to him as strikeable: **a
control's failure text is part of the control; never emit a speculative remediation hint from a deny
path.** His (a)-(d) fixes this instance; the rule aims at the next author.

### 2. Corrected my own corpus row (`ff6f1ef66a`)
AE showed my flag was right about the wrong row: I quoted `:27786`'s command while describing
`:27772`'s output. **`:27786` is the worse one** — it actually ran, actually found the `1 STALE`
that is CTO's item ZERO, and was logged PASS. My row had asserted the adjacent AE row was "this same
run"; it was not. Corrected in place rather than leaving a false claim about another agent's work in
a shared record.

### 3. Re-take handoff sharpened (`8c55c2635d`)
AE supplied the discriminating hashes. My planned UNATTRIBUTED fallback is no longer needed: the two
outcomes are distinguishable.

### 4. Zombie-path census OWNED + SCOPED (Andrew-direct via CTO; nothing executed)
Read-only scoping resolved two of CTO's four items to *no action*:

| CTO item | Verdict | Evidence |
|---|---|---|
| (b) `gold/trigger-pending.json` — "most dangerous item" | **REFUTED x2** | Different buckets (`opal-data-bd` / `opal-data-inf`) **AND both sites are `aws s3 cp <key> /dev/null` inside an `if` — existence PROBES, not writes.** No writer, so no collision. |
| (c) `schwab_bd_account_mapping.parquet` | **CONFIRMED** | All three generations `upload_file` the same key on BD_BUCKET (`:236-238`, `:204`, `:245`). The only verified repo-level multi-writer. |
| (d) `platinum/firm/*` | **REFUTED as collision** | Firm-separated via per-tree `lib/config.py`. CTO's expectation correct; a "cleanup" would have been an incident. |

>> **The census tool classified a READ as a multi-writer sink.** It matched key PATHS, not
>> operations or buckets. CTO called them "candidates, not verdicts" — that framing was right and
>> the HIGH-signal ranking inside it should not be trusted. <<

**NEW LATENT HAZARD found inside the refuted (d), nobody had flagged it:**
```
data/black_diamond/scripts/gold/lib/config.py:14  S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-bd')
data/cot/scripts/gold/lib/config.py:16            S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-cot')
```
**Both trees read the SAME env var name; only the DEFAULTS differ.** One exported `BD_S3_BUCKET`
collapses cot onto bd's bucket — the firm separation here is a property of nobody having set an env
var, not of the code. The COT tree keys on a variable named for **B**lack **D**iamond, which reads
as correct in review. Fails CLOSED (NEVER#2 IAM Deny is the runtime backstop), so not urgent, but
it is a trap and it is one line per tree.

## Decisions Made

| Decision | Rationale |
|---|---|
| Countdown line into IV (Guards), not III | The control did not lie; its mechanism held. Guard property, not instrument property. |
| Generalised CTO's remedy into a standing rule, and told him it was strikeable | His fix addresses this instance; the rule addresses the next author. Flagged rather than smuggled. |
| Corrected my own corpus row rather than letting it stand | It made a false claim about another agent's row in a record CTO reviews. |
| Did NOT duplicate the corpus-purpose finding into CTO's inbox | AE was mid-thread with him; I offered the framing for them to carry. They did, credited, 161216Z. |
| Did NOT execute any census item | CTO said not tonight; the wave outranks it. Scoping is read-only and is what he asked for. |
| Left "concealment vs retirement" and the wrong-label class unwritten | Wave vocabulary during a live wave, and a class CTO raised but has not ruled. |

## Files Modified

see commit messages: `61934358e2`, `ff6f1ef66a`, `8c55c2635d`.

## Blockers

None held by me. Baseline re-take is WAITING (two preconditions), not blocked. Census is
CTO-deferred, not blocked.

## Current State

- Watcher live, Monitor `bek0zd4f3`. Registered PID 28928. Zero crons. `/drive` OFF.
- **16:15Z publisher FIRED** — corroborated from CTO's version census:
  `platinum/mdpf/cottonwood/aggregate-aua-timeseries.json` carries a version at 07-29T16:15:32.
  Cottonwood byte-frozen at 37,518 across all 4 versions while global grows 157947 -> 200059:
  a faithful publisher copying a gold source that lacks the data. Independently corroborates that
  the defect is UPSTREAM in the producer, not in the publish step. AE~A holds that read.
- **Baseline re-take still queued**, two preconditions (run lands + artifact identified by hash);
  discriminating values pinned in `startup_verification_wave_1455-1555Z.md` @`8c55c2635d`.
- Teardown wave (mine, post-fires) now carries: the 3 live legacy-plane clobbers; schwab v1/v2/v3
  (promoted — only CONFIRMED item); the `BD_S3_BUCKET` name collision; price-update
  script-vs-Lambda (unverified); CTO's permanent-red LEGACY-EMIT item.
- Open at CTO from me: the wrong-label class as doctrine; the strikeable generalisation in
  `61934358e2`; whether the corpus PASS column gets fixed or the corpus gets a caveat.

## Next Steps

- **[2.0.0_SA_COO]** 17:15Z emitter observation; then the baseline re-take when DS~A's run lands,
  plane- and artifact-labelled.
- **[2.0.0_SA_COO]** Teardown wave post-fires, sequenced as above — every item on tonight's
  discipline: identify the writer on the APPLIED plane, prove it dead before removing what it
  wrote, never delete a delete marker.
- **[1.0.0_SA_CTO]** Holds: WARN remediation gate (owner AE/DS), cottonwood basis rule, census
  sequencing override if he disagrees with my reordering.
- **[0.7.0_AE_CloudOps]** Carrying the corpus-purpose finding to CTO (done 161216Z); owns the
  audit-archive unwedge, pending his direct word.
- **[0.4.0_DS_ClientPlatform~A]** The ad-hoc cottonwood producer run; deployed-vs-repo confirmation.
