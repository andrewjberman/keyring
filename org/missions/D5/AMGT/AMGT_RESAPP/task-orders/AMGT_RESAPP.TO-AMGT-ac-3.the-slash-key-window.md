# AMGT_RESAPP task order -- `AMGT-ac-3` -- THE SLASH-KEY WINDOW: COPY THE 40 OBJECTS TO ENCODED KEYS, THEN DEPLOY THE BUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ac-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN by the issuer at the cut -- the function's reads stand as simulated in round 51 (crosswalk GetObject ALLOWED; ListBucket and the ranking Query NOT-DECIDABLE, exercised live); the new encoded keys sit under the same prefixes the function already reads. BLIND: the 40 CopyObject calls run under the executor's credentials, not simulated; the plan must show NO IAM change.
comp-adversary: RUN by the issuer at the cut -- AC1, AC2, AC4 FAIL at the base; AC3 is the executor's own pre/post body control (save then compare, byte-equal at the base).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ac-3` (round 53, decomposition s.61)

ONE act, ONE NEVER-2 entry, ONE never-widen pair (CTO round-52 ruling 4), in two legs, in this order:
(a) **COPY** the 40 raw-slash objects (AMENDMENT 1, CTO msg 27160: the ruling's 30 plus scores 4, filings 2, raw/bloomberg 4) listed in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/SLASH_OBJECTS.json`
    (each `raw_key` -> its `encoded_key`, byte-equal; the raw objects are KEPT -- a copy, never a move or a delete);
(b) **DEPLOY** `opal-amgt-scoped-api` built from a checkout at the PIN the issuer's GO names (HEAD at that time), carrying CORPUS z-4's
    slash-safe readers, HARVST q-5's `91b74a9047` (`/timeline` `publishers_found_codes`) and AMGT-ac-4's docstring.
Leg (a) precedes leg (b): a build whose readers use encoded keys must never serve before those keys exist.

**Begin only when all hold:** the issuer's GO names the pin; both halves are committed --
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/NEVER_WIDEN_HALF_COO_AC3.md` and
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND53_AC3_CTO_HALF.md`; `SLASH_OBJECTS.json` exists; and **the base CodeSha256
(`nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w=`) is still live, re-read immediately before the act -- a moved base is a STOP.**
**The order of work, under the entry opened AND COMMITTED first:** (1) the pre-act captures the halves name, INCLUDING
`python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_3_served.py --what save --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ac3-pre`;
(2) leg (a), then verify AC1; (3) build at the pin (`--build-only` content diff saved; STOP on a file beyond the halves' list), upload, ONE
`safe-apply` -- plan printed first, code only; (4) verify AC2-AC4; close the entry. A criterion failing after the act is the ROLLBACK
trigger named in the halves.

## 2. BOUNDS

1. The act and nothing else: 40 CopyObject calls (no delete, no overwrite of an existing encoded key whose bytes differ -- STOP), one
   artifact, one apply of the function's code. A plan beyond the code, a packaged file beyond the halves' list, or a gate refusal is a
   REFUSAL.
2. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ac-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_3_copies.py; echo "exit=$?"</invocation><expect>objects 40; raw kept and encoded byte-equal: 40; THE RAW-SLASH OBJECTS READ AT THEIR ENCODED KEYS, BYTE-EQUAL, RAW KEPT: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ac-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_3_served.py --what codes; echo "exit=$?"</invocation><expect>every AMZN /timeline series entry carries publishers_found_codes; /TIMELINE SERVES PUBLISHERS_FOUND_CODES: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ac-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_3_served.py --what bpng --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ac3-pre; echo "exit=$?"</invocation><expect>bodies 6; moved or empty vs the pre-act capture: 0; BP AND NG READ THE SAME DATA AT THE ENCODED KEYS: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ac-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_3_served.py --what code; echo "exit=$?"</invocation><expect>deployed CodeSha256 differs from nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w=; THE ONE BUILD LANDED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

A fourth criterion, reason: the one act carries an object copy and a build, and each served move keeps its own served read; AC4 is the
landing itself.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ac-3.the-slash-key-window.proof_of_spec.json`. Report once: the 40 copy receipts, the content-diff summary, the prior and new VersionId and CodeSha, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-52 analysis item 3 / ruling 4. Waits on CORPUS round-24 cell 4's drain (every reader routed) and COO~X's 30-object
list + before-state (written by the issuer to round53/SLASH_OBJECTS.json). Base: AC1 FAIL (no list), AC2 FAIL (key absent on 273 entries),
AC3 PASS as a save-then-compare control, AC4 FAIL (nKWCfQRQ). The COO half is written against the pin, the list and the then-live base.

<status>pending</status>
**AMENDMENT 1 (`2.0.0_SA_COO~Z`, ~13:1xZ, before any GO):** scope 40 objects, not 30 (COO~X's full listing, msg 27153 @7e569c4d1d; CTO msg 27160: the pair covers all 40, the 10 extra classes' READERS named and shown slash-safe in the COO half's census before signing). `round53/SLASH_OBJECTS.json` written from the supply with each raw sha256 read live (sizes equal to the supply's); `ac_3_copies.py` requires 40.
**AMENDMENT 2 (`2.0.0_SA_COO~Z`, 2026-09-30 ~16:0xZ, after the act; graded by no gate limb -- a modification, and this order declares no `<placeholders>`):** AC3 re-scoped per row Z-S320 (ruling on the executor's Z-S318): `ac_3_served.py --what bpng` rewrites the encoded name back to raw INSIDE `*_read` provenance subtrees only (the read path the act moves by design) and every other byte must equal the pre-act capture. Issuer re-run on the served plane: AC1 40/40, AC2 273/273, AC3 6 of 6 equal (12 read-path strings rewritten; a plant outside `*_read` FAILS), AC4 /QP4upEV... Successful. Instance VALID (`0.7.0_AE_CloudOps~A`, msg 27240); AC3 graded by the issuer under AMENDMENT 2. No rollback. Z-S319 ruled INERT for served output (Z-S321); repair to round 54.
<status>complete</status>
<round>53</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
