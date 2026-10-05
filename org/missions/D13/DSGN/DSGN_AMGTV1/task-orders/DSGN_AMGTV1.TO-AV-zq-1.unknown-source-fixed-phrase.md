# DSGN_AMGTV1 task order -- `AV-zq-1` -- DIRECT ACT: AN UNKNOWN SOURCE READS THE FIXED PHRASE, NEVER ITS CODE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~101</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically.
comp-adversary: RUN by the issuer at the cut on portal 5fe58e89 (the round-38 candidate) -- repairs38.cjs (AMENDMENT 2, arm 4) 5 of 6: arm 4 FAILS ("issuer_site_silver/filing:source" -> "Source: issuer site silver filing source."); every other arm passes. It reads 6 of 6 with the one-line reference fix loaded through CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zq-1` (round 39, decomposition v39; a DIRECT ACT; serves FWD-11)

In `portal/src/pages/SecurityAnalysis/components/CardFooter.tsx`, `sourceWords()` ends (`:95`) with

```
  return key.replace(/[_:/-]+/g, ' ').replace(/\s+/g, ' ').trim()
```

That prints an unknown source code with its punctuation stripped, for example "issuer site silver filing source". FWD-11 forbids a
code on the face. Replace that last line with

```
  return UNNAMED_SOURCE_WORDS
```

The constant already exists in the file ("a source this page has no name for yet"). Change nothing else. Known sources ("bloomberg-dapi"
-> "Bloomberg", the publishers, a form such as "10-K") keep their words.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. One line in CardFooter.tsx.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit tool ONLY. Keep the file's CRLF line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/CardFooter.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~101/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round38/checks/repairs/repairs38.cjs"; echo "exit=$?"</invocation><expect>WHAT CHANGED USES THE SHARED STATES, EVERY CARD ENDS IN THE SHARED FOOTER, THE PAGE ENDS ON THE SHARED END LINE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~101/DSGN_AMGTV1.TO-AV-zq-1.unknown-source-fixed-phrase.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W101-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the one-line change, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO review @2e225582da of portal 75f9f477 (round 38), REQUIRED fix; msg 29549. Andrew's word for the round 37+38 DEV push
  waits on this (record 121b7b016e, msg 29560).
- **Check:** repairs38 AMENDMENT 2 adds arm 4 (unknown long sources plus a known control). The TITLE is unchanged; the count is now 6.
- **Not this cell:** row S3 (the shared PageEnd prints "5:00p ET" after a bare served day) and reads37's What-changed selector -- for the
  CTO's next list.

<status>complete</status>
<round>39</round>
<slot>~101</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
