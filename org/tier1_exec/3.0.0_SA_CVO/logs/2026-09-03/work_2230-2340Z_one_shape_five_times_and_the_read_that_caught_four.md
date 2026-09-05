# 3.0.0_SA_CVO~Z -- work log 2026-09-03 22:30-23:40Z: one shape five times, and the read that caught four of them

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake and compile. **Prior log:** `work_2155-2230Z_*`. **Push state as read:**
local HEAD ee5784e737; `git ls-remote origin SITEZ` read 001709c96e at 21:55Z and is NOT re-read here, so the
push state is **UNREAD at this vintage** rather than assumed unchanged. **Channel:** 93 rows at the open,
**106 at the close** -- five worker lanes filing concurrently.

## 1. Intake, and how much of it needed nothing

Thirteen rows arrived. **Most needed nothing from this seat and that is the correct outcome**, but two are
worth naming for quality rather than for any defect: **Z-S99**, where an author refuted its OWN trap from
twenty minutes earlier with `aws logs test-metric-filter` and a negative control, and found that the remedy it
had recommended was the LOOSER instrument -- a correction that ran toward tightening the control on the one
alarm anyone will read. And **Z-S100**, the best-evidenced row on this channel: three planes, a falsifiable
secret-envelope check, and a positive control on a known-two-slot secret proving the probe could see slots at
all.

**Z-S99's diagnosis is the transferable part:** every fact in its trap A was measured and TRUE -- the log
format, the prefixing, the emit site -- and the conclusion was false, because the step from those facts to
"the pattern will not match" was **a belief about matcher semantics that was never itself measured**. The true
facts made the false conclusion feel evidenced.

## 2. A check that came back clean, and stopped there

TO-OP-S-6 builds two CloudWatch alarms and an SNS topic, and CLAUDE.md carries a standing veto on exactly
that. I checked the clearance chain: the face names Andrew's word at L2 via FWD-4, the decomposition's OP-s-6
cell records `moratorium exception FWD-4 ONLY`, and the face scopes the exception hard with a tripwire --
*"if you find yourself adding a third alarm, you have left the exception -- that is a ROW and a question,
never a judgement call."* **Three reads, no finding, stop.** Recorded because a check that returns clean is a
result, and because the next seat should not have to re-run it.

## 3. Z-S105 @9e2b6a84d6 -- the rotation surface is 25, not 2

Z-S100 gated TO-OP-S-10 correctly and said its consumer population might exceed two, marking liveness out of
scope. That is answerable from outside the face. **201 live Lambdas (NextToken absent -- a real denominator);
`lambda-execution-role` 13 and `opal-portal-lambda-role` 12; BOTH roles grant `GetSecretValue` on
`opal/auth/jwt-public-key`.** So 25 functions CAN read the key against a face denominator of 2.

⛔ **A GRANT IS NOT A READER and the row says so** -- 25 is an upper bound, not a count. The outliers are
CLEARED rather than counted, because an overstated surface misleads exactly as much as an understated one:
`ticket-center` and `partners-api` are prose COMMENTS, and `cross-firm-secret-deny.tf` is a DENY.

**Why it is the shared-dependency case:** the capability lives on ROLES many functions share, so a check
scoped to the two modelled consumers cannot see it by construction. It composes with Z-S100's own finding of a
SHARED Python module caching the key in a single scalar -- any consumer reaching it that way is single-slot by
construction. **The disarm is not "read all 25": it is that the re-cut STATE its denominator and how it derived
it.**

## 4. Z-S106 @ee5784e737 -- the compile, which is the part no face can do

**One shape, five instances, three task orders: a control deployed, well-formed, healthy on every
configuration probe, and inert.** An authorizer whose key can never arrive (Z-S83, **the only one that
shipped**); a topic with no subscriber (Z-S97); an alarm dimensioned to match no metric (Z-S98 trap B); a
distribution no visitor traverses (Z-S101); an ACL whose only enforcing rule matches an empty set (Z-S102).

**Each seat named the shape inside its own face and two cited each other -- and nobody had a denominator**,
because no single face can produce one. That is what L8 is for.

⛔ **Z-S98's trap A is EXPRESSLY EXCLUDED from the count**, withdrawn by its author at Z-S99. A class row that
inflates its own denominator is the defect it describes.

**The common cause:** the control's effect depends on a second fact the configuration plane does not carry --
a subscriber, a dimension, a route, a non-empty set, an injectable header -- and **it is a different fact every
time**, which is why per-face checks keep finding it late and per-face fixes cannot generalise. **The process
finding for L10:** the instrument that caught four of five was the same mandated **pre-write re-grounding**,
which also produced Z-S100, Z-S103 and Z-S104 the same night. Offered and not ruled: a control face should
carry at least one criterion only an EXERCISED control can satisfy -- the round already contains the model in
S6-AC2's staged burst and S2-AC2's probe pair.

## 5. Corrections to this seat's own carriers

Z-S95 corrected the residual from four live POST writes to **FIVE**. **This seat's log was the fourth carrier
and its memory file the fifth** -- both inherited the number the same way the face amendment and the commit
message did: **quoting the summary line four lines above the enumeration that contradicts it.** Corrected in
place @c44432fe98 and in memory, original text left standing. **An undercount never announces itself.**

**Three MUTATED warnings** (Z-S95, Z-S97, Z-S101/102) -- all measured, all benign, no committed row's DATA
differing in any of them. The deterministic cause is now banked: an append rewrites the separator after the
row that used to be last, so **suspect your own last write before suspecting a peer**. Not re-measured per
instance after the class was established.

## 6. State

**106 rows, 32 this seat's.** Five lanes filing concurrently; the mechanical gate held the channel through
eight consecutive contended probes without ever racing a peer's staged write. **The one blocked item is
unchanged**: the four round-1 closure rows (S2, S11, S13, S17); gate here still `c3ef3a2530`, 0 occurrences of
`REMEDIATED`.

**Worth carrying to L9:** two ARMED items now wait on a fact only a person holds -- Z-S97 needs one email
address, Z-S101 needs a registrar credential or authorization to migrate a zone. Neither is escalated by this
seat; both sit one step up the lane with the issuer, and neither has exhausted that step.
