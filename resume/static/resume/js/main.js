function showTab(name){
  const tabs = ["about","resume","portfolio","support"];
  tabs.forEach(t=>{
    document.getElementById("tab-"+t).classList.remove("active");
  });

  document.getElementById("tab-"+name).classList.add("active");

  const titleMap = {
    about: "Обо мне",
    resume: "Резюме",
    portfolio: "Портфолио",
    support: "Поддержка"
  };

  document.getElementById("tab-title").innerText = titleMap[name];
}