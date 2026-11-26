(() => {
const norm = s => String(s).toLowerCase().replace(/đ/g,"d").normalize("NFD").replace(/[\u0300-\u036f]/g,"");
const root=document.documentElement, theme=document.querySelector("#theme");
try{const saved=localStorage.getItem("hoiuc-theme");if(saved==="dark"||saved==="light")root.dataset.theme=saved;}catch(e){}
theme?.addEventListener("click",()=>{const t=root.dataset.theme==="dark"?"light":"dark";root.dataset.theme=t;try{localStorage.setItem("hoiuc-theme",t);}catch(e){}});
// Decorative category symbols; never present these as original game sprites.
const iconRules=[
  [/^mang cau|^sung(?: |$)/u,"🍈","fruit"],
  [/^dua(?: |$)/u,"🥥","fruit"], [/^xoai(?: |$)/u,"🥭","fruit"], [/^du du(?: |$)/u,"🌿","fruit"],
  [/tao do|dao van tho|trai cay|qua tuoi/u,"🍑","fruit"],
  [/^long den/u,"🏮","festival"], [/^nen(?: |$)/u,"🕯️","festival"], [/phao|phong phao/u,"🎆","festival"],
  [/tuyet nhan/u,"⛄","festival"], [/hoa tuyet|bang tinh/u,"❄️","gem"], [/chuong giang sinh/u,"🔔","festival"], [/vo giang sinh/u,"🧦","festival"],
  [/banh trung thu/u,"🥮","food"], [/banh sinh nhat|banh kem/u,"🎂","food"], [/banh chung|banh tet/u,"🍃","food"], [/^banh|^dau xanh|bot gao|bot tinh|bot mi|bao gao|duong cat|duong tinh/u,"🍚","food"], [/trung ga|^trung$/u,"🥚","food"], [/sua tuoi/u,"🥛","food"],
  [/hoa hong|thiep hoa hong/u,"🌹","flower"], [/hoa sen/u,"🪷","flower"], [/nhanh mai|thao|hat cay|hat giang sinh|hat thien tue|cay con|phan bon|thuoc tru sau/u,"🌱","flower"],
  [/long tinh tra|tuu|bau ruou|men ruou/u,"🍵","potion"], [/duoc lo|duyen lo|bao lo|bach qua lo|tien thuy|binh nuoc|nuoc tinh khiet|thung nuoc/u,"🧪","potion"],
  [/^tong kim .*hoan|tao hoa dan|bach chan don|bach cau hoan/u,"💊","potion"],
  [/hoang kim bao hap|ruong|bao hap/u,"🧰","gift"], [/hong bao|li xi|le bao|^qua |^hop qua|^le vat/u,"🎁","gift"], [/^tui |huong bao/u,"👝","gift"],
  [/^giay|thiep |mat thu|mat do|do pho|^manh tranh|tho dia phu/u,"📜","scroll"], [/mat tich|tam kinh|tay tuy kinh|quyen pho|kiem pho|quyen phap|chuy phap|thuong phap|dao phap|chuong phap|con phap|thuat|quyen [1-9]/u,"📖","scroll"],
  [/lenh bai|^lenh |^moc bai|^dong bai|^ngan bai|^kim bai|^ngoc bai| bac dau mon|^bac dau mon|hieu phu|chi an/u,"🎫","scroll"],
  [/huyen tinh|thuy tinh|bao thach|tinh thach|ngoc khau|khoang|chu sa|thien nien han thiet|thep tinh luyen|kim thach|phu dung thach|chung nhu|khong tuoc thach|tran bang thach/u,"💎","gem"],
  [/nhan|gioi chi|dieu long gioi|phung gioi|dan tam gioi|da tinh hoan/u,"💍","gear"], [/ngoc boi|hang lien|hang khuyen|day chuyen|hoa tai|nghia boi|ngoc can khon boi|lang nha boi|thu trac|tinh y ket/u,"📿","gear"],
  [/truong sam|nghe thuong|huyet sam|ca sa/u,"👘","gear"], [/phat quan|chiec mu/u,"🎩","gear"], [/nhuyen ngoa|nhuyen ly|doi giay/u,"🥾","gear"],
  [/kiem|gioi dao|than chuy|phung nghia dao|u minh thuong|phi dao|^thiet la han/u,"⚔️","gear"],
  [/thanh tre|day coi|to tam|cuon vai|kim chi|^no do|khan quang/u,"🧵","material"],
  [/manh co/u,"🚩","festival"], [/ngoi sao/u,"⭐","festival"], [/bo cau/u,"🕊️","festival"], [/^bong |vo bong|ruot cao su/u,"⚽","material"], [/chien co/u,"🥁","festival"],
  [/tui y te|nuoc hoa/u,"🧴","potion"], [/son|kep toc|guong|luoc/u,"🪞","gear"],
];
for(const card of document.querySelectorAll(".item-card")){
  const name=card.querySelector("strong"); if(!name||card.querySelector(".item-symbol"))continue;
  const key=norm(name.textContent).trim();
  const match=iconRules.find(([pattern])=>pattern.test(key));
  const symbol=document.createElement("span");
  symbol.className="item-symbol item-symbol--"+(match?match[2]:"other");
  symbol.setAttribute("aria-hidden","true");
  symbol.textContent=match?match[1]:"✦";
  card.prepend(symbol);
}
for(const section of document.querySelectorAll("#vat-pham")){
  const grid=section.querySelector(".item-grid");
  if(grid&&!section.querySelector(".icon-legend")){
    const note=document.createElement("p"); note.className="icon-legend";
    note.textContent="Biểu tượng chỉ để minh họa, không phải hình vật phẩm gốc trong game.";
    grid.after(note);
  }
}

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