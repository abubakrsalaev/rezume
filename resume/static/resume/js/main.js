function renderStars(el){
  const stars = parseInt(el.dataset.stars || "0");
  let s = "";
  for(let i=1;i<=5;i++){
    s += (i <= stars) ? "★" : "☆";
  }
  el.innerText = s;
}

document.querySelectorAll(".stars").forEach(renderStars);

async function loadSection(key){
  const res = await fetch(`/api/left/${key}/`);
  const data = await res.json();

  let html = `<h2>${data.title}</h2>
              <p style="white-space: pre-line;">${data.content || ""}</p>`;

  if(key === "support"){
    let links = "";
    if(data.instagram){
      links += <p><b>Instagram:</b> <a href="${data.instagram}" target="_blank">${data.instagram}</a></p>;
    }
    if(data.telegram){
      links += <p><b>Telegram:</b> <a href="${data.telegram}" target="_blank">${data.telegram}</a></p>;
    }
    if(!links){
      links = "<p>Ссылки пока не добавлены (добавь через админку).</p>";
    }

    html += <hr>${links};
  }

  document.getElementById("leftContent").innerHTML = html;
  document.getElementById("leftScroll").scrollTop = 0;
}