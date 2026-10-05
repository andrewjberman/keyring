# AMGT_RESAPP task order -- `AMGT-av-8` -- THE CODE REDEPLOY CARRYING av-1..av-7, PLUS ITS LEGS: THE filings/v1 GRANT, THE DRAFTING REBUILD, THE POOL UNIVERSE WRITE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy and three hand-run legs.
comp-iam: RUN by the issuer at the cut -- av-4 adds a read of `filings/v1/` (removed from the grant at scoped-amgt-api.tf:123); av-6 may add `dynamodb:BatchGetItem`. Every new read path or action carries a simulate-principal-policy arm reading allowed before the code leg is LANDED.
comp-adversary: RUN by the issuer at the cut -- on deployed wbIT0PHv, r72 c39/c41/c42/c43/c44/c45 FAIL; c46/c47 FAIL locally.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-av-8` (round 72, decomposition s.80)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying
av-1..av-7. `memory_size` stays 1769. **The GO names every leg, its keys and its order.** The expected legs, each only as the GO
states it:
1. **Grant leg:** the `filings/v1/` read (and any action av-6 adds), simulated allowed.
2. **Code leg:** one artifact and one code-only `safe-apply`.
3. **Drafting rebuild:** the keys av-3 named.
4. **Pool universe write:** `build_universe --write-pool`, at the key av-7 named.

**Begin only when** the GO names the build commit and every leg, and both halves are committed.
- Re-read the base CodeSha256 live (`wbIT0PHvxKIgJvgVy+u0XhLuSXFK5dUE/wypJPDcf8o=` unless a newer closed entry records another);
  any other value is a STOP.
- Read every live worktree's `.open_deploys/` (a dead entry is the issuer's to rule).
- Build from a detached checkout. Any file in the CONTENT-DIFF not on the halves' list is a STOP. Over 262,144,000 B is a STOP.
- Any destroy, route or gateway change in the plan is a STOP.
- Measure the BEFORE state of every store key you write.

**Right after the code leg,** run `round71/checks/leadpanel_cold_warm.py --label after` (the cold column is perishable).

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`, and each written key
restored from its BEFORE version.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change beyond the GO's grant, no store write outside the GO's keys, no S3
   delete, no vendor call, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c39 c41 c43 c44 c45; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R72 C39, C41, C43, C44 and C45 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c42 --where deployed; echo "exit=$?"</invocation><expect>after the drafting rebuild leg: points with a passage_id 6, C1 PASS failing 0; R72 C42 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-av-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c34 c36 c38; do if [ $c = c38 ]; then PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed || exit 1; else PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_served.py" --cell $c --where deployed || exit 1; fi; done &amp;&amp; for c in c30 c31 c32 c33; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R71 C34/C36/C38 and R70 C30-C33 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-av-8.the-code-redeploy-and-legs.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256 and the VersionId;
- the CONTENT-DIFF summary and size;
- each leg's keys with BEFORE and AFTER versions;
- the simulate arms;
- every criterion's output lines;
- the leadpanel AFTER output.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.80; staged until av-1..av-7 drain and the pair is signed. The GO names the legs from the workers' reports.

<status>staged</status>
<round>72</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

## 4a. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-05 ~22:1xZ) -- the POOL UNIVERSE WRITE LEG IS REMOVED

**Row Z-W243-S1 (ARMED) is disarmed here.** The only stored SEC object (`company_tickers/date=2026-09-22/company_tickers.json`) carries
no EDGAR filing history. A `--write-pool` from it would write `form_expected` "none" over 13 names that the 2026-09-16 pool object
holds as 10-K (7) or 20-F (6), a served-data regression.
- **This act writes NO pool universe object.** av-7's dry-run unblock and plain names still ride the code leg.
- The write returns in round 73 with a rule that keeps the prior `form_expected` when the input does not measure it.
- **The legs are now:** grant (`filings/v1/` read, plus `dynamodb:BatchGetItem` on `etf-classifications` if the role lacks it),
  code, and the drafting rebuild of `drafting/v1/BA_US_Equity.json` and `drafting/v1/ASML_NA_Equity.json` (av-3's named keys).

Gate limb that graded this modification: GATE (viii) on a modify (`<placeholders>NONE</placeholders>`).

## 4b. AMENDMENT 2 (issuer `2.0.0_SA_COO~Z`, 2026-10-05 ~23:0xZ) -- the drafting leg is a NARROW SPLICE, not a rebuild; the legs are fixed

**Measured:** a full `drafting_build --rebuild-pool` re-applies the whole gate. On BA it also adds `anchored` / `text_original` to every
drafted sentence; on ASML it DELETES `thesis_driver_provenance`. That is wider than this act.
- **The drafting leg is therefore** `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/drafting_evidence_splice.py
  --keys BA_US_Equity,ASML_NA_Equity --write --pre-act-dir <your deliverables>/av8-pre-act/`.
- It changes only `.evidence_records` and `.denominators.evidence_records`, round-trips the stored bytes, and refuses otherwise.
- **Run its `--dry-run` first;** it must print `SPLICE: YES`.

**THE LEGS, in order:**
1. **Grant.** In `infra/aws/terraform/harvest/scoped-amgt-api.tf`:
   - add `"filings/v1/",` back to `local.scoped_amgt_pool_prefixes`, updating the AMGT-rk-91 removal comment: av-4's
     `read_segment_breakdown` reads it now;
   - add `"dynamodb:BatchGetItem"` to the etf-classifications GetItem statement (~`:354`).
   Then ONE `safe-apply` targeted at `aws_iam_role_policy.scoped_amgt_api_grants`; the plan is one in-place update, or a STOP.
   `round72/checks/r72_grant_av8.sh` must read `R72 AV8 GRANT: YES` (C1, C2, C3 allowed beside the controls) before the code leg.
2. **Code.** Build commit `7889ef1ae4`. The CONTENT-DIFF against deployed `wbIT0PHv` is exactly:
   - CHANGED `lib/research/api/scoped_amgt.py`, `lib/research/api/monthly_chatter.py`, `lib/research/print/render_pack.py`;
   - ADDED `lib/research/peers/numeric_tickers.py`.
   Then ONE code-only `safe-apply`, then `round71/checks/leadpanel_cold_warm.py --label after` at once.
3. **Drafting splice,** as above. The BEFORE VersionIds: BA `.zSrn_broPgdErEesbpfY8lJH5RMBCSb`, ASML `kQZePsmgbJlF1Tnvf3t2ljwqNnW9wrYX`.

The surfaces gain `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/` (already listed) for the pre-act bytes.

**AC4 (added): the grant.**

<criterion id="AC4" cell_refs="AMGT-av-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_grant_av8.sh"; echo "exit=$?"</invocation><expect>the three controls and C1, C2, C3 all PASS allowed; R72 AV8 GRANT: YES; and exit=0</expect></criterion>

Halves:
- COO: `deliverables/2.0.0_SA_COO~Z/round72/NEVER_WIDEN_HALF_COO_AV8.md`;
- CTO: `ledger/NEVER_WIDEN_ROUND72_AV8_CTO_HALF.md` (owed).

Gate limb that graded this modification: GATE (viii) on a modify (`<placeholders>NONE</placeholders>`).

