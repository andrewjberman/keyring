# NFRA_OPLGTW task order -- `OG-pm-2` -- the latency cause read: per-route counts and p95 on 2026-10-05 and 2026-09-30

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~27</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only reads of the gateway's own audit records / ALB logs; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-17 analysis s.4 item 1, R17).
EGRESS CLASS, declared: NONE beyond read-only Opal AWS (S3 audit/ALB-log reads, CloudWatch, SSM read on the host).
</preflight>

## 1. THE CELL -- `OG-pm-2` (decomposition addendum R3-T.11, item 1; CTO R17)

Row Z-W27-S3: the full-day p95 on 2026-10-05 was 0.947 s, against the 0.6642 s cap. 23 of 24 hours sat near 1 s at
60-151 requests an hour. The one high-volume hour (02Z, 1,356 requests) was under the cap.

Day-level reads (row Z-W27-S2) were 0.545 s on 09-30 and 0.606 s on 10-01, then 0.897 s on 10-02, the day OG-rl-3
(`/hx/teams`) released. Two causes fit:
- (i) a MIX artifact: a new steady caller of a slow route since 10-02;
- (ii) a slowdown of routes that existed at OG-p-1.

This cell SEPARATES them. It fixes nothing.

1. **Instrument.** Pick the instrument that sees per-route (and, where recorded, per-caller) latency. Candidates:
   - the gateway's own audit records (bucket `opal-mcp-audit`, the `AUDIT_S3_BUCKET` value);
   - ALB access logs, if enabled;
   - the host's own request log.

   Name it, and name what it CANNOT see: for example audit-only tool calls versus plain HTTP routes, or unauthenticated
   requests. Print its covered request count beside the ALB `RequestCount` for each day.
2. **For 2026-10-05 and 2026-09-30 (UTC days):**
   - Report each route's request count and p95 (null where the instrument records no latency).
   - Mark each route `at_ogp1: true` if it existed at OG-p-1. Use the OG-p-1 order and record under this project's
     `task-orders/` and `deliverables/` to establish that set, and cite where it comes from.
3. **Hypothesis (i) first.** Is there a steady caller since 10-02? Give its route, caller (principal or label, never a
   secret), hourly rate and p95. Show its share of the quiet-hour requests on 10-05.
4. **Finding:** `MIX` | `SLOWDOWN` | `BOTH` | `UNDETERMINED`, with the numbers that decide it.
5. Write `PM2_CAUSE.json`:
   - `instrument {name, cannot_see}`;
   - `days {"2026-10-05": {routes:[{route, at_ogp1, requests, p95_seconds}], covered_requests, alb_requests}, "2026-09-30": {...}}`;
   - `hypothesis_i {steady_caller_found, route, caller, hourly_rate, p95_seconds}`;
   - `finding`;
   - `writes: 0`.

   Also write a short `PM2_CAUSE.md`.

## 2. BOUNDS

- READ-ONLY. 0 writes anywhere outside your deliverables. No host change. No alarm, monitor or dashboard (moratorium).
- Never print a bearer, a secret, an email beyond the principal label the audit already carries, or any `.env` value.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~27/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W27-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pm-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r18/checks/pm2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)2026-10-05: routes \d+;.*2026-09-30: routes \d+;.*finding (MIX|SLOWDOWN|BOTH|UNDETERMINED); writes 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~27/NFRA_OPLGTW.TO-OG-pm-2.latency-cause-read.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once: the finding and its deciding numbers, coverage, AC output, rows, commits.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 18 (addendum R3-T.11, item 1). Alone. AC1 passes on any finding: the cell measures, and
  the CTO rules (R17).
- Pre-cut: `pm2.AC1` FAIL (the record is absent).

<status>complete</status>
<round>18</round>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
