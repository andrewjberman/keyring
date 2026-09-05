# 3.0.0_SA_CVO~Z -- work log 2026-09-04 02:10-04:00Z: a zero from a probe that could not match

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake and compile. **Prior log:** `work_0050-0210Z_*`. **Channel:** 122 ->
**134 rows**, 38 this seat's, ids contiguous. **Push state:** local HEAD acee77c19a; `origin/SITEZ` last read
001709c96e, **UNREAD at this vintage**.

## 1. Twelve rows in, one filed

Intake was heavy and almost all of it needed nothing. Rows worth naming for quality rather than defect:
**Z-S124** caught a liveness oracle reading `Sum=0` on the busiest consumer in its set -- the metric does not
EXIST for Lambda@Edge in the queried region -- **by a positive control**, and would otherwise have killed a
live function as dead. **Z-S132** is a commissioned sweep done properly: 62 of 62 criteria across 11 of 11
faces, yielding ONE finding and saying so, with the other 61 recorded as sound or already amended.
**Z-S134** proves a repo source IS production by two clean builds byte-identical to each other and to the
2026-01-08 deployed artifact, 12 of 12 files by sha256.

**And the most consequential security finding of the round so far, Z-S127:** a symmetric `JWT_SECRET`, the same
60-character value, in **cleartext Lambda environment variables** on both `trade-auth-handler` and
`trade-authorizer` -- readable by anyone holding `lambda:GetFunctionConfiguration`. Pre-existing, on a
different pipeline, out of the finding face's scope, routed to the issuer to place. Not escalated by this seat;
the chain is live and correct.

## 2. Z-S133 @acee77c19a -- and the part that matters is the zero I did NOT report

Z-S131 named a **split-drift** class (PRD v0.9 split one bucket into a log destination and an evidence store;
artifacts still name the pre-split bucket) and called itself the second instance, citing Z-S114 as the first.
Two instances make a pattern; **what neither row has is a denominator**, which is the compile seat's job.

**PROJECT TREE -- sized and closed.** The drift signature returns 6 hits which resolve completely: **1 real**
(`prd/NFRA_OPSEC202609_PRD.md:321`, the line Z-S131 found), 3 being Z-S131's own row quoting it back, and **2
FALSE POSITIVES on `opal-data-security-access-logs`** -- a DIFFERENT bucket whose name is a superset of the one
searched. ⭐ The raw count of the bucket name in the project tree is **180 across 22 files and almost all of it
is CORRECT**, because that bucket genuinely IS the log destination. **Subtracting the legitimate cases is what
makes it a denominator rather than a scare number.**

**INFRA -- NOT SIZED, AND MY PROBE IS THE REASON.** The same signature returned **0 hits over 6,388 scanned
files**. ⛔ **THAT ZERO IS FALSE AND I NEARLY REPORTED IT.** Positive control, run because a zero from a probe
is worthless without one: the KNOWN Z-S114 instance is at `infra/aws/terraform/opsec/iam.tf:62` and `:72`,
inside the path I had just swept, and my probe did not return it.

**Two independent reasons, both fatal, both measured at source:**
- `Sid = "EvidenceStoreObjects"` is at `:62`; its `Resource` is at `:69` -- **seven lines apart**, and
  comp-find matches within a line.
- ⛔ **The bucket is NEVER WRITTEN AS A LITERAL.** `:69` reads `Resource = "${aws_s3_bucket.data_security.arn}/*"`.
  It is a **terraform resource reference**, so a literal search for the bucket's NAME is structurally incapable
  of finding this grant at any line span -- and every future instance written in idiomatic terraform is
  equally invisible.

**So "two instances" is not a count; it is the number found so far by seats who happened to read those files.**

⛔ **SECOND NAME-SEARCH-VERSUS-MECHANISM ERROR OF THE NIGHT.** At Z-S108, four hours earlier, a literal search
for `jwt-public-key` missed a grant written on the prefix wildcard `opal/auth/*`, and the banked lesson was
that a permission question needs the authorization model rather than a name. Here the same instrument missed a
grant written as a resource REFERENCE. **Different mechanism, identical failure -- the thing that matters does
not spell the name -- and the repeat came inside a row about denominators.**

**Reporting a failed probe rather than a clean plane is the whole value of the row:** the alternative was
telling three seats the infra plane was clear, converting a working class into a closed one, on a measured
number that was wrong.

## 3. Two class rows NOT filed, and why

**Un-failable oracles** (Z-S129's xmlrpc 200 that means both authenticated and rejected; Z-S124's absent
metric; my own `storedBytes`) -- **declined.** That is the DISCRIMINATION axis of the evidence law, and Rule
22a is already the home for instrument traps. Each trap is durable in its own row.

**Propagation** (Z-S134's map entry reaching a decomp row, a face and two GO messages; tonight's undercount
reaching five carriers; the `storedBytes` misreading reaching an L4 routing) -- **declined.** Already estate
law, and three instances with different carrier counts is not a denominator.

⭐ **The two class rows filed tonight were earned because they named shapes the law did NOT already carry.** A
third or fourth restating it would be volume, and the seat that files a class row for every pattern stops being
read.

## 4. Carried forward, not filed

Z-S130 corrected the "seven live lambdas" premise to **two live, five dormant**. That figure appears in this
seat's Z-S122 as a parenthetical, **correctly attributed to Z-S112** -- so the correction is reachable through
the citation chain, and the claim it supports (a grant in a DIFFERENT terraform root) does not depend on it.
**Correct what changes a conclusion, attribute what does not, and let the citation do the work.**

## 5. State

**134 rows, contiguous, 38 this seat's.** Nothing waiting on this seat. **The one blocked item is unchanged:**
the four round-1 closure rows; gate here still `c3ef3a2530`, 0 occurrences of `REMEDIATED`.

⭐ **Three of tonight's findings have moved from rows into standing practice** -- the acceptance criterion
amended at Z-S117 to require a full population with its denominator, disarm records now stating their own
scope (Z-S84's finding), and the issuer commissioning the un-failable-criteria sweep that became Z-S132. **That
is where a finding stops depending on anyone remembering it.**
