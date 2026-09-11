# AMGT_RESAPP.TO-AMGT-s-2 -- THE ON-DEMAND PULL: an uncovered ticker from the page, which means the browser-to-box seam -- DESIGN it (the estate has no precedent), then BUILD the design

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-2; manifest row S2)

```
AMGT-s-2. THE ON-DEMAND PULL -- a ticker outside coverage, from the page. FIRST deliverable: THE SEAM
DESIGN -- how a browser request served from AWS reaches a loopback-only DAPI on this device (section
1b: the estate has no precedent). SECOND: the build on the approved design, the page stating it is
fetching now. Touches NEW securities, the binding cost axis.

FWD-2's bar, verbatim: "An analyst gets the same pack for a company the firm has never covered, by
typing its ticker. DONE WHEN EXERCISED -- a real uncovered name has been pulled and read." The
EXERCISED bar is served by an analyst on the page; this cell builds the request path.

THE SEAM, MEASURED (decomposition s.1b): integrations/bloomberg/README.md s.1 -- "There is exactly one
physical pipe, and it is loopback ... DAPI binds 127.0.0.1 and nothing remote can reach it -- no VPN,
peering, or security-group change. Something running ON the Terminal box must make the blpapi call."
s.5 lists "Remote reach" under what the integration does NOT cover. comp-routes: 28 CloudFront
behaviors, every origin S3 or API Gateway, NO desktop origin. So a request that ORIGINATES in a
browser served from AWS cannot call DAPI; something on this box must consume the request.

TWO DELIVERABLES, IN ORDER:

  (1) THE SEAM DESIGN  .../deliverables/0.9.0_WK_AMGT_RESAPP~2/SEAM_DESIGN.md
      It MUST answer, in its own sections: (i) how a page action becomes a request the box can see;
      (ii) what on the box consumes it, under which interpreter and principal, and how often; (iii)
      how the pull's result reaches the page (the store, AMGT-s-6's grammar); (iv) how the page knows
      the request is IN FLIGHT, LANDED or FAILED -- as DATA in the store, never inferred from absence;
      (v) what happens when the terminal is signed out at consume time (the request is MARKED, never
      lost, never retried into a locked account); (vi) the latency and cost of one request, stated as
      a measurement of the built path (deliverable 2), not an estimate; (vii) the precedents it builds
      on and why -- READ THESE, do not re-invent: the daily pull's push shape
      (integrations/bloomberg/pipeline/publish_to_portal.py: the box writes to S3, the portal reads);
      the estate's cross-device SQS agent bus (.claude/skills/agentbus/SKILL.md: a box-side consumer on
      a per-device inbound queue -- the closest precedent to a box consuming cloud-originated work);
      the README's note that the planned SSM tunnel terminates locally. The brief's pre-brief notes
      (org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_PRE_BRIEF_NOTES_20260910.md s.5) name three
      shapes -- a desktop agent on a queue; pre-compute a bounded universe on the daily vehicle; a
      hybrid -- weigh them against (i)-(vi) and choose ONE, with the reason.

  (2) THE BUILD, the MINIMUM that exercises the design end to end for ONE uncovered ticker:
      - the cloud side: whatever the design names (an SQS queue and an API Gateway route with the
        estate's auth-validator-edge in front are the expected shape; declare it in Terraform under
        infra/aws/terraform/research/ -- the module AMGT-s-6 created -- and, if a Lambda is needed to
        enqueue, under infra/aws/lambda/research/), applied through `bash .tools/safe-apply.sh` under
        a change-management ledger entry opened BEFORE the act (G-16, G-22);
      - the box side: a consumer under integrations/bloomberg/research/ that polls the request
        source, runs AMGT-s-1's pull (integrations/bloomberg/research/model_block_pull.py -- landed;
        import it, do not fork it) for the requested ticker, and writes the status object;
      - the status object: packs/<security_key>/status.json in opal-data-research with
        {state: REQUESTED|FETCHING|LANDED|FAILED, requested_at, updated_at, reason} -- this IS "the page
        states it is fetching now" until a page exists (no .tsx in this order: C-DESIGN-SPEC-FIRST);
      - ONE end-to-end exercise: enqueue a request for ONE uncovered ticker you choose and state,
        watch the box consume it, and read the status object move REQUESTED -> FETCHING -> LANDED
        with the raw objects present under raw/bloomberg/<key>/ (AC3).
```

## DEPENDENCIES

`AMGT-s-1` (the pull this consumer runs) and `AMGT-s-6` (the store the status and the bytes land in).
Both round 1. This slot spawns after both are merged.

## BOUNDS -- what this cell may not cross

```
⛔ THE BOX STAYS LOOPBACK-ONLY. No inbound port, no listener on this device, no tunnel that terminates
remotely, no security-group change (README s.1). The box PULLS work; nothing PUSHES into it. AC5.

⛔ G-24 / C-VENDOR-EGRESS: this cell touches ONE NEW SECURITY, the one uncovered ticker you name for the
end-to-end exercise, and no more. F2: the binding cost is unique securities touched. Every request the
consumer serves in this order is that one ticker; a second is a widening.

⛔ integrations/bloomberg/READ_HERE.md binds the box side exactly as it binds AMGT-s-1: health before
each pull, NEVER a sign-in by this worker, a signed-out terminal MARKS the request FAILED with the
reason and stops (v). Never mint data/bloomberg/.

⛔ G-16 / G-22 / G-19: ledger before the apply, safe-apply, one queue, one status grammar, no shadow path.

⛔ G-20: the consumer is a poller a person can start and stop, or a run the daily vehicle invokes -- it
is NOT a monitor, an alarm, an SNS topic or a notification. A status object is data, not an alert.

⛔ comp-blast IS OWED at the cloud build: adding an API Gateway route changes the portal's request
path. Run `comp-blast` on the distribution/route you touch and `comp-routes behaviors` after the apply;
record both in the deliverable. A behavior that appears unexpectedly is a BLOCKING row.

⛔ C-DESIGN-SPEC-FIRST: no .tsx. The page's "fetching now" is the status object.

⛔ NO IAM WIDER THAN THE DESIGN NAMES: the enqueue principal writes to one queue; the box consumer reads
one queue and writes one bucket. State both principals in the design; `comp-iam service <lambda>` after
any new boto3 call, recorded.

⚠ BOUND EVERY CALL under `timeout 120`; the end-to-end exercise is watched by POLLING the status object
with a stated cap (e.g. 30 polls x 4 s), never by an unbounded wait.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-routes behaviors (RUN, DESIRED plane): 28 behaviors; the F10 precedent SecurityScanner has its own
    /api/scoped/security-scanner/* -> API Gateway behavior with NO edge Lambda; every auth-gated route
    carries viewer-request auth-validator-edge. A new route for this project follows that shape.

integrations/bloomberg/README.md s.1 and s.5: loopback only; remote reach not covered. The seam is
    yours to design; it is not a precedent you can cite.

.claude/skills/agentbus/SKILL.md: the cross-device agent bus -- a persistent consumer Monitor on a
    per-device SQS inbound queue. The closest existing shape to "a box consumes cloud-originated work".

AMGT-s-6's STORE_CONTRACT.md (landed): the key grammar; packs/<security_key>/... is where status lives.

comp-schedule (RUN to completion): 25 gates armed, none this project's; G-16, G-19, G-20, G-22, G-24
    bind this cell. comp-iam (RUN): six services carry secretsmanager:GetSecretValue as a gap -- not
    this cell's shape; this cell's grants are sqs + s3, stated in the design.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/research/
infra/aws/lambda/research/
integrations/bloomberg/research/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-2.on-demand-pull-the-seam-design-then-build.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. AMGT-s-1's module is IMPORTED, not edited;
the README, the agentbus skill, the pre-brief notes and STORE_CONTRACT.md are READ. AWS acts are
operational and not path-gated. `portal/` is NOT in your write surface.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W2-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-2"><invocation>python -c "import io,re; t=io.open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/SEAM_DESIGN.md',encoding='utf-8').read(); need=['page action','consumer','store','IN_FLIGHT|FETCHING','signed out','latency','precedent']; print('SEAM_DESIGN sections answered', sum(1 for n in need if re.search(n, t, re.I)), 'of', len(need), '| loopback stated', bool(re.search(r'127\.0\.0\.1|loopback', t)))"</invocation><expect>"SEAM_DESIGN sections answered 7 of 7 | loopback stated True" -- the design answers all seven questions the face names, in a document that exists before the build; fewer than 7 is a design that leaves a question open and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-2"><invocation>python -c "import glob,io; fs=glob.glob('org/critical_paths/change_management/*amgt-resapp-seam*_deploy_completion.md'); t=io.open(fs[0],encoding='utf-8').read() if len(fs)==1 else ''; print('entries', len(fs), '| names safe-apply', 'safe-apply' in t, '| closed', any(w in t.upper() for w in ('STATUS: CLOSED','STATUS: COMPLETE','CLOSED AT','COMPLETED AT')))"</invocation><expect>"entries 1 | names safe-apply True | closed True" -- exactly one ledger entry for the seam's cloud build, naming the wrapper, closed before this read (G-16)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-2"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/check_e2e.py</invocation><expect>one line of the exact shape "E2E: ticker &lt;key&gt; status REQUESTED-&gt;FETCHING-&gt;LANDED in &lt;n&gt; s; raw objects 2; status.json LANDED" -- read back from S3 by this script (the status object's history and the raw prefix), for the ONE uncovered ticker named in the design; a terminal state of FAILED, a missing transition, or fewer than 2 raw objects is NOT met -- and a FAILED whose reason is "terminal signed out" is recorded as a finding, still NOT met, and never rescued by a sign-in</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-2"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/request_log.json')); print('unique securities requested by this order', len(set(l['securities'])))"</invocation><expect>"unique securities requested by this order 1" -- NEGATIVE: one uncovered ticker, the cost axis bounded at the cut (F2, G-24)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-2"><invocation>grep -r -c -i -E 'listen\(|bind\(|0\.0\.0\.0|--port|ngrok|reverse.?tunnel|ssm start-session.*portNumber' integrations/bloomberg/research/ infra/aws/terraform/research/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE and structural: nothing under the box-side module or the Terraform opens a listener, binds a port, or reverse-tunnels into this device; the box PULLS work and stays loopback-only</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-2"><invocation>comp-routes behaviors 2>&amp;1 | grep -c -E 'research|amgt'</invocation><expect>a count of 1 or greater AFTER the apply -- the request path's route is DECLARED in the estate's source of record and comp-routes sees it; 0 means the build reached AWS without reaching the record (a drift the DESIRED-plane tool cannot see) and is NOT met</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-s-2" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, a census): the design answers every question PART V's precondition asks, before anything is built.
- **AC2** (mechanical): NEVER-2 on the cloud act.
- **AC3** (mechanical, read from S3): the seam works end to end once, with the status object as the witness and the raw bytes as the proof.
- **AC4** (mechanical, NEGATIVE): one new security.
- **AC5** (mechanical, NEGATIVE, structural): the box stayed loopback-only. The bound the README exists for.
- **AC6** (mechanical): the route is in the record, not only in AWS.
- **AC7** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): is the chosen shape honest about its latency and its failure modes -- would an analyst who typed a ticker while the terminal was signed out see a MARKED failure with a reason, or a page that looks like it is still fetching an hour later?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- poll the status object with a cap.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q2, `AMGT-s-2` alone; slot ~2 spawns after `AMGT-s-1` and `AMGT-s-6` land.
**Provenance:** the cell text is the decomposition's row verbatim. Two deliverables inside one engine (design, then build) are cut as separate criteria, never one compound one. The decision to BUILD the chosen shape in this order rather than hold it for a ratification is deliberate: PART V requires that "any design must say how"; it does not name an approver, and an agent-made approval gate is forbidden (CLAUDE.md s.2). The design is graded at L9 (AC7) and a wrong shape comes back in the round-N analysis as a recut.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, C1=23 C2=6 C3=12 C4=20 C5=335, 25 gates armed, none this project's; G-16, G-19, G-20, G-22, G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 167 Lambda / 21 EC2 / 1084 operations / 304 gaps; this cell's grants are sqs + s3, stated in the design and checked with comp-iam service at the build
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors, DESIRED plane, NO desktop origin -- the finding this cell exists to answer; re-run after the apply (AC6)
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this order
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; no queue or route for this project exists yet
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast OWED at the build and named in BOUNDS (an API Gateway route changes the portal's request path); not run at the cut against a change that does not exist.
