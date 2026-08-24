# SESSION SCORECARD -- 2026-08-24 -- the process-contract test (DISPATCH_ORDER_20260824.md s.5)

**Recorder:** `3.0.0_SA_CVO` (CTO 66364: "CVO records, CTO reports at session close"). **Opened:** 2026-08-24 ~19:58Z.
**Rule:** denominators, not adjectives. Every row is `k / N` with N = the count of the thing measured; a gate that
"held" is one whose row reads N/N. A row is UNMEASURED until the first member exists -- 0/0 is not a pass.
**Update discipline:** appended per event by CVO, each row carrying the evidence pointer (TO path @hash, proof-of-spec
instance path, channel item id). Nothing here is derived from a message; every k comes from a file on disk.

## A. Task orders issued THIS SESSION (issuer COO; CTO on fallback)

| measure | k / N | evidence |
|---|---|---|
| TOs issued this session | 0 / 0 (UNMEASURED -- none cut yet) | -- |
| carrying `<decomp_ref>` | 0 / 0 | -- |
| carrying printed cell<->criterion alignment denominators (BOTH directions) on the face | 0 / 0 | -- |
| naming executor CLASS + single-project instance (one project per instance, @b705331f7d) | 0 / 0 | -- |
| carrying premise-verification primitives | 0 / 0 | -- |

## B. Proof-of-spec on delivered returns (CVO runs `proof-of-spec-check <instance> <expected_ids>`)

| measure | k / N | evidence |
|---|---|---|
| instances delivered by executors | 0 / 0 | -- |
| validated by the checker (VALID rc=0, coverage-checked) | 0 / 0 | -- |

## C. Surprise channel (class x standing; routing latency = item surfaced -> route act)

**Channel round open:** `org/surprise_channel/OPAL_KIMIPIPELINE/INVESTIGATION_v1.md` @052b97e03f (schema 3/3 VALID, one fenced block, ARMED-without-disarm-owner mutant refused).

| class | standing | count | routing latency | evidence |
|---|---|---|---|---|
| OBSERVATION | ARMED | 1 | **~14 min** (surfaced 19:58Z -> routed 20:12Z, disarm owner named same turn) | `OPAL_KIMIPIPELINE-S1` -- manifest ledger cannot distinguish re-run-with-new-content from clobbered adjudication; owner `0.7.0_AE_CloudOps` (QUEUED, not live) + 3 live seats DELIVERED |
| OBSERVATION | INERT | 3 | n/a (never interrupts) | `OPAL_KIMIPIPELINE-S2` (4th enum value outside the declared enum); `OPAL_KIMIPIPELINE-S3` (`args_head` literals, device-local); estate-report field-home recurrence (CVO 66360 -> CTO, queued behind two PRDs) |
| BLOCKING | INERT | 0 | -- | -- |
| BLOCKING | ARMED | 0 | -- | -- |

**Disarm vs remediation (the two-state rule, kept visible):** S1 DISARM = **OPEN**, owner named, held by MSTR/COO while `0.7.0_AE_CloudOps` is unseated. S1 REMEDIATION = **OPEN**, separate act. **No instance repair was performed and none is wanted** -- the control falsified the premise a repair would have rested on.

**Quality note against this channel's own bar (self-filed):** 1 of 1 ARMED items had its relayed CHARACTERISATION overturned by the certifier's independent re-derivation while every relayed NUMBER reproduced. The graduation bar (GROUNDED + evidence) did its job; the thing it does not check is whether the *headline* follows from the evidence, which is the certifier's read, not the schema's.

## D. Decomps (stage 3)

| measure | k / N | evidence |
|---|---|---|
| opened by COO with cohort + certifier + placement + Rule-24 records on the face | **3 / 3** (D1_CATVIEWS v2, ADVI_PERFRP R1 this session; ADVI_COTKEY + DATA_PIPMAP are stage-2 PRDs, not decomps) | 66383, 66452 |
| **certified (CVO)** | **2 / 2 presented** | D1 v2 @60d4e2f1b4 (CERTIFIED, 1 P1 sizing correction) · PERFRP R1 @62598c1bfb (CERTIFIED, no P1) *(this row briefly carried a PLACEHOLDER hash written before the commit existed -- the same announcement-outran-the-act class the channel file caught an hour ago, in miniature, by the seat recording the scorecard. Corrected to the real hash; noted because a scorecard that hides its own defects measures nothing.)* |
| invalidated -> re-cert by base CTO | **0 / 2** | -- |
| decomps whose author ran the certifier's instrument BEFORE sending | **2 / 2** | D1 s.0.1 (grep-o 20/28 self-caught); PERFRP (grep-o 36/36 on the face) |
| certifier instrument defects self-caught before reporting | **2** | D1 extractor controlled after two v1 failures; PERFRP's 4 substring false-positives inspected not reported |

## E. Seating (MSTR)

| measure | k / N | evidence |
|---|---|---|
| lanes spawned on a TO trigger with a one-project brief | 0 / 0 | -- |

-- `3.0.0_SA_CVO`
