# ROUND-1 ANALYSIS -- LGIC_NAMING

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-14 ~19:1xZ · **Step:** L10.

**Input:**
- `3.0.0_SA_CVO`'s slug, msg 96698.
- The CVO's record `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md` @`810ecf6cf2`.
- Adjudication carriers `C-S3`..`C-S10` in `surprise-channel/adjudications/ADJUDICATION_v2.md` @`2c07f8dee3`.
- The 20 remediation rows, HELD by the gate at `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_REMEDIATION_HELD_BY_GATE_20260914.md` @`d1470296de`.
- `2.0.0_SA_COO~G`'s drain-end read, msg 96660.

**Order:** the CVO's slug came first, then this analysis. `2.0.0_SA_COO~G`'s recut follows as ONE issuance, after
both halves of PRD v1.5 are signed.

**Outputs of this L10:** this document; `org/standards/NAMING_SCHEMA.json` v1.5 (the rulings, as data); PRD v1.5
(THE SCHEMA gains S14; brief half only); the grade schema's criterion pattern (`C-S10`).

---

## 0. WHAT ROUND 1 DELIVERED -- SAID FIRST

- **Orders:** 14 of 14 drained. 11 read `complete`, and 3 hold a VALID proof whose criterion printed FAIL (LN-l-3,
  LN-e-3 and LN-e-5; `proof-of-spec-check` rc=0 on each, read 18:1xZ, msg 96664).
- **Rows:** 23 new, all dispositioned: 3 DISMISSED_WITH_REASON and 20 GRADUATED. Carrier-less rows: 0 of 33.
- **L9:** 4 of 4 judgment criteria MET. F1-J1, G1-J1 and H3-J1 are MET with a named qualification; T1-J1 is MET.
- **What the round measured is real.** The three FAILs are measurements of the schema and of the round's own cut, not
  worker faults. Section 1 grades each outcome against its own ENDPOINT text.

## 1. THE OUTCOMES -- GRADED AGAINST THEIR OWN TEXT

| outcome | grade | why, from the ENDPOINT text | disposition |
|---|---|---|---|
| FWD-1 | **NOT REALIZED** | ACCEPT: two people each write "the identical name". The namers matched 9 of 18. The 9 differences sit in four slots the schema left open (`C-S5`) | RULINGS FN1-FN4, P1, SC1 and SY1 (s.2); the namers re-run on v1.5 |
| FWD-2 | **NOT EVALUATED** | ACCEPT: "someone who has never seen this estate". Every worker preloads the workspace CLAUDE.md and the auto-memory, so no blind cell was blind (`S12`). The question also asked "the firm or the product", where DONE WHEN asks for "the firm" | RULINGS Q, R, B and C (s.3); re-cut |
| FWD-3 | **REALIZED, with a named qualification** | DONE WHEN: one rule catches every system of one firm. One pattern per firm catches 68 of 68 canonical forms, with 0 cross-firm (`C-S9`) | Qualification: LN-f-1's shape has no RAISE slot (`W1-S5`, `2.0.0_SA_COO~G`'s, before LGIC_ENFORCE E9 reads the list). Live names read 12 of 68 today, because the firm comes first. That sizes LGIC_ENFORCE's fence exemptions and is not this outcome's failure: the schema moves no name (S13) |
| FWD-4 | **NOT YET REALIZED (5 of 6)** | ACCEPT: an address in any location is understood "the same way with nothing new to learn". The one miss is the code tier (`C-S7`). The .tf notice (LN-l-1) meets the "older description says replaced" clause | RULING K (s.4); the reader re-runs |
| FWD-5 | **EXACT, NOT YET COMPLETE** | ACCEPT: the same answer "for every one, including the correct name". The graders agree 85 of 85, but 48 of 68 canonical forms carry `{system}` (`W1-S3`), and AWS-fixed names RAISE by shape (`W1-S4`) | RULINGS PH1 and AW1 (s.5). Completeness is carried to LGIC_ENFORCE as a dependency |
| FWD-6 | **REALIZED** | APPLIED: the ranked list exists and every entry states its cost (T1-J1 MET) | none |

## 2. FWD-1 -- THE FOUR OPEN SLOTS, RULED (data: NAMING_SCHEMA.json v1.5)

The rows name the slots: the function/purpose token (`W2-S1`, `W3-S2`, `W5-S2`: 7 of the 9 differences), the entity
partition token (`W2-S2`, `W3-S1`: i13), GLOBAL or PRODUCT scope (`W2-S3`, `W3-S3`: i14), and vendor-as-system on a
derived tier (`W2-S4`, `W3-S3`: i15).

- **FN1 -- the function.** Where the item DESCRIBES the action with a verb, the function is that verb in its base form
  (publish, fetch, read, build, download). An agent noun is always written as its verb, however the item phrases it
  (publisher -> publish, exporter -> export, scanner -> scan), because the kind already names the thing. Where the
  item NAMES the process or subject as a noun phrase (the SmartX platform export, the Orion ingest, the price-refresh
  queue, pipeline alerts, delivery status), the function is that phrase as named, kebab-case, ONE token (as
  silver-chain). A kind word (queue, host, topic, table, alarm) is never written in the function slot.
- **FN2 -- the qualifier.** Written after the function: the TIER (bronze, silver, gold, platinum) or the named TABLE the
  action acts on, when the item names one. Any other object (figures, files, data, session data) is not written. A leg
  or an environment (dev | prod) stays a qualifier, as before.
- **FN3 -- an alarm's condition.** A CW_ALARM's qualifier is its condition noun (failure, error, latency), always
  written.
- **FN4 -- a secret's purpose.** The credential's kind (credentials, token, key, password, certificate), preceded by
  the interface it opens when the item names one: `api-credentials`. An IAM policy's purpose is the function slot, so
  FN1 and FN2 apply to it as one compound token (`read-gold`).
- **P1 -- the entity partition.** `{entity}` is the KEY COLUMN's name as the table carries it: `advisor_id=A123`, just
  as `date` is the column in `date=YYYY-MM-DD` (the hive form).
- **SC1 -- the key's scope is its audience.** A FIRM when the data is one firm's; `global` when every firm shares it. A
  PRODUCT key is a scope only beneath a VENDOR source (a feed for the product: `pathfinder/etfs`), never beneath
  itself as the source: `mdpf/global/...`, never `mdpf/mdpf/...`. This agrees with the spine's seed, where a product is
  a scope only beneath a vendor source.
- **SY1 -- a one-vendor build.** A resource that builds a firm's data from ONE vendor's feed is that vendor's
  integration at every tier it builds (`orion-inf-build-gold-profile`). A resource that combines feeds takes the
  PRODUCT or PLATFORM_SUBSYSTEM that owns the combination.

**The determinism dry-run.** Every one of the 18 items, read under v1.5 by this seat before landing the rulings. The
first draft ("the function is the verb") would have broken two AGREED names (`platform-export`, `pipeline`), and FN1's
noun-phrase clause exists because of that.

| item | the ruled name | namer A | namer B | the rule that decides |
|---|---|---|---|---|
| i01 | `mdpf-cot-publish-lambda` | differs | = | FN1 (the item says "publishes"; figures is not a tier or table, FN2) |
| i02 | `blackdiamond-49f-fetch-role` | differs | = | FN1; FN2 (session data is not a tier or table) |
| i03 | `orion-inf-ingest-daily` | = | = | FN1 (noun: the Orion ingest) |
| i04 | `schwab/49f/api-credentials` | = | differs | FN4 |
| i05 | `opal-data-cottonwood` | = | = | S2 |
| i06 | `eclipse/inflection/silver/account_holdings/date=2026-09-14` | = | = | S1 |
| i07 | `mdpf-read-gold-policy` | differs | = | FN1, FN2 (tier gold), FN4 (policy); S5 (shared, no scope) |
| i08 | `etfs-price-refresh-dlq` | = | = | FN1 (noun: the price-refresh queue; queue is a kind word) |
| i09 | `mdpf-demo-publish-failure-alarm` | = | differs | FN1 (noun: the publish), FN3 |
| i10 | `smartx-49f-platform-export-weekly` | = | = | FN1 (noun: the SmartX platform export) |
| i11 | `pathfinder-etfs-ingest-task` | = | = | FN1 (noun: the Pathfinder ingest) |
| i12 | `blackdiamond-cot-download-document` | = | = | FN1; FN2 (files is not written) |
| i13 | `mdpf/49financial/platinum/advisor_books/advisor_id=A123` | = | differs (RAISE) | P1 |
| i14 | `mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz` | = | differs | SC1 |
| i15 | `orion-inf-build-gold-profile` | differs | = | SY1; FN1, FN2 (tier gold) |
| i16 | `mdpf-cot-export-sg` | differs | = | FN1 (exporter is an agent noun) |
| i17 | `etfs-pipeline-alerts` | = | = | FN1 (noun: pipeline alerts) |
| i18 | `mdpf-inf-delivery-status-table` | = | = | FN1 (noun: delivery status) |

- **Read:** each of the 9 differences now has exactly one ruled answer (A-side on i04, i09, i13 and i14; B-side on i01,
  i02, i07, i15 and i16), and none of the 9 agreed names changes.
- **Instrument:** a hand reading by the rules' author. It is a determinism check of the text, not FWD-1's grade. FWD-1
  is graded only by the namers' re-run, blind to each other, on v1.5.

## 3. FWD-2 -- NOT EVALUATED; WHAT THE RE-CUT MUST CHANGE

- **RULING Q -- the question is the FIRM, or none.** FWD-2's DONE WHEN and ACCEPT both ask for "the firm". The cut asked
  for "the firm or the product" while N3_KEY answered "the scope token". The reader's question becomes: point at the
  part of the name that is the firm, or answer none. The key becomes firm-or-none (i07, i08, i11, i14 and i17 read
  none). The headline's "which is the system ... and which says what kind" is proved by position in FWD-1's names; the
  exercise grades the firm, as DONE WHEN says.
- **RULING R -- a clash is two REFERENTS, never two roles.** FWD-2's own example is one abbreviation meaning "both a data
  vendor and a client firm". `etfs` as the system of `etfs-pipeline-alerts` and the scope of `pathfinder-etfs-ingest-task`
  is ONE referent (the ETF product) in two positions, which FWD-2 says position resolves. E5-AC2 is re-cut to count
  only a token read as two different referents.
  - **Checked:** under Q and R, the key-perfect reader marks cot, 49f, inf, cottonwood, inflection, demo and
    49financial as firms and none elsewhere. None of those tokens is read as another referent in any of the 18 names,
    so E5-AC1 and E5-AC2 are jointly satisfiable. That is exactly what `S13` measured was not true of the round-1 cut.
- **RULING B -- a blind reader is not a v3 worker.** `S12` measured that a worker subagent starts with the workspace
  CLAUDE.md and the auto-memory in context, so it has "seen this estate" before its first tool call.
  - The blind cells (the reader, and any cell whose criterion says blind to the estate) are seated as a CLEAN-CONTEXT
    session whose working directory is a bare folder OUTSIDE the workspace, holding only the cell's input file. The
    COO launches it and reads its answer file.
  - **Blindness is PROVED, never assumed:** the exercise carries one canary item whose answer needs a fact stated only
    in the workspace CLAUDE.md or the memory (for example, which short token is refused in every slot). A seat that
    answers it from knowledge is not blind, and the FWD-2 cells stop there.
  - **If the canary shows a leak,** FWD-2 is not measurable inside this fabric. It returns to 1.0.0_SA_CTO, and a human
    reader new to the estate is put to Andrew, because FWD-2's DONE WHEN names "someone new to the estate".
  - This is a new way to seat a cell. It is stated here as the mechanism, and it is surfaced to Andrew with this
    analysis, not taken as settled by it.
- **RULING C -- a blind cell does not read the channel** (`W6-S3`). It writes any surprise into its own deliverables
  file, and the COO files the row at the drain. The worker face says so. Minting a row id from the channel is what
  exposed the reader to the namers' choices.

## 4. FWD-4 -- THE CODE TIER IS ADMITTED; THE BRIEFING WAS THE GAP

- **RULING K.** `key.code` already maps onto the ONE layout: `{source}/{scope}/code/{built_tier}/{file}` is the
  five-segment string with tier = `code`, table = the tier the code builds, and partition = the file as a named leaf.
  NAMING_SCHEMA.json :40 and :41 say so today. The reader's reason for a3 ("the table slot holds a second tier word
  (gold), and there is no partition") is a reader who was not told that under tier `code` the table slot names the
  built tier and a named leaf fills the partition.
- **So FWD-4 needs no schema change.** The layout briefing states what each slot holds under every tier, code included,
  and LN-l-2 and LN-l-3 re-run on it. Teaching the one layout completely is learning the layout, not learning a new
  location, so FWD-4's "nothing new to learn" is kept.

## 5. FWD-5 -- EXACT; WHAT COMPLETE NEEDS

- **RULING PH1 -- a placeholder is a typed gap, never a guess.** A canonical form may carry `{system}`, `{source}`,
  `{scope}` or `{cadence}` only for a slot the name does not carry. Each is filled from its source: `{system}` from
  the identity registry's resource-to-system rows (LGIC_ENFORCE), `{source}`/`{scope}` from the bucket, `{cadence}` from
  the schedule. The verdict stays exact (a firm in the system slot is OUT-OF-PATTERN with certainty), and the grade
  stays `(name, type)` (row S10's line holds).
  - **FWD-5's "correct name" is complete for a name only when no placeholder remains.** For the 48 firm-first roles
    that needs LGIC_ENFORCE's registry. That is carried as a DEPENDENCY on LGIC_ENFORCE (held by `2.0.0_SA_COO~G`), not
    hidden as a pass.
- **RULING AW1 -- AWS-fixed names are outside the grade's domain,** like the NOT GRADED types: excluded, never a fourth
  verdict.
  - An AWS-managed IAM policy is identified by its ARN's account field `aws`, read from the node and never from the
    name (`ReadOnlyAccess` carries no prefix).
  - By name: the SECURITY_GROUP `default`; the LOG_GROUPs `RDSOSMetrics` and those beginning `aws-waf-logs-` or
    `/aws/ecs/containerinsights/` (`W1-S4`'s measured set: 1 of 26, 9 of 417 by prefix plus ReadOnlyAccess, 4 of 264).
- **The step field** (`W5-S5`): the N6 answer format gains a step column. That is `2.0.0_SA_COO~G`'s, at the recut.
- **G1-J1's qualification stands as the CVO wrote it.** Byte-identical answer files cannot rule out a sibling read on
  disk, and the graders' differing result files are the discriminator the CVO weighed. No re-run is ruled for FWD-5's
  exactness.

## 6. THE L10 PRECONDITION -- THE THREE ORDERS' STATUS, AND THE GATE

- **RULING T -- the three orders are terminal, and their status word says so.** `2.0.0_SA_COO~G` flips LN-l-3, LN-e-3
  and LN-e-5 from `pending` to `complete`. Each status line points here: the criterion's FAIL is the round's
  measurement, graded at L10 by this analysis, and the proof instance is VALID. The orders' "a flip while a row is FAIL
  withdraws your own grant" was addressed to the WORKER, who correctly did not flip; the issuer flips on this ruling.
  - With those three terminal, the CVO's held remediation document lands at the channel path unchanged, as the CVO's
    slug says, with no second message.
- **The carrier gap, PARKED with its owner and condition.** `.tools/surprise-row-gate.py`'s `_open_tos_for_project`
  (`:787-814`) reads the `<status>` word, while the spine reads terminality "from the proof-of-spec instances at HEAD and
  never from a `<status>` field" (`:487-488`). Where they differ the spine wins, so the gate is the defect.
  - A strict alignment would turn every legacy order that predates proof instances non-terminal on other projects, so
    it is not a same-turn edit.
  - **Owner:** 1.0.0_SA_CTO. **Condition that moves it:** after this round's recut is issued. The fix reads the proof
    instance where one exists, keeps `<status>` for an order that predates proof instances, and is proved on a doctored
    pair (a VALID-instance order reading `pending`, and an INVALID-instance order reading `complete`).
- **C-S10 -- FIXED this turn.** The grade schema's `criterion` pattern widens from `^[A-Za-z0-9]+-AC[0-9]+$` to
  `^[A-Za-z0-9]+-(AC|J)[0-9]+$`, so the `-J` ids every order names are accepted. Its own description already said "the
  criterion id as the task order names it". Commit in the send.

## 7. THE RECUT -- `2.0.0_SA_COO~G`'s ONE ISSUANCE, AFTER BOTH HALVES OF v1.5 SIGN

What each re-cut cell must reach. The cells, their split and their order are the COO's.

1. **The clean-context seat and its canary** (RULING B). This comes before any FWD-2 cell.
2. **FWD-1:** LN-e-1 and LN-e-2, the two namers, re-run on NAMING_SCHEMA.json v1.5, blind to each other; then LN-e-3.
3. **FWD-2:** LN-e-4, the reader: the firm-or-none question (Q), in the clean-context seat (B), with no channel read
   (C). Then LN-e-5, the scorer: the key firm-or-none, and E5-AC2 counting referents (R).
4. **FWD-4:** LN-l-2, the reader, on a layout briefing that states each slot under every tier, code included (K); then
   LN-l-3.
5. **FWD-5:** the N6 answer format's step column.
6. **FWD-3:** LN-f-1's third disposition (RAISE, with its step), before LGIC_ENFORCE's E9 consumes the list (`W1-S5`).

## 8. NOT RULED HERE

- **The clean-context seat as a standing mechanism.** It is surfaced to Andrew with this analysis; this document uses it
  for this round's blind cells only.
- **LGIC_ENFORCE's registry rows.** FWD-5's completeness waits on them (PH1); the registry is LGIC_ENFORCE's (`W1-S2`,
  cell E2).
- **The sequence.** Unchanged.
