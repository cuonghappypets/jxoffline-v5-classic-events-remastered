(() => {
const norm = s => String(s).toLowerCase().replace(/đ/g,"d").normalize("NFD").replace(/[\u0300-\u036f]/g,"");
const root=document.documentElement, theme=document.querySelector("#theme");
try{const saved=localStorage.getItem("hoiuc-theme");if(saved==="dark"||saved==="light")root.dataset.theme=saved;}catch(e){}
theme?.addEventListener("click",()=>{const t=root.dataset.theme==="dark"?"light":"dark";root.dataset.theme=t;try{localStorage.setItem("hoiuc-theme",t);}catch(e){}});
const q=document.querySelector("#search"), y=document.querySelector("#year"), s=document.querySelector("#season");
if(!q)return;
const cards=Array.from(document.querySelectorAll(".event-card")).map(el=>({el,key:norm(el.dataset.search)}));
function filter(){const words=norm(q.value).trim().split(/\s+/).filter(Boolean);let n=0;
for(const {el,key} of cards){const ok=(!y.value||el.dataset.year===y.value)&&(!s.value||el.dataset.season===s.value)&&words.every(w=>key.includes(w));el.hidden=!ok;n+=Number(ok)}
document.querySelector("#count").textContent=n+" / "+cards.length+" sự kiện";
document.querySelector("#empty").hidden=n!==0;
}
q.addEventListener("input",filter);y.addEventListener("change",filter);s.addEventListener("change",filter);
document.querySelector("#clear").addEventListener("click",()=>{q.value="";y.value="";s.value="";filter();q.focus()});
filter();
})();