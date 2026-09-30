# AMGT_RESAPP task order -- `AMGT-ae-1` -- THE POSTURE BATCH OVER THE 12 HELD NAMES, ITS DIFF READ FROM ITS OWN OUTPUT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ae-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the batch runs once, by hand.
comp-iam: RUN by the issuer at the cut -- the same executor identity reads opal-data-harvest (drafting/, posture/, management/, peers/) and wrote posture/v1 under rk-22 (the objects' VersionIds at 2026-09-18); the 12 PutObject calls add no prefix beyond that write. No policy simulation was run.
comp-adversary: RUN by the issuer at the cut -- AC1 FAILS at the base (no capture; with a capture and no batch, 12 keys still at their pre-batch VersionIds); PASSES on a simulated post-state (new VersionIds, packs counting the live D-1 sections); FAILS when the packs still count the pre-hold sentences.
EGRESS CLASS, declared: VENDOR -- Anthropic, 12 messages (one per target, the judge's own call). ON ANDREW'S PER-USE WORD ONLY: the GO names it.
</preflight>

## 1. THE ACT -- `AMGT-ae-1` (round 55, decomposition s.63)

Round 54 held 179 no-span sentences on 12 stored D-1 documents (`drafting/v1/*.json`, `held_no_span`). The posture judgment reads each
name's D-1 through `lib/research/posture/packs.py` `build_pack`, which puts every `sections[].sentences` entry into the evidence pack. So
the next posture run reads packs WITHOUT those sentences. This act is that run, over exactly the 12 targets the check lists (every
posture subject whose own name or comparable holds sentences), and its diff is read from its own output.

**The run, per target K:** `python -m lib.research.posture.judge --security-key K --as-of <A> --write-pool`, where `<A>` is the `as_of` of
K's prior object (from the check's `pre.json`), so every input but D-1 is what the prior run read. This OVERWRITES
`posture/v1/K/<A>.json`. The bucket is versioned, and `pre.json` records each prior VersionId, which is the rollback. `ANTHROPIC_API_KEY`
is exported from `comp-secrets get anthropic-api-key --reveal` in the same shell call. Never run `management_posture_batch.py posture
--force`: it has no key filter and would call Anthropic for all 35 subjects.

**Begin only when all hold:** the issuer's GO names Andrew's per-use word for the 12 calls and the commit to run from, and both halves
are committed (their paths are in the GO). **The order of work, under the entry opened AND COMMITTED first:**
(1) `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round55/checks/ae_1_posture.py --what pre --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ae1-pre`
-- it must list exactly 12 targets; (2) the 12 judge runs; (3) AC1; close the entry. A verdict that moves is a RESULT to report, never a
failure. A failing AC1 is the rollback trigger named in the halves.

## 2. BOUNDS

1. The 12 judge runs and nothing else: no management stage (no Lusha, no Bright Data), no posture object outside the 12, no D-1 / M-1 /
   R-1 write, no delete. A 13th target, a model call beyond 12, or a gate refusal is a REFUSAL.
2. Standing: no S3 delete, no vendor call beyond the named 12, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ae-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round55/checks/ae_1_posture.py --what post --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ae1-pre; echo "exit=$?"</invocation><expect>12 targets each at a new VersionId, packs equal to their live D-1 sections, cites all validated, verdicts in the enum and served as stored, verdict moves printed; THE POSTURE BATCH READS THE HELD PACKS AND SERVES ITS OWN OUTPUT: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ae-1.posture-batch-over-the-held-names.proof_of_spec.json`. Report once: the 12 write receipts (prior and new VersionId), the per-target verdict before and after, the model usage and cost, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-54 analysis item 1 (rulings 1 and 5). The GO waits on (a) Andrew's per-use word on 12 Anthropic calls (CLAUDE.md
Agent Autonomy; CARD 5 covered rk-22 only), and (b) both never-widen halves. Base: AC1 FAIL (no capture; with one, 12 keys unmoved).
Positive arm: PASS on simulated new VersionIds with packs = live D-1 sections; negative: FAIL with packs unchanged. The positive arm
first caught a check defect before the cut: the classed ABSENT verdict `absent` (ASML, HAL, PBR) was off the check's enum -- admitted.

<status>pending</status>
<round>55</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
