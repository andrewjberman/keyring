# 3.0.0_SA_CVO~Z -- work log 2026-09-09 18:17Z-18:35Z: load, and the AC that tested the half that cannot rot

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Seat:** `3.0.0_SA_CVO~Z`, site Z, branch SITEZ, PID 41724. **Prior log:** `2026-09-04/work_0050-0210Z_*`
(this lane; the later 09-04 logs in that folder are the BASE seat's). **Loops:** zero crons; `/watcher`
armed once at load. **Push state:** local HEAD `9263dd2d8b`; `origin/SITEZ` `ff9900b0ea34` by `ls-remote`
at 18:2xZ -- this seat's commits are **LOCAL**, and the integrator is BLOCKED-SOVEREIGN on that push.

## Summary

Load after a five-day gap. The LD-0319 parity control ran FIRST and returned one FAIL, which turned out to
carry a defect its own explanation says is not there. The delivery ledger held **19 rows at READ 0/19**, all
`OFFER-EXHAUSTED` from 09-04 -- opened, read whole, acked. The one item routed to this seat in that mail
(the comp-schedule carrier grammar) was already discharged at HEAD and is verified here on this seat's own
instrument rather than on the reporter's word.

## 1. LD-0319 parity: DRIFTED, and the drift is invisible because the check was already red

`python infra/system/system_parity.py` rc=0. Ontology 4/5; every other domain 5/5. The single FAIL is
`ont-rulebank-version-current`, which is a **known standing FAIL** -- its own explanation text says so and
routes the absence half to a design owner. That is why it is worth reading past the verdict.

**The check's own recorded state:** *"measured under the harness's own exclusions, live version 1.2, 8 of 8
`rule-bank v<digit>` occurrences across 7 files are at v1.2, ZERO stale."* Source and sites AGREED.

**Measured here, and this is the change:**

| | value | instrument |
|---|---|---|
| canonical head | **1.8** | `meta.version` in `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`, read directly |
| that file's vintage | 2026-08-20 22:10 `@5fc45ad69d` | `git log -1 --` on the path |
| assertion sites | **8 hits / 7 files, ALL at v1.2** | `comp-find 'rule-bank v[0-9]' -- infra/system`, denominator 11 hits / 173 files scanned, corpus=all |

The 3 remaining hits of the 11 are `system_parity.py`'s own fixtures, which the harness self-excludes.
So: **0 of 8 live assertion sites followed the source across six versions, and the gap has stood ~20 days.**

⛔ **WHY NOBODY SAW IT, WHICH IS THE FINDING RATHER THAN THE NUMBER.** This check has two independent limbs
-- (a) the 4 required representation files carry no marker at all (ABSENCE, a design call, documented and
owned) and (b) the enumerated assertion sites are current. Limb (a) has been red since it was written. **A
check that is already FAIL cannot signal that its OTHER limb just went FAIL** -- the verdict line was
already the same colour, and the explanation a reader trusts still describes the pre-drift world. The
staleness rode in under a failure that was known, expected and correctly characterised.

⭐ **AND THE ACCEPTANCE CRITERION SAYS THE OPPOSITE OF WHAT THE FILES DO.** `NFRA_SYSPARITY.WS-4` is
`<status>complete</status>` (issued_to `0.8.0_AE_CloudComp~C`) and its **AC-2 reads: *"SDK vocabulary-bound:
@327b615e5 -- v0.1 stub retired, ontology_ref cites the rule-bank not a hand-copy."*** The strings do both
at once:

```
ontology_ref: "NFRA_ONTOLOGY rule-bank v1.2, vocabulary-bound (ratified LD-0311 @086238604;
               canonical: org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml + variance_dimensions.yaml)"
```

The **path citation** is live and cannot rot -- AC-2 tested that half and it passed, correctly, and still
passes today. The **version literal in the same string is the hand-copy AC-2 declares retired**, and it is
the half that drifted. ⛔ **The AC was satisfied on the limb it measured while an untested limb inside the
very same string carried the defect the AC was written to prevent.** This is Rule 22's scoped-check clause
at sub-string grain: the check scoped to the citation certifies the constant beside it clean.

⭐ Corroborating that the estate already knows the pattern and fixed it ELSEWHERE: the sibling check
`ont-archetypes-in-system` PASSES precisely because the Role/Relation/Variance counts were migrated to
DERIVE live ("not hand-copies", CTO~Z re-aim 142116Z). **The counts were de-hand-copied; the version string
in the same files was not.**

**BOUND on this seat's read:** I measured the head version, the vintage, and the full assertion-site census
with its denominator. I did **NOT** determine whether the SDK adapters are semantically broken by running at
a v1.2 understanding of a v1.8 bank -- the drift is in the REPRESENTATION, and whether it implies a
behavioural gap is a separate question with a different owner. Nothing here is ARMED and nothing is hazardous;
this is inert representation staleness. **Verifier-not-fixer: I have edited none of the 7 files** -- they are
`infra/system/sdk/` and not this seat's lane, and WS-4 is a closed TO whose reopening is not mine to declare.

## 2. Delivery ledger: 19 rows, READ 0/19, all opened and acked

`get_delivery_state(since=2026-09-04T00:00:00Z)` returned **19 of 19 `OFFER-EXHAUSTED`, READ COVERAGE
0/19** -- the shape XXX.md B.0 exists for: the RMM reboot killed the session these were offered to, so they
are invisible to `check-inbox`, `get_agent_status` and a "resume from your last log" read. Both live probes
read EMPTY at load and were right to.

All 19 opened from `org/mcp/inbox/3.0.0_SA_CVO/~Z/read/` and read in full, **each Msg-ID taken from its own
`**Msg-ID:**` header line, never from a citation in a neighbouring body** -- the exact defect
`0.0.0_AB_MSTR~Z` disclosed against itself in msg 20497, which was one of the 19. The ack receipt recorded
19 of 19 with **no "already carried an ACK" line**, which independently corroborates the 0/19 measured
before it: no slot was closed by a seat that was not there.

**Substantively owed by this seat: one item, and it was already discharged.** msgs 20360 / 20365 routed the
comp-schedule carrier-grammar remedy here (G-3: a build log QUOTING the G-4 sentinel inside a fenced block
was counted as a second gate). Verified at HEAD on this seat's own instruments, not on the reporter's report:

- `comp-read .tools/comp-schedule --enumerate 'fence'` -- 19 hits / 867 lines / 35 sections: helper
  `_fenced_lines` at `:147`, docstring citing msgs 20360/20365 at `:151`, applied at `:267`/`:272`,
  and the disclosure string at `:283` reading *"EXCLUDES org/mcp/inbox AND any line inside a ``` fence
  ... path-scoped for inbox, fence-scoped everywhere else"*.
- `comp-schedule --self-test` -- 6/6 PASS, and **control 6 guards BOTH directions**: a fenced sentinel is
  refused AND an unfenced one is NOT over-matched. A guard that excluded everything would pass a
  one-directional test; this one cannot.
- Live run: **C1 denominator 20 -> 4 gates.** ⛔ Read as the COMPONENT, never the total: the total now
  reads **22** (C1 4 + C2 6 + C3 12) because C2 moved 5 -> 6, which is msg 20365's trap firing exactly as
  predicted -- a fresh total is not a check on any one carrier.

The remaining 18 asked nothing of this seat (several say so in terms). Andrew's 09-04 rulings -- the five
`/open-calls` at 13:00Z and all ten cards at ~16:5xZ -- are read and carried as grading context.

## 3. One live-fabric observation, surfaced not adjudicated

`2.0.0_SA_COO~ZZ` reads **`BLOCKED: NFRA_REPORT L5 cannot start -- no PRD, no L3 registration ... Awaiting
L4 notifier`** while `ff9900b0ea` (14:08Z, **on origin**, `1.0.0_SA_CTO~Z`) registered NFRA_REPORT under D12
and minted the PRD at v0.1 with the endpoint ratified, and its own message says COO~ZZ is unblocked. A live
seat is idle on a condition that has cleared. **Not this seat's to route** -- surfaced to `0.0.0_AB_MSTR~Z`.
It is msg 20344's shape again: a record does not learn that the world has moved, and only a census finds it.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `system_parity.py` | bare (LD-0319 PRIMARY, not the `comp-system --check` fallback) | rc=0, 1 FAIL | the load-time control; ontology 4/5 |
| `comp-find` | `'rule-bank v[0-9]' -- infra/system` | 11 hits / 173 files, corpus=all | the assertion-site census with its denominator |
| `comp-find` | `--name 'NFRA_SYSPARITY*'`, both pages | 26 hits / 54,602 files | established the project has NO surprise channel |
| `comp-read` | `--enumerate 'fence'` on `.tools/comp-schedule` | 19 hits, banded | the G-3 remedy verified at source |
| `comp-read` | `--enumerate` on the WS-4 task order | 9 hits | `<status>complete</status>` and AC-2's wording |
| `comp-schedule` | bare + `--self-test` | 22 armed; 6/6 | C1 component 20 -> 4 |
| `to-check.py` | `--all --assignee 3.0.0_SA_CVO~Z` | total=0, scanned 2342 | zero TOs held |
| `audit-archive-invoker.py` | bare (A.2) | rc=1, 18 findings | expected device-chain noise, NOT chased |
| `git` | `ls-remote`, `log -1 --`, `rev-parse` | -- | every vintage and push-state claim here |

**What worked:** running the parity control before anything else, then refusing to stop at its verdict --
the FAIL was known, the *reason* inside it was not. Reading each of 19 Msg-IDs from its own header.
**What failed, both mine:** I `tail`-ed `to-check.py` and read its THIRD-POPULATION diagnostic block as my
own work (the real answer was `total=0`), then `head -700`'d a 13-file log read and lost the three most
recent logs -- **two instances of the same banked rule in one load**, and the second came after the first
was already caught. **Gap found:** a two-limb check whose standing FAIL on limb (a) makes a fresh FAIL on
limb (b) unobservable; no instrument in the parity harness distinguishes them.

## Startup protocol -- org/XXX.md

Steps 1 / 1a / 1b(A, A.1, A.2, A.3, B.0, B, B.1, C, D, E, F) / 2 / 3 / 4 complete. Identity cross-checked:
`liveness.json` reads `3.0.0_SA_CVO~Z` at PID 41724, this session's own registration PID -- no conflict.
Drive prefix **resolved, not assumed**: `/cygdrive/c` is NOT mounted on this box, so the Monitor is armed on
`/c/...`; banner reads `parent-tied: pid 313658`. **Zero crons armed.** The Step 1b-F row naming a
`3.0.0_SA_CVO~Z` SYSPARITY cron is the standing LD-0318 fork: `NFRA_SYSPARITY.json` now reads
`status: active` with `closed: 2026-08-25` AND `reopened: 2026-09-01`, and both readings of the fork
converge on ARM NOTHING -- which is also this session's launch term. Row left **unstruck and unannotated**,
per the three prior precedents; it blocks no act and is not escalated as though it does.

## Blockers

None BLOCKED at this seat. The parity drift is EVENT-GATED on an owner; the push is the integrator's.

## Current State

- **LD-0319: DRIFTED.** Ontology domain 4/5. `ont-rulebank-version-current` FAILs on both limbs now, not
  one; limb (b) is new and ~20 days old. Owner routing with `0.0.0_AB_MSTR~Z`; remediation lane is
  `infra/system/sdk/` (WS-4's, `0.8.0_AE_CloudComp`, not currently live).
- Inbox 19/19 read and acked; nothing outstanding owed to any sender.
- comp-schedule G-3 remedy: DISCHARGED at HEAD, verified independently. G-4 stays correctly ARMED.
- NFRA_SYSPARITY has **no surprise channel** on either root -- so this finding has no project carrier and
  is recorded here pending a routing word rather than a channel being minted unilaterally.
- Push: local `9263dd2d8b`, origin/SITEZ `ff9900b0ea34` (ls-remote 18:2xZ). This log rides the next window.

## Next Steps

- [`0.8.0_AE_CloudComp`] the 8 v1.2 assertion sites across 7 `infra/system/sdk/` files -- and the durable
  form is the one the counts already use: **derive the version, do not re-copy it**, or the next bump
  re-opens this exact row.
- [`0.0.0_AB_MSTR~Z`] route the drift to an owner; the `2.0.0_SA_COO~ZZ` stale-BLOCKED observation; whether
  NFRA_SYSPARITY should carry a surprise channel at all.
- [`3.0.0_SA_CVO~Z`] L8/L9 engagement on NFRA_OPSEC202609 and NFRA_REPORT as their rounds reach L8 --
  nothing before. Event-driven off the inbox Monitor.

-- 3.0.0_SA_CVO
