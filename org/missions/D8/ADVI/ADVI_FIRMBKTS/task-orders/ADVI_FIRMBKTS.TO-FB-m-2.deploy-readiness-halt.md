# ADVI_FIRMBKTS task order -- `FB-m-2` -- DEPLOY THE PUBLISHER'S READINESS HALT AND READ ITS THREE ARMS LIVE

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_READYHALT.md</decomp_doc>
<owned_cells>FB-m-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order adds no rule, schedule or cadence; the floor schedule belongs to `FB-l-5`.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added; step 1 simulates whether the function's existing role can read the chosen signal key and stops if not.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a signal that is the Door 6 marker, a missing function CodeSha256, a halt arm whose bucket listing differs before and after, a log line that does not name the date and the signal, an unsigned pair, no recorded rollback and an unclosed ledger entry. Blindness: the record proves the three arms, not that the signal is the right definition of complete; the CTO reads that.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-m-2` (round 8, workstream READYHALT, WORLD)

STAGED. This order deploys the publisher's readiness halt (built by `FB-m-1`) and reads its three arms LIVE. It waits; it is not a standing GO. You act only after the issuer's UN-PARK AMENDMENT (in this file's record face),
which names (1) the merged `FB-m-1` commit and its chosen signal key, (2) the CTO's read of the guard, and (3) the signed never-widen pair (COO half and CTO half, commits named). Until that amendment exists, do nothing.

### 1a. Steps (once un-parked)

1. **Preconditions (read, each recorded):** `FB-m-1` is merged and its AC1 to AC3 PASS at the merged HEAD; the CTO has read the guard; the pair is signed on both halves at the current bytes.
2. **Before (recorded):** the function's `CodeSha256` and last-modified; the bucket listing count of `platinum/firm/snapshots/` and of `platinum/advisors/` (counts only); the prior VersionIds of the keys arm (a) will rewrite.
3. **Ledger** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write.
4. **Deploy:** the new function code through Terraform only (`bash .tools/safe-apply.sh`, scoped to the publisher's function resource); the plan must change the function's code hash and nothing else. Read back the new `CodeSha256`.
5. **Arm (a), complete:** after that day's gold is read complete and the dated inputs read one date D newer than the served `data_as_of`, invoke the publisher once with an empty event; read that it publishes (the three snapshots and the advisor artifacts get new VersionIds, inside the named set) and that the log shows no halt.
6. **Arm (b), the halt:** invoke the publisher a SECOND time at once (a same-day re-fire, D equal to the served date); read the response (`halted` true), the one log line (it names each dated input's date and the served date), and the listing counts again: unchanged (zero keys written). (The part-written case is proven by the unit tests; it cannot be staged live without part-writing gold.)
7. **Roll back** (the saved code hash, the prior VersionIds of the keys written) if a halt writes anything, a complete day halts, or anything outside the named set changes.
8. Close the ledger entry.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/READYHALT_RECORD.json`

The record `READYHALT_RECORD.json` has this shape (the grader checks it):
```json
{"order": "FB-m-2", "read_at": "<ISO UTC>", "signal": {"key": "data frontier: client_perf, holdings, canonical_nna (content date)", "writer": "gold chain outputs read by lambda_function.py:<line>"}, "deployed": {"code_sha256": "<the function CodeSha256>"},
 "arms": {"complete": {"published": true}, "incomplete": {"halted": true, "listing_before": 0, "listing_after": 0}, "log": {"names_date": true, "names_signal": true}},
 "pair": {"coo_half": "<commit>", "cto_half": "<commit>"}, "rollback": {"recorded": true, "how": "<the exact step>"}, "ledger_closed": true, "claim": "measured"}
```
The "incomplete" arm is the live same-day re-fire halt (the key name is the grader's).


## 2. BOUNDS

1. The act touches exactly the publisher's function code and the keys arm (a) rewrites (the named set: the three firm snapshots and the advisor artifacts), and nothing else. A resource outside them is a STOP and a BLOCKING row.
2. `terraform` only through `bash .tools/safe-apply.sh`; AWS from bash is `.tools/aws`; a deploy opens a ledger entry (`org/critical_paths/`) BEFORE the first write and closes it at completion (CLAUDE.md NEVER-2).
3. Print no secret, client name or relationship id. No invoke other than the two named arms. The marker object and the floor schedule are not touched by this order.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/
infra/aws/lambda/inf-portal-publisher/
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-m-2.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-m-2"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py readyhalt --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/READYHALT_RECORD.json</invocation><expect>^READYHALT: OK signal=.+ arms=3$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-m-2.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the code hash before and after, the three arms, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (workstream READYHALT, CTO condition C4 on `FB-l-5` act 3, msg 5536). Un-park conditions (all): `FB-m-1` merged and PASS; the CTO reads the guard and its signal; the never-widen pair for this deploy is signed on both halves (COO half authored by the issuer at the un-park). `FB-l-5` act 3 is then signed on an addendum that cites this order's record. Executor: `0.7.0_AE_CloudOps~FB1`.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-14 ~14:0xZ) -- UN-PARKED, GO once the CTO half is signed:** (1) `FB-m-1` is merged (987e2ca3f9) and complete: six tests, `GUARDDIFF: OK inserted=105 changed=0`, re-run by the issuer. (2) THE PAIR: COO half `ledger/NEVER_WIDEN_ROUND8_READINESS_GUARD_DEPLOY_COO_HALF.md` (committed with this amendment); the CTO half is his file, named at his signing. Read both halves at HEAD before step 1; if the CTO half is not at HEAD and signed, do nothing and say so. (3) THE LIVE ARMS, as the COO half names them (they replace steps 5 and 6 above where they differ): arm (b), the halt, runs TODAY after the apply (a same-day re-fire; today's publish has run, so D equals the served date; zero keys written, listing counts equal before and after); arm (a), the publish, is the FIRST organic marker-triggered run after the deploy (tomorrow's chain, about 13:00Z): do NOT invoke the publisher to hasten it (D must exceed the served date); read it. The record `READYHALT_RECORD.json` is completed when that run is read; until then report the apply and arm (b) to `2.0.0_SA_COO~B1` in one message and wait. Branch B is in the COO half (a wrong halt on a complete day). (4) The signal in the record: `signal.key` = `data frontier: client_perf, holdings, canonical_nna (content date)`, `signal.writer` = the gold chain outputs read by the guard (cite `lambda_function.py` lines from `READINESS_SIGNAL.json`). No criterion changed. Status pending.

<status>pending</status>
<round>8</round>
<workstream>READYHALT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-m-2</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
