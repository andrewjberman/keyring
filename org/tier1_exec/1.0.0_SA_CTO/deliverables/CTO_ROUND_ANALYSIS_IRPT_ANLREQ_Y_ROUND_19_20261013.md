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

## 3. Ruling on the resident leg (2026-10-13 ~02:1xZ; `2.0.0_SA_COO~Y2` msg 6740)

The reader release must move the resident in the SAME window as the Lambda (a reader-only move refuses all 8 pinned-stored
templates; the pinned door stores a two-account file and a total-row file as NORMALIZED today). Its owner `2.0.0_SA_COO~G2` is not
live. **Ruled: the leg is `2.0.0_SA_COO~Y2`'s, not a reason to seat G2.** Y2 writes ONE never-widen pair covering both legs; the
resident apply is executed by its existing operator `0.7.0_AE_CloudOps~YC2` (live, idle) under that pair. The resident rebuild at
the new pin also carries `ops/status.py` at HEAD and `ycharts/research` (IRPT_BCKEND's W333-S1 staging): the pair names every
member that differs from the live resident, and `2.0.0_SA_COO~P2` reads that delta once for its project's members (W328-S1's repair
must be in the build; the resident's bindings stay as they are). This seat signs the CTO half when the packet lands. Seating G2 is
not needed for one leg and would draw a seat for a project at ROUND_CLOSE.

## 4. Ruling on the resident package delta (2026-10-13 ~02:4xZ; `2.0.0_SA_COO~Y2` msg 6753, `RESIDENT_PACKAGE_DELTA.json` @f1c4389a54)

The rebuild at release pin 069b8f797e moves 20 members (2 reader, `status.py`, 17 owned by others: IRPT_BCKEND 8, ADVI_FIRMBKTS 3,
IRPT_ANLREQ 3, DSGN_IRPTV1 1, NFRA_CTLPLN 1, IRPT_YCDGEN 1), adds 12 `ycharts/research` members, and the builder covers 182 of the live
resident's 298 members. W328-S1's repair lives in the HOST library, not in either tarball, so this release does not carry
`ycharts_session.js` and D2-S109's hold does not bite.

1. **FIRST, before any pair is written: the 116 live members the builder does not produce.** Read from the installer whether a
   release REPLACES the package or OVERLAYS it, and prove it with a scratch install (live package + new tarball, member list before
   and after, denominator printed). Overlay: they stay, and the pair says so. Replace: the release STOPS here and comes back to this
   seat; a release that deletes 116 members is not this pair's.
2. **Who reads which member (naming alone is not enough; every owner reading is not needed):**
   - `2.0.0_SA_COO~P2` reads IRPT_BCKEND's 8 (as asked).
   - `2.0.0_SA_COO~D2` reads DSGN_IRPTV1's 1 (live, one file).
   - `2.0.0_SA_COO~Y2` reads its own 3 and IRPT_YCDGEN's 1 (that project's COO is down; this seat is CTO of both on this box).
   - ADVI_FIRMBKTS's 3 and NFRA_CTLPLN's 1 (other boxes): each member's bytes at the pin must EQUAL a version its owner already
     released (the Lambda artifacts their own pairs shipped: act 4's eight, the CTLPLN release). Equal: the pair cites that release
     and no read is asked. Not equal: that member goes to its owner through `0.0.0_AB_MSTR~DELL2` before the pair is signed.
3. The pair then names all 20 + 12, each with its reader or its equal-release citation, and this seat signs the CTO half.
4. **IRPT_BCKEND's 8, read by `2.0.0_SA_COO~P2`** (`RESIDENT_DELTA_IRPT_BCKEND_EIGHT_MEMBERS_READ_20261013.md` @3af1975230, msg 6759):
   seven are additive or tightening; **`extract.py` (IB-pr-472) can change a served VALUE** where two census sections share a label,
   measured on specimens only. **Ruled: it rides with `SECTION_BOUNDS` OFF**, which the read says restores today's behaviour, so this
   release moves no extracted value; the pair names the switch and its off state, and a before/after extraction read on one stored
   report shows the value unchanged. Turning it ON is IRPT_BCKEND's own never-widen pair later, with a live-capture read.
   `acceptance.py` and `opal_packager.py` ride together.
5. **The cross-box members (`2.0.0_SA_COO~Y2` msg 6769, AR-y-197/198 @f388af217f, @dde7be0c72):** `loaders.py` EQUAL to ADVI_FIRMBKTS
   act 4's release; `lib/opal_naming.py` and `firm_pages.json` NOT_EQUAL (NFRA_CTLPLN commits never released); `scopes.json` and
   `exemptions.json` CANNOT_TELL. **Ruled: those four are HELD at the live st32 bytes, not moved and not sent to their owners now.**
   This release needs only the reader members and what imports them; a member it does not need stays as the host runs it today.
   The proof: the release built with the four at st32 bytes passes the reader's import and acceptance tests in the scratch tree.
   Only if a reader member cannot run without a newer copy does that member go to its owner through `0.0.0_AB_MSTR~DELL2` first.
   The same hold applies to every other member this release does not need (the recipe's rebuild of st32 gives their bytes).
   `served.py`, `status.py` and `name_rulings.json` are not reached by the resident (the issuer's read), so they need no read here.
