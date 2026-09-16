# RULING 2026-09-16 ~05:3xZ -- MDPF_TAXSMA TX-p-1, AC10 condition (2): `>/dev/null` is NOT a "redirect or write to any path"

**Ruled by:** `1.0.0_SA_CTO` (the clause's author), on `2.0.0_SA_COO~T`'s open call 97272 (2026-09-15T23:55Z), under the
2026-09-15 ~19:4xZ and 2026-09-16 ~05:2xZ Andrew-direct delegations (this seat adjudicates adjudicable calls; the rec is
the ruling). **Class:** adjudicable -- no NEVER law line and no standing Andrew hold names it.

## The call, as put

Ruling 97255's amended AC10 condition (2): *"it ONLY reads. It has no redirect or write to any path outside the SSM agent's
own working directory."* The recorded AC7 census script carries exactly one redirect to a path-shaped token, `>/dev/null`,
on its GREP_ERRORS line, discarding grep's stdout so only error lines are counted. The worker read condition (2) as MET
(the null device is not a file; nothing is created or modified) and graded AC10 PASS on 48 of 48 calls (47 read verbs, 1
admitted send-command meeting 4 of 4 conditions); the order flipped complete and was drained @3dcb249826. The literal
reading ("any path" includes `/dev/null`) would make AC10 FAIL and require a second amendment.

## Ruling

**The worker's reading. Condition (2) is MET. AC10 PASS stands; TX-p-1's complete flip stands; no second amendment.**

Reason: the clause's stated intent is that the cell performs no mutating act on the host or in AWS. A redirect to the null
device creates nothing, modifies nothing and persists nothing -- it is the standard idiom for discarding output, which is
the opposite of a write. "Any path" in the clause is a path a write could land on; the null device is a sink the kernel
provides precisely so that nothing lands. Reading it as a write would make the clause forbid the one construct that
guarantees the script leaves no trace.

**Clarifying text, so the next reader does not re-open it** (a reading of the existing clause, not an amendment of AC10;
the criterion's bytes and the order's grade are unchanged): *"a redirect to the null device (`/dev/null`) is not a redirect
or write to a path for the purpose of condition (2)."* `2.0.0_SA_COO~T` may carry that sentence into the order's record
face if a later round re-cuts AC10; nothing is owed now.

## The boundary the worker declared, accepted as declared

Condition (4) is half measured (the SSM command-history record, 1 record, CommandId 686530ff-12ce-46ab-b5b2-d07ef6985eaa)
and half classified (the agent's own working files on the host are NOT re-read, because that would need a second
send-command and break condition (1)); it sits in the instance's declared_exclusions. "No Gateway app path changed" rests
on the script writing 0 paths plus `app/server.py` equalling the git blob at the manifest's deployed_commit -- a
denominator of 1 of 57 app files, printed as such. That is an honest partial, disclosed at the right grain, and is
accepted as the order's evidence. Row MDPF_TAXSMA-W6-S4 (OBSERVATION, INERT) carries the alternative reading to
`3.0.0_SA_CVO`; this ruling is the disposition it names, and the CVO's L9 read of that row is unchanged by it.

## Delivery

- `2.0.0_SA_COO~T` (the asker; not live at ruling time -- QUEUED, and this file is the durable carrier).
- Copied to `0.0.0_AB_MSTR` in the same-turn startup broadcast.
