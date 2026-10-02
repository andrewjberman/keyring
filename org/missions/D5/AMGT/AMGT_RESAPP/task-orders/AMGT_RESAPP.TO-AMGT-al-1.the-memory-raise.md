# AMGT_RESAPP task order -- `AMGT-al-1` -- THE MEMORY RAISE: THE BA TIMELINE DAY ROUTE ANSWERS COLD INSIDE THE GATEWAY CEILING (demo risk)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-al-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one config apply by hand, before 12:15Z.
comp-iam: DECLARED-NOT-APPLICABLE -- a memory_size change grants nothing; the plan must show NO IAM change.
comp-adversary: RUN by the issuer at the cut -- the pre probe reads BA /timeline/day/2026-09-08 at 27,194 ms WARM (no Init Duration) at 1769 MB, 2 s under the 29 s ceiling; CVO~Z measured 5 cold timeouts at 10Z. AC1's C0 FAILS at the base (MemorySize unmoved).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-al-1` (round 62, decomposition s.70; CTO round-61 addendum ruling 5 @f1d5dac151)

ONE act under ONE NEVER-2 entry: raise `opal-amgt-scoped-api`'s memory from 1769 to 3538 MB. In
`infra/aws/terraform/harvest/scoped-amgt-api.tf` set `memory_size = 3538`, then run ONE `safe-apply` in `infra/aws/terraform/harvest/`.
**If AC1's C1 still misses at 3538, raise it to 10240 under the same entry and re-run AC1.** Stop at 10240.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round62/checks/timeline_day.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/al1-pre.json`.
2. Edit `memory_size`. Print the plan first: it must show ONE in-place update of the function, with ONLY `memory_size` changing. Any
   code (`source_code_hash`), IAM, route, gateway or destroy change is a STOP; the artifact in S3 is the deployed code, so none is expected.
3. ONE `safe-apply`.
4. AC1 immediately: the post read fires 3 CONCURRENT invokes, which land on fresh sandboxes after the config change, so each is
   COLD. Close the entry, or go to 10240 per above.

A failing C2 (the control's body moved) is the ROLLBACK trigger: `memory_size` back to 1769 through one `safe-apply`.

## 2. BOUNDS

1. The one property and nothing else. No code change, no store write, no S3 delete, no vendor call, no push of shared branches.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-al-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round62/checks/timeline_day.py --what post --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/al1-pre.json --target-ms 20000; echo "exit=$?"</invocation><expect>C0 PASS (MemorySize moved off 1769); C1 PASS (3 of 3 concurrent BA_US_Equity /timeline/day/2026-09-08 invokes each COLD -- REPORT carries Init Duration -- each status 200 with Duration under 20,000 ms); C2 PASS (the AMD timeline control's body sha256 equals its pre value); THE BA DAY ROUTE ANSWERS COLD UNDER TARGET: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-al-1.the-memory-raise.proof_of_spec.json`.
Report once: the MemorySize landed (3538 or 10240), the plan's resource count, each of the 3 runs' Duration and Init Duration, the
control sha, and AC1's verdict. Name any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~11:3xZ) -- act (B): al-2's code-only redeploy (CTO ruling 5a @e041af6102)

Act (A), the memory raise, is done: 10240 MB, proof `339b159ea0`. Act (B) redeploys `opal-amgt-scoped-api` at the commit the GO names,
carrying al-2: the timeline day route's silver read runs under an 18 s deadline from handler start, and on the deadline the mentions
are served with `headline` null and one plain `headline_reason`, as a 200. It runs under its OWN NEVER-2 entry and the never-widen pair:
- `deliverables/2.0.0_SA_COO~Z/round62/NEVER_WIDEN_HALF_COO_AL1B.md`
- `ledger/NEVER_WIDEN_ROUND62_AL1B_CTO_HALF.md`

**The acts, in order:**
1. `timeline_b.py --what pre`: if `round62/AL2_CONTROLS_PRE.json` still matches CodeSha256 `E+FAZF0f...`, it is the pre; otherwise re-run.
2. Build and upload ONE artifact at the GO commit. STOP on any CHANGED/ADDED/REMOVED file other than `lib/research/api/scoped_amgt.py`.
3. ONE code-only `safe-apply`; `memory_size` stays 10240. Any other attribute in the plan is a STOP.
4. Grade act (B) by running both:
   - `round62/checks/timeline_b.py --what post --pre <the pre>`: 3 of 3 concurrent cold BA invokes answer 200, and both control days
     are byte-equal to the pre.
   - `pytest lib/research/api/tests/test_timeline_silver_deadline.py`: the planted slow read.
   Then close the entry.
**FREEZE (ruling 5a):** act (B) is deployed AND graded by 12:30Z, or it waits until after Andrew's demo read. Nothing deploys to this
function between 12:30Z and the end of the demo. Rollback: the prior artifact version through one code-only `safe-apply`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-61 addendum ruling 5 (track A). There is no never-widen pair: ruling 5 names one for track B, not for A. A
memory change moves no served output, and C2 proves it. Track B (a deadline on the silver read serving headline null with a reason, under
the pair) is cut only if A misses at 10240. Track C is after the demo.

<status>pending</status>
<round>62</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**ISSUER GO act (B) (2.0.0_SA_COO~Z, 2026-10-02 ~11:1xZ):** build commit `a2ff06d1a1` (0 packaged files differ from the build-only tree `a12291728f`); halves COO `a12291728f`, CTO `57dfa6bd84`. CTO conditions: CHANGED 1; timeline_b.py + the planted-slow tests; deployed AND graded by 12:30Z; NEVER-2 entry.

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~11:4xZ):** ACCEPTED, acts (A) and (B). (A): proof `339b159ea0`; 3538 missed (21.7/20.4/22.9 s), 10240 passed 3 of 3 cold (16.9/16.6/19.1 s), control unchanged. (B): deployed 11:27Z and graded 11:32Z, inside the 12:30Z freeze (msg 28425, proof `9da65fe4b6`); CodeSha256 E+FAZF0f -> bZBmEtRr, artifact YSqlUTOW -> iDuPquXb, CONTENT-DIFF CHANGED 1, memory 10240 kept; timeline_b YES (3 of 3 cold 200; run 3 hit the deadline at 18,006 ms and served headline_reason, runs 1-2 15.1/16.5 s with headlines), both controls byte-equal, planted-slow tests 3 passed. Issuer read ~11:4xZ: deployed bZBmEtRr at 10240; BA 2026-09-08 warm 200 with 5 of 5 headlines; both controls byte-equal; B1 regression YES. Row Z-S337 (the 18 s line sits inside the cold spread, so some cold BA day views show [no headline]) is the specified outcome; carried for the post-demo track C.

<status>complete</status>
