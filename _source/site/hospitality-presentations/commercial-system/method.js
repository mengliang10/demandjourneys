const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const ready=Reveal.initialize({width:1280,height:750,margin:.11,hash:true,controls:false,progress:true,center:false,transition:reduced?'none':'fade',pdfMaxPagesPerSlide:1,pdfSeparateFragments:false,keyboardCondition:e=>!['INPUT','SELECT','TEXTAREA'].includes(e.target.tagName)});
function status(){document.getElementById('count').textContent=String(Reveal.getIndices().h+1).padStart(2,'0')+' / '+Reveal.getTotalSlides();document.getElementById('chapter').textContent=Reveal.getCurrentSlide().dataset.chapter;}
ready.then(status);Reveal.on('slidechanged',status);
document.getElementById('next').onclick=()=>Reveal.next();
document.getElementById('prev').onclick=()=>Reveal.prev();
document.getElementById('overview').onclick=()=>Reveal.toggleOverview();
document.getElementById('contents').onclick=()=>Reveal.slide(1);
