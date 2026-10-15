// open_first.mjs -- /ui-walk: the order in which walk.mjs expands the closed <details> summaries of one scope.
// Pure: no DOM, no I/O. Used by exploreScope(); the contract is checked by
// org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_walker_open_first_check.mjs
//
// orderSummaries(texts, openFirst) returns a permutation of 0..texts.length-1:
//   - an index whose text (trimmed, lower-cased) equals an openFirst entry (trimmed, lower-cased) comes before every other index;
//   - matching indices follow the position of their entry in openFirst, then their original index;
//   - every other index follows in original order;
//   - an empty or absent openFirst gives the identity order; an entry that matches nothing changes nothing and does not throw.

const norm = (s) => String(s ?? '').trim().toLowerCase()

export function orderSummaries(texts, openFirst) {
  const list = Array.isArray(texts) ? texts : []
  const rank = new Map()
  const entries = Array.isArray(openFirst) ? openFirst : []
  entries.forEach((e, k) => {
    const key = norm(e)
    if (key !== '' && !rank.has(key)) rank.set(key, k)
  })
  const first = []
  const rest = []
  for (let i = 0; i < list.length; i++) {
    const r = rank.get(norm(list[i]))
    if (r === undefined) rest.push(i)
    else first.push([r, i])
  }
  first.sort((a, b) => a[0] - b[0] || a[1] - b[1])
  return [...first.map(([, i]) => i), ...rest]
}
