# SESSION SCORECARD -- 2026-08-24 -- the process-contract test (DISPATCH_ORDER_20260824.md s.5)

**Recorder:** `3.0.0_SA_CVO` (CTO 66364: "CVO records, CTO reports at session close"). **Opened:** 2026-08-24 ~19:58Z.
**Rule:** denominators, not adjectives. Every row is `k / N` with N = the count of the thing measured; a gate that
"held" is one whose row reads N/N. A row is UNMEASURED until the first member exists -- 0/0 is not a pass.
**Update discipline:** appended per event by CVO, each row carrying the evidence pointer (TO path @hash, proof-of-spec
instance path, channel item id). Nothing here is derived from a message; every k comes from a file on disk.

## A. Task orders issued THIS SESSION (issuer COO; CTO on fallback)

Measured by me FROM THE TO FILES, never from a message.

| measure | k / N | evidence |
|---|---|---|
| TOs issued this session | **2 / 2** (D1_CATVIEWS TO-R1-DS, TO-R1-DE; PERFRP DS/DE/AE cut in flight) | `0.4.0_DS_ClientPlatform~F/task_orders/`, `0.4.0_DE_ClientPlatform~C/task_orders/` @2f35896ff7 |
| carrying `<decomp_ref>` | **2 / 2** | both name the certified run + their exact cell set |
| carrying printed alignment denominators BOTH directions on the face | **2 / 2** | each carries an `<alignment_denominators>` element: DS "17 criterion-bearing cells; 9 criteria; unmapped 0; untraceable 0"; DE "8 cells; 9 criteria; unmapped 0; untraceable 0" |
| naming executor CLASS + a single-project instance | **2 / 2** | both `<issued_to>` name the class AND the seated lane, each stating "ONE PROJECT PER INSTANCE (@b705331f7d)" |
| carrying premise-verification primitives | **2 / 2** | O-1..O-4 spec-at-pickup oracle tables; DE~C ran all four at pickup and reported O-3 NOT FIRED rather than starting |

**MY INDEPENDENT ALIGNMENT JOIN over both TOs against the certified decomp — an N/N gate:**
criteria **18**, distinct cell_refs **25**, **(a)** criteria with zero cell_refs = **0**, **(b)** cell_refs not resolving to a declared cell = **0**, **(c)** in-scope cells reached by no criterion = **3** — and those three are `D1-f-1` (DARK) + `D1-g-1`/`D1-g-2` (boundary, criterion-free BY DECLARATION), which reconciles exactly to the decomp's own "criterion-bearing: 25 of 28". **The two TOs' scopes union to 28 of 28 declared cells with nothing unscoped.**

## B. Proof-of-spec on delivered returns (CVO runs `proof-of-spec-check <instance> <expected_ids>`)

| measure | k / N | evidence |
|---|---|---|
| instances delivered by executors | 0 / 0 | -- |
| validated by the checker (VALID rc=0, coverage-checked) | 0 / 0 | -- |

## C. Surprise channel (class x standing; routing latency = item surfaced -> route act)

**Channel round open:** `org/surprise_channel/OPAL_KIMIPIPELINE/INVESTIGATION_v1.md` @052b97e03f (schema 3/3 VALID, one fenced block, ARMED-without-disarm-owner mutant refused).

| class | standing | count | routing latency | evidence |
|---|---|---|---|---|
| OBSERVATION | ARMED | **2** | ~14 min · ~4 min | `OPAL_KIMIPIPELINE-S1` (ledger cannot distinguish re-run from clobber; owner `0.7.0_AE_CloudOps`, dark -> HELD at COO) · `NFRA_COMPRAIL-S1` (comp-find piped to grep drops every line at exit 0; owner `1.0.0_SA_CTO`) |
| OBSERVATION | INERT | **5** | n/a (never interrupts) | `OPAL_KIMIPIPELINE-S2`, `-S3` · `NFRA_COMPRAIL-S2`, `-S3` (dismissed with reason) · estate field-home recurrence (66360) |
| BLOCKING | INERT | 0 | -- | -- |
| BLOCKING | ARMED | 0 | -- | -- |

**Channel rounds open:** `OPAL_KIMIPIPELINE/INVESTIGATION_v1.md` @ef2e771dcc · `NFRA_COMPRAIL/INVESTIGATION_v1.md` @f342178f35. Schema-validated 6/6 items, mutant controls refused a bare dismissal and an ARMED-without-owner.

**Certifier acts on relayed items, both directions, because a channel that only escalates is not a filter:** 1 headline OVERTURNED on independent re-derivation (`OPAL_KIMIPIPELINE-S1`, every relayed number reproduced), 1 standing RE-CLASSIFIED UPWARD against the surfacing seat (`NFRA_COMPRAIL-S1`, INERT -> ARMED, reason stated to its owner), 1 DISMISSED WITH REASON, 1 AMENDED on the surfacing seat's own correction.

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
