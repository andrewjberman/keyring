# 0.7.0_AE_CloudOps~S (lane ~S, THIRD seating) — TO-6-AE AC3: the 07:00Z scheduled fire

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE, COORDINATE

**Window:** 2026-08-28T06:04Z (seated 06:03:49Z by `0.0.0_AB_MSTR~Z`) -> 07:12Z. First log of this
seating; the prior ~S seating's log is `to9_ae_producer_package_apply_0138-0215Z.md` in this folder.
**Commits:** `28c465b93b` (runbook + TO-face pointer), `bae0325e89` (AC3 evidence + face AC3 row).
**MCP:** 6 inbound handled and ACKed (13026, 13059, 13061, 13064, 13067, 13070); 2 outbound sends,
the second to 4 recipients (3 DELIVERED / 1 QUEUED).

---

## WHAT THIS SEATING WAS FOR

Two prior sessions of this serial died. `ETFS_SATELLITES.TO-6-AE` held one undischarged criterion,
`T6AE-AC3`, that could only be measured by a ~07:00Z scheduled fire. Standing order at seating:
**make the post-fire procedure runnable by a seat that is not me, in the record rather than in broker
messages — then read the fire.**

## 1. THE FIRST ACT, AND THE DEFECT IT FOUND

The recipe was already committed on the TO face, so the shallow reading — "it is not in broker
messages, done" — was available and wrong. Tested against the only question that matters: **can a
seat holding zero context run it?**

```
recipe step 1  head-object              HAS a command.
recipe step 2  "the invocation record"  HAS NO COMMAND.
               log group name lived only in a sibling deliverable; the line to grep for only in prose.
```

Per the face's own section (b2), **step 2 is not corroboration-for-a-pass** — on the FAIL branch it is
the ONLY thing separating *the trigger did not fire* (AE lane) from *the trigger fired and the producer
did not write* (DS lane). **The step a cold seat could not run is the step that routes the
investigation.** Closed by `28c465b93b`: four read-only commands verbatim, every one RUN against the
live plane before being written down, plus one decision table folding the face's (b)/(b2)/(d)/(e) into
five rows — observation -> verdict -> LANE.

## 2. PRE-FIRE MEASUREMENTS

| what | value | why it mattered |
|---|---|---|
| anchor @06:07Z | `01:38:46Z` / `c056874e69aa` / 2196 B / 1 log stream, last event `01:39:12Z` | matched the face |
| anchor @06:55:02Z | IDENTICAL, 2 versions, 0 delete markers | the immediately-pre-fire re-read `1.0.0_SA_CTO~Z` asked for (13059) |
| upstream roster partition | `2026-08-28/page_000.json` at `06:00:46+00:00`, 34454 B | control: 08-27 at `06:00:43Z`, 34454 B |

Three reads at three instants agree, so the window flagged in 13059 is **measured closed, not assumed
closed** — the 07:00:19Z change is attributable to this fire and nothing else.

## 3. THE FIRE — VERIFICATION (actual output)

```
07:00:15.7Z  INIT_START
07:00:16.078Z  INVOKE: argv=[] event_keys=['account','detail','detail-type','id','region',
                                            'resources','source','time','version']
07:00:17.804  OK: as_of=2026-08-28 (resolved today-UTC)
07:00:18.043  OK: roster pageCount=1 totalResultCount=65 len(pagedResults)=65
07:00:18.043  OK: derived 9 member(s) of 65 roster row(s)
07:00:18.820  OK: wrote s3://opal-data-cot/platinum/satellites/registry.json (2196 bytes, 9 book(s))
07:00:18.821  RUN COMPLETE {"rc": 0, "argv": [], "dry_run": false}

head-object @07:02:29Z  LastModified 2026-08-28T07:00:19+00:00
                        ETag "df248da3c59786a4aae616c3410e1050"   (was "c056874e69aa...")
                        VersionId 9EnoqfgmUVjuTuIjc1HHeAKgGEP2iCTp
list-object-versions    3 versions, 0 delete markers, not truncated
describe-rule           cot-satellites-registry-producer-daily  cron(0 7 * * ? *)  ENABLED  bus default
body                    as_of 2026-08-28, claim "measured", source = the 2026-08-28 partition, 9 books
```

**VERDICT: `T6AE-AC3` PASS — EXERCISED. `TO-6-AE` is 5 of 5. `T5DS-AC6` MET and named in the row.**

**The discriminator became evidence.** Three seats independently flagged `event_keys` as EXPECTED-shape
and never measured. Both arms are now observed on the same function and the same log line:
`01:39:10Z argv=['--dry-run'] event_keys=['dry_run']` against `07:00:16Z argv=[] event_keys=[envelope]`.
The prediction was falsifiable and it held.

## 4. THE NEAR-MISS WORTH THE RECORD

**`ContentLength` is 2196 BEFORE AND AFTER — identical.** A scorer comparing SIZE reads "unchanged, no
scheduled fire" and files a **FALSE FAIL** against a fire that plainly happened. Only ETag /
LastModified / VersionId / version-count 2->3 separated them. The runbook's anchor named those and
never size — inherited from the face's amendment, not foresight about this trap. A same-size overwrite
is the **ordinary** case for a fixed-shape daily registry, not a coincidence. Third instrument on this
one criterion that looked discriminating and could not see the change it was asked about (the others:
`provenance`, `run_class`). Banked to memory as
`a-fixed-shape-artifact-defeats-a-length-comparison`.

## 5. MCP

Handled 13026 (COO~Z stand-down — held, sent no acknowledgement round), 13059 (CTO~Z ruling: no lane
crossing, two additions), 13061 (MSTR~Z: process truth falsifies "the owner is deaf"), 13064 (CTO~Z:
stand down the proxy read), 13067 (COO~Z withdraws 13055 in full), 13070 (COO~Z: versioning makes the
pre-fire baseline recoverable — not a closing window). Both of 13059's additions were run; addition
two was already committed before 13059 was written. Outbound: a correction to CTO~Z that the baseline
was **not** 2h15m old (re-read at 06:07Z, matched) — the number, not the method — and the 4-recipient
AC3 report.

⚠ **`3.0.0_SA_CVO~Z` is QUEUED, not delivered — no live certifier session.** Certification of AC3 and
of `T5DS-AC6` waits on that seat.

## COMPILER TOOLS

| tool | run | result |
|---|---|---|
| none | — | see below |

**Why none:** every claim in this window is a **live-plane** read — an S3 object's UTC clock and ETag, a
CloudWatch log stream's contents, an EventBridge rule's live `State`. `comp-*` model **DESIRED** state
parsed from Terraform and structurally cannot read any of the three; `comp-iam` models `(action)` never
`(action, resource)` and fails **green**. Rail markers were carried inline on every raw `aws` call.
No code or infra changed, so Rule-20 graph checks do not arise.

## BLOCKERS

**NONE at this seat.** `T6AE-AC3` is discharged and filed.

**Owned elsewhere, listed so they are not read as mine:**
- [`3.0.0_SA_CVO~Z`] certification of `T6AE-AC3` and of `T5DS-AC6` as relocated-and-discharged. Report
  QUEUED at 07:0xZ; no live session.
- [`0.0.0_AB_MSTR~Z`] two unpushed commits from this lane, `28c465b93b` + `bae0325e89`. Integrator act.

## CURRENT STATE (zero prior context)

- `ETFS_SATELLITES.TO-6-AE` (`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ETFS_SATELLITES.TO-6-AE.registry-producer-schedule.md`)
  is **5 of 5 discharged**. AC1/AC2/AC4/AC5 CERTIFIED @`324330f5f2`; **AC3 PASS @`bae0325e89`**. The
  face carries a banner at the top of `<status>`; the pre-fire text below it was KEPT, not rewritten.
- Evidence: `org/tier2_senior/0.7.0_AE_CloudOps~S/deliverables/ETFS_SATELLITES.TO-6-AE_AC3_FIRE_EVIDENCE_20260828.md`.
  Method: `..._POSTFIRE_RUNBOOK_20260828.md`. Pre-fire anchor: `..._PREFIRE_BASELINE_20260828.md`.
- The producer `cot-satellites-registry-producer` **has now written the registry successfully for the
  first time** (both earlier object versions are DS's QA hand-write, a different principal).
- ⛔ **`T6AE-AC5` is NOT exercised by this fire** — 9 members published, not zero, so the empty-publish
  path did not execute. It stands CERTIFIED on its prior evidence; this fire is not a re-derivation.
- ⛔ **Nothing was invoked all session.** Every call is head/get/list/describe/filter. The pre-07:00Z
  ad-hoc ban held to the end. No alarm, monitor, checker or notification was built.
- Push state: **LOCAL @`bae0325e89`** — MEASURED (`git ls-remote origin SITEZ` = `4477e6d8a1`, read
  07:05:44Z; HEAD not an ancestor). Perishable — re-measure before quoting.

## NEXT STEPS

- [`3.0.0_SA_CVO~Z`] Certify `T6AE-AC3`, and `T5DS-AC6` as relocated-and-DISCHARGED — the withholding
  condition is satisfied by measurement. Do **not** grant AC5 on this evidence.
- [`2.0.0_SA_COO~Z`] `TO-6-AE` has no work left; it closes on certification.
- [`0.0.0_AB_MSTR~Z`] Push `28c465b93b` + `bae0325e89`.
- [this lane] Nothing outstanding. The seat is free.
