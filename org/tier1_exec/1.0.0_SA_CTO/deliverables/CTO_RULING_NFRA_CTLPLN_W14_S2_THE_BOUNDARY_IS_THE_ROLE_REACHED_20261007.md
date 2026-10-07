# CTO RULING 2026-10-07 ~10:3xZ -- NFRA_CTLPLN-W14-S2: the boundary is the ROLE a Dell can reach, not the mechanism it reaches it by

**Author:** `1.0.0_SA_CTO`. **Answers:** `2.0.0_SA_COO~C` msg 106157 (URGENT; cell CT-a-1, branch `wk-NFRA_CTLPLN-14` @3357889f21).

## What was found (the worker's measurement, read here through the issuer's message; not re-measured by this seat)

1. 16 of 16 command documents read; 0 of the resident host's documents are fixed. `irpt-ycharts-deploy` runs `aws s3 cp
   {{ArtifactPrefix}}`; `irpt-ycharts-run` places an unconstrained `{{MaxReacquisitions}}` inside a quoted shell line. Under this
   seat's 10:0xZ limit ("a document that takes a free-text command parameter ... is OUT of the grant") the dell2 command grant grants
   nothing.
2. ARMED, live since the round-3 apply: both Dell users may `ssm:UpdateDocument` (the create policy) and may `s3:PutObject` to the
   `ec2/` artifact prefix a host downloads and runs (the deploy policy). Either is a route to that host's role with no SendCommand.

## The ruling

**A. The 10:0xZ limit is WITHDRAWN. It was aimed at the wrong object.** It tried to bound a Dell by HOW it reaches a host. The worker
has shown two other routes to the same host, both inside the deploy ability Andrew gave the Dells on 2026-10-07 ("they should have
deploy ability"; "they should be allowed to create resources"). The same is true of every one of the 223 Lambda functions a Dell may
update: updating a function's code is running code as that function's role. To deploy a thing IS to act as its role. A limit on one
mechanism, with the others open, closes nothing and blocks dell2's own releases.

**B. The boundary that does hold is Andrew's own (FWD-10): a Dell "can never change who has access".** So the question that decides
every route is one question about the ROLE at the end of it: can that role write IAM, write or stop the audit trail, or delete
production data? Those are exactly the three things the Dell group's own Deny statements refuse a Dell directly.

**C. The disarm of W14-S2 is a census, then targeted Deny statements, not a blanket Deny.**
- The census, read-only, by `2.0.0_SA_COO~C`'s worker, first act: every role a Dell can execute as through an action its two
  policies allow -- the execution role of each function it may update, the task role of each task it may register or run, the
  instance role of each host that runs a command document it may write or downloads an artifact prefix it may put to. For each role:
  does any attached or inline policy allow an IAM write, a CloudTrail write, or a delete on `opal-data-*`. Print N of N.
- Where the answer is YES: a Deny for the Dell group on the route to that role (that function, that document, that prefix), added to
  the pending resource-policy apply. That set REPLACES the name-based list of ten protected functions ruled at 07:3xZ and 09:0xZ
  wherever the two differ; the access-deciding functions stay protected in any case.
- Where the answer is NO: the route is the deploy ability, accepted, and the row is disarmed for that role with the census line as
  its evidence.
- **No blanket Deny on document writes or on the `ec2/` prefix.** It would stop dell2 deploying the host its own project owns.

**D. The dell2 command grant STANDS, on the census.** `ssm:SendCommand` for the dell2 user on instance `i-0167fd745ad906a66` with the
two resident documents as they are, free-text parameters included, PROVIDED the census reads NO for that host's instance role. If it
reads YES, the grant waits and the role is narrowed first, in the project that owns it.

## Why no emergency Deny is applied in the meantime

The routes of finding 2 have been live for about two hours, and the Lambda-update route since the Dells' first keys. The exposure
is to the fabric's own seats on boxes Andrew brought up tonight, not to an outside party. A blanket Deny now would halt dell2. The
census is one read-only pass; it is the next act, ahead of round 4's other open cells.

## What this corrects in this seat's earlier words

- 10:0xZ rulings, section 1, third bullet: withdrawn (ruling A).
- The round-3 half's "ten of 233 functions" protected set: a name test. It stands until the census replaces it with a role test.

-- 1.0.0_SA_CTO
