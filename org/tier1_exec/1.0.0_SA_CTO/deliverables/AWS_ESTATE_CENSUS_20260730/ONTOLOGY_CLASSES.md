# Ontology classes — the recurring knowledge-kinds, as captured

> **Canon alignment:** these classes are not a rival ladder. Group A = material for the
> **vertical overlay + D3 contracts** (sovereign legislation); Group B = **C0/C1/C2 population
> gaps in the map**; Group C = **plane/measurement errors** under the intent-denominator law.
> Per-class mapping: `CANON_ALIGNMENT.md`. Changes to canonical vocabulary route through the
> rule-bank ratification chain — this file PROPOSES, it never legislates.

Each class = a KIND of knowledge that closed an instrument-vs-ruling delta, or a KIND of
instrument failure that manufactured a false verdict. One line in `20_rulings/RULINGS_LEDGER.jsonl`
cites its class in `instrument_delta_class`. **This list is the product.** Grouped; dated by first
capture; all 2026-07-30 (session 1) unless noted.

## A. Knowledge only the sovereign holds (instruments structurally blind)

| Class | First specimen | The knowledge |
|---|---|---|
| **ownership-invisible** | `andrew@fideles.capital` SES identity | No instrument models WHOSE a domain/asset is. "The estate has instruments for what is DEPLOYED and zero for what is OURS" (Rule 23 lineage) |
| **external-party-role** | patricia (IAM user + SES), mike | Instruments see a grant; only Andrew sees a working relationship |
| **person-roster** | 16x @opalinvest.com SES identities | Staff address vs relic is a personnel fact, not a config fact |
| **demo-prop** | opal-data-demo (27GB frozen, zero readers) | A frozen, reader-less artifact whose frozenness IS its function |
| **parked-vs-dead** | opal-data-imo + find-insure quartet (59d dormant) | Dormancy length cannot distinguish a paused initiative from an abandoned one |
| **risk-tolerance** | 30d snapshot retention KEPT | Retention length is a business risk judgment no instrument can derive |
| **priority-ranking** | debris sweeps DEFERRED | Only the owner prices cleanup against opportunity cost |

## B. Structure instruments COULD see but currently don't (whitelist/model gaps)

| Class | First specimen | The structure |
|---|---|---|
| **generator-vs-leaf** | 1,016 snapshots + 312 AMIs = ONE Lambda's rotation | Model the GENERATOR + a cohort node (count/retention/cost), never the leaves. Leaf-indexing rotation output is how AWS's own inventory drowned |
| **purpose-expiry** | 5 "pre-delete insurance" snapshots, 55d past their deletions | A resource created AS INSURANCE carries an implicit expiry nobody tracks. Wants `expires`/`insurance_for` properties |
| **zero-edge-four-causes** | the 8 edge-less buckets | Graph silence = code-written(edges exist) / deploy-tool-written / service-written / nobody. Three of four silences are ALIVE. Wants `writer_class` property |
| **abandoned-service-archaeology** | 4 SLRs (RDS/OpenSearch/AOSS/SMSVoice) | An SLR outlives the last resource of its service and forges "in use" forever after |
| **reaper-scope** | 4 "orphan" daily snaps that self-clean | Debris-vs-self-cleaning is decided by a reaper's tag scope, invisible without reading the reaper |
| **out-of-band-deploy** | 4 unmapped Lambdas (news trio + inf-silver-chain) | A Lambda deployed outside the canonical pipeline is invisible to CI drift detection precisely because the map IS the census |
| **superseded-in-place** | opal-data-smartx-v2 (live flow moved to assets monolith 06-01) | An estate can be replaced without being retired; the successor's health masks the predecessor's death |

## C. Instrument failure modes (the instrument manufactured the finding)

| Class | First specimen | The mechanism |
|---|---|---|
| **premise-propagation** | "double-covered backups" → Andrew's AMI-only GO | An unverified agent claim became the premise of a sovereign ruling that returned as an execution order; the volume-grain join refuted it at the last gate. NOT executed |
| **null-reads-as-empty** | ajb-workflow "0 objects" (held 5) | A probe returning null for both empty and broken; null read as zero. Partial success (1/5 CRLF survivor) would have read as "done" without per-item verify |
| **break-on-mixed-level** | inf silver/ "cold since 05-05" (wrote 4x that day) | Traversal rule (stop at a level holding objects+subdirs) manufactured a dormancy verdict; one 05-05 root parquet spoke for 12 live subdirs |
| **cw-metric-absent** | opal-data-schwab size = "no datapoint" (bucket demonstrably full) | CloudWatch storage metrics can silently lack datapoints for a real bucket; absence-of-metric read as absence-of-data |

## A-continued: from the semantic-notes pass (2026-07-30 evening)

| Class | First specimen | The knowledge |
|---|---|---|
| **name-encodes-history** | opal-data-bd ("bd"=Black Diamond, actually 49 Financial) | A name fossilizes its FIRST USE and misleads every later reader with authority. Instruments read names as semantics; names lie |
| **migration-in-flight** | bd/inf/cot → assets consolidation, "mid-migration as of today" | An estate can be instrument-healthy (daily writes, full event spine) while sovereignly scheduled to disappear into a successor. Target state lives only in declarations. Phase-inverse of superseded-in-place |

## Cross-cutting law (earned twice in one session)

**Silence is one symptom with many causes, and an instrument renders all of them identically.**
The world model's job is to make the causes distinguishable — `writer_class`, `generator`,
`expires`, `owner`, `business_function` — so that the next census never again has to ask a human
whether silence means dead.

## A/C addendum — batch 3 (2026-07-30)

| Class | First specimen | The knowledge |
|---|---|---|
| **zombie-flow** | opal-market-update: fred writes DAILY, sovereign rules delete | Activity is not purpose — a producer keeps a corpse warm indefinitely. The clean inverse of false-dead: instruments read ALIVE by flow while the function is null. Detection requires a D3 purpose record, not a D2 cadence read |
| **twin-estates** | opal-data-pm vs opal-data-portfolio | One product, one lambda family, two stores — instruments cannot say which is canonical; only function-level investigation can |

## Addendum — from the 0.7.0 schwab behavior map (2026-07-30)

| Class | First specimen | The knowledge |
|---|---|---|
| **pin-to-last-partition** | wsd-49f-partner-held-etf-daily frozen at rps date=20260723 (+ build_canonical_daily.py, same shape) | Consumers do not FAIL when their producer dies — they pin to the last partition and answer confidently forever. No errors will exist. Detect by frontier comparison (consumer source vs monolith), never by log anomaly |
| **applied-despite-hold** | canonical-schwab-xref-success: TF HELD banner (runner-trigger.tf:13-16), applied anyway; 0 invocations/30d | A written hold is not a gate. The rule waits on an event nothing emits; every config read says GREEN. Only the invocation metric distinguishes idle-between-events from never-once-woken |

CORRECTION NOTE: my earlier "temporal-incoherence: crons at a stopped box" specimen was FALSE
(two-box conflation, retracted in the ledger); applied-despite-hold replaces it.
name-encodes-history claimed its own author: the name-scoped sweep missed the real SI2 box
(quartz-si2-spike carries no "schwab" in its name).

## Addendum — batch 4 + mdpf condemnation (2026-07-30)

| Class | First specimen | The knowledge |
|---|---|---|
| **estimate-shadowing-exact** | wsd-49f partner-held-ETF ESTIMATE feeding MDPF while {bd-49f,inf,cot}-etf-ownership-daily measure ACTUAL holdings | An agent built an estimator for a quantity the estate measures exactly; the estimate circulates as measurement. Detection: for every derived quantity, ask whether an exact source exists upstream. Andrew's name for the genus: "cruft and agentic slop" |
| **unallocated-instrument** | opal-schwab-d4-access-logs (armed 07-17, no project, no TF) | An agent-armed measurement device with no allocation record is indistinguishable from cruft until its SOURCE side is read (get-bucket-logging revealed it mid-measurement on the decommission target) |

## Addendum — DDB layer close (2026-07-30)

| Class | First specimen | The knowledge |
|---|---|---|
| **empty-is-success** | opal-inf-launch-locks (TTL-enabled mutex, 0 rows) | For locks, throttles and queues, ZERO ROWS IS THE HEALTHY STATE. The exact inverse of the false-dead default, and invisible to any row-count heuristic |
| **ttl-discriminates-empty** | launch-locks (TTL on) vs pm-snapshots (TTL off), both 0 items | TTL-enabled emptiness = ephemeral-by-design (KEEP); TTL-disabled emptiness = never-adopted (candidate). One `describe-time-to-live` call separates two opposite verdicts |
| **sample-data-scaffold** | opal-firms 'Smith Wealth Management' / opal-offices 'Boston Office' | A table can be plausibly schema'd, non-empty, and entirely fictional. Row count and schema both read healthy; only the VALUES betray it -- and the join to real users fails |
| **proto-survives-product** | trade-users vs the live trade-submission tables | An early version's tables outlive it INSIDE the successor's name family, so a family-prefix teardown sweeps live product tables |
