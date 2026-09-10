# Three STOPs on a live signing-key rotation, and not one of them came from a check this seat wrote -- 2.0.0_SA_COO~Z

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

**Date:** 2026-09-09 -> 2026-09-10 (window 17:00Z -> 03:15Z; 13:00 -> 23:15 US Eastern)
**Task Order:** ad-hoc -- `/watcher` once + `org/XXX.md` startup, then `/canonical-flow NFRA_OPSEC202609` to calibrate a midstream pickup, then `/drive NFRA_OPSEC202609` ticks 1-8 under the LD-0530 standing arm (cron `b8af0997`, Andrew-direct 2026-09-10 ~00:3xZ, relayed msg 20690)
**Status:** IN PROGRESS -- NFRA_OPSEC202609 round 2 is TERMINAL at 31 of 31 and sitting at L9 with `3.0.0_SA_CVO~Z`. Startup COMPLETE.
**Push state:** LOCAL. local HEAD `a961b8731d`, `origin/SITEZ` `93ab120af1`, 70 ahead / 0 behind, read by `git ls-remote origin refs/heads/SITEZ` at 03:19Z. Pushes are `0.0.0_AB_MSTR~Z`'s on Andrew's word (LD-0522); this log asserts nothing about origin beyond that read.

---

## Objective

Pick up NFRA_OPSEC202609 midstream as its COO, drive round 2 to a terminal order set, and hand L8 to the CVO. The substantive work under it was FWD-10: rotate the portal's live login signing key without signing anybody out. This log's thesis is the part worth carrying forward -- the rotation was stopped three times, every stop prevented a distinct silent production failure, and **not one of them was caught by a condition this seat wrote.**

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `proof-of-spec-check.py` | `.tools/proof-of-spec-check.py <instance>` on 29 instances | PARTIAL | 29 VALID of 29 at HEAD, each re-run here rather than accepted from a lane's rc. Run WITHOUT the criterion-id argument all night -- see Gap found. |
| `to-pipeline-gate.py` | staged-order gate, 4 newly cut faces | PASS | passed `TO-OP-S-10D`, `-10E`, `-10F`, `NFRA_SYSPARITY.TO-RB1-SITEZ`. One refusal was correct and named a missing `dep_stage` I declined to invent. |
| `surprise-row-gate.py` | at every row commit | PASS | also the L10 predicate's source of truth: `:677` `open_items = sorted(k for k, v in latest.items() if v in UNDISPOSITIONED)` -- keyed by ITEM, across BOTH channel documents. |
| `safe-commit.sh` | 17 commits under this serial | PASS | refused twice on a FOREIGN `.git/MERGE_HEAD` (another seat mid-merge). Both refusals were correct; no override exists by design, so I waited and retried. |
| `safe-merge.sh` | 1 drain (`9263dd2d8b`) | PASS | the `--no-commit` window graded the MERGED index, which is the only place a cross-index row-id collision is visible. |
| `comp-surprise` | `--project NFRA_OPSEC202609 --json`, every tick | PASS | the rail REFUSED it piped into `tail`; re-run unpiped. Correct refusal. |
| `comp-find` | token/id censuses across both roots | PARTIAL | accurate here, but blind to a linked worktree by design -- from one it returns the MAIN tree's answer as a confident zero (`NFRA_SYSPARITY-Z-S1`). Every criterion I cut naming a `comp-find` invocation names the MAIN tree explicitly. |
| `comp-read` | face shapes, spine sections, gate source | PASS | rail refused `comp-read \| tail`; re-ran unpiped. |
| `comp-schedule` | cron census at arm time | PASS | same pipe-refusal class, same remedy. |
| `to-check.py` | `--all --project NFRA_OPSEC202609` | PARTIAL | correct output, wrongly read -- see What failed. |
| `missions-tree-index.py check` | tree <-> index <-> DIRECTIVES.yaml | PASS | its refusal drove the `PROJECT_TREE.contract.json` level-2 regex widening from `{4,12}` to `{4,18}`. |

Role minimums: the standard's table names DS/DE/DT/AE/RD and carries **no COO row**, so no pre-work minimum binds this seat. The eleven rows above are what actually ran.

**What worked:** `surprise-row-gate.py` read at source settled a number three of my own tick logs had carried wrong -- reading `:677` was worth more than any amount of re-counting. `to-pipeline-gate.py` is a real neck: it refused every face that was not yet legal and named why, so no defective order reached a lane.

**What failed:** four comp-tool invocations piped into a receiver (`comp-read | tail`, `comp-find | head`, `comp-schedule | tail`, `comp-surprise | tail`); the rail refused each and each re-ran clean unpiped or with a native `--limit`. Separately, `to-check.py` returned a correct census that I read as mine -- the rows were THIRD-POPULATION and my header said `0 active TOs`. Printing the denominator fixed it. A `.get('agents',{})` read of `liveness.json` returned "live serials: 0"; the top-level keys ARE the serials, and the real count was 8.

**Gap found:** `proof-of-spec-check.py`'s COVERAGE limb is only reachable by passing the criterion-id argument, and **nothing in a bare invocation warns you that its VALID verdict certifies the rows present and never that the expected set is complete.** I ran it bare on every instance tonight; "29 of 29 VALID" was true and narrower than it sounded. `3.0.0_SA_CVO~Z` measured that limb independently at L8 (0 mismatches across 29) -- and caught a false positive in its own first probe of it, because a prose-regex cannot separate a criterion from a sibling criterion the block merely cites.

---

## Work Completed

### 1. Startup, and seven messages no inbox probe could see

`/watcher` armed once (not a loop). `check-inbox`, `get_agent_status` and the ferry scan all read the lane inbox clean -- and seven `OFFER-EXHAUSTED` messages were nonetheless addressed to this serial. Recovered them directly from `org/mcp/broker.db` (`messages` table: `id, from_serial, to_serial, subject, body, sent_at, delivered, polled_at, emitted_at, acked_by, offer_count`), content-hash-compared each against what I had already handled to prove they were not duplicates, and only then acked. **Three probes agreeing on empty was three instruments sharing one blind spot, not corroboration.**

### 2. Midstream pickup

`/canonical-flow NFRA_OPSEC202609` measured the project at L7 with 31 orders cut, PRD v0.14 `@5f4d4b894f`, decomposition v0.1.16 (35 cell ids: 29 work cells + 6 `OP-x-*` decide-first). Classified `STALLED-AT-OWNER` with the COO as owner. That read is what let obligation 3 fire the moment the order set went terminal instead of a tick later.

### 3. FWD-10 -- the rotation landed, and nobody was signed out

`TO-OP-S-10` terminal, instance VALID 5/5, ledger CLOSED 5/5, drain `a5b269c9b0`. The bar was tested **on the pre-act artifact itself**: a refresh token signed at 00:13:16Z with the OLD key, written before any secret moved and untouched on disk since, presented at 01:21:40Z after the switch -- crypto ACCEPTED, failing later at the user lookup, which is the pre-act baseline discriminator unchanged. A neither-slot token demonstrated the REJECT answer on the same axis. Secret preservation verified independently here: `01cfa582` AWSCURRENT, `fabe94f0` AWSPREVIOUS, no `DeletedDate`, `RotationEnabled` unset.

**The 7-day refresh lifetime was both the hazard and the proof** -- the property that made a single-key verify path a week-long outage risk is what preserved a testable pre-act token after the 15-minute ones aged out.

**THE THREE STOPS, and the third one is mine:**

| stop | what it prevented | whose defect |
|---|---|---|
| `Z-S157` | a THIRD verifier nobody had counted, still single-key | nobody's -- an uncounted surface |
| `Z-S159` | an unbounded signing-key read | the design's |
| `Z-S160` | `S10E-AC2` -- **a criterion I wrote** that made the signer's PUBLIC read single-key, when that read is a pure verify path (`/auth/refresh`, 7-day tokens) | **mine** |

On `Z-S160`, all five conditions on my own GO would have returned GREEN while every returning user was signed out for seven days. Not one of the three came from a check this seat specified; all three came from the re-grounding the faces mandate. That is the finding, and it is an argument for the faces, not for me.

Also recorded: **L4 reached production broken for 3m52s** (`Z-S161`) -- a multi-line PEM truncated to its 27-byte first line through `.tools/aws.cmd` while the API returned rc=0, a real `VersionId` and `AWSCURRENT`. Reported by the lane against itself, in the hour. Its fix then ARMED THE ROLLBACK (re-writing moved `AWSPREVIOUS` onto the truncated version, converting the documented recovery path into a second outage); found by looking for it, disarmed 01:18:14Z.

### 4. Four faces cut, all gate-passed

| face | commit | note |
|---|---|---|
| `NFRA_OPSEC202609.TO-OP-S-10D` session-analytics two-slot | `9e2818276c` | teach the third verifier two slots |
| `NFRA_OPSEC202609.TO-OP-S-10E` signer key-read TTL | `204b608f94` | carried my wrong `AC2`; see stop 3 |
| `NFRA_OPSEC202609.TO-OP-S-10F` signer verify path two-slot | `f776c1f7ba` | `S10F-AC2` deliberately PAIRED |
| `NFRA_SYSPARITY.TO-RB1-SITEZ` rule-bank version drift | `afc1c9dec9`, renamed `71762eacd6` | Andrew's assignment |

`TO-RB1-SITEZ` is the one that cost time: the order id lacked `.TO-`, so `cvo_send_guard.py:134` refused two GOs (a CITE is a token `<PROJECT>.TO-<id>` whose file exists AND whose `<issued_to>` is the recipient), and I did not notice for two hours -- `get_delivery_state` showed zero rows reaching the lane. **I renamed the order rather than writing a matching token into the body**, because the body would have satisfied the guard while leaving the id wrong everywhere else.

### 5. The two orders that could not complete as written

`TO-OP-S-15-19` (blocking input ABSENT FROM THE WORLD, not unfinished) and `TO-OP-S-23` (date-gated 24 days out AND iterating the same absent list). I refused to invent a terminal status for either. `1.0.0_SA_CTO~Z` supplied the ruling and the two re-entry pointers `cancelled` requires (`affef41b63`), which met L7's exit condition by arithmetic: 29 complete + 2 cancelled-with-pointer = 31 of 31.

Related and worth reading first: **`TO-OP-S-20`'s MEASURED NEGATIVE IS ITS DELIVERABLE.** 97.8% of the only observable sign-in window is this project's own `opal-s6`/`opal-s7` probe traffic, firm attribution inexpressible on every available source, firms observed 0 of 4. `S20-AC2`, named on the face as the control that must be able to fail, FIRED. Grading that as an incomplete would invert the finding.

### 6. L8 packet compiled and handed

`ledger/L8_PACKET.round2.final.md` @`4cef4a058c`, label corrected @`514272320c`. Six sections: order set terminal; FWD-10 outcome and how it was proven; the two judgment criteria (`S10D-AC2`, `S10E-AC6`) left ungraded for L9; the row census; what the CTO's L10 read receives; and what the packet does NOT claim. READ-acked by `3.0.0_SA_CVO~Z` at 02:30:36Z, 35 seconds after it was handed.

### 7. Eight drive ticks

Ticks 1, 2, 3, 5, 6, 7, 8 logged (`a83be2865a`, `e6837096b6`, `b5897ccda0`, `141e0a23ea`, `8c7b3fe16b`, `514272320c`, `cf066e0c5e`). **Tick 4 was quiet and correctly wrote nothing** -- the skill logs substantive ticks only. Tick 2's nudge found a real idle lane whose cause was mine (the unsent GO above).

### 8. Corrections this seat made against itself

- **154 -> 137/138 undispositioned.** I counted per-ROW across ONE document; the gate walks `latest.items()` keyed by ITEM across BOTH. 23 rows dispositioned by a later carrier were being counted as open. It rode three tick logs before I read `:677`. Recomputed on the gate's own shape it matched the CVO's independent parse exactly -- two seats, two instruments, one figure.
- **Relayed "CLAUDE.md AND org/XXX.md BOTH CHANGED IN THIS MERGE" as bare fact.** False. Blobs identical at the pre-merge tip, the merged head, and the CLOUD side. Mechanism, from the CVO via the CTO: **a merge diff taken against the FOREIGN parent reports CONVERGENT edits as changes.** Corrected to both AE lanes.
- **My own retraction on the `{4,12}` regex was itself wrong.** `0.7.0_AE_CloudOps~V` corrected me: it had quoted the hook's LIVE REFUSAL TEXT, so nothing wrong reached anyone downstream and there was no error to retract. Its point is the one to keep: *a wrong entry in the record is not made harmless by being self-blaming.* I withdrew the paragraph as a matter of record.
- **My channel parser assumed one ```json fence per document** and died `JSONDecodeError: Extra data` on the CVO's multi-block adjudication. The counts had been right only because the assumption happened to hold. Fixed to `re.findall(r"```json\s*(.*?)```", s, re.S)`, each block parsed independently with a printed count of unparseable blocks. **It failed loudly, which is the only reason this is a note and not a wrong number.**
- **The packet's own first line said "handed for L9".** The spine section 1 reads *"L8 -- Compilation. Owner: `3.0.0_SA_CVO`, whose engagement with the project begins here."* **L8 is the CVO's LIMB**; the packet is the COO's HANDOFF INTO IT. The CTO named the identical mechanism against itself -- both of us inferred the owner from the tree map (who WRITES the artifact) instead of section 1 (who OWNS the limb).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Refused to set a `dep_stage` on NFRA_SYSPARITY to satisfy a gate; took an audited `pipeline-override` instead | Setting a machine-readable stage to pass a gate describes the gate, not the world. The override leaves an audit row saying exactly that. |
| Refused to guess `ROUND_CLOSE` on NFRA_OPSEC202609 | Measured at source: spine `:347` -- `ROUND_CLOSE` flips on the CTO's RECEIPT OF THE SLUG, and it is the CTO's flip. `EXECUTING` is correct while no slug is cut. Corroborated on a second instrument: NFRA_OUTSET also carries an L8 packet and also reads `EXECUTING`. |
| Renamed `TO-RB1-SITEZ` rather than writing a matching cite token into its body | The body would have satisfied `cvo_send_guard.py` while leaving the id wrong in every other carrier. |
| Fired no nudge at tick 7 | Obligation 4's trigger is *no READ ack at one tick*. The ack was measured at 02:30:36Z. A nudge there would have been noise dressed as diligence. |
| Cut the caller-migration face as **round 3's opening order**, not a 32nd order in round 2 | My L8 packet asserts 31 of 31 terminal and L9 is adjudicating it. A 32nd order in round 2 falsifies that mid-adjudication. |
| Routed the caller migration to the three owning lanes rather than moving the callers myself | Andrew-direct msg 20760 authorised the ask and the two in-lane Lambdas; it did NOT authorise moving three callers into this project's territory or editing another lane's code. |

---

## Files Modified

See commit messages -- each carries its own per-file summary: `89b4f89afd`, `9263dd2d8b`, `145e75a5bc`, `9e2818276c`, `199ebff70b`, `204b608f94`, `afc1c9dec9`, `f776c1f7ba`, `a83be2865a`, `e6837096b6`, `71762eacd6`, `b5897ccda0`, `141e0a23ea`, `4cef4a058c`, `8c7b3fe16b`, `514272320c`, `cf066e0c5e`.

**17 commits, and the count needed a correction before it could be written.** `git log --author="2.0.0_SA_COO~Z"` returned 34 -- `--author` is a SUBSTRING match and `2.0.0_SA_COO~ZZ` (a live seat, driving NFRA_REPORT) contains this serial as a prefix, so its drains were being counted as mine. Re-derived with an exact-equality split on `%an`: 173 commits in the window across 20 distinct authors, **17 of them exactly `2.0.0_SA_COO~Z`** and 17 exactly `2.0.0_SA_COO~ZZ`. The two seats did the same volume of work tonight and a substring filter cannot tell them apart.

Rows needing more than their commit message:

| File | Change | Committed |
|------|--------|-----------|
| `org/standards/PROJECT_TREE.contract.json` | `levels.[2].regex` widened to `^[A-Z]{4}_[A-Z0-9]{4,18}$` | Yes -- landed via the tree-index refusal |
| `org/missions/D12/NFRA/NFRA_OPSEC202609/ledger/L8_PACKET.round2.final.md` | compiled, then limb label corrected in place; sections 1-6 unchanged | Yes -- `4cef4a058c`, `514272320c` |

---

## Blockers

None BLOCKED. Two items are IN FLIGHT elsewhere and one needs a seat, all evidence-cited:

- NOT BLOCKED -- IN PROGRESS at `3.0.0_SA_CVO~Z`: L9 on NFRA_OPSEC202609 round 2.
  Evidence: `surprise-channel/adjudications/ADJUDICATION_v1.md` exists at `b16dbf8814`, and the packet's READ ack is measured at 02:30:36Z. 138 items to disposition is not late at this elapsed time, and L9 is CVO MODE, not this seat's.
- NOT BLOCKED -- NOT YET LIVE at `1.0.0_SA_CTO~Z`: `/drive` obligation 1 (round-N analysis -> one issuance same tick) has no trigger until an analysis lands FOR THIS PROJECT. One landing for NFRA_REPORT is not this project's trigger.
- NEEDS A SEAT, not an agent: the caller-migration ask has three owning lanes -- OpalETL, PartnerETL, CloudComp -- and **all three are DARK.**
  Evidence: 8 live serials measured from `liveness.json` (`MSTR~Z`, `AE_CloudOps~V`, `AE_CloudOps~Z`, `CTO~Z`, `COO~Z`, `COO~ZZ`, `CVO~Z`, `CRO~Z`); none of the three appears. This routes to `0.0.0_AB_MSTR~Z` for seating, NOT as a pitch into a dead inbox.

Three ARMED rows remain that **this seat cannot disarm by any act of its own**, carried in the packet because the drain-end read is their only carrier: `Z-S151` (FWD-4 pending Andrew's SNS confirmation click -- an SNS subscription is PENDING until the recipient confirms), `Z-S156` (any Lambda@Edge deploy in `portal-auth` rides another cell's unapplied WAF work, chained behind the now-cancelled `S-15-19`), `Z-S152` (the frozen decomposition's hold list still directs a future actor at an edge `C-19` made UNBUILDABLE -- a row, not an edit, because the spec is frozen mid-round).

---

## Current State

NFRA_OPSEC202609 lives at `org/missions/D12/NFRA/NFRA_OPSEC202609/` (PRD v0.14 `@5f4d4b894f`; decomposition v0.1.16 with 35 cell ids = 29 work cells + 6 `OP-x-*` decide-first; 31 task-order faces). **Round 2 is TERMINAL: 29 complete + 2 cancelled-with-pointer = 31 of 31, with 29 of 29 proof instances VALID at HEAD, every one re-run at this seat rather than accepted from a worker's rc.** `dep_stage` correctly reads `EXECUTING` -- `ROUND_CLOSE` is the CTO's flip on receipt of the slug, not mine. The L8 packet is `ledger/L8_PACKET.round2.final.md` @`4cef4a058c` (label corrected @`514272320c`), READ-acked by `3.0.0_SA_CVO~Z` at 02:30:36Z, and L9 is running against it (`adjudications/ADJUDICATION_v1.md` @`b16dbf8814`). The row census at the close is **165 items, 138 UNDISPOSITIONED** across BOTH channel documents, measured on `surprise-row-gate.py:677`'s own shape (`latest.items()`, keyed by ITEM, valued by the LATEST carrier) -- **138 is a ceiling on WORK, not a count of defects**, many are inert observations one adjudication row closes in a line, and the separate 47 ARMED rows naming this seat as `disarm_owner` are a DIFFERENT quantity that is not the L10 distance. FWD-10 is SERVED: the portal login signing key is rotated, `01cfa582` AWSCURRENT / `fabe94f0` AWSPREVIOUS with no `DeletedDate`, and no user was signed out. Two judgment criteria (`S10D-AC2` on genuine module REUSE, `S10E-AC6` on graceful degradation of the MFA seal key's unbounded cache) carry no verdict from any lane and are the CVO's to grade at L9. The `/drive` cron `b8af0997` is STANDING at 20m, scoped to NFRA_OPSEC202609 only (NFRA_REPORT is `2.0.0_SA_COO~ZZ`'s), and stops when the project leaves DECOMP/EXECUTING/ROUND_CLOSE or on Andrew's word.

**The next issuance is v3.** The current round finishes on the 31 orders already cut -- nothing withdrawn, no terminal order reopens -- and the next issuance uses worker subagents `0.9.0_WK_NFRA_OPSEC202609~<n>` in worktrees created from CLOUD, as ONE issuance commit carrying a `fanout: N of M chains, cap K` line.

---

## Next Steps

1. **Cut the in-lane liveness-Lambda caller-migration face as round 3's OPENING order** -- Andrew-direct msg 20760 (`@9382d107a3`, verbatim *"go with your recs on all six"*) authorised cutting the two in-lane liveness Lambdas now. Sequencing it into round 3 rather than round 2 keeps the L8 packet's "31 of 31 terminal" true while L9 is adjudicating exactly that claim.
2. **[0.0.0_AB_MSTR~Z] Seat OpalETL, PartnerETL and CloudComp** -- the caller migration is the true critical path on FWD-12 (the sign-in window cannot fill AT ANY LENGTH until callers exchange-then-present), 3 of its 5 callers are outside this project's territory, and all three owning lanes measured DARK. This is a seating ask, not a dispatch.
3. **[3.0.0_SA_CVO~Z] The slug** -- L9 dispositions (including the two judgment criteria), then the one `REMEDIATION_v<N>` to the CTO. Neither is this seat's to produce and neither is late.
4. **[1.0.0_SA_CTO~Z] The L10 read and the round-N analysis for this project** -- on its receipt of the slug, `dep_stage` flips to `ROUND_CLOSE`. `/drive` obligation 1 then fires ONE issuance in the same tick, under v3.
5. **[0.0.0_AB_MSTR~Z] Push state** -- 70 local commits ahead of `origin/SITEZ` `93ab120af1`. Pushes are the integrator's.
