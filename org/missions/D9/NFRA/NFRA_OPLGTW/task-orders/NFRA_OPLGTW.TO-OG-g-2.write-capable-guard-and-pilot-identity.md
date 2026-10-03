# NFRA_OPLGTW task order -- `OG-g-2` -- does a WRITE_CAPABLE principal bypass the Schwab entitlement guard; and the pilot principal's identity, verified

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-g-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~23</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; reads with existing access (a tenant user read, one Secrets Manager read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the question is the CTO's (ruling msg 28154 (2)), measured, not designed.
EGRESS CLASS, declared: Opal's own AWS (one secret read) plus ONE authoritative Entra tenant read of one user. No vendor API.
</preflight>

## 1. THE CELL -- `OG-g-2` (decomposition addendum R3-T.7, item 1)

The walkthrough principal is Alyssa Keith (alyssa@opalinvest.com), who will hold Menachem's approved grant after Andrew's
own speed tests (CTO 28154, Andrew-direct 2026-09-28). She is on the gateway's WRITE_CAPABLE roster. Before any grant is
written, the CTO needs ONE fact: is a WRITE_CAPABLE principal's Schwab request evaluated against its data grant, or does
her tier short-circuit the entitlement guard? You MEASURE it, and you verify her identity. You write NO grant and change
nothing served.

1. **The guard, at the live release.** Read the deciding code at `4231bd2ddc6fd975304ed5a2c097473bdd5b41a5` (live; NOT
   CLOUD): `git show 4231bd2ddc:infra/aws/ec2/opal-gateway/app/data_entitlement.py`, the Schwab integration under
   `app/integrations/schwab/`, `app/tools.py`'s tier resolution (`resolve_tier`), and wherever the tier reaches the guard.
   Decide EVALUATES or BYPASSES and cite every deciding line (path + line at that commit).
2. **One probe.** In a scratch checkout of `4231bd2ddc` (`git worktree add --detach <scratch> 4231bd2ddc`, removed
   after), run the guard as a principal resolved to the WRITE_CAPABLE tier, holding a grant for master `08242234` only,
   asking for master `08335338`. Use the test suite's own fixtures (moto/in-memory access state, as
   `tests/test_data_entitlement_guard.py` does); a synthetic principal key; `AUDIT_PATH` isolated. Record REFUSED or
   SERVED. No live call, no state-store write.
3. **Her identity.** Read her `oid` from an AUTHORITATIVE tenant source (`az ad user show --id alyssa@opalinvest.com
   --query id -o tsv` if `az` is signed in; name the instrument). Read the host-side roster
   `aws secretsmanager get-secret-value --secret-id gateway/principals/rosters --region us-east-1` IN MEMORY and find the
   write-capable pair whose oid matches. Never print, log or commit an oid or the secret; compare by sha256. If no
   authoritative instrument is available, that is a BLOCKING row naming what a human must run, and you stop step 3.
4. Write `deliverables/0.9.0_WK_NFRA_OPLGTW~23/WRITE_CAPABLE_GUARD.json`:
   `{"guard_verdict": "EVALUATES"|"BYPASSES", "code_citations": [{"path","line","why"}], "probe": {"principal_tier":
   "WRITE_CAPABLE", "granted_master": "08242234", "asked_master": "08335338", "outcome": "REFUSED"|"SERVED",
   "envelope_code": "<the refusal code or empty>"}, "note": "<one paragraph>"}`; and
   `deliverables/0.9.0_WK_NFRA_OPLGTW~23/IDENTITY_PILOT.json`: `{"tid": "6810043e-d171-4adc-9975-068b35e179da",
   "tenant_read_instrument": "<command name>", "oid_sha256_tenant": "<hex>", "oid_sha256_roster": "<hex of the matching
   roster oid, or of none>", "match": "MATCH"|"DIFFER"}` -- no raw oid, no email, no other GUID.

## 2. BOUNDS

Read only: no grant, no POLICY write, no `ENABLED_INTEGRATIONS` change, no deploy, no secret written. Never print a
secret or identifier. Never push, merge, rebase, stash, `checkout --` or `clean`; never override a gate.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~23/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W23-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-g-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/g2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)verdict (EVALUATES|BYPASSES); probe tier WRITE_CAPABLE.*verdict and probe agree True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-g-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/g2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)tid equals tenant True.*equal True; recorded MATCH; other GUIDs 0; emails 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the guard's behavior for the WRITE_CAPABLE tier, cited at live and agreeing with one probe.
- `AC2`: the pilot principal's tenant oid matches the host-side write-capable roster pair, by hash.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~23/NFRA_OPLGTW.TO-OG-g-2.write-capable-guard-and-pilot-identity.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if both PASS, append a `complete` status tag after the
order's last status line in the same commit. Report once: the verdict with its deciding lines, the probe outcome, MATCH/DIFFER.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 1). Pre-cut: the live Schwab integration and `data_entitlement.py` carry no
  `WRITE_CAPABLE` token (git grep at 4231bd2ddc); the tier may still act upstream (`resolve_tier`), hence the probe.
- The verdict decides FWD-3's arms: EVALUATES -> graded on her; BYPASSES -> UNEXERCISED until Menachem (CTO 28154 (2)).

<status>pending</status>
<round>14</round>
<slot>~23</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
