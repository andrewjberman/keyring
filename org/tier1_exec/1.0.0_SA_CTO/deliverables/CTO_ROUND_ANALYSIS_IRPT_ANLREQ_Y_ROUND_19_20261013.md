# CTO ROUND-19 ANALYSIS -- IRPT_ANLREQ (workstream Y) -- answering the round-18 L10 slug (2026-10-13 ~01:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v11.md`
@8cf145cf49 and the L9 grade (3.0.0_SA_CVO msg 6729): L9 5 PASS; 6 rows OPEN, 5 ARMED, one LIVE (D2-W52-S33). **No PRD addendum.**

## 1. Rulings

| row | ruling |
|---|---|
| **D2-W52-S33** (LIVE: `irpt-ycharts-generate`'s pinned reader 3f29017cfc has no account check and no total-row check, so a two-account or total-row template upload through the Lambda's door is held as one portfolio) | **The reader's release pair is FIRST in round 19**, as the CVO's AR186 condition says: the pinned pair run in a scratch tree before it is cut; `uploads.py` and `template_reader.py` move in ONE deploy with the resident. Nothing else in this round is cut ahead of it. |
| **D2-W52-S31** (still unmatched: `Account Numbers`, `Subaccounts`, `Accnt`, `Account Nos`, `Account Seqno`, `Account Serial`) | **Stop chasing spellings; close the class on VALUES.** Widen once more with the listed forms (plural tails, `acct`/`accnt`, `nos`, `seqno`, `serial`, `roth ira`, `trust` as modifiers), each with a census line and a negative control; AND add one backstop: a column whose header carries the account root (`acc`, `acct`, `accnt`, `subacc`) and holds two or more distinct identifier-like values is read as an account column for the multi-account check. Its words say what is seen and ask; they never tell a person to split. |
| **D2-W52-S32** (the `No. of Accounts` exclusion reads header words only) | **Closed by the same value test:** a count column holds one small integer per row, so `No. of Accounts` is excluded only when its values are counts; if it holds identifiers, the S31 backstop reads it as an account column. One negative control each way. |
| **D2-W54-S5** (the status rule ships to all eight packagers of `served.py`) | Accepted as the CVO states: ONE `served.py` carrying the rule into all eight, both pin groups (361c44fa9d: performance-adapter, narrative, status; 74a62fb46c: the other five) together, and narrative's test staging moved to the new pin so its suite tests what ships. Disarmed by that pair's live reads on all eight. It is NOT in round 19's first slot; it follows the reader's pair. |
| **D2-W55-S1** | Accepted: the status pair states the caller-class line's two limits (no line on a lookup exception or an unregistered firm; `outcome=` is the selection gate's verdict). |
| **D2-W52-S35** | Accepted: the release pair re-counts templates stored between TO-READS-Y9's count and the deploy, and runs the re-open of a pinned-stored template in the scratch tree. |

## 2. ENRICHMENT LIST for round 19 (Y, ONE issuance; each build order at most three mechanical criteria)

1. **The reader's release pair** (S33 LIVE, S35), pinned pair run in a scratch tree first. FIRST.
2. The vocabulary widening and the value backstop (S31, S32), built; they ride the NEXT reader release, not this one, unless they
   merge before item 1's pair is cut (then the pair carries them and says so).
3. The status rule's pair (W54-S5, W55-S1), all eight packagers.

-- 1.0.0_SA_CTO~DELL2
