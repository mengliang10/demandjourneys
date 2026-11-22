
"use strict";
const NS="http://www.w3.org/2000/svg";
const W=1840,H=4200;
const COLS={brand:"--brand",sg:"--sg",hk:"--hk",cn:"--cn",ops:"--ops",ok:"--ok",warn:"--warn",bad:"--bad",info:"--info"};
const MKTS=[
 {k:"sg",code:"ENGINE SG-01",name:"SINGAPORE",zh:"新加坡",dom:"Singapore website ◆",lang:"English · SGD · Singapore ◆",x:60,
  pos:"HQ & flagship. Mature repeat clientele, corporate/MICE adjacency, Virtuoso-grade servicing. Keys as the self-serve on-ramp.",
  kpi:[["24%","enquiry→book ◇"],["S$28k","avg booking ◇"],["1,200","Keys signups ◇"]],
  bud:30,budAmt:"S$540k",comp:"PDPA + DNC Registry — hard opt-in, consent proof, DNC scrub before calls",team:"HQ · Head of Marketing + Digital Mgr + specialist bench",
  plays:["Virgin Galactic media night → UHNW capture list","2027 Signatures launch dinner with Virtuoso partners","Keys member-get-member referral + Rewards"]},
 {k:"hk",code:"ENGINE HK-01",name:"HONG KONG",zh:"香港",dom:"Hong Kong website ◆",lang:"繁體中文 + EN · HKD ◆",x:640,
  pos:"Dense HNW outbound market. Traditional-Chinese storytelling, WhatsApp-first servicing, WeChat for trade & cross-border clients.",
  kpi:[["22%","enquiry→book ◇"],["HK$220k","avg booking ◇"],["900","Keys signups ◇"]],
  bud:25,budAmt:"S$450k",comp:"PDPO — direct-marketing notice, opt-out honored & logged",team:"HK Director + local pod · trade relationships",
  plays:["CNY & Golden Week outbound pushes (zh-Hant)","Belmond rail showcase — VSOE / Andean Explorer","Tatler & lifestyle-press authority features"]},
 {k:"cn",code:"ENGINE CN-01",name:"CHINA",zh:"中国",dom:"mainland China website ◆",lang:"简体中文 · CNY · BJ / SH pods ◆",x:1220,
  pos:"Closed-loop digital ecosystem. Xiaohongshu seeds desire; WeChat owns conversion, data and the advisor relationship. Next-gen affluent entry via Keys.",
  kpi:[["18%","enquiry→book ◇"],["¥180k","avg booking ◇"],["2,500","Keys signups ◇"]],
  bud:45,budAmt:"S$810k",comp:"PIPL — separate consent for cross-border transfer · WeCom keeps contacts enterprise-owned",team:"CN Marketing Mgr + Beijing / Shanghai pods (Frances Liu et al. ◆)",
  plays:["XHS 种草矩阵 — 西藏 · 新疆 · 极光 · 不丹 seeds","WeChat 直播 — 2027 精致小团 departure launch","WeCom 老客唤醒 — &Beyond 8-pay-7 offer ◆"]}
];
const CH={
 sg:[
 ["sg1","Instagram + Meta Ads","DISCOVER","Reels of not-googleable access; lookalikes off guest list","CTR · saves · CPL","30% of mkt ◇","plan","Paid + organic Instagram/Facebook. Creative from the shared KV kit; UTM-tagged into the one CRM. Audience: SG HNW 50+, family decision-makers, Keys lookalikes."],
 ["sg2","Google SEO / SEM · EN","CAPTURE","Own 'luxury tailor-made travel' + destination long-tails","Organic share · QS · CVR","25% of mkt ◇","mix","destination editorial already ranks destination guides (Madrid, Uyuni, Bhutan ◆). Plan: defend brand terms, buy high-intent non-brand, route to enquiry form + WhatsApp."],
 ["sg3","WhatsApp · SleekFlow","CONVERT","One inbox: WA + IG + Messenger; 75% open benchmark","≤15min response · book rate","10% of mkt ◇","plan","Consolidated team inbox with routing by market and specialist. Broadcasts to past travellers only with PDPA opt-in; 75% open benchmark from prior campaigns."],
 ["sg4","LinkedIn","B2B","Corporate / MICE / family-office partnerships","SQLs · partner deals","10% of mkt ◇","plan","Thought leadership from specialists; target family offices, private banks and corporate travel managers for incentive & buyout business."],
 ["sg5","EDM Newsletter","RETAIN","Monthly Stories digest + partner offers ◆ signup live","Open ≥35% · repeat rate","10% of mkt ◇","mix","Newsletter capture exists on site ◆. Plan: segment by past destination & tier; feature Virtuoso / Belmond perks; PDPA consent ledger."],
 ["sg6","Partner Events & PR","AUTHORITY","Virtuoso luncheons · VG media night · hotel showcases","UHNW leads · tier-1 hits","20% of mkt ◇","mix","Virgin Galactic story pages live ◆; media events proposed. Co-host with FSPP / Rosewood / Belmond; guest lists feed ABM-style named-account plays."]
 ],
 hk:[
 ["hk1","Instagram + Facebook","DISCOVER","zh-Hant creative; harbour-luxe visual language","CTR · saves · CPL","25% of mkt ◇","plan","Meta remains the open-web discovery layer in HK. Transcreated captions, not translations; Reels + carousel itineraries with HKD pricing."],
 ["hk2","Google SEO · 繁 + EN","CAPTURE","Dual-language Stories hub at /hk ◆; buy intent terms","Organic share · CVR","25% of mkt ◇","mix","The /hk site already serves zh-Hant and zh-Hans stories ◆. Plan: hreflang discipline,繁体 keyword map, SEM on outbound-luxury intent."],
 ["hk3","WhatsApp · SleekFlow","CONVERT","Shared SG/HK inbox, routed by locale & specialist","≤15min response · book rate","10% of mkt ◇","plan","Same SleekFlow backbone as SG; Cantonese/English bilingual routing. PDPO opt-out honored on every broadcast."],
 ["hk4","WeChat · Trade & Cross-border","B2B","Agent QR networking; mainland client hand-offs","Trade SQLs · referral GMV","10% of mkt ◇","plan","WeChat is the trade lingua franca: itineraries, roadshow invites, partner groups. Cross-border client hand-offs to CN pod with PIPL consent."],
 ["hk5","Expos & Partner Dinners","CONVERT","Travel expos · Belmond rail showcase · hotel dinners","Face-to-face SQLs","20% of mkt ◇","plan","High-touch conversion theatre: VSOE / Golden Eagle showcases, &Beyond safari evenings. Badge lists scanned into CRM within 5 minutes."],
 ["hk6","PR · Tatler / Lifestyle","AUTHORITY","Expert quotes, founder profiles, VG halo story","SOV · tier-1 placements","15% of mkt ◇","plan","Position specialists as the human answer to AI itineraries. Earned wins amplified via hk1 with permission."]
 ],
 cn:[
 ["cn1","Xiaohongshu 小红书","DISCOVER","种草 notes: 西藏 · 新疆 · 极光 · 不丹; KOC + specialist voices","Saves · search rank · DMs","35% of mkt ◇","mix","CN stories already exist in 简体 ◆. Plan: native 3:4 notes, authentic first-person specialist accounts, keyword-seeded for outbound-luxury search; DMs bridged to CRM."],
 ["cn2","WeChat OA + Mini Program","CONVERT","Official Account articles → Mini Program proposals & deposit","Follows · MP CVR · own data","25% of mkt ◇","plan","The conversion hub: long-form OA storytelling, Menu → Mini Program for itineraries, quotes in CNY, WeChat Pay deposit. All first-party data, PIPL-scoped."],
 ["cn3","WeCom Clienteling 1:1","RETAIN","Advisor-owned contacts; event-driven 老客唤醒","Repeat rate · response SLA","10% of mkt ◇","plan","Enterprise WeChat keeps the relationship with the travel company, not the individual advisor. Moments + 1:1 pushes keyed to past trips; &Beyond 8-pay-7 ◆ as reactivation hook."],
 ["cn4","Douyin Short Video","DISCOVER","Cinematic destination cuts; livestream teasasers","VV · profile visits · leads","15% of mkt ◇","plan","Reach engine for next-gen affluent. Hook in 3s, specialist face by 8s, CTA to WeChat search. No hard sell — seed, then let XHS/WeChat close."],
 ["cn5","Baidu SEO / SEM","CAPTURE","简体 destination long-tails on .cn ◆ + intent buys","Organic share · CPL","10% of mkt ◇","mix","mainland China website already publishes 简体 guides ◆. Plan: Baidu-native meta, MIP speed, brand-zone defense, SEM on 高端定制旅行 intent."],
 ["cn6","KOL / 直播 Livestream","AUTHORITY","Travel KOL fams + WeChat Channels 直播 launches","EMV · launch-day deposits","10% of mkt ◇","plan","Invite 2–3 vetted luxury-travel KOLs on a Finesse departure; content rights reused across cn1/cn4. Channels livestream for 2027 small-group launch."]
 ]
};
const FUNNEL=[
 ["Enquiry Capture","auto-ack ≤1min","WA · IG · form ◆","WA · WeChat trade","XHS DM→CRM · QR→WeCom","Every touchpoint lands in one CRM with UTM + market tag. CN Mandarin DMs get an instant bilingual auto-ack so no high-intent lead waits overnight."],
 ["Bilingual Routing","≤15min","EN specialist pod","繁 / EN / Cantonese","简体 pod · BJ/SH","Route by language, destination expertise and past-trip history. SleekFlow rules for SG/HK; WeCom assignment for CN. SLA board visible to all pods."],
 ["Specialist Design","first draft ≤48h","300+ yrs collective ◆","same bench, 繁 proposals","same bench, 简体 proposals","The human moat: specialists (ex-TV producers, wildlife obsessives ◆) craft not-googleable itineraries. AI drafts logistics; humans own judgment and access."],
 ["Proposal & Quote","valid 7 days","SGD · PDF + web view","HKD · PDF + web view","CNY · Mini Program view","Two curated options, one recommendation. Perk stack shown explicitly: upgrade, breakfast, US$100 credit, points stacking ◆."],
 ["Deposit & Contract","30% deposit","SGD transfer / card","HKD transfer / card","WeChat Pay via MP","Contract + insurance + visa checklist. CN payments stay inside the Mini Program; cross-border data transfer only with separate PIPL consent."],
 ["Concierge & Travel","24/7 in-trip","WA line + local guides ◆","WA / WeChat line","WeCom line · 24/7","Local guide network ◆, proactive check-ins, surprise-and-delight moments. Any issue escalates to the duty concierge within 10 minutes."],
 ["NPS · Referral · Rewards","NPS at T+3d","Keys Rewards + referral","Keys Rewards + referral","WeCom 唤醒 + Rewards","Post-trip NPS (target 65 ◇), testimonial capture ◆ pattern, referral ask, Keys Rewards credited on completed stays ◆ — the loop that feeds stage 1."]
];
const CONTENT=[
 ["Brand Brief","HQ · monthly","Quest platform, KV kit, offer calendar (8-pay-7 ◆, Belmond voucher ◆), 2027 Signatures priorities."],
 ["EN Master","Stories SEO · 8/mo","Long-form destination guides in the proven destination editorial format ◆ — Madrid, Uyuni, Bhutan, Tibet altitude, aurora solar-max."],
 ["繁體 Adapt","HK pod","Transcreation, not translation: Cantonese idiom, HKD pricing,繁体 proof points and local press hooks."],
 ["简体 Adapt","CN pod + 合规","简体 transcreation with claims review; sensitive-destination wording checked; PIPL-safe asset metadata."],
 ["Native Cuts","per platform","Reels 9:16 · XHS notes 3:4 with 种草 hooks · OA long-form · Douyin 15s cuts · LinkedIn expert posts."],
 ["Publish & Calendar","UTM registry","One calendar, three clocks: SG/HK open web + CN closed loop. Every asset tagged source/medium/campaign before flight."]
];
const STORIES=["Madrid First-Timers ◆","Salar de Uyuni ◆","Bhutan Forest-Bathing ◆","Tibet · Nyingchi Altitude ◆","Aurora · Solar Max 25 ◆","Xinjiang 12-Day ◆"];
const KEYS=[
 ["Discover","Stories · ads · perk pages","Guest lands on a collection page (Virtuoso, Fan Club, Bellini ◆) or a Stories guide with Keys CTA."],
 ["Create Account","email · member login ◆","Live signup flow on hotel membership portal ◆. Position as the entry tier for next-gen affluent — especially CN via WeChat MP entry."],
 ["Live Book","4,700+ hotels ◆","Real-time rates with chaincoded perks ◆: Virtuoso advance-purchase, Fan Club offers, upgrade + breakfast + US$100 credit."],
 ["Stay & Earn","Rewards + points stack ◆","member rewards on completed stays, on top of hotel loyalty points ◆ (IHG One + Ambassador combinable ◆, KrisFlyer eligible ◆)."],
 ["Redeem & Rebook","community earns too ◆","Rewards redeemable for future stays; community contributors earn too ◆. Graduate Keys guests into tailor-made and Finesse."]
];
const CAL=[
 ["sg","Aurora · Solar-Max 25",0,2,0,"mix","Tromsø / Fairbanks / Svalbard pushes riding the solar-maximum story already published ◆. IG Reels + EDM; specialist aurora nights."],
 ["sg","2027 Signatures Early-Bird",1,3,0,"plan","Sell 2027 small-group departures (India tigers S$11,880 ◆, Rwanda S$15,980 ◆) with early-bird perk stacking."],
 ["sg","Summer Family · Jun Hols",4,5,0,"plan","China for the Curious ◆ + multi-gen safaris; Meta family lookalikes; school-holiday urgency, real seat limits only."],
 ["sg","Festive & Nov-Dec Hols",9,11,0,"plan","White-Christmas rail & cruise (VSOE, Silversea ◆), festive Keys promos, year-end gifting of journeys."],
 ["hk","CNY Outbound 春節",0,1,0,"plan","Peak HK outbound window: 繁中 family & couple itineraries, WhatsApp broadcast to opted-in past guests."],
 ["hk","Sakura & Easter",2,3,0,"plan","Japan cherry-blossom luxury (ryokan + private tea ◆ story angles); Easter family escapes."],
 ["hk","Golden Week Push",8,9,0,"plan","October window: Europe autumn & southern-hemisphere spring; partner dinner conversion theatre."],
 ["hk","White Christmas · Rail",10,11,0,"plan","Belmond rail showcase ◆ partners; HKD festive pricing; Tatler gift-of-travel feature."],
 ["cn","春节 CNY Campaign",0,1,0,"plan","XHS 种草 + OA long-form + WeCom 红包-adjacent gifting mechanics (compliant); family & aurora hooks."],
 ["cn","五一 Golden Week",3,4,0,"plan","Short-haul luxury + early summer seeding; Douyin cuts + XHS search interception."],
 ["cn","暑期 Family Season",5,7,0,"plan","China for the Curious inverted: outbound family journeys; KOL fam content from spring departures."],
 ["cn","十一 Golden Week",8,9,0,"plan","Biggest CN outbound window: MP flash offers with real inventory; WeCom 1:1 to warm lists."],
 ["cn","双11 Keys Promo",9,10,1,"plan","Ride Double-11 attention with Keys stay credits & Rewards multipliers — luxury framing, no discount race."],
 ["brand","VG Media Events · SG/HK/BJ/SH",0,2,0,"mix","Virgin Galactic halo (US$250k/seat story live ◆): media nights across all four cities, UHNW capture lists."],
 ["brand","2027 Small-Group Launch",1,1,0,"obs","Signature Small Group Journeys 2027 launch ◆ — coordinated announcement across all three sites."],
 ["brand","Always-On Stories SEO",0,11,1,"obs","The compounding engine: destination guides in EN/繁/简 already publishing ◆; 8/month cadence proposed."]
];
const KPIS=[["ROMI ≥4.0x","◇"],["CAC : LTV ≥1:6","◇"],["Enquiry→Book ≥22%","◇"],["Keys activation ≥35%","◇"],["NPS 65","◇"],["Hotel CSAT 90%","◇"],["First response ≤15min","◇"]];
const RISKS=[
 ["CN platform policy shifts","XHS/WeChat rules change fast. Mitigate: own the Mini Program + WeCom graph; never rent the whole funnel."],
 ["PIPL transfer friction","Cross-border CRM sync needs separate consent. Mitigate: CN data stays in-region; only consented summaries sync."],
 ["Advisor dependency","Star specialists take relationships with them. Mitigate: WeCom enterprise ownership + shared trip memory in CRM."],
 ["Luxury demand cyclicality","HNW travel is cyclical. Mitigate: Keys entry tier, offers like 8-pay-7 ◆, and referral compounding."]
];
const state={s:.62,tx:0,ty:0,focus:"all",speed:1,density:"full",theme:"dark",sel:null,
  L:{flows:true,anim:true,labels:true,grid:true,glow:true,exec:true,cal:true,gov:true}};
const geom={},dossiers={},adj={},edges=[],labelJobs=[],searchIndex=[];
let world;const svg=document.getElementById("scene"),stage=document.getElementById("stage");
const $=id=>document.getElementById(id);
const fx=n=>Math.round(n*10)/10;
const esc=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
function el(tag,attrs,parent){const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
function txt(parent,x,y,str,cls,anchor,extra){const t=el("text",Object.assign({x:fx(x),y:fx(y),"class":cls||"","text-anchor":anchor||"start"},extra||{}),parent);t.textContent=str;return t;}
function A(id,side,f){const g=geom[id];f=(f==null?.5:f);
  if(side==="t")return[g.x+g.w*f,g.y];if(side==="b")return[g.x+g.w*f,g.y+g.h];
  if(side==="l")return[g.x,g.y+g.h*f];return[g.x+g.w,g.y+g.h*f];}
function reg(id,kind,name,div,ev,role,desc,inp,out,kp){
  dossiers[id]={kind,name,div,ev:ev||"plan",role:role||"",desc:desc||"",inp:inp||[],out:out||[],kp:kp||[]};
  searchIndex.push({id,label:name+(role?" · "+role:""),kind:kind.slice(0,4).toUpperCase(),div});
}
const SVG_CSS=`
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
text{font-family:var(--sans);fill:var(--ink)}
.c-brand{--c:var(--brand)}.c-sg{--c:var(--sg)}.c-hk{--c:var(--hk)}.c-cn{--c:var(--cn)}.c-ops{--c:var(--ops)}
.c-ok{--c:var(--ok)}.c-warn{--c:var(--warn)}.c-bad{--c:var(--bad)}.c-info{--c:var(--info)}
.frame{fill:none;stroke:var(--line2);stroke-width:1.2}
.crop{stroke:var(--faint);stroke-width:1}
.gridrect{fill:url(#gridpat)}
.t-mast{font-family:var(--disp);font-size:42px;font-weight:700;letter-spacing:1px}
.t-mastsub{font-family:var(--mono);font-size:11.5px;fill:var(--mut);letter-spacing:2.5px}
.t-tag{font-family:var(--disp);font-size:15px;font-style:italic;fill:var(--brand)}
.t-sec{font-family:var(--mono);font-size:12px;letter-spacing:3px;fill:var(--mut);font-weight:600}
.t-secsub{font-family:var(--mono);font-size:10px;fill:var(--faint);letter-spacing:1px}
.secrule{stroke:var(--line2);stroke-width:1}
.tb-line{stroke:var(--line2)}
.t-tb1{font-family:var(--disp);font-size:14px;font-weight:700;letter-spacing:1px}
.t-tb2{font-family:var(--mono);font-size:9px;fill:var(--mut);letter-spacing:1.4px}
.routeline{fill:none;stroke:var(--brand);stroke-width:1.4;stroke-dasharray:2 6;stroke-linecap:round;stroke-opacity:.8}
.routedot{fill:var(--c)}
.t-route{font-family:var(--mono);font-size:8.5px;fill:var(--c);letter-spacing:1px}
.fnode{cursor:pointer}
.fnode .box{fill:var(--surface);stroke:var(--line2);stroke-width:1;transition:stroke .18s}
.fnode:hover .box{stroke:var(--c);stroke-width:1.6}
.fnode:focus-visible{outline:none}.fnode:focus-visible .box{stroke:var(--warn);stroke-width:2.2}
.fnode,.chip,.calbar,.edge,.budseg{transition:opacity .25s}
.t-code{font-family:var(--mono);font-size:9px;fill:var(--c);letter-spacing:1px;font-weight:600}
.t-name{font-size:15.5px;font-weight:600}
.t-sub{font-size:10.5px;fill:var(--mut)}
.t-metric{font-family:var(--mono);font-size:9.5px;fill:var(--c)}
.t-ev{font-family:var(--mono);font-size:9px;font-weight:600}
.ndot{fill:var(--c)}
.platform{fill:color-mix(in srgb,var(--brand) 12%,var(--surface));stroke:var(--brand);stroke-opacity:.65;stroke-width:1.4}
.t-plat{font-family:var(--disp);font-size:24px;font-weight:700;fill:var(--brand);letter-spacing:1px}
.t-platsub{font-size:11.5px;fill:var(--mut)}
.langchip{fill:var(--surface2);stroke:var(--brand);stroke-opacity:.5}
.t-lang{font-family:var(--mono);font-size:10px;fill:var(--brand)}
.mcol{fill:color-mix(in srgb,var(--c) 5%,var(--surface2));stroke:var(--c);stroke-opacity:.5;stroke-width:1.3}
.mhead{fill:color-mix(in srgb,var(--c) 16%,var(--surface));stroke:var(--c);stroke-opacity:.6}
.t-mname{font-family:var(--disp);font-size:27px;font-weight:700}
.t-mzh{font-family:var(--disp);font-size:17px;fill:var(--c);font-weight:600}
.t-mdom{font-family:var(--mono);font-size:9.5px;fill:var(--mut);letter-spacing:.5px}
.t-mcode{font-family:var(--mono);font-size:9.5px;fill:var(--c);letter-spacing:1.5px;font-weight:600}
.mrule{stroke:var(--c);stroke-width:2;stroke-opacity:.85}
.kpibox{fill:var(--surface);stroke:var(--line2)}
.t-kpin{font-family:var(--mono);font-size:17px;font-weight:600;fill:var(--c)}
.t-kpil{font-size:9.5px;fill:var(--mut)}
.roletag{font-family:var(--mono);font-size:8px;letter-spacing:1px;font-weight:600}
.fstep{fill:var(--surface);stroke:var(--line)}
.t-fstep{font-size:11px}
.farrow{stroke:var(--c);stroke-opacity:.55;fill:none;stroke-width:1.3}
.budbar{fill:var(--c);fill-opacity:.8}
.t-bud{font-family:var(--mono);font-size:10px;fill:var(--ink)}
.compchip{fill:color-mix(in srgb,var(--warn) 8%,var(--surface));stroke:var(--warn);stroke-opacity:.5}
.t-comp{font-family:var(--mono);font-size:9.5px;fill:var(--warn)}
.teamchip{fill:var(--surface);stroke:var(--line2)}
.t-team{font-size:10.5px;fill:var(--mut)}
.playbox{fill:var(--surface);stroke:var(--c);stroke-opacity:.35;stroke-dasharray:4 3}
.t-play{font-size:10.5px}
.edge .base{fill:none;stroke:var(--c);stroke-width:1.6;stroke-opacity:.55}
.edge .pulse{fill:none;stroke:var(--c);stroke-width:1.8;stroke-opacity:.9;stroke-dasharray:5 11;animation:flow var(--fd,2.6s) linear infinite}
.edge .hit{fill:none;stroke:#000;stroke-opacity:0;stroke-width:16;pointer-events:stroke;cursor:pointer}
.edge:hover .base{stroke-opacity:1;stroke-width:2.4}
@keyframes flow{to{stroke-dashoffset:-64}}
.paused .pulse{animation-play-state:paused}
.off-anim .pulse{display:none}
.elabel rect{fill:var(--labelbg);fill-opacity:.94;stroke:var(--c);stroke-opacity:.4}
.elabel text{font-family:var(--mono);font-size:11px;fill:var(--c);letter-spacing:.3px}
.off-labels .elabel{display:none}
.off-flows #gEdges{display:none}
.off-grid .gridrect{display:none}
.off-exec #gExec{display:none}
.off-cal #gCal{display:none}
.off-gov #gGov{display:none}
.compact .t-sub,.compact .t-note,.compact .t-metric{display:none}
.glowon .sel .box{filter:url(#glow)}
.glowon .mrule{filter:url(#glow)}
.glowon .edge.hot .pulse{filter:url(#glow)}
.dim{opacity:.13}.softdim{opacity:.22}
.sel .box{stroke:var(--c);stroke-width:2.6}
.linked .box{stroke:var(--c);stroke-width:1.8}
.edge.hot .base{stroke-opacity:1;stroke-width:2.6}
.edge.hot .pulse{stroke-opacity:1;stroke-width:2.4}
.chip{cursor:pointer}
.chip .box{fill:var(--surface);stroke:var(--line);transition:stroke .15s}
.chip:hover .box,.chip.sel .box{stroke:var(--c);stroke-width:1.8}
.t-chip{font-size:11.5px}
.lanebox{fill:color-mix(in srgb,var(--surface2) 85%,transparent);stroke:var(--line2)}
.t-laneh{font-family:var(--mono);font-size:11.5px;font-weight:600;letter-spacing:2.5px;fill:var(--ink)}
.t-lanen{font-family:var(--mono);font-size:9.5px;fill:var(--mut)}
.bus{stroke:var(--ops);stroke-width:2;stroke-opacity:.8;fill:none}
.t-bus{font-family:var(--mono);font-size:9.5px;fill:var(--ops);letter-spacing:1.5px}
.carrow{stroke:var(--c);stroke-width:1.7;fill:none;stroke-opacity:.8}
.t-sla{font-family:var(--mono);font-size:9px;fill:var(--warn);font-weight:600}
.t-mnote{font-size:9.5px}
.calgrid{stroke:var(--grid2);stroke-width:1}
.t-month{font-family:var(--mono);font-size:9.5px;fill:var(--mut);letter-spacing:1px}
.t-lane{font-family:var(--mono);font-size:9.5px;fill:var(--c);font-weight:600;letter-spacing:1px}
.calbar{cursor:pointer}
.calbar .box{fill:color-mix(in srgb,var(--c) 22%,var(--surface));stroke:var(--c);stroke-opacity:.7;transition:all .15s}
.calbar:hover .box,.calbar.sel .box{fill:color-mix(in srgb,var(--c) 38%,var(--surface));stroke-width:1.8}
.t-cal{font-size:10px;font-weight:600}
.gate{fill:var(--bg);stroke:var(--warn);stroke-width:1.5}
.govbox{fill:color-mix(in srgb,var(--surface2) 85%,transparent);stroke:var(--line2)}
.t-govh{font-family:var(--mono);font-size:11.5px;font-weight:600;letter-spacing:2.5px}
.tree{stroke:var(--line2);fill:none;stroke-width:1.2}
.northstar{fill:color-mix(in srgb,var(--brand) 14%,var(--surface));stroke:var(--brand);stroke-opacity:.7}
.t-north{font-family:var(--disp);font-size:15px;font-weight:700;fill:var(--brand)}
.budseg{cursor:pointer}
.budseg rect.seg{fill:var(--c);fill-opacity:.85;transition:fill-opacity .18s}
.budseg:hover rect.seg{fill-opacity:1}
.budseg.sel rect.seg{stroke:var(--ink);stroke-width:1.5}
.t-budlab{font-family:var(--mono);font-size:9px;fill:var(--mut)}
.warnnote{fill:color-mix(in srgb,var(--warn) 9%,var(--surface));stroke:var(--warn);stroke-opacity:.55}
.t-warn{font-family:var(--mono);font-size:9.5px;fill:var(--warn)}
.comprow{cursor:pointer}
.comprow .box{fill:var(--surface);stroke:var(--line2)}
.comprow:hover .box,.comprow.sel .box{stroke:var(--c);stroke-width:1.8}
.t-law{font-family:var(--mono);font-size:11px;font-weight:600;fill:var(--c)}
.t-lawsub{font-size:9.5px;fill:var(--mut)}
.orgbox{fill:var(--overlay);stroke:var(--c);stroke-opacity:.6}
.t-org{font-size:12px;font-weight:600}
.t-orgsub{font-family:var(--mono);font-size:8.5px;fill:var(--mut)}
.orgline{stroke:var(--ops);stroke-opacity:.6;fill:none;stroke-width:1.3}
.riskbox{fill:color-mix(in srgb,var(--bad) 6%,var(--surface));stroke:var(--bad);stroke-opacity:.4}
.t-risk{font-size:12px;font-weight:600;fill:var(--bad)}
.t-risksub{font-size:10px;fill:var(--mut)}
.t-foot{font-family:var(--mono);font-size:9.5px;fill:var(--mut);letter-spacing:1px}
.boot .fnode,.boot .chip,.boot .calbar{animation:nIn .5s both;animation-delay:var(--d,0s)}
@keyframes nIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.exported *{animation:none!important}
`;
function build(){
  const style=el("style",{},svg);style.textContent=SVG_CSS;
  const defs=el("defs",{},svg);
  for(const k in COLS){
    const m=el("marker",{id:"ar-"+k,viewBox:"0 0 10 10",refX:8,refY:5,markerWidth:7,markerHeight:7,orient:"auto-start-reverse"},defs);
    el("path",{d:"M0 0L10 5L0 10z",style:"fill:var("+COLS[k]+")"},m);
    const md=el("marker",{id:"dt-"+k,viewBox:"0 0 8 8",refX:4,refY:4,markerWidth:5,markerHeight:5},defs);
    el("circle",{cx:4,cy:4,r:2.6,style:"fill:var("+COLS[k]+")"},md);
  }
  const f=el("filter",{id:"glow",x:"-60%",y:"-60%",width:"220%",height:"220%"},defs);
  el("feGaussianBlur",{stdDeviation:3.2,result:"b"},f);
  const mg=el("feMerge",{},f);el("feMergeNode",{in:"b"},mg);el("feMergeNode",{in:"SourceGraphic"},mg);
  const pat=el("pattern",{id:"gridpat",width:120,height:120,patternUnits:"userSpaceOnUse"},defs);
  el("path",{d:"M120 0H0V120",fill:"none",style:"stroke:var(--grid2);stroke-width:1"},pat);
  el("path",{d:"M24 0V120M48 0V120M72 0V120M96 0V120M0 24H120M0 48H120M0 72H120M0 96H120",fill:"none",style:"stroke:var(--grid);stroke-width:.6"},pat);
  const hp=el("pattern",{id:"hatch",width:7,height:7,patternUnits:"userSpaceOnUse",patternTransform:"rotate(45)"},defs);
  el("path",{d:"M0 0V7",style:"stroke:var(--bg);stroke-width:2.4;stroke-opacity:.42"},hp);
  world=el("g",{id:"world"},svg);
  el("rect",{x:0,y:0,width:W,height:H,style:"fill:var(--bg)"},world);
  el("rect",{x:0,y:0,width:W,height:H,"class":"gridrect"},world);
  el("rect",{x:20,y:20,width:W-40,height:H-40,"class":"frame",rx:6},world);
  [[20,20],[W-20,20],[20,H-20],[W-20,H-20]].forEach(c=>el("path",{d:`M${c[0]-12} ${c[1]}H${c[0]+12}M${c[0]} ${c[1]-12}V${c[1]+12}`,"class":"crop"},world));
  buildMasthead();buildBrand();buildMarkets();buildExecution();buildCalendar();buildGovernance();buildEdges();
}
function secLabel(parent,n,title,y,sub){
  txt(parent,60,y,n+" // "+title,"t-sec");
  el("line",{x1:60,y1:y+10,x2:1780,y2:y+10,"class":"secrule"},parent);
  if(sub)txt(parent,1780,y-2,sub,"t-secsub","end");
}
function evMark(g,x,y,ev){
  const t=txt(g,x,y,ev==="obs"?"◆":ev==="mix"?"◈":"◇","t-ev","end");
  t.style.fill=ev==="obs"?"var(--ok)":ev==="mix"?"var(--info)":"var(--warn)";
}
function buildMasthead(){
  const g=el("g",{},world);
  txt(g,60,112,"MARKETING BLUEPRINT","t-mast");
  txt(g,60,140,"TRI-MARKET MARKETING PLAN & EXECUTION · SINGAPORE / HONG KONG / CHINA","t-mastsub");
  txt(g,60,166,"One brand · Three engines · 一个品牌 · 三个引擎","t-tag");
  const rt=el("g",{},g);
  el("path",{d:"M690 150 Q 990 55 1330 118","class":"routeline"},rt);
  [["sg",690,150,"SG"],["hk",990,88,"HK"],["cn",1330,118,"CN"]].forEach(r=>{
    const rg=el("g",{"class":"c-"+r[0]},rt);
    el("circle",{cx:r[1],cy:r[2],r:4,"class":"routedot"},rg);
    el("circle",{cx:r[1],cy:r[2],r:8,style:"fill:none;stroke:var(--c);stroke-opacity:.4"},rg);
    txt(rg,r[1],r[2]-13,r[3],"t-route","middle");
  });
  el("path",{d:"M1052 82l14 4-14 4 3-4z",style:"fill:var(--brand)",transform:"rotate(8 1059 86)"},rt);
  el("rect",{x:1400,y:60,width:380,height:110,style:"fill:var(--surface2);stroke:var(--line2)"},g);
  el("line",{x1:1400,y1:100,x2:1780,y2:100,"class":"tb-line"},g);
  el("line",{x1:1400,y1:136,x2:1780,y2:136,"class":"tb-line"},g);
  txt(g,1416,86,"TRI-MARKET BLUEPRINT","t-tb1");
  txt(g,1416,122,"DWG IJ-MKT-27 · REV 1.0 · FY2027 · SHEET 1/1","t-tb2");
  txt(g,1416,158,"◆ OBSERVED IN SOURCE SITES · ◈ HYBRID · ◇ PROPOSED","t-tb2");
}
function buildBrand(){
  const g=el("g",{id:"gBrand"},world);
  secLabel(g,"01","BRAND SPINE — THE SHARED CORE",210,"one platform · three localized engines");
  geom.platform={x:60,y:228,w:1720,h:76};
  const pg=el("g",{"class":"fnode c-brand","data-id":"platform",tabindex:0},g);
  el("rect",{x:60,y:228,width:1720,height:76,rx:13,"class":"box platform"},pg);
  const q=el("g",{transform:"translate(84,246)"},pg);
  el("circle",{cx:19,cy:19,r:16,style:"fill:none;stroke:var(--brand);stroke-width:2.4"},q);
  el("path",{d:"M28 28l10 10",style:"stroke:var(--brand);stroke-width:3;stroke-linecap:round"},q);
  txt(pg,140,262,"A QUEST FOR EXCEPTIONAL TRAVEL","t-plat");
  txt(pg,140,286,"Human expertise · 300+ years collective ◆ · not-googleable access · exceptional people, places, memories ◆","t-platsub");
  [["EN",1210],["繁體中文",1330],["简体中文",1470]].forEach((l,i)=>{
    el("rect",{x:l[1],y:250,width:i===0?90:110,height:30,rx:8,"class":"langchip"},pg);
    txt(pg,l[1]+(i===0?45:55),269,l[0],"t-lang","middle");
  });
  txt(pg,1756,290,"Stepworks brand system ◆","t-secsub","end");
  reg("platform","PLATFORM","A Quest for Exceptional Travel","brand","obs","Brand platform · EN / 繁 / 简","The unified promise across all three markets: exceptional destinations, services, people and memories ◆. Human judgment and insider access are the moat against AI-commoditized itineraries. Trilingual identity system built for SG, HK and CN ◆.",["Guest insight","Partner privileges","Specialist expertise"],["Positioning","KV & tone kit","Trilingual copy system"],["Brand salience","Message recall","NPS 65 ◇"]);
  const AUD=[
   ["aud1","Silver Gems 银发宝石","HNW boomers 50+ · repeat explorers","Exotic, off-the-beaten-track; comfort without crowds. The core buyer across all three markets ◆.","obs"],
   ["aud2","Multi-Gen Families","China for the Curious ◆ · school holidays","Parents + kids + grandparents; private guides, pacing, wildlife and living history. SG/HK outbound, CN both ways ◆.","obs"],
   ["aud3","Ultra-HNW Collectors","Virgin Galactic ◆ · jets · buyouts","Once-in-a-lifetime trophies: spaceflight US$250k ◆, private yachts ◆, villa buyouts. Served by named specialists.","obs"],
   ["aud4","Next-Gen Affluent","XHS discovery · Keys entry tier","25–45 professionals entering via hotel perks and self-serve; graduate into tailor-made. CN-weighted ◇.","plan"]];
  AUD.forEach((a,i)=>{
    const x=60+i*435,y=324,w=415,h=96;
    if(i>0){}
    const xx=[60,495,930,1365][i];
    geom[a[0]]={x:xx,y,w,h};
    const ng=el("g",{"class":"fnode c-brand","data-id":a[0],tabindex:0,style:`--d:${i*60}ms`},g);
    el("rect",{x:xx,y,width:w,height:h,rx:11,"class":"box"},ng);
    txt(ng,xx+14,y+24,"AUDIENCE 0"+(i+1),"t-code");
    evMark(ng,xx+w-12,y+22,a[4]);
    txt(ng,xx+14,y+48,a[1],"t-name");
    txt(ng,xx+14,y+66,a[2],"t-sub");
    txt(ng,xx+14,y+84,a[3].slice(0,58),"t-sub");
    reg(a[0],"AUDIENCE",a[1],"brand",a[4],a[2],a[3],[],[],[]);
  });
  const PROD=[
   ["pr1","Tailor-Made 定制","bespoke private journeys ◆","Every detail shaped to pace, taste and curiosity; the flagship service ◆."],
   ["pr2","Finesse Small Group 精致小团","2027 Signatures on sale ◆","Expert-led departures: India tigers S$11,880 ◆, Rwanda gorillas S$15,980 ◆, France SGD 7,080 ◆."],
   ["pr3","Hotel Membership","4,700+ hotels · live ◆","Instant-book membership with preferred-partner perks; Rewards on completed stays ◆."],
   ["pr4","Ultraluxe & Exclusive","jet · yacht · villa ◆","Absolute privacy: private aviation, crewed yachts ◆, full buyouts. UHNW named-account play."],
   ["pr5","Cruise & Rail","Silversea · Belmond · Golden Eagle ◆","Ocean, expedition and river ◆ plus VSOE / Andean Explorer / Al Andalus rail ◆."],
   ["pr6","Virgin Galactic","US$250k halo ◆","Spaceflight story live in EN/繁/简 ◆; media events across SG·HK·BJ·SH proposed."]];
  PROD.forEach((p,i)=>{
    const x=60+i*290,y=444,w=270,h=116;
    geom[p[0]]={x,y,w,h};
    const ng=el("g",{"class":"fnode c-brand","data-id":p[0],tabindex:0,style:`--d:${120+i*50}ms`},g);
    el("rect",{x,y,width:w,height:h,rx:11,"class":"box"},ng);
    txt(ng,x+12,y+22,"PRODUCT 0"+(i+1),"t-code");
    evMark(ng,x+w-10,y+20,"obs");
    txt(ng,x+12,y+46,p[1],"t-name");
    txt(ng,x+12,y+64,p[2],"t-sub");
    const words=p[3].split(" ");let l1="",l2="";
    words.forEach(wd=>{if((l1+" "+wd).length<=36&&!l2)l1=(l1+" "+wd).trim();else l2=(l2+" "+wd).trim();});
    txt(ng,x+12,y+84,l1,"t-sub");txt(ng,x+12,y+99,l2.slice(0,38),"t-sub");
    reg(p[0],"PRODUCT",p[1],"brand","obs",p[2],p[3],[],[],[]);
  });
  geom.priv={x:60,y:584,w:500,h:156};
  const pv=el("g",{"class":"fnode c-brand","data-id":"priv",tabindex:0},g);
  el("rect",{x:60,y:584,width:500,height:156,rx:12,"class":"box"},pv);
  txt(pv,76,610,"THE PRIVILEGE STACK","t-code");
  evMark(pv,548,608,"obs");
  ["Confirmed one-category upgrade at booking ◆","Breakfast for two · VIP welcome amenity ◆","US$100 hotel credit per stay ◆","Early check-in / late check-out ◆","Stacks with hotel loyalty: IHG One + Ambassador ◆","KrisFlyer miles eligible on select stays ◆"].forEach((l,i)=>txt(pv,76,632+i*18,"· "+l,"t-sub"));
  reg("priv","MECHANISM","The Privilege Stack","brand","obs","Preferred-partner benefits","The concrete reason to book through the travel advisor rather than direct: upgrades confirmed at booking, breakfast, US$100 credit, early/late, and — critically — benefits stack on top of hotel loyalty points and elite status ◆. This is the核心 conversion argument on every channel.",["Partner program memberships"],["Perk display on proposals","Keys rate plans","Objection handling"],["Perk attach rate","Booking conversion"]);
  el("rect",{x:580,y:584,width:1200,height:156,rx:12,"class":"lanebox"},g);
  txt(g,596,610,"PARTNER CONSTELLATION — PREFERRED PROGRAMS ◆","t-laneh");
  txt(g,1764,610,"15 PROGRAMS","t-lanen","end");
  const PARTNERS=["Virtuoso ◆","Four Seasons Preferred ◆","Rosewood Elite ◆","Hilton for Luxury ◆","Hyatt Privé ◆","MO Fan Club ◆","Marriott STARS ◆","Belmond Bellini Club ◆","Design Hotels Collective ◆","Couture by Langham ◆","VITA by LHW ◆","LH withIN ◆","Accor Preferred HERA ◆","The Luxury Circle ◆","&Beyond · Silversea ◆"];
  PARTNERS.forEach((p,i)=>{
    const c=i%5,r=Math.floor(i/5),x=596+c*236,y=624+r*38,id="pt"+i;
    geom[id]={x,y,w:224,h:30};
    const cg=el("g",{"class":"chip c-brand","data-id":id,tabindex:0,style:`--d:${Math.min(i*30,600)}ms`},g);
    el("rect",{x,y,width:224,height:30,rx:8,"class":"box"},cg);
    el("circle",{cx:x+13,cy:y+15,r:3.2,"class":"ndot"},cg);
    txt(cg,x+24,y+19.5,p,"t-chip");
    reg(id,"PARTNER",p.replace(" ◆",""),"brand","obs","Preferred partner program","Listed across hotel membership portal collections and site partner pages ◆. Feeds the privilege stack, co-marketing events and Keys rate plans.",[],[],[]);
  });
  const PROOF=[["destination editorial SEO library ◆","obs"],["Specialist team pages ◆","obs"],["Named-staff testimonials ◆","obs"],["Newsletter capture live ◆","obs"],["NPS 65 target ◇","plan"],["90% hotel CSAT target ◇","plan"]];
  PROOF.forEach((p,i)=>{
    const x=60+i*290,y=756,id="pf"+i;
    geom[id]={x,y,w:270,h:30};
    const cg=el("g",{"class":"chip c-"+(p[1]==="obs"?"ok":"warn"),"data-id":id,tabindex:0},g);
    el("rect",{x,y,width:270,height:30,rx:8,"class":"box"},cg);
    el("circle",{cx:x+13,cy:y+15,r:3.2,"class":"ndot"},cg);
    txt(cg,x+24,y+19.5,p[0],"t-chip");
    reg(id,"PROOF",p[0].replace(/ [◆◇]/,""),"brand",p[1],"Trust asset",p[1]==="obs"?"Live on the source sites ◆ — reuse as social proof, SEO surface and proposal appendix.":"Proposed measurement target ◇ — validate baseline before committing to the number.",[],[],[]);
  });
}
function buildMarkets(){
  const g=el("g",{id:"gMarkets"},world);
  secLabel(g,"02","MARKET ENGINES — THREE DISTINCT PLANS",850,"same brand · different physics");
  MKTS.forEach(m=>{
    const cid="m-"+m.k,X=m.x,Y=880;
    geom[cid]={x:X,y:Y,w:560,h:1080};
    const cg=el("g",{"class":"mcolwrap c-"+m.k,"data-id":cid},g);
    el("rect",{x:X,y:Y,width:560,height:1080,rx:15,"class":"mcol"},cg);
    const hd=el("g",{"class":"fnode",style:"cursor:pointer"},cg);
    el("rect",{x:X,y:Y,width:560,height:84,rx:15,"class":"mhead"},hd);
    el("rect",{x:X,y:Y+66,width:560,height:18,style:"fill:color-mix(in srgb,var(--c) 16%,var(--surface))"},hd);
    txt(hd,X+18,Y+38,m.name,"t-mname");
    txt(hd,X+18+m.name.length*17+14,Y+38,m.zh,"t-mzh");
    txt(hd,X+542,Y+26,m.code,"t-mcode","end");
    txt(hd,X+18,Y+62,m.dom+"  ·  "+m.lang,"t-mdom");
    el("line",{x1:X+14,y1:Y+84,x2:X+546,y2:Y+84,"class":"mrule"},cg);
    reg(cid,"ENGINE",m.name+" ENGINE ["+m.zh+"]",m.k,"mix",m.code+" · "+m.dom,"Market-specific plan: positioning, channel stack, funnel, budget and compliance for "+m.name+". Shares the brand spine; everything below the header is localized.",[],[],m.kpi.map(k=>k[0]+" "+k[1]));
    const po=el("g",{"class":"fnode c-"+m.k,"data-id":cid+"-pos",tabindex:0},cg);
    geom[cid+"-pos"]={x:X+16,y:Y+96,w:528,h:74};
    el("rect",{x:X+16,y:Y+96,width:528,height:74,rx:10,"class":"box"},po);
    txt(po,X+30,Y+118,"POSITIONING","t-code");
    const pw=m.pos.split(" ");let pl=["",""];let pi=0;
    pw.forEach(w=>{if((pl[pi]+" "+w).length<=72)pl[pi]=(pl[pi]+" "+w).trim();else if(pi===0){pi=1;pl[1]=w;}});
    txt(po,X+30,Y+140,pl[0],"t-sub");txt(po,X+30,Y+156,pl[1],"t-sub");
    reg(cid+"-pos","POSITIONING",m.name+" positioning",m.k,"plan","Market stance",m.pos,[],[],[]);
    m.kpi.forEach((k,i)=>{
      const x=X+16+i*176,y=Y+182,id=cid+"-k"+i;
      geom[id]={x,y,w:168,h:64};
      const kg=el("g",{"class":"fnode c-"+m.k,"data-id":id,tabindex:0},cg);
      el("rect",{x,y,width:168,height:64,rx:10,"class":"box kpibox"},kg);
      txt(kg,x+12,y+30,k[0],"t-kpin");
      txt(kg,x+12,y+50,k[1],"t-kpil");
      reg(id,"KPI",m.name+" · "+k[1],m.k,"plan","FY27 target",k[0]+" — proposed FY27 target for "+m.name+". Baseline from CRM before locking; reviewed at quarterly ROMI gates.",[],[],[k[0]]);
    });
    txt(cg,X+16,Y+270,"CHANNEL STACK — PLATFORM-SPECIFIC ◇","t-code");
    CH[m.k].forEach((c,i)=>{
      const col=i%2,row=Math.floor(i/2),x=X+16+col*268,y=Y+282+row*96,id=c[0];
      geom[id]={x,y,w:260,h:88};
      const ng=el("g",{"class":"fnode c-"+m.k,"data-id":id,tabindex:0,style:`--d:${i*50}ms`},cg);
      el("rect",{x,y,width:260,height:88,rx:10,"class":"box"},ng);
      txt(ng,x+12,y+22,c[1],"t-name");
      const rt=txt(ng,x+248,y+18,c[2],"roletag","end");
      rt.style.fill=c[2]==="DISCOVER"?"var(--info)":c[2]==="CAPTURE"?"var(--brand)":c[2]==="CONVERT"?"var(--ok)":c[2]==="RETAIN"?"var(--warn)":"var(--ops)";
      evMark(ng,x+248,y+34,c[6]);
      const tw=c[3].split(" ");let tl=["",""];let ti=0;
      tw.forEach(w=>{if((tl[ti]+" "+w).length<=40)tl[ti]=(tl[ti]+" "+w).trim();else if(ti===0){ti=1;tl[1]=w;}});
      txt(ng,x+12,y+42,tl[0],"t-sub");txt(ng,x+12,y+57,tl[1],"t-sub");
      txt(ng,x+12,y+76,c[4],"t-metric");
      txt(ng,x+248,y+76,c[5],"t-metric","end");
      reg(id,"CHANNEL",c[1]+" · "+m.name,m.k,c[6],c[2]+" · "+c[5],c[7],["Brand spine assets","Local insight"],["Leads → one CRM","Content feedback"],[c[4]]);
    });
    txt(cg,X+16,Y+580,"MINI-FUNNEL — HOW A LEAD MOVES HERE","t-code");
    const fb=el("g",{"class":"fnode c-"+m.k,"data-id":cid+"-fun",tabindex:0},cg);
    geom[cid+"-fun"]={x:X+16,y:Y+592,w:528,h:144};
    el("rect",{x:X+16,y:Y+592,width:528,height:144,rx:10,"class":"box"},fb);
    const steps=m.k==="cn"?["XHS note / Douyin cut → save & search","DM or QR → bilingual auto-ack ≤1min","WeCom advisor add ≤15min · 简体 pod","Mini Program proposal in CNY ≤48h","WeChat Pay deposit → concierge → NPS"]:
      m.k==="hk"?["IG / Google 繁+EN / expo → enquiry","WhatsApp or WeChat trade → SleekFlow","繁 / Cantonese specialist ≤15min","HKD proposal ≤48h · perks shown","Deposit → 24/7 concierge → NPS & referral"]:
      ["IG / Google EN / EDM / event → enquiry","WhatsApp → SleekFlow shared inbox","EN specialist matched ≤15min","SGD proposal ≤48h · perk stack shown","Deposit → 24/7 concierge → NPS & Keys"];
    el("line",{x1:X+34,y1:Y+612,x2:X+34,y2:Y+716,"class":"farrow"},fb);
    steps.forEach((s,i)=>{
      const y=Y+612+i*26;
      el("circle",{cx:X+34,cy:y,r:7,"class":"fstep"},fb);
      txt(fb,X+34,y+3.5,String(i+1),"t-metric","middle");
      txt(fb,X+50,y+4,s,"t-fstep");
    });
    reg(cid+"-fun","FUNNEL",m.name+" mini-funnel",m.k,"plan","Lead motion, localized",steps.join(" → "),[],[],["≤15min routing","≤48h proposal"]);
    const bg=el("g",{"class":"fnode c-"+m.k,"data-id":cid+"-bud",tabindex:0},cg);
    geom[cid+"-bud"]={x:X+16,y:Y+748,w:528,h:56};
    el("rect",{x:X+16,y:Y+748,width:528,height:56,rx:10,"class":"box"},bg);
    txt(bg,X+30,Y+768,"BUDGET SHARE ◇","t-code");
    txt(bg,X+532,Y+768,m.bud+"% · "+m.budAmt+" of S$1.8M","t-bud","end");
    el("rect",{x:X+30,y:Y+778,width:500,height:14,rx:4,style:"fill:var(--surface2);stroke:var(--line)"},bg);
    el("rect",{x:X+30,y:Y+778,width:fx(500*m.bud/100),height:14,rx:4,"class":"budbar"},bg);
    el("rect",{x:X+30,y:Y+778,width:fx(500*m.bud/100),height:14,rx:4,fill:"url(#hatch)"},bg);
    reg(cid+"-bud","BUDGET",m.name+" budget",m.k,"plan",m.bud+"% · "+m.budAmt,"Proposed share of the S$1.8M FY27 envelope ◇. CN carries the heaviest digital load; SG funds events & PR; HK balances open web with trade theatre. Reallocated quarterly against ROMI with a 10% test reserve.",[],[],[m.budAmt]);
    const cc=el("g",{"class":"fnode c-warn","data-id":cid+"-comp",tabindex:0},cg);
    geom[cid+"-comp"]={x:X+16,y:Y+816,w:528,h:44};
    el("rect",{x:X+16,y:Y+816,width:528,height:44,rx:10,"class":"box compchip"},cc);
    txt(cc,X+30,Y+834,"⚖ COMPLIANCE GATE","t-code").style.fill="var(--warn)";
    txt(cc,X+30,Y+851,m.comp,"t-comp");
    reg(cid+"-comp","COMPLIANCE",m.name+" privacy gate","warn","plan","Law real ◆ · implementation ◇",m.comp+". Non-negotiable before any broadcast, retargeting or cross-border sync. Consent ledger audited quarterly.",[],[],["Consent coverage 100%"]);
    const tc=el("g",{"class":"fnode c-"+m.k,"data-id":cid+"-team",tabindex:0},cg);
    geom[cid+"-team"]={x:X+16,y:Y+872,w:528,h:44};
    el("rect",{x:X+16,y:Y+872,width:528,height:44,rx:10,"class":"box teamchip"},tc);
    txt(tc,X+30,Y+890,"OWNERSHIP","t-code");
    txt(tc,X+30,Y+907,m.team,"t-team");
    reg(cid+"-team","TEAM",m.name+" ownership",m.k,"mix","Pod & accountability",m.team+". Specialist bench is shared across markets; marketing execution is local.",[],[],[]);
    const pb=el("g",{"class":"fnode c-"+m.k,"data-id":cid+"-plays",tabindex:0},cg);
    geom[cid+"-plays"]={x:X+16,y:Y+928,w:528,h:120};
    el("rect",{x:X+16,y:Y+928,width:528,height:120,rx:10,"class":"box playbox"},pb);
    txt(pb,X+30,Y+950,"SIGNATURE PLAYS ◇","t-code");
    m.plays.forEach((p,i)=>{
      txt(pb,X+30,Y+974+i*24,"✦","t-metric");
      txt(pb,X+48,Y+974+i*24,p,"t-play");
    });
    reg(cid+"-plays","PLAYBOOK",m.name+" signature plays",m.k,"mix","Three flagship moves",m.plays.join(" · "),[],[],[]);
  });
}
function buildExecution(){
  const g=el("g",{id:"gExec"},world);
  secLabel(g,"03","EXECUTION — ONE PIPELINE, THREE INTAKES",2040,"content factory · lead-to-book · keys self-serve");
  txt(g,60,2096,"LEAD-TO-BOOK PIPELINE — SHARED SPINE","t-laneh");
  txt(g,1150,2118,"ONE CRM · ONE PIPELINE","t-bus","middle");
  el("path",{d:"M171 2130 H1500","class":"bus"},g);
  el("path",{d:"M171 2130 V2148","class":"bus","marker-end":"url(#ar-ops)"},g);
  FUNNEL.forEach((f,i)=>{
    const x=60+i*248,y=2150,w=222,h=180,id="f"+(i+1);
    geom[id]={x,y,w,h};
    const ng=el("g",{"class":"fnode c-ops","data-id":id,tabindex:0,style:`--d:${i*45}ms`},g);
    el("rect",{x,y,width:w,height:h,rx:11,"class":"box"},ng);
    txt(ng,x+12,y+24,"0"+(i+1)+" "+f[0],"t-name");
    txt(ng,x+w-12,y+22,f[1],"t-sla","end");
    el("line",{x1:x+12,y1:y+36,x2:x+w-12,y2:y+36,"class":"secrule"},ng);
    [["sg",f[2]],["hk",f[3]],["cn",f[4]]].forEach((r,j)=>{
      const yy=y+58+j*30;
      const rg=el("g",{"class":"c-"+r[0]},ng);
      el("circle",{cx:x+18,cy:yy-3,r:3,"class":"ndot"},rg);
      txt(rg,x+28,yy,r[0].toUpperCase(),"t-metric");
      const words=r[1].split(" ");let ln=["",""];let li=0;
      words.forEach(w=>{if((ln[li]+" "+w).length<=27)ln[li]=(ln[li]+" "+w).trim();else if(li===0){li=1;ln[1]=w;}});
      txt(rg,x+58,yy,ln[0],"t-mnote");
      if(ln[1])txt(rg,x+58,yy+12,ln[1],"t-mnote");
    });
    txt(ng,x+12,y+h-12,"stage "+(i+1)+" of 7","t-lanen");
    reg(id,"STAGE","Pipeline "+(i+1)+": "+f[0],"ops","plan",f[1],f[5],[],[],[f[1]]);
    if(i<6)el("path",{d:`M${x+w} 2240 H${x+248}`,style:"stroke:var(--ops)","class":"carrow c-ops","marker-end":"url(#ar-ops)"},g);
  });
  geom.content={x:60,y:2420,w:1720,h:240};
  const cb=el("g",{"class":"fnode c-ops","data-id":"content",tabindex:0},g);
  el("rect",{x:60,y:2420,width:1720,height:240,rx:13,"class":"box lanebox"},cb);
  txt(cb,80,2448,"CONTENT FACTORY — EN MASTER → 繁 / 简 TRANSCREATION → NATIVE CUTS","t-laneh");
  txt(cb,1760,2448,"8 STORIES / MONTH ◇","t-lanen","end");
  reg("content","PIPELINE","Content Factory","ops","mix","Trilingual production line","One brief, one EN master in the proven Stories format ◆, then transcreation — not translation — into 繁體 and 简体, then platform-native cuts. Every asset carries UTM tags before it flies.",["Brand brief","Offer calendar","Specialist voices"],["EN / 繁 / 简 assets","Native cuts","SEO surface"],["8 stories/mo ◇","Asset reuse"]);
  CONTENT.forEach((c,i)=>{
    const x=80+i*283,y=2470,w=266,h=120,id="cf"+i;
    geom[id]={x,y,w,h};
    const ng=el("g",{"class":"fnode c-brand","data-id":id,tabindex:0,style:`--d:${i*40}ms`},g);
    el("rect",{x,y,width:w,height:h,rx:10,"class":"box"},ng);
    txt(ng,x+12,y+24,"0"+(i+1)+" "+c[0],"t-name");
    txt(ng,x+12,y+42,c[1],"t-code");
    const words=c[2].split(" ");let ln=["",""];let li=0;
    words.forEach(w=>{if((ln[li]+" "+w).length<=38)ln[li]=(ln[li]+" "+w).trim();else if(li===0){li=1;ln[1]=w;}});
    txt(ng,x+12,y+66,ln[0],"t-sub");
    txt(ng,x+12,y+81,ln[1].slice(0,40),"t-sub");
    txt(ng,x+12,y+96,ln[1].slice(40,80),"t-sub");
    reg(id,"STAGE","Factory "+(i+1)+": "+c[0],"brand","mix",c[1],c[2],[],[],[]);
    if(i<5)el("path",{d:`M${x+w} 2530 H${x+283}`,"class":"carrow c-brand","marker-end":"url(#ar-brand)"},g);
  });
  STORIES.forEach((s,i)=>{
    const x=80+i*283,y=2606,id="st"+i;
    geom[id]={x,y,w:266,h:32};
    const cg=el("g",{"class":"chip c-ok","data-id":id,tabindex:0},g);
    el("rect",{x,y,width:266,height:32,rx:8,"class":"box"},cg);
    el("circle",{cx:x+13,cy:y+16,r:3.2,"class":"ndot"},cg);
    txt(cg,x+24,y+20.5,s,"t-chip");
    reg(id,"ASSET",s.replace(" ◆",""),"ok","obs","Live Stories guide ◆","Published destination guide on the source sites ◆ — the compounding SEO surface. Refresh annually; transcreate into 繁/简; cut into Reels and XHS notes.",[],[],[]);
  });
  txt(g,60,2744,"Hotel Membership — SELF-SERVE LANE ◆","t-laneh");
  txt(g,1780,2744,"ENTRY TIER → GRADUATE TO TAILOR-MADE ◇","t-lanen","end");
  KEYS.forEach((k,i)=>{
    const x=60+i*347,y=2760,w=330,h=120,id="k"+(i+1);
    geom[id]={x,y,w,h};
    const ng=el("g",{"class":"fnode c-brand","data-id":id,tabindex:0,style:`--d:${i*40}ms`},g);
    el("rect",{x,y,width:w,height:h,rx:11,"class":"box"},ng);
    txt(ng,x+14,y+26,"0"+(i+1)+" "+k[0],"t-name");
    evMark(ng,x+w-12,y+24,"obs");
    txt(ng,x+14,y+44,k[1],"t-code");
    const words=k[2].split(" ");let ln=["",""];let li=0;
    words.forEach(w=>{if((ln[li]+" "+w).length<=46)ln[li]=(ln[li]+" "+w).trim();else if(li===0){li=1;ln[1]=w;}});
    txt(ng,x+14,y+68,ln[0],"t-sub");
    txt(ng,x+14,y+84,ln[1].slice(0,48),"t-sub");
    txt(ng,x+14,y+100,ln[1].slice(48,96),"t-sub");
    reg(id,"STAGE","Keys "+(i+1)+": "+k[0],"brand","obs",k[1],k[2],[],[],[]);
    if(i<4)el("path",{d:`M${x+w} 2820 H${x+347}`,"class":"carrow c-brand","marker-end":"url(#ar-brand)"},g);
  });
}
function buildCalendar(){
  const g=el("g",{id:"gCal"},world);
  secLabel(g,"04","ANNUAL CAMPAIGN CALENDAR — FY2027",2960,"three clocks · one brand beat");
  const mx=i=>150+i*(1630/12);
  ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"].forEach((m,i)=>{
    txt(g,(mx(i)+mx(i+1))/2,3020,m,"t-month","middle");
    el("line",{x1:fx(mx(i)),y1:3030,x2:fx(mx(i)),y2:3392,"class":"calgrid"},g);
  });
  el("line",{x1:fx(mx(12)),y1:3030,x2:fx(mx(12)),y2:3392,"class":"calgrid"},g);
  const lanes=[["sg",3040,"SINGAPORE"],["hk",3136,"HONG KONG"],["cn",3232,"CHINA"],["brand",3328,"BRAND BEAT"]];
  lanes.forEach(l=>{
    const lg=el("g",{"class":"c-"+l[0]},g);
    el("rect",{x:60,y:l[1],width:1720,height:88,rx:10,style:"fill:color-mix(in srgb,var(--c) 5%,transparent);stroke:var(--line)"},lg);
    txt(lg,70,l[1]+20,l[2],"t-lane");
    txt(lg,70,l[1]+36,l[0]==="brand"?"shared":"engine","t-lanen");
  });
  CAL.forEach((c,i)=>{
    const laneY={sg:3040,hk:3136,cn:3232,brand:3328}[c[0]];
    const x=mx(c[2])+4,w=mx(c[3]+1)-mx(c[2])-8,y=laneY+8+c[4]*40,id="cal"+i;
    geom[id]={x,y,w,h:32};
    const bg=el("g",{"class":"calbar c-"+c[0],"data-id":id,tabindex:0,style:`--d:${i*30}ms`},g);
    el("rect",{x:fx(x),y,width:fx(w),height:32,rx:8,"class":"box"},bg);
    const label=c[1]+(c[5]==="obs"?" ◆":c[5]==="mix"?" ◈":" ◇");
    const t=txt(bg,x+10,y+20.5,label,"t-cal");
    reg(id,"CAMPAIGN",c[1],c[0],c[5],["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"][c[2]]+" → "+["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"][c[3]],c[6],[],[],[]);
  });
  [3,6,9,12].forEach((m,i)=>{
    const gx=mx(m),gy=3372;
    el("rect",{x:fx(gx-5),y:gy-5,width:10,height:10,"class":"gate",transform:`rotate(45 ${fx(gx)} ${gy})`},g);
    const id="gate"+i;
    geom[id]={x:gx-14,y:gy-14,w:28,h:28};
    const gg=el("g",{"class":"fnode c-warn","data-id":id,tabindex:0},g);
    el("rect",{x:gx-14,y:gy-14,width:28,height:28,style:"fill:none;stroke:transparent;pointer-events:all","class":"box"},gg);
    reg(id,"GATE","Q"+(i+1)+" ROMI gate","warn","plan","Quarterly checkpoint","Budget release only against ROMI evidence: holdout readouts, channel CPA corridors, consent audit. 10% test reserve re-bid each quarter. Copy fatigue review rides the same gate.",[],[],["ROMI ≥4.0x ◇"]);
  });
  txt(g,150,3416,"◇ = quarterly ROMI gate · budget release & creative refresh","t-secsub");
}
function buildGovernance(){
  const g=el("g",{id:"gGov"},world);
  secLabel(g,"05","MEASUREMENT, BUDGET & GOVERNANCE",3460,"the loop that keeps three engines honest");
  el("rect",{x:60,y:3500,width:560,height:220,rx:13,"class":"govbox"},g);
  txt(g,76,3528,"KPI TREE","t-govh");
  geom.north={x:80,y:3542,w:520,h:44};
  const ng=el("g",{"class":"fnode c-brand","data-id":"north",tabindex:0},g);
  el("rect",{x:80,y:3542,width:520,height:44,rx:10,"class":"box northstar"},ng);
  txt(ng,340,3562,"NORTH STAR ◇","t-code","middle");
  txt(ng,340,3580,"Repeat + referral revenue ≥45%","t-north","middle");
  reg("north","KPI","North Star: repeat + referral ≥45%","brand","plan","FY27 north star","Luxury travel compounds on trust: the healthiest revenue is a second journey or a warm introduction. Keys Rewards ◆ and the referral loop exist to feed this number.",[],[],["≥45% ◇"]);
  KPIS.forEach((k,i)=>{
    const c=i%4,r=Math.floor(i/4),x=80+c*132,y=3606+r*44,id="kpi"+i;
    geom[id]={x,y,w:124,h:34};
    el("path",{d:`M${x+62} 3586 V${y}`,"class":"tree"},g);
    const cg=el("g",{"class":"chip c-brand","data-id":id,tabindex:0},g);
    el("rect",{x,y,width:124,height:34,rx:8,"class":"box"},cg);
    txt(cg,x+62,y+15,k[0],"t-chip","middle").setAttribute("font-size","10");
    txt(cg,x+62,y+28,"target ◇","t-lanen","middle");
    reg(id,"KPI",k[0],"brand","plan","Shared target","Proposed FY27 threshold ◇ across all three engines; market-level variants live in each engine column. Baseline before locking.",[],[],[k[0]]);
  });
  el("rect",{x:640,y:3500,width:560,height:220,rx:13,"class":"govbox"},g);
  txt(g,656,3528,"BUDGET & REALLOCATION ◇","t-govh");
  txt(g,1184,3528,"S$1.8M ENVELOPE","t-lanen","end");
  let bx=660;
  MKTS.forEach((m,i)=>{
    const w=520*m.bud/100,id="bud-"+m.k;
    geom[id]={x:bx,y:3548,w,h:26};
    const sg2=el("g",{"class":"budseg c-"+m.k,"data-id":id,tabindex:0},g);
    const tt=el("title",{},sg2);tt.textContent=m.name+" · "+m.bud+"% · "+m.budAmt;
    el("rect",{x:fx(bx),y:3548,width:fx(w),height:26,"class":"seg"},sg2);
    if(i%2===1)el("rect",{x:fx(bx),y:3548,width:fx(w),height:26,fill:"url(#hatch)","pointer-events":"none"},sg2);
    txt(sg2,bx+w/2,3592,m.k.toUpperCase()+" "+m.bud+"%","t-budlab","middle");
    reg(id,"BUDGET",m.name+" allocation",""+m.k,"plan",m.bud+"% · "+m.budAmt,"Channel split ◇ — SG: Meta 30 / Google 25 / Events+PR 20 / CRM 10 / LinkedIn 10 / Test 5. HK: Meta 25 / Google 25 / Events 20 / PR 15 / WeChat trade 10 / Test 5. CN: XHS 35 / WeChat 25 / Douyin 15 / Baidu 10 / KOL 10 / Test 5.",[],[],[m.budAmt]);
    bx+=w;
  });
  el("rect",{x:660,y:3548,width:520,height:26,style:"fill:none;stroke:var(--line2)"},g);
  [["SG","Meta 30 · Google 25 · Events/PR 20 · CRM 10 · LI 10 · Test 5","sg"],["HK","Meta 25 · Google 25 · Events 20 · PR 15 · WeChat 10 · Test 5","hk"],["CN","XHS 35 · WeChat 25 · Douyin 15 · Baidu 10 · KOL 10 · Test 5","cn"]].forEach((r,i)=>{
    const rg=el("g",{"class":"c-"+r[2]},g);
    txt(rg,660,3622+i*18,r[0],"t-metric");
    txt(rg,692,3622+i*18,r[1],"t-sub");
  });
  geom.crit={x:660,y:3676,w:520,h:32};
  const cr=el("g",{"class":"fnode c-warn","data-id":"crit",tabindex:0},g);
  el("rect",{x:660,y:3676,width:520,height:32,rx:8,"class":"box warnnote"},cr);
  txt(cr,672,3696,"⚠ Attribution ≠ causation — geo-holdouts before scaling CN spend","t-warn");
  reg("crit","GUARDRAIL","Attribution guardrail","warn","plan","Critical measurement note","Platform-reported ROAS double-counts. Before any big CN reallocation: run geo-holdouts or ghost ads, triangulate with MMM, and treat last-click as a steering signal only. Correlation is not causation.",[],[],[]);
  el("rect",{x:1220,y:3500,width:560,height:220,rx:13,"class":"govbox"},g);
  txt(g,1236,3528,"COMPLIANCE MATRIX — LAW ◆ · IMPLEMENTATION ◇","t-govh");
  [["sg","PDPA + DNC","Hard opt-in for WA/EDM · DNC scrub before calls · consent proof kept for audit",3536],
   ["hk","PDPO","Direct-marketing notice at collection · opt-out honored & logged on every send",3596],
   ["cn","PIPL","Separate consent for cross-border transfer · CN data in-region · WeCom enterprise-owned",3656]].forEach(r=>{
    const id="law-"+r[0];
    geom[id]={x:1236,y:r[3],w:528,h:52};
    const rg=el("g",{"class":"comprow fnode c-"+r[0],"data-id":id,tabindex:0},g);
    el("rect",{x:1236,y:r[3],width:528,height:52,rx:9,"class":"box"},rg);
    el("circle",{cx:1252,cy:r[3]+18,r:3.5,"class":"ndot"},rg);
    txt(rg,1264,r[3]+22,r[0].toUpperCase()+" · "+r[1],"t-law");
    txt(rg,1252,r[3]+41,r[2],"t-lawsub");
    reg(id,"COMPLIANCE",r[0].toUpperCase()+" · "+r[1],r[0],"mix","Statute ◆ · controls ◇",r[2]+". Violations are brand-killers in luxury: one spam complaint from a UHNW guest costs more than a quarter of media budget.",[],[],["Zero violations"]);
  });
  el("rect",{x:60,y:3740,width:1100,height:200,rx:13,"class":"govbox"},g);
  txt(g,76,3768,"TEAM & RACI — HQ GOVERNS, PODS EXECUTE","t-govh");
  const ORG=[
   ["o1","Head of Marketing","SG HQ · brand + P&L ◇","brand",330,3782,220,40],
   ["o2","Digital Marketing Mgr","tri-market budget ◇","ops",180,3842,200,36],
   ["o3","Marketing Project Mgr","cross-border coordination ◇","ops",430,3842,200,36],
   ["o4","SG Pod","events · CRM · EN","sg",90,3894,150,36],
   ["o5","HK Director + Pod","繁中 · trade · expos","hk",270,3894,150,36],
   ["o6","CN Mktg Mgr · BJ/SH","XHS · WeChat · WeCom","cn",450,3894,170,36],
   ["o7","Specialist Bench ◆","300+ yrs · design & sell","brand",650,3894,180,36],
   ["o8","Concierge & Ops ◆","24/7 in-trip · guides","ops",860,3894,180,36]];
  ORG.forEach(o=>{
    geom[o[0]]={x:o[4],y:o[5],w:o[6],h:o[7]};
    const og=el("g",{"class":"fnode c-"+o[3],"data-id":o[0],tabindex:0},g);
    el("rect",{x:o[4],y:o[5],width:o[6],height:o[7],rx:9,"class":"box orgbox"},og);
    txt(og,o[4]+12,o[5]+16,o[1],"t-org");
    txt(og,o[4]+12,o[5]+30,o[2],"t-orgsub");
    reg(o[0],"ROLE",o[1],o[3],o[1].includes("◆")?"obs":"plan",o[2],"Part of the operating model: HQ sets brand, budget and gates; local pods own language, platforms and relationships. Specialist bench ◆ and concierge ◆ are shared across all three engines.",[],[],[]);
  });
  [["M440 3822 V3842","o2"],["M440 3822 V3832 H530 V3842","o3"],["M280 3878 V3894","o4"],["M280 3878 V3886 H345 V3894","o5"],["M280 3878 V3886 H535 V3894","o6"],["M630 3860 H740 V3894","o7"],["M630 3860 H950 V3894","o8"]].forEach(p=>el("path",{d:p[0],"class":"orgline"},g));
  el("rect",{x:1180,y:3740,width:600,height:200,rx:13,"class":"govbox"},g);
  txt(g,1196,3768,"OPERATING CADENCE ◇","t-govh");
  [["MON","Pipeline standup — all pods, one board · SLA breaches surfaced"],["MONTHLY","Channel review + creative refresh · fatigue rotation · Stories cadence"],["QUARTERLY","ROMI gate ◇ budget reallocation · consent audit · copy re-baseline"],["ANNUAL","Plan + brand audit · partner renegotiation · Keys tier review"]].forEach((r,i)=>{
    const y=3796+i*30;
    txt(g,1196,y,r[0],"t-metric").style.fill="var(--brand)";
    txt(g,1288,y,r[1],"t-sub");
  });
  ["≤15min first response","≤48h first proposal","24/7 in-trip cover"].forEach((s,i)=>{
    const x=1196+i*192;
    el("rect",{x,y:3902,width:180,height:24,rx:7,"class":"langchip"},g);
    txt(g,x+90,3918,s,"t-lang","middle");
  });
  RISKS.forEach((r,i)=>{
    const x=[60,495,930,1365][i],y=3960,id="risk"+i;
    geom[id]={x,y,w:415,h:80};
    const rg=el("g",{"class":"fnode c-bad","data-id":id,tabindex:0},g);
    el("rect",{x,y,width:415,height:80,rx:11,"class":"box riskbox"},rg);
    txt(rg,x+14,y+24,"⚠ "+r[0],"t-risk");
    const words=r[1].split(" ");let ln=["",""];let li=0;
    words.forEach(w=>{if((ln[li]+" "+w).length<=58)ln[li]=(ln[li]+" "+w).trim();else if(li===0){li=1;ln[1]=w;}});
    txt(rg,x+14,y+46,ln[0],"t-risksub");
    txt(rg,x+14,y+62,ln[1].slice(0,60),"t-risksub");
    reg(id,"RISK",r[0],"bad","plan","Mitigation planned",r[1],[],[],[]);
  });
  el("rect",{x:60,y:4080,width:1720,height:60,rx:11,"class":"govbox"},g);
  txt(g,76,4106,"PREPARED FOR MARKETING BLUEPRINT · MARKETING LEADERSHIP · FY2027 PLANNING CYCLE","t-foot");
  txt(g,76,4126,"◆ OBSERVED: REGIONAL WEBSITES AND HOTEL MEMBERSHIP PORTAL   |   ◇ PROPOSED: targets, budgets & channel tactics — validate baselines before budget commit","t-foot");
}
function roundedPath(pts,r){
  const p=pts.filter((pt,i)=>i===0||Math.abs(pt[0]-pts[i-1][0])>.01||Math.abs(pt[1]-pts[i-1][1])>.01);
  if(p.length<2)return"";
  let d=`M${fx(p[0][0])} ${fx(p[0][1])}`;
  for(let i=1;i<p.length-1;i++){
    const c=p[i],a=p[i-1],b=p[i+1];
    const l1=Math.hypot(c[0]-a[0],c[1]-a[1]),l2=Math.hypot(b[0]-c[0],b[1]-c[1]);
    if(l1<.01||l2<.01)continue;
    const rr=Math.min(r,l1/2,l2/2);
    const u1=[(c[0]-a[0])/l1,(c[1]-a[1])/l1],u2=[(b[0]-c[0])/l2,(b[1]-c[1])/l2];
    d+=` L${fx(c[0]-u1[0]*rr)} ${fx(c[1]-u1[1]*rr)} Q${fx(c[0])} ${fx(c[1])} ${fx(c[0]+u2[0]*rr)} ${fx(c[1]+u2[1]*rr)}`;
  }
  const last=p[p.length-1];
  return d+` L${fx(last[0])} ${fx(last[1])}`;
}
function addEdge(g,spec){
  const pts=[A.apply(null,spec.f)].concat(spec.via,[A.apply(null,spec.t)]);
  const d=roundedPath(pts,12);
  const eg=el("g",{"class":"edge c-"+spec.div,"data-id":spec.id},g);
  el("path",{d,"class":"base","marker-end":`url(#ar-${spec.div})`,"marker-start":`url(#dt-${spec.div})`},eg);
  el("path",{d,"class":"pulse"},eg);
  el("path",{d,"class":"hit","data-id":spec.id},eg);
  if(spec.lab){
    const lg=el("g",{"class":"elabel"},eg);
    if(spec.rot)lg.setAttribute("transform",`rotate(-90 ${spec.lp[0]} ${spec.lp[1]})`);
    const rect=el("rect",{rx:4},lg);
    const t=txt(lg,spec.lp[0],spec.lp[1],spec.lab,"","middle",{dy:".34em"});
    labelJobs.push({t,rect});
  }
  const fn=dossiers[spec.f[0]],tn=dossiers[spec.t[0]];
  dossiers[spec.id]={kind:"FLOW",name:spec.lab||"flow",div:spec.div,ev:"plan",role:spec.f[0].toUpperCase()+" → "+spec.t[0].toUpperCase(),
    desc:"Directed interaction from "+(fn?fn.name:spec.f[0])+" to "+(tn?tn.name:spec.t[0])+".",inp:[],out:[],kp:[],flow:{from:spec.f[0],to:spec.t[0],payload:spec.pl,cad:spec.cad}};
  edges.push(spec);
  (adj[spec.f[0]]=adj[spec.f[0]]||[]).push({e:spec.id,o:spec.t[0],dir:"out",lab:spec.lab});
  (adj[spec.t[0]]=adj[spec.t[0]]||[]).push({e:spec.id,o:spec.f[0],dir:"in",lab:spec.lab});
  searchIndex.push({id:spec.id,label:(spec.lab||"flow")+" · "+spec.f[0].toUpperCase()+"→"+spec.t[0].toUpperCase(),kind:"FLOW",div:spec.div});
}
function buildEdges(){
  const g=el("g",{id:"gEdges"},world);
  const E=[
  {id:"e1",f:["platform","l"],t:["m-sg","l",.056],via:[[36,266],[36,940]],lab:"brand system · EN",lp:[36,620],rot:1,div:"sg",pl:"Positioning, KV kit, products, partner stack",cad:"annual + quarterly refresh"},
  {id:"e2",f:["platform","b",.5],t:["m-hk","t",.5],via:[[920,572],[570,572],[570,748],[920,748]],lab:"brand system · 繁體",lp:[745,748],div:"hk",pl:"Trilingual identity, 繁中 messaging house",cad:"annual + quarterly refresh"},
  {id:"e3",f:["platform","r"],t:["m-cn","r",.056],via:[[1804,266],[1804,940]],lab:"brand system · 简体",lp:[1804,620],rot:1,div:"cn",pl:"简体 identity, PIPL-safe asset rules",cad:"annual + quarterly refresh"},
  {id:"e4",f:["m-sg","b",.5],t:["f1","t",.5],via:[[340,2130],[171,2130]],lab:"WA · IG · EDM leads",lp:[340,2050],rot:1,div:"sg",pl:"Tagged enquiries from open-web channels",cad:"real-time"},
  {id:"e5",f:["m-hk","b",.5],t:["f1","t",.5],via:[[920,2130],[171,2130]],lab:"WA · WeChat trade leads",lp:[920,2050],rot:1,div:"hk",pl:"Bilingual enquiries incl. trade hand-offs",cad:"real-time"},
  {id:"e6",f:["m-cn","b",.5],t:["f1","t",.5],via:[[1500,2130],[171,2130]],lab:"XHS · WeCom leads",lp:[1500,2050],rot:1,div:"cn",pl:"DM-bridged leads with bilingual auto-ack",cad:"real-time · ≤1min ack"},
  {id:"e7",f:["content","t",.1366],t:["m-sg","b",.4196],via:[],lab:"EN assets ↑",lp:[295,2240],rot:1,div:"sg",pl:"Reels, EDM blocks, EN Stories, event kits",cad:"monthly calendar"},
  {id:"e8",f:["content","t",.425],t:["m-hk","b",.2696],via:[],lab:"繁中 assets ↑",lp:[791,2240],rot:1,div:"hk",pl:"繁中 transcreations, HKD proposals, expo kits",cad:"monthly calendar"},
  {id:"e9",f:["content","t",.8576],t:["m-cn","b",.5625],via:[],lab:"简中 assets ↑",lp:[1535,2240],rot:1,div:"cn",pl:"XHS notes, OA articles, Douyin cuts, MP pages",cad:"monthly calendar"},
  {id:"e10",f:["f7","b",.5],t:["f1","b",.5],via:[[1659,2380],[171,2380]],lab:"referral · NPS · re-book loop",lp:[915,2380],div:"ops",pl:"NPS 65 ◇, testimonials ◆, referral asks, Keys Rewards ◆",cad:"T+3d then annual"},
  {id:"e11",f:["content","b",.0645],t:["k1","t",.336],via:[],lab:"SEO → self-serve",lp:[171,2710],div:"brand",pl:"Stories traffic routed to Keys collections",cad:"always-on"},
  {id:"e12",f:["k5","r",.5],t:["f7","r",.5],via:[[1804,2820],[1804,2240]],lab:"Rewards → advocacy",lp:[1804,2530],rot:1,div:"brand",pl:"Keys graduates into tailor-made & Finesse",cad:"per completed stay ◆"}
  ];
  E.forEach(s=>addEdge(g,s));
}
function sizeLabels(){
  labelJobs.forEach(j=>{
    try{const b=j.t.getBBox();if(!b.width)return;
      j.rect.setAttribute("x",fx(b.x-7));j.rect.setAttribute("y",fx(b.y-4));
      j.rect.setAttribute("width",fx(b.width+14));j.rect.setAttribute("height",fx(b.height+8));
    }catch(e){}
  });
}
let flyToken=0;
const spineInd=$("spineInd"),spine=$("spine");
function render(){
  world.setAttribute("transform",`translate(${fx(state.tx)} ${fx(state.ty)}) scale(${state.s.toFixed(4)})`);
  const pc=Math.round(state.s*100)+"%";
  $("hz").textContent=pc;$("zVal").textContent=pc;
  if(document.activeElement!==$("zoom"))$("zoom").value=Math.round(state.s*100);
  const sh=spine.clientHeight;
  if(sh>0){
    const y0=Math.max(0,-state.ty/state.s),y1=Math.min(H,(stage.clientHeight-state.ty)/state.s);
    spineInd.style.top=(y0/H*sh)+"px";
    spineInd.style.height=Math.max(8,(y1-y0)/H*sh)+"px";
  }
}
function clampS(s){return Math.max(.12,Math.min(2.6,s));}
function zoomAt(cx,cy,f){
  const s2=clampS(state.s*f);
  state.tx=cx-(cx-state.tx)*s2/state.s;state.ty=cy-(cy-state.ty)*s2/state.s;state.s=s2;render();
}
function fitRect(wr,anim){
  const vw=stage.clientWidth,vh=stage.clientHeight;
  const s=clampS(Math.min(vw/wr.w,vh/wr.h)*.94);
  flyTo(s,(vw-wr.w*s)/2-wr.x*s,(vh-wr.h*s)/2-wr.y*s,anim);
}
function flyTo(s,tx,ty,anim){
  const tok=++flyToken;
  const reduce=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if(anim===false||reduce){state.s=s;state.tx=tx;state.ty=ty;render();return;}
  const f={s:state.s,tx:state.tx,ty:state.ty},t0=performance.now(),dur=650;
  const step=t=>{
    if(tok!==flyToken)return;
    let p=Math.min(1,(t-t0)/dur);p=1-Math.pow(1-p,3);
    state.s=f.s+(s-f.s)*p;state.tx=f.tx+(tx-f.tx)*p;state.ty=f.ty+(ty-f.ty)*p;render();
    if(p<1)requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}
const NAVS={brand:{x:0,y:40,w:1840,h:780},markets:{x:0,y:830,w:1840,h:1160},execution:{x:0,y:2020,w:1840,h:900},calendar:{x:0,y:2940,w:1840,h:500},governance:{x:0,y:3440,w:1840,h:720}};
const NAVNAME={brand:"01 Brand spine",markets:"02 Market engines",execution:"03 Execution lanes",calendar:"04 Campaign calendar",governance:"05 Governance"};
function goNav(key,silent){
  if(key==="execution"&&!state.L.exec){state.L.exec=true;$("lExec").checked=true;applyState();}
  if(key==="calendar"&&!state.L.cal){state.L.cal=true;$("lCal").checked=true;applyState();}
  if(key==="governance"&&!state.L.gov){state.L.gov=true;$("lGov").checked=true;applyState();}
  document.querySelectorAll("[data-nav]").forEach(b=>b.classList.toggle("on",b.dataset.nav===key));
  const wr=NAVS[key],vw=stage.clientWidth;
  if(key==="brand"||key==="markets"){
    let s=clampS(vw/wr.w*.97);
    if(vw<760)s=Math.max(.46,s);
    flyTo(s,vw<760?18:(vw-wr.w*s)/2-wr.x*s,14-wr.y*s,true);
  }else fitRect(wr,true);
  sizeLabels();
  if(!silent)toast(NAVNAME[key]);
}
function flyToNode(id){
  const g=geom[id];if(!g)return;
  const vw=stage.clientWidth,vh=stage.clientHeight;
  const s=clampS(Math.max(state.s,Math.min(1.15,vw/(g.w+560))));
  flyTo(s,vw/2-(g.x+g.w/2)*s,vh/2-(g.y+g.h/2)*s,true);
}
function ownerOf(id){const d=dossiers[id];return d?d.div:"ops";}
function applyState(){
  const L=state.L;
  svg.classList.toggle("off-flows",!L.flows);
  svg.classList.toggle("off-anim",!L.anim);
  svg.classList.toggle("off-labels",!L.labels);
  svg.classList.toggle("off-grid",!L.grid);
  svg.classList.toggle("glowon",L.glow);
  svg.classList.toggle("off-exec",!L.exec);
  svg.classList.toggle("off-cal",!L.cal);
  svg.classList.toggle("off-gov",!L.gov);
  svg.classList.toggle("compact",state.density==="compact");
  svg.classList.toggle("paused",state.speed<=0);
  svg.style.setProperty("--fd",(state.speed>0?(2.6/state.speed):2.6).toFixed(2)+"s");
  document.documentElement.setAttribute("data-theme",state.theme);
  const sel=state.sel,linked=new Set();
  if(sel&&adj[sel])adj[sel].forEach(a=>linked.add(a.o));
  if(sel&&dossiers[sel]&&dossiers[sel].flow){linked.add(dossiers[sel].flow.from);linked.add(dossiers[sel].flow.to);}
  svg.querySelectorAll("[data-id]").forEach(n=>{
    if(n.classList.contains("hit"))return;
    const id=n.dataset.id,isEdge=n.classList.contains("edge");
    n.classList.remove("sel","linked","hot","dim","softdim");
    if(sel){
      if(isEdge){
        const e=edges.find(x=>x.id===id);
        if(id===sel||(e&&(e.f[0]===sel||e.t[0]===sel)))n.classList.add("hot");else n.classList.add("softdim");
      }else if(n.classList.contains("mcolwrap")){}
      else if(id===sel)n.classList.add("sel");
      else if(linked.has(id))n.classList.add("linked");
      else n.classList.add("softdim");
    }else if(state.focus!=="all"){
      if(isEdge){
        const e=edges.find(x=>x.id===id);
        const touch=e&&[e.f[0],e.t[0]].some(x=>ownerOf(x)===state.focus||x==="m-"+state.focus);
        if(!touch)n.classList.add("dim");
      }else if(n.classList.contains("mcolwrap")){
        if(id!=="m-"+state.focus)n.classList.add("dim");
      }else if(ownerOf(id)!==state.focus)n.classList.add("dim");
    }
  });
  document.querySelectorAll("#legend button").forEach(b=>b.classList.toggle("on",b.dataset.k===state.focus));
  $("focus").value=state.focus;
  render();
}
function clearSel(){document.dispatchEvent(new Event("atlas:clear"));state.sel=null;$("drawer").classList.remove("open");stage.classList.remove("dopen");applyState();}
function select(id,fly){
  if(!dossiers[id])return;
  state.sel=id;applyState();openDrawer(id);
  document.dispatchEvent(new CustomEvent("atlas:select",{detail:{id}}));
  if(fly)flyToNode(id);
}
function chipHtml(dk){
  const names={brand:"BRAND CORE",sg:"SINGAPORE",hk:"HONG KONG",cn:"CHINA",ops:"SHARED OPS",ok:"OBSERVED",warn:"GUARDRAIL",bad:"RISK",info:"INFO"};
  const v=COLS[dk]||"--ops";
  return`<span class="dchip" style="color:var(${v});border-color:color-mix(in srgb,var(${v}) 50%,transparent)"><i style="background:var(${v})"></i>${esc(names[dk]||dk.toUpperCase())}</span>`;
}
function openDrawer(id){
  const d=dossiers[id];let h="";
  h+=`<div class="dk">${esc(d.kind)} DOSSIER · ${esc(id.toUpperCase())}</div>`;
  h+=`<h2>${esc(d.name)}</h2>`+chipHtml(d.div);
  if(d.role)h+=`<div class="role">${esc(d.role)}</div>`;
  if(d.ev==="obs")h+=`<div class="evbox obs">◆ OBSERVED — present on the regional websites and hotel membership portal. Reuse with confidence.</div>`;
  else if(d.ev==="mix")h+=`<div class="evbox obs" style="color:var(--info);border-color:color-mix(in srgb,var(--info) 55%,transparent);background:color-mix(in srgb,var(--info) 9%,transparent)">◈ HYBRID — asset or law observed ◆; the tactic or target around it is proposed ◇.</div>`;
  else h+=`<div class="evbox plan">◇ PROPOSED — plan assumption. Validate baseline & cost before budget commit.</div>`;
  h+=`<div class="desc">${esc(d.desc)}</div>`;
  if(d.flow){
    const f=dossiers[d.flow.from],t=dossiers[d.flow.to];
    h+=`<div class="dmeta"><b>PAYLOAD</b><span>${esc(d.flow.payload)}</span><b>CADENCE</b><span>${esc(d.flow.cad)}</span></div>`;
    h+=`<div class="dsec">ENDPOINTS</div><div class="iface">
      <button data-jump="${d.flow.from}"><span class="ar">FROM</span><span>${esc(f?f.name:d.flow.from)}<small>${esc(d.flow.from.toUpperCase())}</small></span></button>
      <button data-jump="${d.flow.to}"><span class="ar">TO</span><span>${esc(t?t.name:d.flow.to)}<small>${esc(d.flow.to.toUpperCase())}</small></span></button></div>`;
  }
  if(d.inp&&d.inp.length)h+=`<div class="dsec">INPUTS</div><ul class="io in">${d.inp.map(x=>`<li>${esc(x)}</li>`).join("")}</ul>`;
  if(d.out&&d.out.length)h+=`<div class="dsec">OUTPUTS</div><ul class="io out">${d.out.map(x=>`<li>${esc(x)}</li>`).join("")}</ul>`;
  if(d.kp&&d.kp.length)h+=`<div class="dsec">KPIs</div><div class="kpis">${d.kp.map(x=>`<span>${esc(x)}</span>`).join("")}</div>`;
  const links=adj[id];
  if(links&&links.length){
    h+=`<div class="dsec">INTERFACES · ${links.length}</div><div class="iface">`;
    links.forEach(a=>{const o=dossiers[a.o];
      h+=`<button data-jump="${a.o}"><span class="ar">${a.dir==="out"?"↗":"→"}</span><span>${esc(o?o.name:a.o)}<small>${esc(a.lab||"flow")}</small></span></button>`;});
    h+=`</div>`;
  }
  h+=`<div class="dsec">NAVIGATE</div><div class="iface"><button data-locate="${id}"><span class="ar">◎</span><span>Center on sheet</span></button></div>`;
  $("dBody").innerHTML=h;
  $("drawer").classList.add("open");stage.classList.add("dopen");$("drawer").scrollTop=0;render();
}
$("dBody").addEventListener("click",e=>{
  const j=e.target.closest("[data-jump]");if(j){select(j.dataset.jump,true);return;}
  const l=e.target.closest("[data-locate]");if(l)flyToNode(l.dataset.locate);
});
$("dClose").addEventListener("click",clearSel);
const ptrs=new Map();let moved=0,pinchD=0,downTarget=null;
const OVERLAY=".pills,#legend,#hud,#spine";
stage.addEventListener("pointerdown",e=>{
  if(e.target.closest(OVERLAY))return;
  downTarget=e.target;ptrs.set(e.pointerId,{x:e.clientX,y:e.clientY});moved=0;
  if(ptrs.size===2){const a=[...ptrs.values()];pinchD=Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y);}
  try{stage.setPointerCapture(e.pointerId);}catch(err){}
  stage.classList.add("grabbing");
});
stage.addEventListener("pointermove",e=>{
  if(!ptrs.has(e.pointerId))return;
  const p=ptrs.get(e.pointerId),dx=e.clientX-p.x,dy=e.clientY-p.y;
  p.x=e.clientX;p.y=e.clientY;moved+=Math.abs(dx)+Math.abs(dy);
  const rect=stage.getBoundingClientRect();
  if(ptrs.size===1){flyToken++;state.tx+=dx;state.ty+=dy;render();}
  else if(ptrs.size===2){
    const a=[...ptrs.values()],d=Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y);
    const mx2=(a[0].x+a[1].x)/2-rect.left,my2=(a[0].y+a[1].y)/2-rect.top;
    if(pinchD>0)zoomAt(mx2,my2,d/pinchD);pinchD=d;
  }
});
function endPtr(e){
  if(!ptrs.has(e.pointerId))return;
  ptrs.delete(e.pointerId);pinchD=0;
  if(ptrs.size===0){
    stage.classList.remove("grabbing");
    if(moved<7&&downTarget&&downTarget.closest){
      const n=downTarget.closest("[data-id]");
      if(n&&dossiers[n.dataset.id])select(n.dataset.id,false);
      else if(state.sel)clearSel();
    }
    downTarget=null;
  }
}
stage.addEventListener("pointerup",endPtr);
stage.addEventListener("pointercancel",e=>{ptrs.delete(e.pointerId);pinchD=0;downTarget=null;stage.classList.remove("grabbing");});
stage.addEventListener("wheel",e=>{
  e.preventDefault();
  const rect=stage.getBoundingClientRect();
  zoomAt(e.clientX-rect.left,e.clientY-rect.top,Math.exp(-e.deltaY*.0013));
},{passive:false});
svg.addEventListener("keydown",e=>{
  if(e.key==="Enter"||e.key===" "){const n=e.target.closest("[data-id]");if(n){e.preventDefault();select(n.dataset.id,true);}}
});
document.addEventListener("keydown",e=>{
  if(e.target.tagName==="INPUT"||e.target.tagName==="SELECT"){
    if(e.key==="Escape"){e.target.blur();$("results").classList.remove("open");}return;}
  const pan=80;
  if(e.key==="Escape"){clearSel();$("results").classList.remove("open");stopTour();}
  else if(e.key==="+"||e.key==="=")zoomAt(stage.clientWidth/2,stage.clientHeight/2,1.15);
  else if(e.key==="-")zoomAt(stage.clientWidth/2,stage.clientHeight/2,1/1.15);
  else if(e.key==="ArrowLeft"){flyToken++;state.tx+=pan;render();}
  else if(e.key==="ArrowRight"){flyToken++;state.tx-=pan;render();}
  else if(e.key==="ArrowUp"){flyToken++;state.ty+=pan;render();}
  else if(e.key==="ArrowDown"){flyToken++;state.ty-=pan;render();}
  else if(e.key==="f")goNav("brand");
});
const SPINE=[["brand","01","BRAND",0,820,"--brand"],["markets","02","ENGINES",820,2000,"--sg"],
  ["execution","03","EXECUTE",2000,2920,"--ops"],["calendar","04","CALENDAR",2920,3420,"--hk"],["governance","05","GOVERN",3420,4200,"--cn"]];
SPINE.forEach(s=>{
  const b=document.createElement("button");
  b.className="sb";b.dataset.nav=s[0];b.style.setProperty("--sc","var("+s[4]+")");
  b.style.height=((s[3]-s[2])/H*100)+"%";
  b.innerHTML=`<b>${s[1]}</b>${s[2]}`;
  spine.insertBefore(b,spineInd);
});
let spineDrag=false,spineMoved=0,spineBtn=null;
function spineSeek(e){
  const r=spine.getBoundingClientRect();
  const frac=Math.max(0,Math.min(1,(e.clientY-r.top)/r.height));
  flyToken++;state.ty=stage.clientHeight/2-frac*H*state.s;render();
}
spine.addEventListener("pointerdown",e=>{
  e.stopPropagation();spineDrag=true;spineMoved=0;spineBtn=e.target.closest("[data-nav]");
  try{spine.setPointerCapture(e.pointerId);}catch(err){}
  if(!spineBtn)spineSeek(e);
});
spine.addEventListener("pointermove",e=>{if(!spineDrag)return;spineMoved+=Math.abs(e.movementY||1);if(spineMoved>4)spineSeek(e);});
spine.addEventListener("pointerup",e=>{
  e.stopPropagation();
  if(spineMoved<5&&spineBtn)goNav(spineBtn.dataset.nav);
  spineDrag=false;spineBtn=null;
});
spine.addEventListener("pointercancel",()=>{spineDrag=false;spineBtn=null;});
$("zoom").addEventListener("input",e=>{
  const target=clampS(e.target.value/100);
  zoomAt(stage.clientWidth/2,stage.clientHeight/2,target/state.s);
});
$("speed").addEventListener("input",e=>{state.speed=e.target.value/10;$("sVal").textContent=state.speed.toFixed(1)+"×";applyState();});
$("focus").addEventListener("change",e=>{state.focus=e.target.value;state.sel=null;$("drawer").classList.remove("open");stage.classList.remove("dopen");applyState();});
$("density").addEventListener("change",e=>{state.density=e.target.value;applyState();sizeLabels();});
$("theme").addEventListener("change",e=>{state.theme=e.target.value;applyState();toast(state.theme==="dark"?"Midnight atlas":"Parchment atlas");});
const LAYERMAP=[["lFlows","flows"],["lAnim","anim"],["lLabels","labels"],["lGrid","grid"],["lGlow","glow"],["lExec","exec"],["lCal","cal"],["lGov","gov"]];
LAYERMAP.forEach(([id,k])=>$(id).addEventListener("change",e=>{state.L[k]=e.target.checked;applyState();sizeLabels();}));
document.querySelectorAll("[data-nav]").forEach(b=>{if(!b.closest("#spine"))b.addEventListener("click",()=>{stopTour();goNav(b.dataset.nav);});});
$("bFit").addEventListener("click",()=>{stopTour();fitRect({x:0,y:0,w:W,h:H},true);toast("Full sheet · 1840 × 4200");});
$("b100").addEventListener("click",()=>{stopTour();flyTo(1,stage.clientWidth/2-920,stage.clientHeight/2-920,true);});
$("bRand").addEventListener("click",()=>{
  stopTour();
  const pool=["sg1","sg3","hk4","hk5","cn1","cn2","cn3","cn6","pr3","pr6","priv","f3","f7","k3","cal13","cal12","north","crit","law-cn","m-cn-plays"];
  const id=pool[Math.floor(Math.random()*pool.length)];
  select(id,true);toast("Spotlight · "+dossiers[id].name);
});
let tourT=null,tourI=0;
function stopTour(){if(tourT){clearInterval(tourT);tourT=null;$("bTour").classList.remove("on");$("bTour").textContent="▶ AUTO TOUR";}}
$("bTour").addEventListener("click",()=>{
  if(tourT){stopTour();toast("Tour stopped");return;}
  const seq=["brand","markets","execution","calendar","governance"];
  tourI=0;$("bTour").classList.add("on");$("bTour").textContent="■ STOP TOUR";
  clearSel();goNav(seq[0]);
  tourT=setInterval(()=>{tourI=(tourI+1)%seq.length;goNav(seq[tourI]);},3600);
});
$("bReset").addEventListener("click",()=>{
  stopTour();
  state.focus="all";state.speed=1;state.density="full";state.theme="dark";state.sel=null;
  Object.keys(state.L).forEach(k=>state.L[k]=true);
  $("speed").value=10;$("sVal").textContent="1.0×";$("density").value="full";$("theme").value="dark";$("focus").value="all";$("search").value="";
  LAYERMAP.forEach(([id,k])=>$(id).checked=state.L[k]);
  $("drawer").classList.remove("open");stage.classList.remove("dopen");
  $("results").classList.remove("open");
  applyState();sizeLabels();goNav("brand",true);toast("System reset");
});
[["brand","BRAND CORE"],["sg","SINGAPORE"],["hk","HONG KONG"],["cn","CHINA"],["ops","SHARED OPS"]].forEach(l=>{
  const b=document.createElement("button");b.dataset.k=l[0];
  b.innerHTML=`<i style="background:var(${COLS[l[0]]})"></i>${l[1]}`;
  b.addEventListener("click",()=>{state.focus=state.focus===l[0]?"all":l[0];state.sel=null;
    $("drawer").classList.remove("open");stage.classList.remove("dopen");applyState();});
  $("legend").appendChild(b);
});
const results=$("results");
$("search").addEventListener("input",e=>{
  const q=e.target.value.trim().toLowerCase();
  if(q.length<2){results.classList.remove("open");results.innerHTML="";return;}
  const hits=searchIndex.filter(x=>x.label.toLowerCase().includes(q)).slice(0,9);
  results.innerHTML=hits.length?hits.map(x=>
    `<button data-rid="${x.id}"><span class="dot" style="background:var(${COLS[x.div]||"--ops"})"></span><span style="flex:1">${esc(x.label)}</span><span class="rk">${x.kind}</span></button>`).join("")
    :`<button disabled style="color:var(--mut)">No match on this sheet</button>`;
  results.classList.add("open");
});
$("search").addEventListener("keydown",e=>{
  if(e.key==="Enter"){const first=results.querySelector("[data-rid]");
    if(first){stopTour();select(first.dataset.rid,true);results.classList.remove("open");$("search").blur();}}
});
results.addEventListener("mousedown",e=>{
  const b=e.target.closest("[data-rid]");
  if(b){e.preventDefault();stopTour();select(b.dataset.rid,true);results.classList.remove("open");$("search").blur();}
});
document.addEventListener("click",e=>{if(!e.target.closest(".searchwrap"))results.classList.remove("open");});
const EXPORT_VARS=["--bg","--bg2","--surface","--surface2","--overlay","--line","--line2","--ink","--mut","--faint","--brand","--sg","--hk","--cn","--ops","--ok","--warn","--bad","--info","--grid","--grid2","--labelbg","--disp","--sans","--mono"];
function serialize(){
  sizeLabels();
  const clone=svg.cloneNode(true);
  clone.classList.add("exported");clone.classList.remove("boot");
  clone.removeAttribute("style");
  const cs=getComputedStyle(document.documentElement);
  EXPORT_VARS.forEach(v=>clone.style.setProperty(v,cs.getPropertyValue(v).trim()));
  clone.style.setProperty("--fd",svg.style.getPropertyValue("--fd")||"2.6s");
  clone.setAttribute("width",W);clone.setAttribute("height",H);
  clone.setAttribute("viewBox","0 0 "+W+" "+H);clone.setAttribute("xmlns",NS);
  const w=clone.querySelector("#world");if(w)w.removeAttribute("transform");
  clone.querySelectorAll(".hit").forEach(n=>n.remove());
  return'<?xml version="1.0" encoding="UTF-8"?>\n'+new XMLSerializer().serializeToString(clone);
}
function download(name,blob){
  const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download=name;
  document.body.appendChild(a);a.click();a.remove();
  setTimeout(()=>URL.revokeObjectURL(a.href),4000);
}
function exportSVG(){download("tri-market-blueprint-fy27.svg",new Blob([serialize()],{type:"image/svg+xml"}));toast("SVG exported in current state");}
function exportPNG(){
  toast("Rasterizing sheet…");
  const url=URL.createObjectURL(new Blob([serialize()],{type:"image/svg+xml"}));
  const img=new Image();
  img.onload=()=>{
    const sc=Math.min(2,6000/H);
    const cv=document.createElement("canvas");cv.width=Math.round(W*sc);cv.height=Math.round(H*sc);
    const ctx=cv.getContext("2d");
    ctx.fillStyle=getComputedStyle(document.documentElement).getPropertyValue("--bg").trim()||"#0A0F1E";
    ctx.fillRect(0,0,cv.width,cv.height);ctx.drawImage(img,0,0,cv.width,cv.height);
    URL.revokeObjectURL(url);
    cv.toBlob(b=>{if(b){download("tri-market-blueprint-fy27.png",b);toast("PNG exported · "+cv.width+"×"+cv.height);}else toast("PNG failed — use SVG");},"image/png");
  };
  img.onerror=()=>{URL.revokeObjectURL(url);toast("PNG failed — use SVG export");};
  img.src=url;
}
async function copySVG(){
  const str=serialize();
  try{await navigator.clipboard.writeText(str);toast("SVG markup copied · "+Math.round(str.length/1024)+" KB");}
  catch(e){
    const ta=document.createElement("textarea");ta.value=str;ta.style.position="fixed";ta.style.opacity="0";
    document.body.appendChild(ta);ta.select();
    try{document.execCommand("copy");toast("SVG markup copied");}catch(e2){toast("Clipboard blocked — use ↓ SVG");}
    ta.remove();
  }
}
$("bSvg").addEventListener("click",exportSVG);$("bSvg2").addEventListener("click",exportSVG);
$("bPng").addEventListener("click",exportPNG);$("bPng2").addEventListener("click",exportPNG);
$("bCopy").addEventListener("click",copySVG);
let toastT;
function toast(msg){const t=$("toast");t.textContent=msg;t.classList.add("show");clearTimeout(toastT);toastT=setTimeout(()=>t.classList.remove("show"),2400);}
build();
sizeLabels();
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{sizeLabels();render();});
$("stats").innerHTML=`<b>3</b> ENGINES · <b>18</b> CHANNELS · <b>${edges.length+16}</b> FLOWS · <b>16</b> CAMPAIGNS · <b>${searchIndex.length}</b> NODES`;
applyState();
goNav("brand",true);
setTimeout(()=>svg.classList.remove("boot"),1700);
window.addEventListener("resize",()=>{render();sizeLabels();});

// Read-only public adapter for the Astro navigation layer.
window.MarketBlueprintAtlas={select,clearSel,goNav,hasNode:id=>Boolean(dossiers[id]),getNode:id=>dossiers[id]||null};
document.dispatchEvent(new Event("atlas:ready"));
