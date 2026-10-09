# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 5 (FWD-4 acceptance and FWD-5's one real narrowing)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-10-09.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` @`20c2fcabe8` (the ENRICHMENT LIST,
E1-E3) and the FWD-4 ruling `ledger/CTO_RULING_FWD4_OWNER_OF_RECORD_20261009.md` @`fa8ec0e726`.

Rounds 1-4 stay in place so their instances keep resolving. This is a fifth file, not an edit.

---

## 1. THE RECTANGLE -- THREE ENRICHMENT ITEMS, FOUR ORDERS

| cell | analysis item | outcome | issued to | the act |
|---|---|---|---|---|
| `IAM-v-1` | E1 | FWD-4 | `0.7.0_AE_CloudOps~Z` | **ACCEPT ROWS 8 AND 10.** The owner of record writes its own acceptance onto rows 8 (`opal-data-refresh-lambda-role`) and 10 (`portal-auth-lambda-role`) of `GOVERNANCE_DISPOSITION.md`. The adopting Terraform stays INERT at `zz_adoption_candidate.tf.proposed`; applying it is a separate WORLD act under its own pair and is NOT this cell. |
| `IAM-v-2` | E2 | FWD-4 | `0.7.0_AE_CloudOps~Z` | **ACCEPT THE OTHER TEN, PLUS A PER-FAMILY PLAN.** The same lane accepts rows 1, 2, 3, 5, 6, 7, 9, 11, 14 and 16 and writes one adoption (or, for row 7, retirement) plan per family. No apply this round. |
| `IAM-v-3` | E3, half 1 | FWD-5 | worker `0.9.0_WK_NFRA_IAMROLES202609~13` | **PREDICT BEFORE THE CHANGE.** Pick ONE never-used permission on ONE Terraform-declared role from the round-4 population, run the existing pre-flight instrument on it, commit the prediction, the exact narrowing as a patch and the rollback. Nothing is applied. |
| `IAM-v-4` | E3, half 2 | FWD-5 | `0.7.0_AE_CloudOps~Z` | **NARROW AND READ THE OUTCOME.** Under a signed never-widen pair, apply v-3's patch with `safe-apply`, read the result against the prediction, and keep the rollback ready. |

**The issuer's two rulings inside its own decomposition** (canonical-drive obligation 7; no gate limb grades a
decomposition):
1. **E3 is split into two orders.** The prediction has to exist, committed, BEFORE the change; that is the bar's
   own word ("checked in advance"). And the pair cannot name a blast radius until the role and the permission are
   chosen. So the check (v-3) and the act (v-4) are two orders on one chain.
2. **E3's apply half goes to the CloudOps lane, not to a worker.** The analysis issues E3 to "a worker, under
   `2.0.0_SA_COO~ZI`". The prediction half stays with a worker. The apply is an IaC change on a live role, and it
   goes to the seat that owns `safe-apply` and the deploy ledger (CLAUDE.md NEVER-2 and NEVER-9). That seat is also
   FWD-4's owner of record.

**Mapping, binding for every later reader:** E1 = `IAM-v-1`, E2 = `IAM-v-2`, E3 = `IAM-v-3` + `IAM-v-4`.
`CELL_ID_RE` from `.tools/proof-of-spec-check.py`: `IAM-v-1`, `IAM-v-4` match=True; positive control `IAM-u-3` True;
negative control `v-1`, `IAM-v-` False.

**NOT IN THE RECUT, per the analysis:** FWD-1, 2, 3, 6, 7 and 8 are REALIZED and are not re-cut. Z-S17 and Z-S18 go
to `2.0.0_SA_COO~C` and do not hold this project.

---

## 2. THE BATTERY, AT ROUND-5 VINTAGE (2026-10-09, base `e9bda7b982`)

```
comp-iam           RUN, `bash .tools/comp-iam stats` from the main checkout: 214 IAM roles parsed / 196
                   services / 1154 operations (unchanged since round 4). v-3 reads it to confirm the
                   candidate role is DECLARED in Terraform.
comp-schedule      RUN, `python .tools/comp-schedule --budget 220`: BUDGET REACHED, 1 of 6 carriers,
                   C1=23, C2=22 PARTIAL (0 of 22 scanned), C3-C6 NOT-SCANNED, rc=3. ANSWER-STATE
                   PARTIAL_OR_BLIND -- not read as clean. v-4 reads `.open_deploys/` for its module
                   itself before opening its own ledger entry.
comp-adversary     the recut is taken as GIVEN; re-derived premises 3 of 3: the 16-row table and its
                   owner fields (12 NO-ACCEPTING-SEAT, 3 1.0.0_SA_CTO~Z, 1 DECLARED at the base), the
                   INERT candidate (blob b3a1298d6b, 110 lines, adopts rows 8 and 10 by `import`), and
                   the round-4 bundle (blob 3ac4deb7f6, 280 roles, 1486 never-used rows).
pre-flight         round-2 instrument deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/preflight-blast-radius.py,
instrument         blob bd7620790c6884d55969779812bebe9ba7565355; it composes comp-iam-usage
                   permission-cold and reach-check (simulate-principal-policy). It is READ-ONLY.
comp-blast         DEFERRED TO v-3: the module the narrowing touches is unknown until v-3 picks the role.
                   v-3 runs comp-blast on that module and records it in PREDICTION.md.
```

---

## 3. BOUNDS -- what no cell in this round may cross

```
C-NO-ACCESSDENIED     ONE permission on ONE role, in v-4 only, under a signed pair, with a named rollback.
                      v-1, v-2 and v-3 narrow, revoke, detach and apply NOTHING.
C-TWO-REMEDIES        v-1 and v-2 move GOVERNANCE (owner fields) only; v-3 and v-4 move PERMISSIONS only.
                      No cell does both.
PRODUCTION ROLES      v-3 does NOT pick rows 8 or 10, nor any role a portal or client login path assumes.
INERT STAYS INERT     zz_adoption_candidate.tf.proposed is not renamed, edited or applied this round.
C-ANALYZER-PRICED-FIRST + G-25   NO AWS Access Analyzer.
G-21                  no alert, alarm, SNS, SES send, notification, freshness checker, monitor or schedule.
INSTRUMENTS ARE RUN   .tools/ and every other worker's directory are read surfaces.
NOT REWRITTEN
FROZEN SPEC           mid-round the PRD and this rectangle do not move; a bound that seems wrong is a
                      surprise ROW, and the work goes on.
```

---

## 4. DEPENDENCY EDGES

```
IAM-v-1  <- (none)
IAM-v-2  <- IAM-v-1    same assignee, same file (GOVERNANCE_DISPOSITION.md); sequential, never concurrent
IAM-v-3  <- (none)
IAM-v-4  <- IAM-v-3 complete AND both never-widen halves SIGNED
            (ledger/NEVER_WIDEN_ROUND5_FWD5_NARROWING_CTO_HALF.md + ..._COO_HALF.md, each naming the
            role, the action, the blast radius v-3 predicted and the rollback)
```

**WRITE SURFACE**

```
IAM-v-1   deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md (rows 8, 10 only)
          + deliverables/0.7.0_AE_CloudOps~Z/
IAM-v-2   the same file (the ten other unowned rows) + deliverables/0.7.0_AE_CloudOps~Z/
IAM-v-3   deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/   only
IAM-v-4   deliverables/0.7.0_AE_CloudOps~Z/fwd5/ + the ONE Terraform file v-3's patch names, added to
          its <paths> by an issuer amendment when v-3 drains, before its GO
```

v-1 and v-2 share one file and one assignee, so they are one chain, not two. The append-only surprise channel is
shared by construction and resolves as a union by row id at the drain. Minimum chain partition = 2, so
`fanout: 2 of 2 chains, cap 8`.

---

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD

**(i) MECE over a DECLARED domain.** Domain = the analysis's enrichment list, E1-E3. E1 -> v-1, E2 -> v-2,
E3 -> v-3 + v-4. 3 of 3 items covered, 0 uncovered; 4 orders, 0 orphans. The 16 rows partition as
rows 8 and 10 (v-1), rows 1, 2, 3, 5, 6, 7, 9, 11, 14 and 16 (v-2), rows 4, 12 and 15 (owned by
`1.0.0_SA_CTO~Z`, untouched) and row 13 (DECLARED, untouched): 2 + 10 + 3 + 1 = 16.

**(ii) SAME GRAIN.** v-1 and v-2 are one acceptance per row; v-3 and v-4 are one permission on one role.

**(iii) INTENT COHERENCE.** Two axes kept apart (C-TWO-REMEDIES): governance (who owns a role) for v-1 and v-2,
permissions (what a role may do) for v-3 and v-4.

**(iv) STATE COHERENCE.** v-1 and v-2 move owner fields from `NO-ACCEPTING-SEAT` to the lane's serial; they do NOT
move any role into Terraform. v-3 moves FWD-5 from *instrument exists* to *a prediction on record*; it does NOT
change AWS. v-4 moves one grant; it does NOT move custody, and it does NOT touch any other permission on that role.

---

## 6. WHAT THE ROUND CANNOT CLAIM, STATED AT THE CUT

- **FWD-4 is APPLIED-graded on owner fields, not on adoption.** 16 of 16 named closes the bar; it does not put a
  single role into Terraform.
- **FWD-5 is one narrowing.** A matched prediction on one permission is the bar; it says nothing measured about
  narrowing any other grant.
- **A prediction that does NOT match is a finding, not a failure to hide.** v-4 records it and rolls back if
  anything broke.
