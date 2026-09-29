import concurrent.futures,csv,datetime,io,json,pathlib,sys,time
import requests
sys.path.insert(0,str(pathlib.Path.cwd()))
from lib.trading_calendar import trading_days_between,calendar_source
sys.stdout.reconfigure(encoding='utf-8')
OUT=pathlib.Path('.runtime/amgt-reconn-daily-census-20260929/gqgu');OUT.mkdir(parents=True,exist_ok=True)
dates=trading_days_between('2025-07-14','2026-09-28')
def fetch(d):
 p=OUT/(str(d)+'.json')
 if p.exists():return json.loads(p.read_text())
 url='https://gqg.filepoint.live/assets/data/SEI_GQG_Tradedate_Holdings_'+d.strftime('%m%d%Y')+'.txt'
 row={'requested_date':str(d),'url':url,'at':datetime.datetime.now().astimezone().isoformat()}
 try:
  r=requests.get(url,timeout=25);row['http_status']=r.status_code
  if r.status_code==200:
   vals=list(csv.DictReader(io.StringIO(r.content.decode('utf-8-sig')),delimiter='|'))
   selected=[x for x in vals if x.get('fund_ticker','').strip()=='GQGU']
   row['rows']=len(selected);row['internal_dates']=sorted({x.get('date') for x in selected})
   row['weight_sum']=sum(float(x.get('percent_of_net_assets') or 0) for x in selected)
   row['date_matches']=row['internal_dates']==[d.strftime('%m/%d/%Y')]
   if selected:(OUT/(str(d)+'.txt')).write_bytes(r.content)
 except Exception as e:row['error']=str(e)
 p.write_text(json.dumps(row,indent=2),encoding='utf-8');time.sleep(.15);return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 rows=[]
 for row in pool.map(fetch,dates):
  rows.append(row)
  if len(rows)%25==0:print('GQGU',len(rows),'/',len(dates),'valid',sum(x.get('date_matches',False) for x in rows),flush=True)
(OUT/'summary.json').write_text(json.dumps({'calendar':calendar_source(),'count':len(dates),'results':rows},indent=2),encoding='utf-8')
print('GQGU COMPLETE',len(rows),'valid',sum(x.get('date_matches',False) for x in rows),flush=True)
