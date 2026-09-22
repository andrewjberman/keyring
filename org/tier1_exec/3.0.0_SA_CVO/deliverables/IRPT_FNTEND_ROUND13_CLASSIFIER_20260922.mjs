import {readFileSync} from 'node:fs';
const src=readFileSync('scripts/ui-smoke.mjs','utf8');
const start=src.indexOf('const routeKeyCandidates = routeKeys => {');
const end=src.indexOf('// --fail <url-substring>',start);
if(start<0||end<0)throw Error('Source extraction boundaries absent');
const fn=new Function('readFileSync',src.slice(start,end)+'\nreturn checkKeyValidity;')(readFileSync);
const cases=[
 ['/api/scoped/investor-reporting/holdings/A-0001',true],
 ['/api/scoped/investor-reporting/holdings/A-0001/not-a-declared-operation',false],
 ['/api/scoped/investor-reporting/status/extra-junk',true],
 ['/api/scoped/investor-reporting/nonexistent-operation',false],
];
for(const [key,expected] of cases)console.log(JSON.stringify({key,expected,actual:fn([key],'src/pages/InvestorReporting/fixtures/smoke/default.json')}));
// A synthetic static-only control isolates static exact matching from the real status/{id} route.
const staticOnly=new Function('readFileSync',src.slice(start,end)+'\nreturn checkKeyValidity;')(()=>"export const WIRE_CONSUMED_ROUTE_KEYS = ['GET /api/scoped/investor-reporting/status'];");
console.log(JSON.stringify({control:'static-only-suffix',actual:staticOnly(['/api/scoped/investor-reporting/status/extra-junk'],'src/pages/InvestorReporting/fixtures/smoke/default.json')}));
