# 3.0.0_SA_CVO~Z -- work log 2026-09-03 21:55-22:30Z: a field that is nearly right, and the grain it hides in

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_2045-2155Z_*`. **Push state as read:** local HEAD
16e567f53e; `git ls-remote origin SITEZ` 001709c96e at 21:55Z, so everything below is LOCAL and the claim ages
the moment an integrator runs. **Channel:** 89 rows at the open, **93 at the close**, 28 this seat's.

## 1. Z-S90 arrived and needed nothing from this seat

`0.7.0_AE_CloudOps~S` stopped TO-OP-S-20 at its own GO condition. The best thing in it is a refusal: a
SUBSTRING filter over the gateway WAF log matched **2,990** records where the EXACT paths matched **2**, over an
identical 111,904 scanned, and the substring list is dominated by internet scanner probes headed by one address
with 2,357 hits. **Building the partner allowlist from that census would have ALLOW-LISTED the scanner into the
control C-4 exists to protect** -- a lockout-prevention control turned into a persistent allow for hostile
traffic. It also names a second, independent blocker: no field in that source attributes an address to a firm.

Nothing needed correcting. The row measured before building, printed its denominators, and stopped.

## 2. THE NEAR-MISS, which is the part worth keeping

Z-S90 cites in passing that `aws-waf-logs-opal-cloudfront` holds **storedBytes 0**. That group is TO-OP-S-5's,
and TO-OP-S-5 is COMPLETE with 7/7 PASS -- the exact profile this seat had established an hour earlier as the
most invisible place a defect can sit.

Measured: logging **is** configured on the sole CLOUDFRONT-scope ACL, no `LoggingFilter`, and the ACL allowed
**1,746 requests** over 09:22:09Z-22:10Z (12 hourly datapoints; dimension names taken from `list-metrics` rather
than guessed, because a wrong dimension returns an empty series indistinguishable from a true zero).

**1,746 requests against 0 bytes is configured-but-not-delivering** -- a THIRD instance of the
applied-versus-exercised gap, in a completed face. The row was half-written.

⛔ **The stream probe refuted my own hypothesis.** `describe-log-streams` returns one stream with
`lastEventTimestamp` **20:15:56Z**, two hours old, with a POSITIVE CONTROL in the same call (the gateway group,
2 streams, 20:47:25Z) so the probe demonstrably separates a live destination from a silent one. **It was
delivering the whole time.** Filed on `storedBytes` alone it would have been a false alarm against a completed
face, one hour after this seat filed a row about exactly that overclaim. **The discipline that catches it is not
scepticism about other seats; it is running the control on your OWN reading first.**

## 3. What survived is better than the finding I nearly filed -- Z-S92 @1ae00e35f5

Z-S90 offers the issuer three options, and option **(b)** -- *"the CloudFront WAF group is empty ... so OP-s-5's
coverage may need extending"* -- rests on that same zero. It is mis-premised. The group is live, and a partial
page (**91 events, nextToken still present, so NOT a census and no count a denominator**) shows it already
carries **/auth/login, /auth/me, /auth/refresh, /auth/mfa/send and /auth/mfa/verify**, including a genuine
browser POST sign-in on opalinvest.dev. Against **2** `/auth/login` in 19.7 days on the gateway surface.

**So the sparseness remedy is TIME, not construction: (a) and (b) collapse into WAIT, and commissioning (b)
would have ordered work that already exists.** Z-S90's attribution blocker is CONFIRMED on this source too --
no cookie present at all, and a sign-in's credentials ride in a POST body WAF records the size of and not the
contents -- so option (c) remains the only route to attribution. **Sent as a pointer BEFORE the choice.**

Z-S90 is not re-graded, stays BLOCKING/ARMED, and its disarm is not this seat's.

## 4. The issuer took it, corrected an L4 routing -- and offered a sharpening that is a GRAIN error

20006: the refutation confirmed at that seat; and it had at 22:04Z told L4 the sign-in surface *"has no usable
log at all"*, **relaying the `storedBytes` reading upward as established without running one call against it**
-- its own second relay-without-measuring of the day. Corrected at 22:19Z.

Its sharpening: *"storedBytes reads 0 on the GATEWAY group too, the one holding 111,904 records ... it is not a
delivery signal at all on this API."* **Measured here, that is right about one object and wrong about another:**

```
describe-log-GROUPS   storedBytes    cloudfront 0  |  gateway 84,723,696     <- the field WORKS
describe-log-STREAMS  storedBytes    all 3 streams 0, incl. the 111,904-record one
```

**Same field name, two objects, opposite answers.** At the stream grain the observation holds exactly and is the
stronger trap. At the group grain it fails: 84.7 MB on the very same gateway group, so the CloudFront zero is
the small-and-lagging value Z-S92 described rather than a dead field. **Z-S93 @16e567f53e**, filed rather than
left in a message because 20006 said it was banking the sharpening: carried at the group grain it would license
dismissing a future NON-ZERO reading that is real, and **a bound with the wrong subject outlives the
conversation that produced it.** A narrowing, not a reversal.

**NOT ESTABLISHED and recorded as such:** whether the stream-level field is a documented deprecation. That needs
AWS documentation and egress is excluded without Andrew's word. The measurement stands without the explanation.

⭐ **AND THE PART THE ISSUER GOT RIGHT THAT THIS SEAT MISSED:** the negative control was sitting inside the
FIRST output. Either response lists a known-full group beside the subject, which answers "can this field be
non-zero?" without a second call. **I fetched another call instead of reading the output I already had.**

## 5. Memory and state

New: `storedbytes-is-not-a-delivery-oracle` (written, then AMENDED within the hour with the two-grain finding
and the read-your-first-output lesson, rather than left half-right). Index line rewritten.

**Rows this window: Z-S92, Z-S93.** Both answered by the issuer inside minutes. **The one blocked item is
unchanged:** the four round-1 closure rows (S2, S11, S13, S17); gate here still `c3ef3a2530`, 0 occurrences of
`REMEDIATED`. Cost: nothing live.

**The through-line of the last two windows, worth stating once:** three times now the useful act was checking a
number that everybody had already read and nobody had controlled -- an attachment count that was not a
reachability count, a disarm that named a plane that did not exist, and a byte count that was not a delivery
signal. **None of them was hidden. All three were sitting in output somebody had quoted.**
