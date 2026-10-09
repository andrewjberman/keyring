# CTO ruling -- fold UB-48b3 (ETFS_RIVALS) and UB-cbf8 (MDPF_SECHIST) into ONE site-Z Terminal sign-in check

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:0xZ, on `4.0.0_SA_CRO~DELL1` msg 1624. UB-ea48 (AMGT_CORPUS) benefits from the
same check but is not folded.

1. **One act, before 10:45Z:** confirm that the site-Z Bloomberg Terminal session is signed in and answering. It serves the 11:00Z
   RIVALS vehicle run, SECHIST's 07:00 ET (11:00Z) pull and the AMGT 13:00Z fire. Both unblock files cite this one act. Neither
   carries its own.
2. **Owner: site Z names it.** The act is site-bound. Site Z's four per-project lanes hold no act until Andrew answers (site Z
   `1.0.0_SA_CTO~Z` msg 32344), so dell1 does not address a lane. The ask goes MSTR to MSTR (Rule 32): `0.0.0_AB_MSTR~DELL1` to
   `0.0.0_AB_MSTR~Z`, which names one owner and the check's record path.
3. **Not metered.** A sign-in check reads session state and requests no security fields, so it is not a Bloomberg draw and does not
   count against MDPF_DEMQUE's queue. If the check requests any field (for example, a test quote), that is a draw and goes through the
   queue as a quoted request.
4. **If the check fails, or no record exists by 10:55Z:** the 11:00Z runs do not draw. Each project files one surprise row naming the
   missed run. No retry outside the queue.
