# SOVEREIGN CALL — OPAL_MDPFCLEANUP TO-4: deleting the legacy `json/mdpf/*` served keys

**Not time-critical today. Grounded on CTO ruling @fc74f8f6b4 (`docs/architecture/MDPF_PROVENANCE_CANONICAL_FORM_RULING_20260818.md` §3) + AE pre-stage 130752Z + COO's own three primitive reads 1308Z. CC: MSTR, CTO.**
**Deleting a served S3 key is your reserved act (NEVER#3 + your reserved categories). Nothing is deleted until you say.**

---

## THE CALL (one decision, when it is ready — not today)

**The condition we set on 08-15 for deleting the legacy `json/mdpf/*` keys — "zero direct hits over a
denominator-printed request count across seven fully-delivered CloudFront log days" — CANNOT BE MET,
AND NEVER COULD HAVE BEEN:**

1. **The instrument does not exist.** CloudFront logging on the portal distribution is OFF; S3
   server-access logging on `opal-data-portal-v2` is not configured; CloudTrail data events do not
   cover that bucket. There are zero log days to query. (AE found it pre-staging; COO re-read all
   three primitives; CTO concurred.)
2. **Worse — the right log would still have missed the reader that matters.** The canonical
   scheduled `mdpf-gold-lambda` ITSELF reads `json/mdpf/49financial/aggregate-aua-timeseries.json`
   on every 49F build and **fails loudly if the key is gone** (verified by CTO at the *executing*
   package bytes, not the repo). That is an internal Lambda read that never touches CloudFront. So
   "enable logging and wait a week" would have read CLEAN and been WRONG, and the delete would have
   broken the 13:30Z gold the next morning.

**So the served-key delete is HELD — not on your word alone, but on a hard prerequisite: the gold
Lambda's count-carry must first be re-pointed off `json/mdpf` (DS lane, to a gold self-carry from the
prior day's own vintage — same tier, no circularity), proven on a scheduled run; and one second
deployed reader (`opal-smartx-ingestion-pipeline`, currently untriggered) dispositioned. Only then
does the delete come back to you.** The rest of TO-4 (retiring the producer legs, the copy-manifest)
proceeds now — none of it touches a served key.

**Your one decision now:** whether to ALSO turn on CloudFront standard logging for the portal
distribution. **Be aware it is a detection build — moratorium-adjacent under your 07-28 standing
order — and, per (2), it would NOT have caught the reader that mattered here.** It has value only as
a general external-access instrument going forward, not for this delete.

- **(A) NO logging.** The delete rests on the STRUCTURAL oracle CTO defined: (i) route negative
  (no CloudFront route serves `json/mdpf` — already exercised at TO-0); (ii) principal census on
  LIVE IAM/bucket policy for `s3:GetObject` reaching `json/mdpf/*`; (iii) deployed-code reader census
  per principal at the executing packages — the read that found the two hits. Denominators printed on
  each leg. Ready when the re-point lands.
- **(B) YES logging.** Same structural oracle for THIS delete (logging cannot substitute for it),
  plus CloudFront standard logs enabled as a standing external-access instrument. Costs a build under
  the moratorium; buys nothing for the decision in front of you.

---

## RECOMMENDATION (COO; CTO concurs on the mechanism)

**(A) NO logging.** The structural oracle is the CORRECT instrument for "does anything still read this
key" — code and policy are the domain the question lives in; an access log is a proxy that, by
construction, cannot see the internal reader that already broke the condition. Enabling logging here
would be building a monitor because a monitor is the cheapest-feeling deliverable, and it would
answer the wrong question precisely — the pattern your 07-28 order names.

**What happens next without further word from you:** DS re-points the count carry (COO decomposes
into a dated TO under CTO's ruling; verified on a scheduled 13:30Z run); the smartx-ingestion global
read is dispositioned; the three-legged structural oracle is run with denominators; THEN this card
comes back to you with the results and the single yes/no on the delete. If any oracle leg is non-zero,
the delete does not come back at all — the reader gets named and fixed first.

**Two honest lines for the record:** (i) 08-15's "satisfiable on trailing history" was true of the
window arithmetic and false of the instrument — nobody checked the plane had a log; CTO and COO both
own that. (ii) It is the fifth instrument this week whose domain did not contain the question and
which read clean anyway (a plan verb hiding a stop/start; a screenshot that cannot see a relabel; a
cold seat that cannot see H1; a warm session that cannot see a token; a log that cannot see an SDK
read). Every one was caught by asking what the instrument could NOT have said, not by running it
more carefully.

---

## CORRECTED ROW (added 2026-08-18 ~1340Z — for your awareness, NOT an ask): the mdpf runner EC2 stop/terminate

Your 08-14 "all recs approved" covered a kill list whose census said the mdpf daily runner
(`i-02448edb624a7a7cf`) was K3-only. **That premise is falsified:** the runner is the execution host of
the KEEP accrual bridge (a scheduled Lambda starts it and SSM-runs a DS script on it, 1-8x/day incl.
today), and the K3 DLQ is the KEEP scheduled floor's dead-letter target. **So the runner stop/terminate
row is RETRACTED from tonight's work — your word on it was given on a wrong census, and we are not
spending it.** The rest of K3 (the legacy producer: rule + trigger Lambda + their IAM) is being killed
as ruled; the runner and DLQ stay until the two KEEP paths are re-homed (build acts, dated, owned).
Nothing for you to decide here; if you WANT the runner gone sooner, that is a re-home order, and it
comes back to you as its own card.
