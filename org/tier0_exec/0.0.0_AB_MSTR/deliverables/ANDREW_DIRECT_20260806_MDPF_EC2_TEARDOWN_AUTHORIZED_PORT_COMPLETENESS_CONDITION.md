# ANDREW-DIRECT — 2026-08-06, site-Z MSTR terminal: MDPF EC2 teardown AUTHORIZED, conditioned on port completeness

**Recorded by:** `0.0.0_AB_MSTR~Z` · same turn, per `org/XXX.md` record+broadcast law
**Channel:** direct message at the site-Z MSTR terminal, 2026-08-06
**Resolves:** `projects/MDPF_PROPVALIDATION/04_VALIDATION_ROLLBACK_AND_OPEN_HOLES.md` §6 **H4**

## VERBATIM

> "Teardown is fine just need to make sure any necessary code on that ec2 is properly ported to the lambda."

Context of the ask: MSTR~Z surfaced H4 as the one item on the open-holes list that no measurement could
close — the 2026-08-05 ruling mandated one Lambda but explicitly did not authorize teardown, and whether
the 08-06 consolidation direction authorized **terminating** instance `i-02448edb624a7a7cf` and deleting
its EBS (as opposed to removing it from the production route) was a question about the scope of a
sovereign instruction.

## WHAT THIS SETTLES

**H4 IS RESOLVED. Physical teardown of the MDPF EC2 is AUTHORIZED.** The open-holes file's instruction
to "not perform irreversible physical deletion without a clear governing record" is satisfied — this
document is that record. `03_IMPLEMENTATION_PLAN.md` Phase 6 may proceed to physical termination, and
the closure template's `remaining irreversible teardown item:` resolves to **none**, once the condition
below is discharged.

## THE CONDITION, AND WHAT IT IS NOT

The authorization carries one condition in his words: **any necessary code on that EC2 is properly
ported to the Lambda.**

⚠ **THIS IS NOT A GATE AND MUST NOT BE BUILT AS ONE.** It is a correctness condition the sovereign
attached to his own authorization, not an approval step, co-sign, or hold. Nobody "clears" it; the team
discharges it with evidence and records that evidence. Manufacturing an approval checkpoint around it
would be the exact 2026-08-06 no-gates violation, on the very instruction that removed a blocker.

## THE HAZARD THIS CONDITION IS POINTED AT — and it is a real one, already measured

The condition is not a formality, because **deployed EC2 code is known to diverge from the repository**:

- `01_VERIFIED_FINDINGS.md` §10: the live publisher lacks the later roster-completeness logic, the Lambda
  source map "describes the publisher as the old build-alongside path, lists the old fenced role, and
  records an old deployed commit," and *"a blind rebuild from repository source would introduce a roster
  read against a missing object."*
- `04` **H8**: deployed source provenance must be reconstructed from artifact/hash/commit history —
  i.e. it is not currently known from the repo alone.
- `02_NEEDED_VS_NOT_AUDIT.md` §Dependency/package closure: the EC2 performs **runtime package
  installation**, so part of its effective runtime exists only on the instance.
- `02` §Provisional retirement names the exact shape of the risk: *"any EC2 script not directly visible
  in Stage 6 but used as a library or imported source."*

**Therefore: terminating the instance can destroy the only authoritative copy of code we have not yet
enumerated.** Termination is irreversible and EBS deletion takes the evidence with it.

## DISCHARGE MECHANISM (MSTR-specified; CTO~Z may sharpen, COO~Z decomposes)

1. **CAPTURE BEFORE TERMINATE.** Take a full inventory of the EC2's on-disk MDPF code and its installed
   dependency set, and preserve it (S3 per the EC2 code-deployment standard, and/or an EBS snapshot
   retained until closeout). This happens **before** any irreversible step, not as part of it.
2. **DIFF captured-vs-repo.** Every file present on the instance is either (a) byte-identical to a
   committed source, (b) ported into the `mdpf-gold-lambda` package closure and hash-tied in
   `BUILD_MANIFEST.json`, or (c) demonstrated unnecessary under `02`'s decision rule with its evidence
   recorded. There is no fourth bucket, and "not visible in Stage 6" is not evidence of unnecessary —
   `02` explicitly flags library/imported-source usage as the miss.
3. **CLOSE THE PROVISIONAL SET WITH THE STATIC GRAPH, not by name:** `wsb-49f-model-aua-daily`,
   `wsd-49f-partner-held-etf-daily`, writers/readers of `s3://opal-data-mdpf/mdpf/feeds/*`, and the
   feeder computations behind `mdpf_aggregate_aua.py`.
4. **STATE THE DENOMINATOR.** The discharge record reports files enumerated on the instance and the
   disposition of each. A port-completeness claim without the denominator of what was on the box is not
   a claim, and this is exactly the retrieval-control discipline in CLAUDE.md Rule 22.
5. **ROUTE RETIREMENT AND PHYSICAL TEARDOWN STAY SEQUENCED.** `03` Phase 6 order holds: prove the old
   route was not invoked, remove it, stop/detach — then terminate. Keeping old compute inert through one
   scheduled acceptance is rollback preparation (H9); it is only a shadow if it stays on an active path
   afterwards.

## SCOPE DISCIPLINE

His word authorizes teardown of the MDPF EC2 under a port-completeness condition. **It says nothing
about H10** (external/manual consumers of zero-reader S3 outputs) — that remains structurally
uncloseable and closes as a recorded limitation, never as a proof. Do not read this ruling as
authorization to delete S3 data; `03` Phase 6 is explicit that data is never deleted as part of route
retirement, and S3 versioning is load-bearing for rollback.
