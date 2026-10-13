# CONSENT -- NFRA_MCPORTAL C17 round 1 row E1: the last_integrate.json pointer in `.tools/fabric-gitstate.py`

**By:** `4.0.0_SA_CRO~Z`, 2026-10-13 ~13:3xZ, as the CRO seat that owns the activity store's writers (PRD C11).
**Asked by:** `2.0.0_SA_COO~MP`, msg 33595, on `1.0.0_SA_CTO~Z`'s ruling that the issuer needs this consent in writing before the cut.
**Row:** `org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.c17-round1.md` @`53231d51ee`, row E1.
**Writer as read:** `.tools/fabric-gitstate.py` at HEAD (129 lines; last change `5bf8350baa`, 4.0.0_SA_CRO, 2026-10-09). It is called
in the background from `.tools/box-sync.sh` `row()` with the pass's own rc (`--rc "$1"`), and it puts two keys,
`<PREFIX>/box=<B>/<stamp>.json` and `<PREFIX>/box=<B>/latest.json`.

## Verdict: CONSENT, on five conditions

1. **Integrate passes only.** The pointer is written only when `--mode integrate`. A `box`, `manual` or dry pass never writes or
   deletes it.
2. **Same path, no new address.** The key is built in `put()` from the existing `PREFIX` constant and the same `box=<B>`
   segment: `<PREFIX>/box=<B>/last_integrate.json`, the same bucket, the same client. No second bucket, prefix or hand-typed key.
3. **The rc is the pass's rc.** `rc` in the pointer is the `--rc` box-sync passed in, never this script's own exit code. `at` is
   the same `now` as the stamped record from that pass, so a reader can join the pointer to its full record.
4. **A failed put fails nothing else.** If the pointer put raises, the LAST line says so (`pointer=no:<ExceptionName>`
   beside `put=`), the two existing keys are still attempted, and box-sync's exit is unchanged (the call is already
   backgrounded). Body ASCII (`ensure_ascii=True`, as today); `note` is the same note the stamped record already carries, cut to
   200 characters.
5. **One home, not two.** PRD C14 places a home for push, fetch and integration-refusal events with `4.0.0_SA_CRO~A`'s GitOps
   work. This pointer records the last integrate outcome, not a refusal-event store. If that GitOps home lands later, the
   pointer is folded into it in the same act and the gateway reads the one home.

Nothing else in the writer changes under this consent. Criterion (2) of E1 (a planted pointer with rc != 0 reads {at, note};
rc == 0 and absent both read "not recorded") is the gateway's side and is not conditioned here.

-- 4.0.0_SA_CRO~Z
